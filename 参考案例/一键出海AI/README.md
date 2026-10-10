# 参考案例：一键出海AI 多行业外贸出海平台 V1.0

本目录是软著申请材料生成工具包的**首个落地案例**，供后续项目照猫画虎。

## 本案登记口径

- 软件全称：一键出海AI多行业外贸出海平台　版本号：V1.0
- 著作权人：温州火烈鸟网络科技有限公司（91330304MABY9NPX93）
- 开发完成日期：2026-09-14　首次发表：未发表
- 开发方式：独立开发　权利取得方式：原始取得

## 本案产物（已生成，可直接参考）

| 文件 | 说明 |
|------|------|
| `01-软件开发基本信息表-一键出海AI多行业外贸出海平台V1.0.docx` | 基本信息表 Word |
| `02-程序鉴别材料-源程序前后各30页.pdf` | 源代码前后各30页，60页，每页50行 |
| `03-文档鉴别材料(含界面截图)-软件使用说明书.pdf` | 说明书 17 页，内嵌 12 张真实运行界面截图 |
| `screenshots/` | 12 张截图源文件（登录/主界面/8大功能/行业包/2个生成站） |
| `sw_manual_一键出海AI.md` | 说明书源 markdown（图片为绝对路径引用） |
| `config_一键出海AI.py` | 本案实际配置（= ruanzhu_config.py 的填好版） |

## 复现命令

```
venv="C:\Users\book\.workbuddy\binaries\python\envs\default\Scripts\python.exe"
"$venv" "D:\软著申请工具包\scripts\gen_basic_info_docx.py"
"$venv" "D:\软著申请工具包\scripts\gen_code_pdf.py"
"$venv" "D:\软著申请工具包\scripts\gen_screenshots.py"
"$venv" "D:\软著申请工具包\scripts\gen_manual_pdf.py"
```

> 注：本案例的 `manual_md` 指向 `scripts/sw_manual_一键出海AI.md`，图片用绝对路径，因此截图解析正常。
