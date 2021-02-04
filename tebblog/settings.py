BOT_NAME = 'tebblog'
SPIDER_MODULES = ['tebblog.spiders']
NEWSPIDER_MODULE = 'tebblog.spiders'
LOG_LEVEL = 'WARNING'
ROBOTSTXT_OBEY = True
ITEM_PIPELINES = {
   'tebblog.pipelines.DatabasePipeline': 300,
}
