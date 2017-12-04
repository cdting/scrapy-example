# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from scrapy.pipelines.images import ImagesPipeline
import os
from scrapy.utils.project import get_project_settings
from scrapy.exceptions import DropItem


class BaiduimagePipeline(ImagesPipeline):
    IMAGES_STORE = get_project_settings().get("IMAGES_STORE")
    nm = 0
    # 下载图片
    def get_media_requests(self, item, info):
        image_urls = item["image_urls"]
        yield scrapy.Request(image_urls)

    # 完成下载后的动作
    def item_completed(self, result, item, info):
        # image_path获得下载图片的相对目录。
        # 一般是full/哈希值.jpg 
        image_path = [x["path"] for ok, x in result if ok]
        self.nm += 1
        os.rename(self.IMAGES_STORE + "/" + image_path[0], self.IMAGES_STORE + "/" + str(self.nm)+ ".jpg")
        return item
       
