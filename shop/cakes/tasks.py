from celery import shared_task
import time


@shared_task
def get_request_info(url, method):
    time.sleep(5)
    print('REQUEST', method, 'on', url)