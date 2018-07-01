import scrapy

class RadioSpider(scrapy.Spider):
    name = "getRadio"

    def start_requests(self):
        urls = [
            'https://www.g-cores.com/categories/9'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
        allSelector = response.xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]")
        for i in range(2,22):
            selector = allSelector.xpath("div[%d]"%i)
            head = selector.xpath('div[1]/div[1]/span[1]/a[1]/text()').extract()[0]
            time = selector.xpath('div[1]/div[1]/text()').extract()[1]
            href = selector.xpath('div[1]/div[2]/a[1]/@href').extract()[0]
            imgSrc = selector.xpath('div[1]/div[2]/a[1]/img[1]/@src').extract()[0]
            imgTitle = selector.xpath('div[1]/div[2]/a[1]/img[1]/@alt').extract()[0]
            describe = selector.xpath('div[1]/div[3]/div[1]/text()').extract()[0]

            yield {
                'head' : head,
                'time' : time,
                'href' : href,
                'imgSrc' : imgSrc,
                'imgTitle' : imgTitle,
                'describe' : describe,
            } 