SPIDER_MODULES = ['edge.spiders']
NEWSPIDER_MODULE = 'edge.spiders'

SCHEDULER = "scrapy_redis.scheduler.Scheduler"
SCHEDULER_PERSIST = True
# SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderPriorityQueue"
# SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderQueue"
# SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderStack"

ITEM_PIPELINES = {
    'edge.pipelines.EdgePipeline': 300,
    'scrapy_redis.pipelines.RedisPipeline': 400,
}
REDIS_URL = 'redis://user:R`s^_9RjTig8hev8KR%wRL`@103.21.140.84:6789'
