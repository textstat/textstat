# TextStat - 智能文本分析工具 [![CI/CD](https://github.com/yamamunesakura/textstat/actions/workflows/python-package.yml/badge.svg)](https://github.com/yamamunesakura/textstat/actions)

<div align="center">
  <img src="docs/assets/textstat-demo.gif" width="800" alt="交互式分析演示">
</div>

## 🧩 功能特性
### 核心分析模块
| 模块名称        | 支持语言       | 算法版本  | 性能基准       |
|----------------|---------------|----------|---------------|
| 词频统计        | 中/英/日       | v2.1     | 100MB/s       |
| 情感分析        | 中/英          | v1.4     | BERT-base     |
| 实体识别        | 中/英          | v3.2     | spaCy+CRF     |
| 可读性评估      | 中/英          | v2.0     | Flesch-Kincaid|

### 可视化引擎
```python
# 高级配置示例
from textstat.visualization import (
    WordCloudGenerator,
    InteractivePlotter
)

wc_config = {
    "max_words": 150,
    "colormap": "viridis",
    "mask_shape": "circle"
}

plotter = InteractivePlotter(
    theme="dark",
    export_options=["png", "svg"]
)