# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TendersDetailsItem(scrapy.Item):
    tendor_no = scrapy.Field()
    tendor_issue_date = scrapy.Field()
    tendor_bid_close_date = scrapy.Field()
    tendor_submission_date = scrapy.Field()
    tendor_discription = scrapy.Field()
    bidders = scrapy.Field()
    bid_winner = scrapy.Field()
    order_value = scrapy.Field()


