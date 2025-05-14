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
