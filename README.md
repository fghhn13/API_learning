# API_learning

个人练习 **HTTP / REST API** 的仓库：在 `src/` 里写接口与业务，在 `tests/` 里写测试，日志输出到 `logs/`（具体日志文件已被 `.gitignore` 忽略）。

## 目录说明

| 目录 | 说明 |
|------|------|
| `src/` | 应用与 API 代码 |
| `tests/` | 测试 |
| `logs/` | 运行日志（目录保留，内容不入库） |
| `config/` | 配置文件 |
| `scripts/` | 辅助脚本 |

## 环境（Python）

```bash
python -m venv .venv
.venv\Scripts\activate   # Windows
pip install -r requirements.txt
```

按需编辑 `requirements.txt`（例如 FastAPI、uvicorn、httpx、pytest），再安装依赖。

## 运行

```bash
python -m src.main
```

（接入 Web 框架后，通常改为 `uvicorn` 等启动命令。）
