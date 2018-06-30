import scrapy

class PriceSpider(scrapy.Spider):
    name = "getPrice"

    def start_requests(self):
        urls = [
            'https://eshop-prices.com/prices'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
        
        allgameSelector = response.xpath("/html[1]/body[1]/div[1]/table[1]/tbody[1]/tr")
#        gameRegionSelector = response.xpath("/html[1]/body[1]/div[1]/table[1]/thead[1]/tr[1]/th")
        
        for gameSelector in allgameSelector:
            
            name = gameSelector.xpath("th[1]/a[1]/text()").extract()
            
            priceSelector = gameSelector.xpath("td")
            price = []
            for areaPrice in priceSelector:
                price.append(areaPrice.xpath("text()").extract()[0])

            yield {
                'name' : name,
                'price' : price,
            }
        
#        skipFirst = True
#        regionHead = []
#        for region in gameRegionSelector:
#            if (skipFirst):
#                skipFirst = False
#                continue
#            regionHead.append(region.xpath("@title").extract())
#        yield {'regions':regionHead}