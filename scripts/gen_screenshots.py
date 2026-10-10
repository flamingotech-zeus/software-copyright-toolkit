# -*- coding: utf-8 -*-
"""抓取软件真实运行界面截图，用于【文档鉴别材料】。
依赖：playwright  +  本机 Chromium 内核浏览器（Edge/Chrome）
运行：python gen_screenshots.py
说明：
  - 用 Playwright 驱动本机 Edge 无头模式打开 index.html，按 VIEWS 逐个切换模块截图；
  - 截图存到 output_dir/screenshots/，文件名与说明书 markdown 中的引用保持一致；
  - 行业包截图会先 setPack(pack_id) 制造区分度，避免与默认视图重复（代理机构要求“文档中不得出现重复截图”）。
"""
import os
from playwright.sync_api import sync_playwright
from ruanzhu_config import C

EDGE = C["edge_path"]
SRC = C["index_html"]
OUT = os.path.join(C["output_dir"], "screenshots")
os.makedirs(OUT, exist_ok=True)

VIEWS = C["views"]
LOGIN_SUFFIX = C.get("login_url_suffix", "")
PACK_VIEW = C.get("pack_view", "generate")
PACK_ID = C.get("pack_id", "")
DEMO_SITES = C.get("demo_sites", [])


def shot(page, name, full=False, wait=1200):
    page.wait_for_timeout(wait)
    path = os.path.join(OUT, name)
    page.screenshot(path=path, full_page=full)
    print("saved", name, os.path.getsize(path) // 1024, "KB")
    return path


def open_index(page, suffix=""):
    page.goto("file:///" + SRC.replace("\\", "/") + suffix)
    page.wait_for_timeout(2500)


with sync_playwright() as p:
    browser = p.chromium.launch(
        executable_path=EDGE, headless=True,
        args=["--no-sandbox", "--disable-gpu", "--force-device-scale-factor=1.5"],
    )
    page = browser.new_page(viewport={"width": 1440, "height": 900})

    # 1) 登录界面
    open_index(page, LOGIN_SUFFIX)
    shot(page, "01-登录界面.png", wait=1800)

    # 2) 系统主界面（默认视图，通常已含左侧导航）
    open_index(page)
    dom = page.evaluate("() => ({side: document.getElementById('side')?.children.length, "
                        "title: document.getElementById('workTitle')?.textContent})")
    print("MAIN DOM:", dom)
    shot(page, "02-系统主界面.png")

    # 3) 各功能模块界面
    start = 3
    for i, (vid, title) in enumerate(VIEWS[1:], start=start):
        page.evaluate(f"switchView('{vid}')")
        page.wait_for_timeout(1400)
        t = page.evaluate("() => document.getElementById('workTitle')?.textContent")
        print(f"view {vid} -> title={t}")
        shot(page, f"0{i}-{title}.png")

    # 4) 行业包体系（选中 pack_id 制造区分度）
    page.evaluate(f"switchView('{PACK_VIEW}')")
    page.wait_for_timeout(1500)
    if PACK_ID:
        page.evaluate(f"setPack('{PACK_ID}')")
        page.wait_for_timeout(1500)
    shot(page, "11-行业包体系.png")

    # 5) 生成的行业外贸站示例（视口截图，整页太长会缩太小看不清）
    for site_url, fname in DEMO_SITES:
        page.goto("file:///" + site_url.replace("\\", "/"))
        shot(page, fname, full=False, wait=1800)

    browser.close()
print("ALL DONE ->", OUT)
