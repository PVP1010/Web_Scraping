import scrapy


class LustranewparsSpider(scrapy.Spider):
    name = "lustranewpars"
    allowed_domains = ["https://colorlon.ru/"]
    start_urls = ["https://colorlon.ru/catalog/lyustry"]

    def parse(self, response):
        lustras = response.css('div.product-card')
        for lustra in lustras:
            yield {
                'name' : lustra.css('div.product-card__body a.product-card__name::text').get().strip(),   # get()-берём первое попавшееся, strip()-убираем пробелы
                'price' : lustra.css('div.product-card__price::text').get().strip(),                      # get()-берём первое попавшееся, strip()-убираем пробелы
                'url' : lustra.css('a').attrib['href'].strip()                                            # strip()-убираем пробелы
            }
# lustraparsscrapy