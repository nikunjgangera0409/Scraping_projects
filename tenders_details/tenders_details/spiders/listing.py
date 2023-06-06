import json

import scrapy
from tenders_details.items import TendersDetailsItem
from tenders_details.spiders.helper import get_form_data
from urllib.parse import urlencode


class ListingSpider(scrapy.Spider):
    name = 'listing'
    allowed_domains = ['tenders.eil.co.in']
    start_urls = ['https://tenders.eil.co.in/NewTenders/Threshold']

    # handle_httpstatus_list = [404]
    def start_requests(self):
        headers = {"Content-Type": "application/x-www-form-urlencoded"}

        formdata = get_form_data()
        yield scrapy.FormRequest(url=self.start_urls[0], method='POST', body=urlencode(formdata),
                                 headers=headers,
                                 callback=self.parse1, dont_filter=True)

    def parse1(self, response):
        item = TendersDetailsItem()
        for i in response.xpath('//table[@id="ctl00_ContentPlaceHolder1_dlThreshold"]/tr/td/table'):
            item['tendor_no'] = i.xpath('./tr//span[contains(@id,"lblTenderNo")]/font/text()').get('').strip()
            item['tendor_issue_date'] = i.xpath('./tr/following-sibling::tr/td/span[contains(@id,'
                                                '"lblIssueDate")]/text()').get('').strip()
            item['tendor_bid_close_date'] = i.xpath('./tr/following-sibling::tr/td/following-sibling::td/span['
                                                    'contains(@id,"lblDueDate")]/text()').get('').strip()
            item['tendor_submission_date'] = i.xpath('./tr/following-sibling::tr/td[contains(text(),'
                                                     '"PO Date:")]/following-sibling::td/span[contains(@id,'
                                                     '"lblPODate")]/text()').get('').strip()
            item['tendor_discription'] = i.xpath('./tr/following-sibling::tr/td[contains(text(),"MR Description:")]/following-sibling::td/span[contains(@id,"lblMRDesc")]/text()').get('').strip()
            item['bidders'] = []
            for bidder in i.xpath('.//table//tr[@valign="top"]'):
                bidder1 = {
                'S.no': bidder.xpath('./td[1]/font/text()').get('').strip(),
                'Vendor_code': bidder.xpath('./td[2]/font/text()').get('').strip(),
                'Vendor_name': bidder.xpath('./td[3]/font/text()').get('').strip(),
                'reply_status': bidder.xpath('./td[4]/font/text()').get('').strip(),
                'Qualified After Technical Evaluation': bidder.xpath('./td[5]/font/text()').get('').strip()
                }
                item["bidders"].append(bidder1)
            winner = i.xpath('./tr/following-sibling::tr/td/following-sibling::td/span[contains(@id,"lblVendorName")]/text()').get('').strip()

            item['bid_winner'] = winner
            item['order_value'] = i.xpath('./tr/following-sibling::tr/td/following-sibling::td/span[contains(@id,"lblOrderValue")]/text()').get('').strip()

            yield item


# from scrapy.cmdline import execute
# execute("scrapy crawl listing".split(" "))
