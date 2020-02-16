import scrapy
import json

class PhoneSpider(scrapy.Spider):
    name = "phone"

    def start_requests(self):
        urls = [
            'https://www.gsmarena.com/samsung_galaxy_s20_ultra_5g-10040.php'
        ]

        for url in urls:
            yield scrapy.Request(url = url, callback = self.parse)
    
    def parse(self, response):
        details = {}
        for table in response.css('table'):
            # Get attribute.
            attribute = table.css('th::text').get()

            sub_attributes = {}
            for tr in table.css('tr'):

                # Bail early if not attribute is found.
                if (None == attribute):
                    continue

                # Get sub attribute.
                sub_attribute = tr.css('.ttl a::text').get()
                if None == sub_attribute:
                    continue

                # Get sub attribute info.
                info = tr.css('.nfo::text').get()
                if None == info:
                    info = tr.css('.nfo a::text').get()
                sub_attributes[sub_attribute] = info

            details[attribute] = sub_attributes

        yield details