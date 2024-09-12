from celery import shared_task

@shared_task(bind=True)
def test_func(self):    # task-1 execute by celery 
    # operations
    print("::: print Using Celery :::")
    for i in range(20):
        print(i)
    return "Complete"

@shared_task()
def send_email(email):  # task-2 execute by celery 
    print(f"A sample message is sent to {email}.")