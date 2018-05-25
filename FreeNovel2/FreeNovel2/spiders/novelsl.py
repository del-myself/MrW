# -*- coding: utf-8 -*-
from datetime import datetime

import scrapy
from FreeNovel2.items import NovelsItem
from FreeNovel2.items import ChaptersItem
from scrapy_redis.spiders import RedisSpider


class NovelsSpider(RedisSpider):
    name = 'novels'
    allowed_domains = ['www.ybdu.com']
    # start_urls = ['https://www.ybdu.com/book1/0/1/']

    def parse(self, response):
        li_list = response.xpath('//div[@id="content"]//div[@class="clearfix rec_rullist"]/ul')
        for li_ in li_list:
            novel = NovelsItem()
            novel['title'] = li_.xpath('.//li[@class="two"]/a/text()').extract_first().replace('全文阅读', '')
            novel['author'] = li_.xpath('.//li[@class="four"]/text()').extract_first()
            word_count = li_.xpath('.//li[@class="five"]/text()').get()
            if word_count:
                novel['word_count'] = int(word_count.replace('K', '')) * 512
            else:
                novel['word_count'] = 1
            category = li_.xpath('.//li[@class="sev"]/span/a/text()').get()
            if category:
                novel['category'] = category.rsplit('全本')[-1].rsplit('小说')[0]
            else:
                novel['category'] = '不明'
            novel['title_url'] = li_.xpath('.//li[@class="two"]/a/@href').extract_first()
            novel['title_id'] = li_.xpath('.//li[@class="two"]/a/@href').extract_first().split('/')[-2]
            novel['update_at'] = li_.xpath('.//li[@class="six"]/a/text()').get()
            info_url = li_.xpath('.//li[@class="three"]/a/@href').get()
            yield scrapy.Request(url=info_url, callback=self.parse_novel_info, meta={'novel': novel})
            yield scrapy.Request(url=novel['title_url'], callback=self.parse_chapter,
                                 meta={'title_id': novel['title_id']})
        next_page = response.xpath('//div[@id="pagelink"]/a[@class="next"]/@href').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

    def parse_novel_info(self, response):
        novel = response.meta['novel']
        novel_info = response.xpath('//div[@class="intro"]/text()').extract()
        if novel_info:
            novel['novel_info'] = '<br>'.join([i.replace('\xa0', '&nbsp;') for i in novel_info])
        else:
            novel['novel_info'] = '暂无简介'
        update_at = response.xpath('//table[@class="ui_tb1"]/tbody/tr[3]/td/div[1]/text()').get()
        if update_at:
            update_at = update_at.replace('更新时间：', '')
            novel['update_at'] = datetime.strptime(update_at, '%Y-%m-%d')
        else:
            novel['update_at'] = datetime.strptime('2017-3-11', '%Y-%m-%d')
        novel['novel_img'] = ''.join(['https://www.ybdu.com', response.xpath('//div[@class="pic"]/img/@src').get()])
        num_list = [num.split('：')[-1] for num in response.xpath('//div[@class="pic"]/div/text()').extract()]
        # 总点击
        novel['total_ck'] = num_list[0]
        # 月点击
        novel['mon_ck'] = num_list[1]
        # 收藏数
        novel['collect_counts'] = num_list[3]
        # 总推荐
        novel['recommend'] = num_list[4]
        # 月推荐
        novel['mon_reco'] = num_list[5]
        yield novel

    def parse_chapter(self, response):
        t_id = response.meta['title_id']
        chapter_list = response.xpath('//ul[@class="mulu_list"]/li')
        for chapter_ in chapter_list:
            chapter_title = chapter_.xpath('.//a/text()').extract_first()
            chapter_url = ''.join([response.url, chapter_.xpath('.//a/@href').extract_first()])
            chapter_id = chapter_.xpath('.//a/@href').extract_first().rsplit('.')[0]
            yield scrapy.Request(url=chapter_url, callback=self.parse_chapter_content,
                                 meta={
                                     'chapter_title': chapter_title,
                                     'chapter_url': chapter_url,
                                     'chapter_id': chapter_id,
                                     'title_id': t_id,
                                 })

    def parse_chapter_content(self, response):
        chapter = ChaptersItem()
        chapter['chapter_title'] = response.meta['chapter_title']
        chapter['chapter_url'] = response.meta['chapter_url']
        chapter['chapter_content'] = '<br>'.join([i.replace('\xa0', '&nbsp;')
                                                  for i in response.xpath('//div[@id="htmlContent"]/text()').extract()])
        chapter['title_id'] = response.meta['title_id']
        chapter['chapter_id'] = response.meta['chapter_id']
        chapter['tc_id'] = '%s_%s' % (chapter['title_id'], chapter['chapter_id'])

        yield chapter
