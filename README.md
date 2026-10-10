# Software Copyright Application Toolkit

[English](README.md) | [简体中文](README.zh-CN.md)

> Turn the production of software copyright registration material into a reusable baseline: edit the config, run the scripts, deliver.

> **Note.** This repository contains company-specific content — brand copy, logos and asset paths. The layout, effects and code are what is worth taking. Replace the content before publishing.


## What this is

This is not a document template pack. Templates still leave you assembling three deliverables by hand, every time, with the same fiddly formatting.

Here one configuration file drives all three outputs. The registration form, the source-code excerpt and the user manual are generated, so a repeat application is config editing rather than document work.

## Why we open-sourced it

We did a software copyright application and found that most of the work was mechanical: same structure, different content, repeated across three documents.

The application process is the same for everyone, so this is a straightforward tool to publish. The case study bundled inside it is an example and can be replaced.

## What's in it

- **One config drives three deliverables:**
  - the software basic information form, as a `.docx`
  - the program identification material — the first 30 pages and the last 30 pages of source, as a PDF
  - the documentation identification material, i.e. the user manual, as a PDF, including screenshots
- **Automatic screenshot generation** for interface-based software.
- **Templates** with placeholders for both the basic information form and the manual.
- **A written working handbook** describing the process end to end.
- **A complete worked example** — configuration, source markdown, all three outputs and the screenshots — so the expected shape of each artifact is visible.

## Requirements

Python 3 · python-docx · a PDF generation dependency

## Getting started

1. Copy the configuration file and fill in the software name, copyright holder, code paths, interface modules and environment details.
2. Point the manual markdown at your document and its image directory.
3. Run the four scripts in order: basic information form, source excerpt, screenshots, manual.

The repository README walks through each step with the exact commands.

## Structure

```
├── scripts/
│   ├── gen_basic_info_docx.py
│   ├── gen_code_pdf.py
│   ├── gen_manual_pdf.py
│   ├── gen_screenshots.py
│   ├── ruanzhu_config.py
│   └── sw_manual_一键出海AI.md
├── templates/
│   ├── 软件使用说明书模板.md
│   └── 软件基本信息表模板.md
├── 参考案例/
│   └── 一键出海AI/
│       ├── 01-软件开发基本信息表-一键出海AI多行业外贸出海平台V1.0.docx
│       ├── 02-程序鉴别材料-源程序前后各30页.pdf
│       ├── 03-文档鉴别材料(含界面截图)-软件使用说明书.pdf
│       ├── config_一键出海AI.py
│       ├── screenshots/
│       └── sw_manual_一键出海AI.md
└── 软著申请工作手册.md
```

## Notes and limits

1. **Source excerpts are page-based.** The first and last 30 pages rule assumes a certain code volume. Check how it behaves for a very small or very large codebase.
2. **Screenshots need a runnable interface.** For software without a UI, that step does not apply.
3. **Formatting rules are administrative.** The registration authority's requirements are the authority here, not this toolkit.
4. **The bundled example is company content.** Replace it before publishing.

## License

MIT
