# -*- coding: utf-8 -*-
# @Author : lihuiwen
# @file : goods_spider
# @Email : huiwennear@163.com
# @Time : 2024/5/23 14:00
from urllib.parse import urljoin

import scrapy
from scrapy import Request


class GoodsSpider(scrapy.Spider):
    name = "goods_spider"

    def __init__(self):
        self.list_headers = {
            'device-memory': '8',
            'sec-ch-device-memory': '8',
            'dpr': '1',
            'sec-ch-dpr': '1',
            'viewport-width': '1920',
            'sec-ch-viewport-width': '1920',
            'rtt': '250',
            'downlink': '6.2',
            'ect': '4g',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-ch-ua-platform-version': '"10.0.0"',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-User': '?1',
            'Sec-Fetch-Dest': 'document',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cookie': 'session-id=144-0505994-1538449; session-id-time=2082787201l; i18n-prefs=USD; lc-main=zh_CN; sp-cdn="L5Z9:HK"; skin=noskin; ubid-main=135-0977405-0565156; session-token=bk6CHdcphPvhkGj5RJfoN1Z85lvwoB5LmX0sd2X3z3BZCIEauAknCltkiMIJBHThnZq3+cG/DwhP5FloDezHwAil64hF43zP75dIzy3iqV8AUKfRTx3y/GpPUefE1T+YhVTo6coAUPxq/W1a5S5CzwyCV29YulFtR5LlSMTcg9e/oxoO1ModT98H2JnfNMlWGT4rgcxvIMbdN6pU5GyPcFGF1oB/Ofkx53HWeuUf/VHc70+qp0XzrGnx+/HSpV28xIMQ80XBUm7Uoa/5qhVBuPEscwaokH4d10uEPKPm95lWK0OpDi7LzdYcQSO4hqx1S1MRhwbA3RWaCfbuM00tuKqeh6f8+PgS; csm-hit=adb:adblk_no&t:1716434454228&tb:QA89W053S9Q0GMK7QAE6+sa-QA89W053S9Q0GMK7QAE6-ZHF7XQ1HF0E0DQF0PGZN|1716434454228',
        }
        self.detail_headers = {
            'device-memory': '8',
            'sec-ch-device-memory': '8',
            'dpr': '1',
            'sec-ch-dpr': '1',
            'viewport-width': '1920',
            'sec-ch-viewport-width': '1920',
            'rtt': '100',
            'downlink': '10',
            'ect': '4g',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-ch-ua-platform-version': '"10.0.0"',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-User': '?1',
            'Sec-Fetch-Dest': 'document',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cookie': 'session-id=144-0505994-1538449; session-id-time=2082787201l; i18n-prefs=USD; lc-main=zh_CN; sp-cdn="L5Z9:HK"; skin=noskin; ubid-main=135-0977405-0565156; session-token=V5Hj1NoAn60oz/TOJM0EgzeKJj6J1dC2qX3JSWrYkYoNo/0nWD+2xWR/8ltzeXEa0n4iUfnrABhMWQbJNZf2CSO2UapuwO1qdYebmNNSYZeHM0olhh+/pdUrkKS6tHC6EhAmCJMl6l2EMEbHvyqg6TQoJM4u8WvH3ec4pLayTD2QDUZK83ci4gmiy819L+/ZXupT09CjA1juRNRqdyKikLvmZkymgeOJXhZPYltdWo+DDcdlRAXDcTbQ0GNcnOWB855nEBYeGWKRMqPJO4wYrOw8X7ThnWD/kqLnJuQ6onoTi7ZnuwcXnmdozgIlzsRvw0tGZBunI6D5Dh29kXjJJDd74BRnm1EC; csm-hit=adb:adblk_no&t:1716451534511&tb:00SSKCCJSEKG9BC2WMBQ+s-00SSKCCJSEKG9BC2WMBQ|1716451534511',
        }
        self.proxy = ""

    def start_requests(self):
        keyword = "华为"
        page = 1
        req_url = f'https://www.amazon.com/-/zh/s?k={keyword}&page={page}&language=zh'
        req_meta = {"keyword": keyword, "page": page,
                    # "proxy":self.proxy
                    }
        yield Request(url=req_url, method='GET', headers=self.list_headers,
                      callback=self.detail_page_parse, meta=req_meta,
                      dont_filter=True)

    def detail_page_parse(self, response):
        keyword = response.meta.get('keyword')
        page = response.meta.get('page')
        div_list = response.xpath('//div[@class="a-section"]/div[@class="puisg-row"]')
        if (div_list):
            for div_index in range(len(div_list)):
                div_item = div_list[div_index]
                goods_item = {}
                goods_item["name"] = div_item.xpath(
                    './/span[@class="a-size-medium a-color-base a-text-normal"]/text()').extract_first().strip()
                goods_item["detail_url"] = urljoin("https://www.amazon.com/", div_item.xpath(
                    './/a[span[@class="a-size-medium a-color-base a-text-normal"]]/@href').extract_first().strip())
                goods_item["price"] = div_item.xpath('.//span[@class="a-offscreen"]/text()').extract_first().strip()
                req_meta = {"keyword": keyword, "goods_item": goods_item,
                            # "proxy":self.proxy
                            }
                yield Request(url=goods_item["detail_url"], method='GET', headers=self.detail_headers,
                              callback=self.detail_parse, meta=req_meta,
                              dont_filter=True)
            page += 1
            req_url = f'https://www.amazon.com/-/zh/s?k={keyword}&page={page}&language=zh'
            req_meta = {"keyword": keyword, "page": page}
            yield Request(url=req_url, method='GET', headers=self.list_headers,
                          callback=self.detail_page_parse, meta=req_meta,
                          dont_filter=True)
        else:
            print("没有下一页")

    def detail_parse(self, response):
        keyword = response.meta.get('keyword')
        goods_item = response.meta.get('goods_item')
        goods_item["goods_detail"] = (
            "\n".join([x.strip() for x in response.xpath('//*[@id="feature-bullets"]/ul//text()').extract()])).strip()
        print(goods_item)
