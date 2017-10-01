import scrapy
from scrapy import Request
from blog.items import BlogItem
#该项目存在问题：读取不出来没有分类的name，url，author，skim，sort
#只能读出来有分类的博客
class Blog(scrapy.Spider):

    name = 'blog'
    headers = {'User-Agent':
                   'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0'
               }
    global num
    num = int(input('请输入你要执行的几个页面？'))

    def start_requests(self):
        url = 'http://blog.csdn.net/'
        yield Request(url, headers=self.headers)

    def parse(self, response):

        item = BlogItem()
        items = response.xpath('//div[@class="blog_list_wrap"]/dl[@class="blog_list clearfix"]')

        for i in items:
            item['name'] = i.xpath('.//h3[@class="csdn-tracking-statistics"]/a/text()').extract()
            item['url'] = i.xpath('.//h3[@class="csdn-tracking-statistics"]/a/@href').extract()
            item['author'] = i.xpath('.//dt/a[2]/text()').extract()
            item['skim'] = i.xpath('.//dd/div[2]/div[2]/span/em/text()').extract()
            item['sort'] = i.xpath('.//dd/div[2]/div[1]/span/a/text()').extract()

            yield item

        for i in range(1, num):
            next_url = 'http://blog.csdn.net/?&page={}'.format(i)
            yield Request(next_url, headers=self.headers)





