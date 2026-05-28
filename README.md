# cursor-demo-project

用于熟悉 **Cursor** 的 Python 练习项目（CLI、示例数据、读取与处理代码）。

## 环境要求

- Python 3.11+

## 安装

```bash
cd ~/Projects/cursor-demo-project
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
```

## 使用

```bash
cursor-demo --help
cursor-demo greet
cursor-demo greet --name Alice
```

## 示例数据与处理

项目自带示例数据：

- `data/users.csv` — 用户表（CSV）
- `data/sales.json` — 销售记录（JSON）

读取并汇总的示例代码在 `src/cursor_demo_project/data_loader.py`；可直接运行：

```bash
python examples/process_sample_data.py
```
