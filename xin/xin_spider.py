import json
import re

import requests
from lxml import etree

from config.config import *


class X_spider(object):

    def get_html(self, registration_number):

        resp = requests.get(url=url.format(registration_number)).content.decode()

        return resp

    def analysis_html(self, resp):
        item = {
            "title": "",
            "name": "",
            "capital": "",
            "time": "",
            "site": "",
            "scope": "",
            "registration_number": "",
        }
        title = re.findall('"entName":"(.*?)"', resp, re.S)
        if title:
            item['title'] = title[0]
            item['title'] = eval("u'" + title[0] + "'")
        name = re.findall('"legalPerson":"(.*?)"', resp, re.S)
        if name:
            item['name'] = eval("u'" + name[0] + "'")
        capital = re.findall('"regCap":"(.*?)"', resp, re.S)
        if capital:
            item['capital'] = eval("u'" + capital[0] + "'")
        date = re.findall('"validityFrom":"(.*?)"', resp, re.S)
        if date:
            item['time'] = eval("u'" + date[0] + "'")
        site = re.findall('"domicile":"(.*?)"', resp, re.S)
        if site:
            item['site'] = eval("u'" + site[0] + "'")
        scope = re.findall('"scope":"(.*?)"', resp, re.S)
        if scope:
            item['scope'] = eval("u'" + scope[0] + "'")
        registration_number = re.findall('"queryWord":"(.*?)"', resp, re.S)
        if registration_number:
            item['registration_number'] = eval("u'" + registration_number[0] + "'")
        # print(item)
        return item
        # for i in a:
            # entName=i.replace(':','=')

            # i = "u'" + i + "'"
            # print(eval(i))
            # print(eval(a))
            # resp = etree.HTML(resp)
            # div_resp = resp.xpath('//*[@class="info"]')
            # item = {}
            # if div_resp:
            #     title = div_resp[0].xpath('./div/h3/a/text()')
            #     if title:
            #         item['title'] = title[0]
            #     else:
            #         item['title'] = ''
            #     name = div_resp[0].xpath('./div/div/span/span[2]/@title')
            #     if name:
            #         item['name'] = name[0]
            #     else:
            #         item['name'] = ''
            #     capital = div_resp[0].xpath('./div/div/span[2]/text()')
            #     if capital:
            #         item['capital'] = capital[0]
            #     else:
            #         item['capital'] = ''
            #     date = div_resp[0].xpath('./div/div/span[3]/text()')
            #     if date:
            #         item['time'] = date[0]
            #     else:
            #         item['time'] = ''
            #     site = div_resp[0].xpath('./div/div/span[4]/text()')
            #     if site:
            #         item['site'] = site[0]
            #     else:
            #         item['site'] = ''
            #     scope = div_resp[0].xpath('./div/div/span[5]/@data-content')
            #     if scope:
            #         item['scope'] = scope[0]
            #     else:
            #         item['scope'] = ''
            #     registration_number=div_resp[0].xpath('./div/div[2]/span/em/text()')
            #     if registration_number:
            #         item['registration_number'] = registration_number[0]
            #     else:
            #         item['registration_number'] = ''
            # return item

    def run(self, registration_number):
        resp = self.get_html(registration_number)
        item = self.analysis_html(resp)
        return item


if __name__ == '__main__':
    x = X_spider()
    print(x.run('91430100MA4PR1JAXA'))
