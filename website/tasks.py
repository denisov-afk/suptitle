from celery import shared_task


@shared_task
def get_results_from_stt(result):
    print(result)
