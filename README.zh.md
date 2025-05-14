# Textstat
[![PyPI](https://img.shields.io/pypi/v/textstat.svg)](https://pypi.org/project/textstat/)
[![Build Status](https://img.shields.io/github/actions/workflow/status/textstat/textstat/test.yml?branch=main&label=main&logo=github&logoColor=white)](https://github.com/textstat/textstat/actions/workflows/test.yml)
[![Downloads](https://img.shields.io/pypi/dm/textstat?logo=pypi&logoColor=white)](https://pypistats.org/packages/textstat)

**Textstat is an easy to use library to calculate statistics from text. It helps determine readability, complexity, and grade level.**

<p align="center">
  <img width="100%" src="https://images.unsplash.com/photo-1457369804613-52c61a468e7d?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&h=400&q=80">
</p>
<p align="right">
  <sup>Photo by <a href="https://unsplash.com/@impatrickt">Patrick Tomasso</a>
  on <a href="https://unsplash.com/images/things/book">Unsplash</a></sup>
</p>

>> import textstat  # 导入文本分析库
>>> test_data = (  # 定义测试文本内容
"玩游戏一直被认为对培养全面发展、富有创造力的儿童至关重要；"
 "然而，游戏在成年人生活中应扮演的角色却从未被深入研究过。" 
"我认为游戏对成年人的重要性绝不亚于儿童。" 
"不仅与孩子和其他成年人共度游戏时光能促进人际关系，" 
"同时也是释放累积压力的绝佳方式。"
)
# 执行各类文本分析算法>>> textstat.flesch_reading_ease(test_data)      
# 计算弗莱什易读度>>> textstat.flesch_kincaid_grade(test_data)      
# 计算弗莱什-金凯德年级水平>>> textstat.smog_index(test_data)                # 计算SMOG复杂度指数>>> textstat.coleman_liau_index(test_data)        
# 计算科尔曼-廖可读性指数>>> textstat.automated_readability_index(test_data)  
# 计算自动可读性指标>>> textstat.dale_chall_readability_score(test_data) 
# 计算戴尔-查尔可读性评分>>> textstat.difficult_words(test_data)           
# 统计困难词汇数量>>> textstat.linsear_write_formula(test_data)     
# 应用Linsear写作公式>>> textstat.gunning_fog(test_data)               
# 计算冈宁雾化指数>>> textstat.text_standard(test_data)             
# 获取文本标准等级>>> textstat.fernandez_huerta(test_data)          
# 执行西语费尔南德斯-韦尔塔算法>>> textstat.szigriszt_pazos(test_data)           
# 执行西语西格里斯特-帕佐斯算法>>> textstat.gutierrez_polini(test_data)          
# 执行西语古铁雷斯-波利尼算法>>> textstat.crawford(test_data)                  
# 执行西语克劳福德算法>>> textstat.gulpease_index(test_data)            
# 计算Gulpease意大利语可读性指数>>> textstat.osman(test_data)                     
# 执行奥斯曼特定制算法
shell复制代码
# 软件包安装方法
pip install textstat                 # 使用pip工具安装
easy_install textstat                # 使用easy_install工具安装
git clone https://github.com/textstat/textstat.git  # 克隆GitHub代码库
cd textstat && pip install .         # 安装本地最新开发版
tar xfz textstat-*.tar.gz            # 解压PyPI下载的压缩包
cd textstat-*/ && python setup.py install  # 通过源码编译安装
python复制代码
# 多语言配置模块
textstat.set_lang(lang)  # 设置分析语言（控制音节分割和公式版本）
# 西班牙语专用算法调用示例>>> textstat.fernandez_huerta(test_data)   
# 西语费尔南德斯-韦尔塔可读性公式>>> textstat.szigriszt_pazos(test_data)    
# 西语西格里斯特-帕佐斯可读性公式>>> textstat.gutierrez_polini(test_data)   
# 西语古铁雷斯-波利尼可读性公式>>> textstat.crawford(test_data)           
# 西语克劳福德可读性公式
语言支持对照表（中英对照）
函数名称	英语	德语	西班牙语	法语	意大利语	荷兰语	波兰语	俄语
flesch_reading_ease	✔	✔	✔	✔	✔	✔		✔
gunning_fog	✔						✔	

#### 西班牙语专用测试 
以下函数专为西班牙语设计（也可用于其他语言，但不推荐）： 
```python 
textstat.fernandez_huerta(text) # Fernández Huerta指数 textstat.szigriszt_pazos(text) # Szigriszt-Pazos指数 textstat.gutierrez_polini(text) # Gutiérrez de Polini公式 textstat.crawford(text) # Crawford公式 
``` 
各公式的详细信息请参考对应的文档注释。 
## 核心算法说明 
### Flesch 阅读易度公式 
```python 
textstat.flesch_reading_ease(text) 
``` 
返回 Flesch 阅读易度分数，分数对照表如下： 
| 分数 | 难度等级 |
 |-------|------------------| 
|90-100 | 非常容易 | 
|80-89 | 容易 | 
|70-79 | 较为容易 | 
|60-69 | 标准 | 
|50-59 | 较为困难 |
 |30-49 | 困难 | 
|0-29 | 非常难以理解 | 
> 扩展阅读：
 [维基百科](https://en.wikipedia.org/wiki/Flesch%E2%80%93Kincaid_readability_tests#Flesch_reading_ease) ```
Flesch-Kincaid 年级水平
python复制代码
textstat.flesch_kincaid_grade(text)
返回文本的 Flesch-Kincaid 年级水平评分。该评分对应美国学制，例如得分为 9.3 表示九年级学生可理解该文本。
扩展阅读请参考
(https://en.wikipedia.org/wiki/Flesch%E2%80%93Kincaid_readability_tests#Flesch%E2%80%93Kincaid_grade_level)

雾化指数（Gunning FOG 公式）
python复制代码
textstat.gunning_fog(text)
返回文本的 FOG 指数。该评分对应美国学制，例如得分为 9.3 表示九年级学生可理解该文本。
扩展阅读请参考
(https://en.wikipedia.org/wiki/Gunning_fog_index)

SMOG 指数
python复制代码
textstat.smog_index(text)
返回文本的 SMOG 指数。该评分对应美国学制，例如得分为 9.3 表示九年级学生可理解该文本。
注意：原始 SMOG 公式基于 30 个句子的样本验证，若文本少于 30 句统计结果可能不准确。本库要求至少 3 个句子才进行计算。
扩展阅读请参考
(https://en.wikipedia.org/wiki/SMOG)

自动可读性指数
python复制代码
textstat.automated_readability_index(text)
返回自动可读性指数（ARI），该数值近似表示理解文本所需的年级水平。例如得分为 6.5 表示适合 6-7 年级学生阅读。
扩展阅读请参考
(https://en.wikipedia.org/wiki/Automated_readability_index)

Coleman-Liau 指数
python复制代码
textstat.coleman_liau_index(text)
使用 Coleman-Liau  公式计算文本的年级水平。例如得分为 9.3 表示九年级学生可理解该文本。
扩展阅读请参考
(https://en.wikipedia.org/wiki/Coleman%E2%80%93Liau_index)

Linsear 写作公式
python  复制代码
textstat.linsear_write_formula(text)
使用 Linsear Write 公式计算文本的年级水平。例如得分为 9.3 表示九年级学生可理解该文本。
扩展阅读请参考
[维基百科](https://en.wikipedia.org/wiki/Linsear_Write)
Dale-Chall 可读性分数
python     复制代码
textstat.dale_chall_readability_score(text)
使用新 Dale-Chall 公式计算文本可读性，基于 3000 个常用英语单词表。评分对应如下年级水平：
分数	理解群体
4.9 或更低	平均四年级及以下学生
5.0–5.9	平均五至六年级学生
6.0–6.9	平均七至八年级学生
7.0–7.9	平均九至十年级学生
8.0–8.9	平均十一至十二年级学生
9.0–9.9	平均大学一至三年级学生
扩展阅读请参考
维基百科
综合可读性评估
python 复制代码
textstat.text_standard(text, float_output=False)
综合所有测试结果，返回文本所需的预估年级水平。
可选参数 float_output 控制是否返回浮点数结果，默认 False 返回字符串格式。

Spache  可读性公式
python  复制代码
textstat.spache_readability(text)
返回英语文本的年级水平。
特别适用于四年级及以下儿童读物。
扩展阅读请参考
维基百科 https://de.wikipedia.org/wiki/Lesbarkeitsindex#Wiener_Sachtextformel
McAlpine EFLaw 可读性分数
python   复制代码
textstat.mcalpine_eflaw(text)
评估英语作为外语学习者的文本可读性，重点关注"迷你词汇"数量和句子长度。
建议目标分数≤ 25。
扩展阅读请参考
这篇博客文章
Wiener Sachtextformel（德语）
python复制代码
textstat.wiener_sachtextformel(text, variant)
返回德语文本的年级水平评分。4 分表示非常容易，15 分表示非常困难。
扩展阅读请参考
维基百科
________________________________________
统计指标
音节计数
python复制代码
textstat.syllable_count(text)
统计文本总音节数。
英语使用 cmudict 词典，其他语言使用 Pyphen 模块。
词汇统计
python复制代码
textstat.lexicon_count(text, removepunct=True)
统计有效词汇数量。
可选参数 removepunct 控制是否过滤标点符号（默认开启）。
句子统计
python复制代码
textstat.sentence_count(text)
统计文本中的句子总数。
字符统计
python复制代码
textstat.char_count(text, ignore_spaces=True)
统计字符数量。
可选参数 ignore_spaces 控制是否忽略空格（默认开启）。
字母统计
python复制代码
textstat.letter_count(text, ignore_spaces=True)
统计不含标点的纯字母数量。
多音节词统计
python复制代码
textstat.polysyllabcount(text)
统计音节数 ≥3 的复杂词汇数量。
单音节词统计
python复制代码
textstat.monosyllabcount(text)
统计单音节简单词汇数量。
________________________________________
贡献指南
发现问题请提交 issue。
修复问题请提交 pull request。
1.	在 GitHub 上 Fork 本仓库（基于 master 分支开发）
2.	编写验证问题修复/功能实现的测试用例
3.	提交 Pull Request
开发环境配置
推荐使用 虚拟环境 或 Pipenv 隔离开发环境
bash复制代码
$ git clone https://github.com/<你的用户名>/textstat.git  # 克隆你的fork仓库
$ cd textstat
$ pip install -r requirements.txt  # 安装依赖

$ # 进行代码修改

$ python -m pytest test.py  # 运行测试

