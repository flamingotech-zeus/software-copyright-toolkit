# -*- coding: utf-8 -*-
"""软著申请材料生成 · 统一配置（ruanzzhu_config.py）
=================================================
复用方法（后续每次申请都这样）：
  1) 复制本文件为 config_<项目名>.py，按注释修改下面字段；
  2) 把生成脚本里 `from ruanzhu_config import C` 改成 `from config_<项目名> import C`；
  3) 运行 scripts/ 下对应脚本即可。

路径规则：
  - code_root / output_dir / edge_path / index_html 建议用绝对路径；
  - manual_md / manual_img_dir 若填相对路径，则相对“本配置文件所在目录（scripts/）”解析；
  - code_ordered / code_tools_dir / demo_sites 里的相对路径，相对 code_root 解析。
"""
import os

_HERE = os.path.dirname(os.path.abspath(__file__))


def _resolve(p, base):
    return p if os.path.isabs(p) else os.path.join(base, p)


CONFIG = {
    # ===== 1. 软件与著作权人基本信息 =====
    "sw_name": "一键出海AI多行业外贸出海平台",     # 软件全称（不含版本号）
    "sw_short": "一键出海AI",                       # 软件简称（无则留空字符串）
    "version": "V1.0",
    "owner_name": "温州火烈鸟网络科技有限公司",
    "owner_credit": "91330304MABY9NPX93",
    "owner_addr": "浙江省温州市鹿城区七都街道山水智创大楼5号楼8层8056",
    "owner_industry": "信息传输、软件和信息技术服务业——软件开发（其他软件开发）",
    "dev_finish_date": "2026年9月14日",
    "first_publish": "未发表",
    "dev_method": "独立开发",
    "rights_method": "原始取得",
    "rights_scope": "全部",
    "write_date": "2026年9月",                      # 说明书落款月份
    "sw_purpose": "面向中小制造工厂与贸易商的一站式外贸出海服务平台：AI市场调研、英文外贸官网生成、一键上线、SEO/GEO优化、询盘管理与经营数据分析",

    # ===== 2. 代码与输出路径 =====
    "code_root": r"D:\一键出海AI",
    "output_dir": r"D:\一键出海AI\10-软著申请材料",
    # 源代码文件“逻辑顺序”（相对 code_root）；前30页优先放核心入口文件
    "code_ordered": [
        r"01-平台原型\index.html",
        r"01-平台原型\styles.css",
        r"01-平台原型\app.js",
        r"01-平台原型\sites\valve-demo.html",
        r"01-平台原型\sites\bag-demo.html",
        r"06-后端接入\api\_auth.php",
        r"06-后端接入\api\auth-check.php",
        r"06-后端接入\api\auth-login.php",
        r"06-后端接入\api\auth-logout.php",
        r"06-后端接入\api\auth-send-code.php",
        r"06-后端接入\api\auth.config.php",
        r"06-后端接入\api\chat.php",
        r"06-后端接入\api\domain-check.php",
        r"06-后端接入\api\health.php",
        r"06-后端接入\api\qiniu-save.php",
        r"06-后端接入\api\qiniu-status.php",
        r"06-后端接入\api\qiniu-token.php",
        r"06-后端接入\auth.config.example.php",
        r"06-后端接入\llm.config.example.php",
        r"07-本地开发\server.py",
    ],
    "code_tools_dir": r"09-上线执行\tools",   # 该目录下所有 .js/.py 追加到源代码末尾（相对 code_root）
    "code_exclude_dirs": ["node_modules", ".git", "__pycache__", ".workbuddy", "dist", "build", "08-部署包"],
    "code_ext": [".py", ".js", ".ts", ".html", ".css", ".vue", ".jsx", ".tsx", ".java", ".go", ".php", ".sql"],

    # ===== 3. 说明书（文档鉴别材料） =====
    "manual_md": "sw_manual_一键出海AI.md",   # 相对本配置目录；也支持绝对路径
    "manual_img_dir": "screenshots",          # 图片基准目录（相对本配置目录；markdown 内用相对文件名）

    # ===== 4. 截图（gen_screenshots.py 用） =====
    "edge_path": r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    "index_html": r"D:\一键出海AI\01-平台原型\index.html",  # 可用 file:// 打开的入口页
    "login_url_suffix": "?auth=1",            # 拼在 index_html 后的登录态参数（无则留空）
    "views": [
        ("analyze", "市场营销分析"),
        ("generate", "出海网站生成"),
        ("launch", "一键上线"),
        ("mysites", "我的网站"),
        ("seo", "SEO与GEO"),
        ("inquiry", "询盘中心"),
        ("data", "数据中心"),
        ("radar", "市场雷达"),
    ],
    "pack_view": "generate",     # 行业包截图所在视图
    "pack_id": "shoes",         # 选中该行业包再截图（制造区分度，避免与默认视图重复）
    "demo_sites": [
        (r"D:\一键出海AI\01-平台原型\sites\valve-demo.html", "12-泵阀行业外贸站示例.png"),
        (r"D:\一键出海AI\01-平台原型\sites\bag-demo.html", "13-箱包行业外贸站示例.png"),
    ],

    # ===== 5. 开发/运行环境（基本信息表用） =====
    "dev_env": {
        "硬件": "CPU：Intel Core i5 及以上四核处理器；内存：16GB 及以上；硬盘：512GB SSD；显示：1920×1080 及以上分辨率",
        "操作系统": "Windows 11；Linux（Ubuntu 18+）",
        "开发工具/IDE": "Visual Studio Code、Git、浏览器开发者工具（Chrome DevTools）",
        "主要开发语言": "JavaScript（ES2020）、HTML5、CSS3、PHP 7.4+、Python 3.8+",
        "主要技术框架/依赖": "原生前端三件套（无框架依赖）、PHP cURL/OpenSSL 扩展、Python 标准库 HTTP 服务、七牛云对象存储 SDK（Kodo）、大模型 API（HTTPS 调用）",
        "源程序量": "约 10102 行（不含部署副本）",
    },
    "run_env": {
        "运行硬件环境（服务器端）": "CPU 2核及以上；内存 4GB 及以上；硬盘 40GB 及以上；具备公网 IPv4 地址，带宽 5Mbps 及以上",
        "运行硬件环境（客户端）": "CPU 双核 1.8GHz 及以上；内存 4GB 及以上；分辨率 1366×768 及以上",
        "服务器端操作系统": "Linux（CentOS 7+/Ubuntu 18+）或 Windows Server 2016 及以上",
        "Web 服务软件": "Nginx 1.18+ 或 Apache 2.4+",
        "运行支撑软件": "PHP 7.4 及以上（含 cURL、OpenSSL 扩展）；Python 3.8 及以上（本地开发服务）",
        "客户端运行环境": "Chrome 90+、Edge 90+、Firefox 88+ 或其他基于 Chromium 的现代浏览器",
        "网络环境": "互联网接入；访问大模型 API、域名注册商接口、七牛云对象存储需支持 HTTPS 出网",
    },
    "functions": [
        ("1", "市场营销分析（深度研究版）", "输入产品照片，按深度研究方法论产出 12 章海外市场调研报告，含事实卡片、来源分级、置信度与独立校验，可导出 Word/PDF"),
        ("2", "出海网站生成", "依据工厂信息与行业包参数生成可部署英文外贸官网，含产品中心、资质背书、询盘表单与中英切换"),
        ("3", "一键上线", "域名可注册性实时检查、服务器与证书选择、一键部署流程"),
        ("4", "我的网站", "已上线网站的预览、访客数据、AI 体检、编辑更新、重新部署与暂停下线管理"),
        ("5", "SEO 与 GEO", "SEO 体检、关键词排名与收录监控、六大 AI 引擎引用检测、AI 生成 SEO 长文并按平台规则改写分发"),
        ("6", "询盘中心", "全站统一询盘收件箱，AI 起草买家母语回复，状态跟进与报价单生成"),
        ("7", "数据中心", "全站访客/询盘/成交率看板、转化漏斗、一键导出 Word 经营月报"),
        ("8", "市场雷达", "多源并行扫描生成 30 天市场简报、趋势判断与品类机会 SVG 关系图"),
    ],
    "tech_features": [
        "AI Agent 工作流驱动：八大功能均按“拆解任务 → 调用模型/数据源 → 结构化产出”的智能体工作流实现",
        "可插拔行业包架构：泵阀、鞋服、教玩具、服装辅料、农产品等行业包插件化切换，支持用户自建自定义行业包",
        "事实可追溯机制：调研报告采用来源分级（L1 官方/法规至 L4 社区）、事实卡片与独立校验记录",
        "轻量部署架构：前端平台 + PHP 接口 + Python 本地服务 + Node.js/Python 自动化上线工具，可部署于普通云服务器",
        "安全机制：密钥仅存服务端配置文件，上传凭证采用 HMAC-SHA1 签名，登录采用验证码与会话凭证校验",
    ],
}

# ---- 路径解析（相对路径按规则归位） ----
C = dict(CONFIG)
cr = CONFIG["code_root"]
cr = cr if os.path.isabs(cr) else os.path.join(_HERE, cr)
C["code_root"] = cr
C["output_dir"] = CONFIG["output_dir"] if os.path.isabs(CONFIG["output_dir"]) else os.path.join(_HERE, CONFIG["output_dir"])
C["code_ordered"] = [p if os.path.isabs(p) else os.path.join(cr, p) for p in CONFIG["code_ordered"]]
C["code_tools_dir"] = CONFIG["code_tools_dir"] and (
    CONFIG["code_tools_dir"] if os.path.isabs(CONFIG["code_tools_dir"]) else os.path.join(cr, CONFIG["code_tools_dir"]))
C["manual_md"] = _resolve(CONFIG["manual_md"], _HERE)
C["manual_img_dir"] = _resolve(CONFIG["manual_img_dir"], _HERE)
C["edge_path"] = _resolve(CONFIG["edge_path"], _HERE)
C["index_html"] = _resolve(CONFIG["index_html"], _HERE)
C["demo_sites"] = [(_resolve(p, _HERE), n) for p, n in CONFIG["demo_sites"]]
