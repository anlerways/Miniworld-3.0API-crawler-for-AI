# 迷你世界 UGC 3.0 API 文档爬虫

> **提示词不断更新，最新提示词请到本仓库下载。**
> **本资源完全免费，收费是被骗了！**
> —— BY TEMP AXIS

## 🚀 项目说明

本工具从 [迷你世界 UGC 3.0 官方 Wiki](https://dev-wiki.mini1.cn/ugc-wiki/) 自动爬取所有 API 函数和枚举常量，生成结构化的 Markdown 文档，方便开发者查阅、集成到 AI 辅助开发或 VSCode 插件中。

---

## 📦 使用方法

### 1. 运行爬虫，获取最新 API 文档
- 下载 `crawler.exe`（或运行 `crawler.py`）
- 双击运行，根据提示选择输出模式（完整版/精简版/两者）
- 等待爬取完成，会在当前目录生成 `.md` 文件

### 2. 将生成的所有 `.md` 文件喂给 AI
- **对话模式**：投喂 `api_reference.md`（详细版 API）
- **API 模式（配合 VSCode 插件）**：使用 `api_summary.md`（简单查找版），需配合官方 VSCode 插件使用：[https://dev-wiki.mini1.cn/cyclopdeia?wikiMenuId=3&wikiId=2324](https://dev-wiki.mini1.cn/cyclopdeia?wikiMenuId=3&wikiId=2324)
- **枚举库**：`enum_reference.md`
- **事件使用限定词**：`event_registration.md`
- **主提示词**：`ugc3.0_main.md`（建议从本仓库获取最新版本）

---

## 📁 生成文件说明

| 文件名 | 用途 |
|--------|------|
| `api_reference.md` | 完整 API 手册（含参数、返回值），适合详细查阅或对话式投喂 |
| `api_summary.md` | 精简速查表（仅函数名+描述，表格），便于 VSCode 插件快速补全 |
| `enum_reference.md` | 所有枚举常量，按枚举组分类 |
| `event_registration.md` | 事件注册/触发的限定词和注意事项（手动维护） |
| `ugc3.0_main.md` | 主提示词，用于 AI 角色设定或系统提示（建议每次从仓库拉取最新版） |

---

## 🔧 依赖环境（仅适用于源码运行）

- Python 3.6+
- `requests`
- `beautifulsoup4`

安装依赖：
```bash
pip install requests beautifulsoup4
```

---

## 📥 获取最新资源

- **所有提示词和文档** 均已放在本仓库，克隆或直接下载即可：
  ```bash
  git clone https://github.com/anlerways/Miniworld-3.0API-crawler-for-AI.git
  ```
- **可执行文件**：前往 [Releases](https://github.com/anlerways/Miniworld-3.0API-crawler-for-AI/releases) 下载最新版 `crawler.exe`，无需安装 Python。

---

## 💡 常见问题

**Q：运行 `crawler.exe` 报毒？**
A：部分杀软会误报，请添加信任，或自行使用源码运行。

**Q：提示词如何更新？**
A：直接 `git pull` 拉取最新仓库，或重新下载 `ugc3.0_main.md` 等文件。

---

## 📜 许可证

本项目采用 [MIT License](LICENSE) 开源，可自由使用、修改、分发。

---

## 👤 作者

**BY TEMP AXIS**
仓库：[https://github.com/anlerways/Miniworld-3.0API-crawler-for-AI](https://github.com/anlerways/Miniworld-3.0API-crawler-for-AI)
