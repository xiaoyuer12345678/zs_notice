# -*- coding: utf-8 -*-
import scrapy
import json
from scrapy.selector import Selector
from ..items import ZsNoticeItem

class ZsggSpider(scrapy.Spider):
    name = 'zsgg'
    # allowed_domains = ['http://www.cs.com.cn/']
    # start_urls= ['http://xinpi.cs.com.cn/page/xp/zuixinGg.html']
    start_urls=['http://xinpi.cs.com.cn//new/data/bulletin/all_all/1.json']
    #url = 'http://xinpi.cs.com.cn/new/file/bulletin/2019/12/7/1207143734.PDF'
    # #url = 'http://www.czce.com.cn/cn/DFSStaticFiles/Future/2019/20191206/FutureDataDelsettle.htm'
    # headers = {
    #     # 'cookie': 'csrftoken=e48c6b1f429014ea3349bbbd2132bcba; tt_webid=6735613024013714948; s_v_web_id=7e83e5e72e26d297d3833b40fb44b88c; WEATHER_CITY=%E5%8C%97%E4%BA%AC; __tasessionId=x43wsz2xs1568257125498; tt_webid=6735613024013714948',
    #     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
    #     'x-requested-with': 'XMLHttpRequest',
    #     'referer': 'http://xinpi.cs.com.cn/page/xp/zuixinGg.html',
    #     # 'path': '/api/search/content/?aid=24&app_name=web_search&offset=0&format=json&keyword=lolita&autoload=true&count=20&en_qc=1&cur_tab=1&from=search_tab&pd=synthesis&timestamp=1568258424601',
    # }
    i = 1
    # i = i + 1



    def parse(self, response):
        data = json.loads(response.body_as_unicode())
        gg_url = data['rows']
        print(gg_url)
        print(data['rows'][0]['cell'][4])
        #today = datetime.date.today()
        if self.i < 3:
            self.i = self.i + 1
            url = 'http://xinpi.cs.com.cn//new/data/bulletin/all_all/'+ str(self.i) +'.json'
            print(str(self.i))
            print(url)
            yield scrapy.Request(url)


        page_url = 'http://xinpi.cs.com.cn/new/file/'

        selector = Selector(response)
        ggs = selector.xpath("//table[@id='table_all_all']/tbody")
        #dat = selector.jsonpath("//")
        print(ggs)

        #download_url = 'http://xinpi.cs.com.cn/new/file/bulletin/2019/12/9/1207148030.PDF'
        # download_url = page_url + gg_url
        # print(download_url)
        item = ZsNoticeItem()

        # item['file_urls'] = [download_url]
        # yield item
        # download_url = 'http://xinpi.cs.com.cn/new/file/bulletin/2019/12/9/1207147741.PDF'
        # item = ZsNoticeItem()
        # item['file_urls'] = [download_url]
        # yield item
        # for notice in ggs:
        #     article_url =
        #     article_url = notice.xpath("tr/td[@class='title']/a/@href").extract_first()
        #     articles_url = 'http://xinpi.cs.com.cn/new/file/bulletin/2019/12/9/1207148030.PDF'
        #     print(article_url)
        #     print(articles_url)
        #
        #     item["file_urls"] = [articles_url]
        #     yield item
        for notice in gg_url:
            article_url = page_url + notice['cell'][4]
            # article_url = notice.xpath("tr/td[@class='title']/a/@href").extract_first()
            # articles_url = 'http://xinpi.cs.com.cn/new/file/bulletin/2019/12/9/1207148030.PDF'
            print(article_url)
            # print(articles_url)

            item["file_urls"] = [article_url]
            yield item

        #download_url = ''+ today.strftime(%Y%m%d) +

