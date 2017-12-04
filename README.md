## 安装scrapy
### Ubuntu:
- 安装非Python的依赖:
 ```
 sudo apt-get install python-dev python-pip libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev
 ```
- 安装scrapy
```
sudo pip install scrapy
```
### Window

>以Python3.5为例

1. 升级pip
    ```shell
    python -m pip install -U pip
    ```
2. 安装wheel,用于安装本地whl文件
    ```shell
    pip install wheel
    ```
3. 安装Pillow用于操作图片
    ```shell
    pip install Pillow
    ```
4. 下载Twisted 和  Scrapy对应Python版本的whl文件[下载链接](https://www.lfd.uci.edu/~gohlke/pythonlibs/),

    - 安装下载的Twisted和Scrapy文件，cd到下载路径
    ```
    pip install [文件名称].whl
    ```
5.  查看Scrapy是否安装成功
    ```
    scrapy -h
    ```

## 初始化项目
```shell
scrapy startproject [项目名称]
```
### 目录结构

```
├── myScrapy 　//项目的Python模块
│   ├── __init__.py　//
│   ├── items.py //项目的目标文件
│   ├── middlewares.py　//
│   ├── pipelines.py //项目的管道文件
│   ├── settings.py //项目的设置文件
│   └── spiders　//存储爬虫代码目录
│       └── __init__.py
├── readme.md
└── scrapy.cfg //项目配置文件
```

## items.py文件

- 用于定义存储字段对象，需要继承scrapy.Item

```
例：
    name  = scrapy.Field()
    age = scrapy.Field()
    后面的scrapy.Field()是固定统一的。这种类似于Java中的对象属性
```

## 初始化爬虫编码

 - 首先定位目录到spiders文件夹下，运行命令:

 ```shell
 scrapy genspider [爬虫名称] [爬虫域范围]
 ```

- 执行命令后会在spiders文件夹下生成一个py文件

```shell
//这个规则都是固定的，parse方法名称不能改，重写，这里用于处理爬取获得结果。
class BaiduSpider(scrapy.Spider):
    name = 'baidu'   //爬虫名称
    allowed_domains = ['image.baidu.com']   //域名范围
    start_urls = ['http://image.baidu.com/']   //开始url，可设置多个

    //重写parse方法，些爬虫代码的地方
    def parse(self, response):
        pass
```

## pipelines.py 管道文件

- 需要重写process_item方法，用于处理爬虫返回的结果,如存储，下载等等。   
- 有两个参数：item - 爬取的item（内容）,spider - 爬取该item的Spider

## 启动爬虫项目
- cd到spiders目录，运行
```
 scrapy crawl [爬虫名称] //bdimage.py文件中的name属性值
 ```

>` 注：`在安装完Scrapy后，修改settings.py文件中的`IMAGES_STORE`路径，即可直接运行`scrapy crawl bdimage`测试项目