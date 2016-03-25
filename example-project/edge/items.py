from scrapy.item import Item, Field
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst, Join

class EdgeItem(Item):
    name = Field()
    description = Field()
    content = Field()
    link = Field()
    crawled = Field()
    spider = Field()
    url = Field()

class EdgeLoader(ItemLoader):
    default_item_class = EdgeItem
    default_input_processor = MapCompose(lambda s: s.strip())
    default_output_processor = TakeFirst()
    description_out = Join()
