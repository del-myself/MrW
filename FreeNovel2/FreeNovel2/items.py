# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NovelsItem(scrapy.Item):
    table_name = 'novels'
    title = scrapy.Field()
    author = scrapy.Field()
    word_count = scrapy.Field()
    category = scrapy.Field()
    title_url = scrapy.Field()
    title_id = scrapy.Field()
    novel_info = scrapy.Field()
    update_at = scrapy.Field()
    novel_img = scrapy.Field()
    # 总点击
    total_ck = scrapy.Field()
    # 月点击
    mon_ck = scrapy.Field()
    # 收藏数
    collect_counts = scrapy.Field()
    # 总推荐
    recommend = scrapy.Field()
    # 月推荐
    mon_reco = scrapy.Field()


class ChaptersItem(scrapy.Item):
    table_name = 'chapters'
    chapter_title = scrapy.Field()
    chapter_url = scrapy.Field()
    chapter_content = scrapy.Field()
    chapter_id = scrapy.Field()
    title_id = scrapy.Field()
    tc_id = scrapy.Field()
