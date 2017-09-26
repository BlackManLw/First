import scrapy
from douban_movie.items import DoubanMovieItem
from scrapy import Request

class DouBan(scrapy.Spider):
    name = "douban"
    headers = {'user-agent':
               'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Mobile Safari/537.36'
               }

    def start_requests(self):
        url = 'https://movie.douban.com/top250'
        yield Request(url, headers=self.headers)

    def parse(self, response):
        item = DoubanMovieItem()

        movies = response.xpath('//ol[@class="grid_view"]/li')

        for movie in movies:

            item['rank'] = movie.xpath('.//div[@class="pic"]/em/text()').extract()[0]
            item['score'] = movie.xpath('.//div[@class="star"]/span[@class="rating_num"]/text()').extract()[0]
            item['name'] = movie.xpath('.//div[@class="hd"]/a/span[1]/text()').extract()[0]

            yield item
        next_url = response.xpath('//span[@class="next"]/a/@href').extract()
        if next_url:
            next_url = 'https://movie.douban.com/top250' + next_url[0]
            yield Request(next_url, headers=self.headers)



