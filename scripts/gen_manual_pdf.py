# -*- coding: utf-8 -*-
"""将软件说明书 markdown 渲染为软著【文档鉴别材料】PDF（支持内嵌界面截图）。
依赖：reportlab, Pillow
运行：python gen_manual_pdf.py
markdown 中图片写法：![图注](相对或绝对路径.png)
  - 绝对路径且存在 → 直接使用
  - 否则按文件名在 manual_img_dir 中查找；再尝试 manual_img_dir/相对路径
"""
import os, re, time
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, PageBreak,
                                HRFlowable, KeepTogether, Table, TableStyle, Image)
from reportlab.lib import colors
from PIL import Image as PILImage
from ruanzhu_config import C

SRC = C["manual_md"]
IMG_DIR = C["manual_img_dir"]
OUT = os.path.join(C["output_dir"], "03-文档鉴别材料-软件使用说明书.pdf")
SW_NAME = C["sw_name"] + C["version"]

pdfmetrics.registerFont(UnicodeCIDFont("STSong-Light"))


def resolve_img(md_path):
    if os.path.isabs(md_path) and os.path.exists(md_path):
        return md_path
    base = os.path.join(IMG_DIR, os.path.basename(md_path))
    if os.path.exists(base):
        return base
    if not os.path.isabs(md_path):
        cand = os.path.join(IMG_DIR, md_path)
        if os.path.exists(cand):
            return cand
    return None


def esc(t):
    t = t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    return t


S = dict(
    h1=ParagraphStyle("h1", fontName="STSong-Light", fontSize=16, leading=24,
                      alignment=TA_CENTER, spaceAfter=14),
    h2=ParagraphStyle("h2", fontName="STSong-Light", fontSize=13, leading=20,
                      spaceBefore=14, spaceAfter=8),
    h3=ParagraphStyle("h3", fontName="STSong-Light", fontSize=11.5, leading=18,
                      spaceBefore=10, spaceAfter=6),
    body=ParagraphStyle("body", fontName="STSong-Light", fontSize=11, leading=19,
                        firstLineIndent=22, alignment=TA_JUSTIFY, spaceAfter=4),
    item=ParagraphStyle("item", fontName="STSong-Light", fontSize=11, leading=19,
                        leftIndent=14, alignment=TA_JUSTIFY, spaceAfter=3),
    cover=ParagraphStyle("cover", fontName="STSong-Light", fontSize=14, leading=26,
                         alignment=TA_CENTER),
)


def add_image(alt, path):
    real = resolve_img(path)
    if not real:
        story.append(Paragraph(esc("[截图 " + (alt or path) + " 未找到]"), S["item"]))
        return
    try:
        iw, ih = PILImage.open(real).size
    except Exception:
        iw, ih = 1440, 900
    maxw = A4[0] - 104
    w = maxw
    h = w * ih / iw
    if h > A4[1] * 0.62:
        h = A4[1] * 0.62
        w = h * iw / ih
    story.append(Spacer(1, 4))
    story.append(Image(real, width=w, height=h))
    if alt:
        story.append(Paragraph("图：" + esc(alt),
                      ParagraphStyle("cap", parent=S["body"], firstLineIndent=0,
                                     alignment=TA_CENTER, fontSize=9, textColor=colors.grey)))
    story.append(Spacer(1, 6))


story = []
lines = open(SRC, encoding="utf-8").read().splitlines()
cover_done = False
table_buf = []


def flush_table():
    global table_buf
    if not table_buf:
        return
    rows = []
    for row in table_buf:
        cells = [c.strip() for c in row.strip().strip("|").split("|")]
        if all(re.fullmatch(r":?-{2,}:?", c) for c in cells):
            continue
        rows.append([Paragraph(esc(c), ParagraphStyle("tc", parent=S["body"], firstLineIndent=0,
                                                      fontSize=10, leading=15)) for c in cells])
    table_buf = []
    if not rows:
        return
    t = Table(rows, colWidths=[120, 320])
    t.setStyle(TableStyle([
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#EFF3F8")),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]))
    story.append(Spacer(1, 4))
    story.append(t)
    story.append(Spacer(1, 6))


for raw in lines:
    ln = raw.rstrip()
    if not ln.strip():
        continue
    if ln.strip().startswith("|"):
        if cover_done:
            table_buf.append(ln)
        continue
    flush_table()
    if ln.startswith("# "):
        continue
    if ln.strip() == "---":
        continue
    m = re.match(r'^!\[(.*?)\]\((.*?)\)\s*$', ln)
    if m:
        add_image(m.group(1), m.group(2))
        continue

    if ln.startswith("## 目录"):
        story.append(Paragraph(SW_NAME, S["cover"]))
        story.append(Spacer(1, 18))
        story.append(Paragraph("软 件 使 用 说 明 书", S["cover"]))
        story.append(Paragraph("（文档鉴别材料）", S["cover"]))
        story.append(Spacer(1, 30))
        story.append(Paragraph("版本号：" + C["version"], S["cover"]))
        story.append(Paragraph("著作权人：" + C["owner_name"], S["cover"]))
        story.append(Paragraph("编写日期：" + C["write_date"], S["cover"]))
        story.append(PageBreak())
        cover_done = True
        story.append(Paragraph("目　录", S["h1"]))
        story.append(HRFlowable(width="100%", thickness=0.8))
        continue
    if not cover_done:
        continue
    if ln.startswith("## "):
        story.append(Paragraph(esc(ln[3:]), S["h2"]))
    elif ln.startswith("### "):
        story.append(Paragraph(esc(ln[4:]), S["h3"]))
    elif ln.startswith("（") or re.match(r"^第[一二三四五六七八九十]步|^（\d+）|^步骤\d", ln):
        story.append(Paragraph(esc(ln), S["item"]))
    elif re.match(r"^\d+\s", ln) or re.match(r"^步骤\d", ln):
        story.append(Paragraph(esc(ln), S["item"]))
    else:
        story.append(Paragraph(esc(ln), S["body"]))

flush_table()


def on_page(canv, doc):
    canv.saveState()
    if doc.page == 1:
        canv.restoreState()
        return
    canv.setFont("STSong-Light", 9)
    canv.drawString(46, A4[1] - 34, SW_NAME + " 软件使用说明书")
    canv.drawRightString(A4[0] - 46, A4[1] - 34, f"第 {doc.page} 页")
    canv.setLineWidth(0.6)
    canv.line(46, A4[1] - 40, A4[0] - 46, A4[1] - 40)
    canv.restoreState()


TMP = OUT + ".building.pdf"
doc = SimpleDocTemplate(TMP, pagesize=A4,
                        leftMargin=52, rightMargin=52,
                        topMargin=56, bottomMargin=48,
                        title=SW_NAME + " 软件使用说明书",
                        author=C["owner_name"])
doc.build(story, onFirstPage=on_page, onLaterPages=on_page)

final = OUT
for attempt in range(3):
    try:
        os.replace(TMP, final)
        break
    except PermissionError:
        if attempt == 2:
            final = OUT.replace("03-文档鉴别材料", "03-文档鉴别材料(含界面截图)")
            os.replace(TMP, final)
        else:
            time.sleep(2)
print("已生成:", final)
