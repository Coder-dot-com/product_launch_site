from product_launch_site.celery import app
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

@app.task
def my_task(arg1, arg2):
    # Task logic here
    result = arg1 + arg2
    logger.info('hkjhkjhjkhtest', result)