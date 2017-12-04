# -*- coding: utf-8 -*-
import scrapy
from baiduImage.items import BaiduimageItem
import json
import os
import shutil


class BdimageSpider(scrapy.Spider):
    name = 'bdimage'
    allowed_domains = ['image.baidu.com']
    pn = 0
    init_url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E8%AF%81%E4%BB%B6%E7%85%A7&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&word=%E8%AF%81%E4%BB%B6%E7%85%A7&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=3&fr=&rn=30&gsm=1e&1511849521600=&pn='
    start_urls = [init_url + str(pn)]
    def __init__(self):
        # shutil.rmtree("C:/Users/mibok/Desktop/images/")
        # os.remove(
        #     "E:/Gitlab/python/11-crawler/scrapy/baiduImage/baiduImage/spiders/j.json")

    def parse(self, response):
        data = json.loads(response.text)["data"]
        # data = ["https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=3564655510,851815907&fm=27&gp=l,0.jpg", "https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=2327293755,3239161135&fm=27&gp=0.jpg", "https://ss2.bdstatic.com/70cFvnSh_Q1YnxGkpoWK1HF6hhy/it/u=685078701,332814593&fm=27&gp=0.jpg", "https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=1248758867,1325487746&fm=27&gp=0.jpg"]
    
        for each in data: 
            if not each.__contains__("thumbURL"):
                continue
            item = BaiduimageItem()
            item["image_urls"] = each["thumbURL"]
            yield item
        self.pn += 1  
        yield scrapy.Request(self.init_url + str(self.pn), callback=self.parse)


