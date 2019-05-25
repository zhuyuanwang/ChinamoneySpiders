# -*- coding: utf-8 -*-
import scrapy
import json
from ..settings import DEFAULT_REQUEST_HEADERS
from ..items import ChinamoneyprojectItem


class CmSpider(scrapy.Spider):
    name = 'cm'
    allowed_domains = ['www.chinamoney.com.cn']
    start_urls = ['http://www.chinamoney.com.cn/']

    def start_requests(self):
        for page in range(1, 3):
            form_data = {
                'eventCode': '100104',
                'drftClAngl': '1001',
                'bondNameOrCode':'',
                'pageNo': str(page),
                'pageSize': '30',
                'startDate': '1977-04-01',
                'endDate': '2019-04-25',
                'limit': '1',
                'timeln': '1',
                        }
            start_url = 'http://www.chinamoney.com.cn/ags/ms/cm-u-notice-issue/majorMatters'
            yield scrapy.FormRequest(url=start_url,formdata=form_data,callback=self.parse_info,headers=DEFAULT_REQUEST_HEADERS)

    def parse_info(self, response):
        item = ChinamoneyprojectItem()
        datajson = json.loads(response.text)
        recordsdata = datajson['records']
        for data in recordsdata:
            item['title'] = data['title']
            pdfdownloadurl = 'http://www.chinamoney.com.cn/dqs/cm-s-notice-query/fileDownLoad.do?contentId={}&priority=0&mode=open'.format(data['contentId'])
            item['contentId'] = pdfdownloadurl
            item['releaseDate'] = data['releaseDate']
            pdfdetailsurl = 'http://www.chinamoney.com.cn' + data['draftPath']
            item['draftPath'] = pdfdetailsurl
            yield item
