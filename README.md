# 牛客排名信息爬取



## 简介

### 信息爬取方式：

1. 使用 $requests$ 方式的 $BeautifulSoup$ 匹配模式

2. 使用 $scrapy$ 框架的 $xpath$ 匹配模式




### 数据存储：

主要存储在前缀为 $data$ 的文件夹及文件内



### 数据处理：

采用 $plotly$ 库进行数据分析作图，图标为 $html$ 格式（浏览器打开）



## 项目演示

位于 $design$ 文件夹下的 $demo preview.mp4$ 

首先打开 $design$ 文件夹下的 $analysis.py$ 文件运行（最好在 $pycharm$ 下运行），然后根据提示去输入你得要求，就可以得到所要的信息。





## 库函数安装

请提前安装好以下库函数，若运行时报错，可以打开文件寻找未安装的库函数(由于是以前实现的，忘了为其打包环境，可以直接安装函数)。

```
numpy,scipy,openpyxl,plotly,scrapy,lxml,re,requests,user_agent,bs4,
```

**为避免出现意外，请将整个项目放在纯英文路径下。**



## 实现过程

### 信息爬取：

1. 首先对原始网站[Rating排行榜_程序设计竞赛能力竞技榜_牛客竞赛OJ (nowcoder.com)](https://ac.nowcoder.com/acm/contest/rating-index)进行榜单爬取，收集目前页面内的信息，然后收集团队主页链接。

2. 接着对团队主页链接进行爬取，进一步爬取团队信息和成员链接，完善团队信息。

3. 最后对通过成员链接对成员主页进行爬取，完善成员信息。

**$requests$ 模式对按顺序对任务 $1$ 到 $3$ 爬取，$scrapy$ 模式建立 $3$只爬虫对任务 $1$ 到 $3$ 顺序爬取。**



### 数据储存：

$1.requests$ 模式将收集到的数据存放在

```
\design\BS4\Data_Rank\
\design\BS4\Data_Member\
```

$2.scrapy$ 模式将收集到数据存放在

```
\design\Design\spiders\data_Rank
\design\Design\spiders\data_member
```

**文件名后缀数字代表爬取的页数。**



### 数据处理

使用 $plotly$ 库对不同数据进行可视化，加入数据拟合函数拟合方程便于分析。

图像为 $html$格式，需用浏览器打开。

图像存放在

```
\design\data_analysis\img...
```

$img$ 后缀数字为查询页数。



### 运行细节

由于该项目会爬取大量网页获取信息，且大数据下涉及上万的网页爬取，时间消耗大，因此对所有爬取的结果进行保存，下次使用时将直接调用数据返回结果（数据以搜索页数分开存储），若想要对某个数据重新爬取，只需要到

```
\design\BS4\Data_Rank\
\design\BS4\Data_Member\
\design\Design\spiders\data_Rank\
\design\Design\spiders\data_member\
```

目录下删掉对应页数后缀的文件即可重新爬取。

**数据集已经预先加载入页数为2，10，20，50，100的数据，可直接使用。**

**页数为1由于爬取页数较少，将会重新爬取，不会直接调用返回。**
