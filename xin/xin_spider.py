import requests
from lxml import etree

from config.config import *


class X_spider(object):

    def get_html(self, registration_number):

        resp = requests.get(url=url.format(registration_number)).text

        return resp
    def analysis_html(self,resp):
        resp = etree.HTML(resp)
        div_resp = resp.xpath('//*[@class="zx-ent-info"]')
        item = {}
        if div_resp:
            title = div_resp[0].xpath('./div/h3/a/text()')
            if title:
                item['title'] = title[0]
            else:
                item['title'] = ''
            name = div_resp[0].xpath('./div/div/span/span[2]/@title')
            if name:
                item['name'] = name[0]
            else:
                item['name'] = ''
            capital = div_resp[0].xpath('./div/div/span[2]/text()')
            if capital:
                item['capital'] = capital[0]
            else:
                item['capital'] = ''
            date = div_resp[0].xpath('./div/div/span[3]/text()')
            if date:
                item['time'] = date[0]
            else:
                item['time'] = ''
            site = div_resp[0].xpath('./div/div/span[4]/text()')
            if site:
                item['site'] = site[0]
            else:
                item['site'] = ''
            scope = div_resp[0].xpath('./div/div/span[5]/@data-content')
            if scope:
                item['scope'] = scope[0]
            else:
                item['scope'] = ''
            registration_number=div_resp[0].xpath('./div/div[2]/span/em/text()')
            if registration_number:
                item['registration_number'] = registration_number[0]
            else:
                item['registration_number'] = ''
            return item
    def run(self,registration_number):
        resp=self.get_html(registration_number)
        item=self.analysis_html(resp)
        return item
if __name__ == '__main__':
    x=X_spider()
    print(x.run('91350302087425297W'))