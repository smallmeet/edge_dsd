from scrapy_redis.spiders import RedisSpider

from edge.items import EdgeLoader


class Security(RedisSpider):
    name = 'security'
    redis_key = 'security:start_urls'

    def __init__(self, *args, **kwargs):
        domain = kwargs.pop('domain', '')
        self.alowed_domains = filter(None, domain.split(','))
        super(Security, self).__init__(*args, **kwargs)

    def parse(self, response):
        el = EdgeLoader(response=response)
        el.add_xpath('name', '//title[1]/text()')
        el.add_value('content', response.body)
        el.add_value('url', response.url)
        return el.load_item()
