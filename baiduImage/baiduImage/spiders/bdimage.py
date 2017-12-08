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

    def parse(self, response):
        data = json.loads(response.text)["data"]
    
        for each in data: 
            if not each.__contains__("thumbURL"):
                continue
            item = BaiduimageItem()
            item["image_urls"] = each["thumbURL"]
            yield item
        self.pn += 1  
        yield scrapy.Request(self.init_url + str(self.pn), callback=self.parse)


