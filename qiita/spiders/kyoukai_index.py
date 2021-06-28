import scrapy


class KyoukaiIndexSpider(scrapy.Spider):
    #spaiderの名前
    name = 'kyoukai_index'
    #アクセスするドメイン
    allowed_domains = ['be-tech.ne.jp']
    #spaiderが初めにアクセスするURL
    start_urls = ['https://be-tech.ne.jp/']

    def parse(self, response):
        pass
