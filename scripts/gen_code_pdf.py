# -*- coding: utf-8 -*-
"""生成软著【程序鉴别材料】PDF：源程序前连续30页 + 后连续30页，每页50行，带页码。
依赖：reportlab
运行：python gen_code_pdf.py   （脚本会从同目录 ruanzhu_config 读取配置）
"""
import os
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from ruanzhu_config import C

OUT_DIR = C["output_dir"]
os.makedirs(OUT_DIR, exist_ok=True)
SW_NAME = C["sw_name"] + C["version"]
OUT_PDF = os.path.join(OUT_DIR, "02-程序鉴别材料-源程序前后各30页.pdf")

LINES_PER_PAGE = 50
FRONT_PAGES = 30
BACK_PAGES = 30
MAX_CHARS = 100

COMMENT = {".py": "#", ".js": "//", ".php": "//", ".html": None, ".css": None,
           ".ts": "//", ".tsx": "//", ".jsx": "//", ".vue": "//", ".java": "//",
           ".go": "//", ".sql": "--"}


def read_lines(path):
    ext = os.path.splitext(path)[1].lower()
    rel = os.path.relpath(path, C["code_root"])
    head = COMMENT.get(ext)
    sep = "========== 文件: " + rel + " =========="
    if head:
        sep = head + " " + sep
    elif ext == ".html":
        sep = "<!-- " + sep + " -->"
    else:
        sep = "/* " + sep + " */"
    out = [sep]
    with open(path, "r", encoding="utf-8", errors="ignore") as fh:
        for ln in fh:
            ln = ln.rstrip("\r\n").replace("\t", "    ")
            if len(ln) > MAX_CHARS:
                ln = ln[:MAX_CHARS]
            out.append(ln if ln.strip() else "")
    return out


# ---- 收集源代码（按逻辑顺序；末尾追加工具脚本目录） ----
files = list(C["code_ordered"])
if C["code_tools_dir"] and os.path.isdir(C["code_tools_dir"]):
    for f in sorted(os.listdir(C["code_tools_dir"])):
        if f.endswith((".js", ".py")):
            files.append(os.path.join(C["code_tools_dir"], f))

all_lines = []
for p in files:
    if os.path.exists(p):
        all_lines.extend(read_lines(p))
    else:
        print("WARN 文件不存在，跳过:", p)

total_lines = len(all_lines)
total_pages = (total_lines + LINES_PER_PAGE - 1) // LINES_PER_PAGE
print(f"源代码总行数 {total_lines}，满排页数 {total_pages}")

if total_pages <= FRONT_PAGES + BACK_PAGES:
    selected = all_lines
    pages_text = [selected[i:i + LINES_PER_PAGE] for i in range(0, len(selected), LINES_PER_PAGE)]
else:
    front = all_lines[: FRONT_PAGES * LINES_PER_PAGE]
    back = all_lines[-(BACK_PAGES * LINES_PER_PAGE):]
    pages_text = ([front[i:i + LINES_PER_PAGE] for i in range(0, len(front), LINES_PER_PAGE)]
                  + [back[i:i + LINES_PER_PAGE] for i in range(0, len(back), LINES_PER_PAGE)])

N = len(pages_text)
print(f"实际输出 {N} 页（前 {min(FRONT_PAGES, N//2)} + 后 {min(BACK_PAGES, N - N//2)}）")

pdfmetrics.registerFont(UnicodeCIDFont("STSong-Light"))
c = canvas.Canvas(OUT_PDF, pagesize=A4)
W, H = A4
M_L, M_R, M_T, M_B = 46, 46, 46, 40
FS, LEAD = 8, 9.7
x0 = M_L
y_top = H - M_T - 14


def header(page_no):
    c.setFont("STSong-Light", 9)
    c.drawString(M_L, H - 34, SW_NAME)
    c.drawRightString(W - M_R, H - 34, f"第 {page_no} 页 / 共 {N} 页")
    c.setLineWidth(0.6)
    c.line(M_L, H - 40, W - M_R, H - 40)


for idx, page in enumerate(pages_text, 1):
    header(idx)
    c.setFont("STSong-Light", FS)
    y = y_top
    for ln in page:
        if ln:
            c.drawString(x0, y, ln)
        y -= LEAD
    c.showPage()

c.save()
print("已生成:", OUT_PDF)
