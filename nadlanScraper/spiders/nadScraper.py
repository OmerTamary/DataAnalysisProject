import scrapy
from ..items import NadlanscraperItem
import sys
class NadscraperSpider(scrapy.Spider):
    name = 'nadScraper'
    page_number = 2
    start_urls = [
                'https://www.ad.co.il/nadlanprice?city=tel-aviv&hood=%D7%A0%D7%95%D7%94-%D7%91%D7%A8%D7%91%D7%95%D7%A8'
                ,'https://www.ad.co.il/nadlanprice?city=tel-aviv&hood=%d7%a9%d7%a4%d7%99%d7%a8%d7%90'
                ,'https://www.ad.co.il/nadlanprice?city=tel-aviv&hood=%d7%94%d7%aa%d7%a7%d7%95%d7%95%d7%94'
                , 'https://www.ad.co.il/nadlanprice?city=tel-aviv&hood=%d7%99%d7%93-%d7%90%d7%9c%d7%99%d7%94%d7%95'
                ,'https://www.ad.co.il/nadlanprice?city=tel-aviv&hood=%d7%a4%d7%9c%d7%95%d7%a8%d7%a0%d7%98%d7%99%d7%9f'
                ,'https://www.ad.co.il/nadlanprice?city=tel-aviv&hood=%d7%a0%d7%95%d7%94-%d7%97%d7%9f'
                ,'https://www.ad.co.il/nadlanprice?city=tel-aviv&hood=%d7%a0%d7%95%d7%94-%d7%91%d7%a8%d7%91%d7%95%d7%a8'
                ,'https://www.ad.co.il/nadlanprice?city=tel-aviv&hood=%d7%a2%d7%96%d7%a8%d7%90'
            ]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse,dont_filter=True)

    def parse(self, response):
        base_url = response.url
        yield scrapy.Request(response.url, callback=self.parse_area, cb_kwargs= dict(base_url=base_url))
        NadscraperSpider.page_number = 2


    def parse_area(self, response,base_url):           

        all_date = response.css('td:nth-child(1)').css('::text').getall()
        all_address = response.css('td:nth-child(3)').css('::text').getall()
        all_numOfRooms = response.css('td:nth-child(4)').css('::text').getall()
        all_size = response.css('td:nth-child(5)').css('::text').getall()
        all_floor = response.css('td:nth-child(6)').css('::text').getall()
        all_price = response.css('td:nth-child(7)').css('::text').getall()
        all_pricePerMeter = response.css('td:nth-child(8)').css('::text').getall()
        all_buildYear = response.css('td:nth-child(9)').css('::text').getall()
        area = response.css('.btn-sm+ .btn-sm .me-2').css('::text').get()

        item = NadlanscraperItem()
        for i  in range(len(all_date)):
            try:
                item['area'] = area
                print(area)
            except:
                item['area'] = "None"
            try:
                item['date'] = all_date[i]
            except:
                item['date'] = "None"
            try:
                item['address'] = all_address[i]
            except:
                item['address'] = "None"
            try:
                item['numOfRooms'] = all_numOfRooms[i]
            except:
                item['numOfRooms'] = "None"
            try:
                item['size'] = all_size[i]
            except:
                item['size'] = "None"
            try:
                item['floor'] = all_floor[i]
            except:
                item['floor'] = "None"
            try:
                item['price'] = all_price[i]
            except:
                item['price'] = "None"
            try:
                item['pricePerMeter'] = all_pricePerMeter[i]
            except:
                item['pricePerMeter'] = "None"
            try:
                item['buildYear'] = all_buildYear[i]
            except:
                item['buildYear'] = "None"

            yield item
        
        next_page = base_url+"&pageindex="+str(NadscraperSpider.page_number)
        if NadscraperSpider.page_number <= 100:
            NadscraperSpider.page_number+=1 
            yield response.follow(next_page, callback = self.parse_area,cb_kwargs= dict(base_url=base_url))
