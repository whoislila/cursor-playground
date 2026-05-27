# new-project

Python CLI 项目。

## 环境要求

- Python 3.11+

## 安装

```bash
cd ~/Projects/new-project
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
```

## 使用

```bash
new-project --help
new-project greet
new-project greet --name Alice
```

## 示例数据与处理

项目自带示例数据：

- `data/users.csv` — 用户表（CSV）
- `data/sales.json` — 销售记录（JSON）

读取并汇总的示例代码在 `src/new_project/data_loader.py`；可直接运行：

```bash
python examples/process_sample_data.py
```
