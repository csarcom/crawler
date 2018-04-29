BOT_NAME = 'gizmodo'
SPIDER_MODULES = ['webscrapy.spiders']
NEWSPIDER_MODULE = 'webscrapy.spiders'
ITEM_PIPELINES = {'webscrapy.pipelines.SqlitePipeline': 300}
DATABASE = {
    'drivername': 'sqlite',
    'database': 'posts.sqlite'
}