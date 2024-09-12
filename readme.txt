Task:
-----
Task1:  (using celery worker) 
    - print 1 to 20 numbers using celery. when user can start django project and hit the specified urls path 
    at that time automatically execute yout selected task but before this run your celery package.
Task2:  (hint: using celery beat to setup periodic task)
    - send a mail in every 15 min.  


Celery Worker & Beat:
---------------------
- A Celery worker is a process that executes tasks in the background, allowing for asynchronous processing and handling of time-consuming operations. 
- Celery Beat is a scheduler that periodically sends tasks to the Celery worker, enabling scheduled and recurring tasks such as database cleanups or 
sending periodic emails.


Celery Events:
---------------
- an event refers to a notification or message about the state or status of tasks, workers, or the overall system. These events can be used for monitoring, debugging, and managing tasks. 
Key types of events in Celery include:
1)Task Events:
    - task-sent: Indicates a task has been sent to a worker.
    - task-received: Signals that a worker has received a task.
    - task-started: Shows that a worker has started processing a task.
    - task-succeeded: Notifies that a task has been successfully completed.
    - task-failed: Indicates that a task has failed.
2)Worker Events:
    - worker-online: Shows that a worker has started and is online.
    - worker-offline: Indicates that a worker has gone offline or has been stopped.
3)Worker and Task Monitoring:
    - Events can be used to monitor the activity and health of workers and tasks in real-time, helping with 
    debugging and system management.


steps to run celery task1:
---------------------------
step0: install redis/RabbitMQ server and install celery package using "pip install celery", "django-celery-beat,
step1: register in installed app "django_celery_beat", "django_celery_results" & add some configrations of celery into settings.py file.
step2: migrate all the migrations availble in django, celery-beat, celery-result.
step3: create celery.py file in django project and add some code in that file.
step4: add celery app into __init__py file of django peoject.
step5: create tasks.py file in application and create function related to your task.
step6: call to your task from views.py file's selected view.
step7: start redis server then run celery command: 
            - celery -A celery_with_django worker -l info        # for celery worker
step8: start django server using "python manage.py runserver".


steps to run celery task2:
---------------------------
step0 to step2 as per Task1.
step3: create celery.py file in django project and add some code in that file; add celery beat scheduler
        app.conf.beat_schedule = {
                'every-15-seconds':{        # schedule beat task name
                    'task': 'mainapp.tasks.send_email',      # created task name with location
                    'schedule': 15,     # execute task in every 15 sec 
                    'args': ("demo@gmail.com",)          # set here default email address.
                }
            }

step4: as per task1
step5: start celery worker script using "celery -A celery_with_django worker -l info" in other terminal
step6: start celery beat script using "celery -A celery_with_django beat -l info" in other terminal
    Note: you can see send_email fun calling from celery beat terminal & all also check into celery worker 
        terminal to view/receive execute the periodic task.



commands:
**********
celery -A project_name worker -l info --> to run celery worker node with log information
celery -A project_name beat -l info --> to run celery beat for schedulling periodic task with log information
celery -A project_name status --> to view all running worker node
celery -A project_name inspect active --> This command lists all currently executing tasks. It shows which tasks are actively being processed by the workers at the moment.
celery -A project_name inspect reserved --> This command displays the tasks that have been reserved by workers but are not yet being executed. These tasks are in the queue waiting to be processed.
celery -A project_name inspect scheduled --> This command lists tasks that are scheduled to be run in the future. It shows tasks that have been deferred to run at a specific time or after a certain delay.
celery -A project_name inspect revoked --> This command lists tasks that have been revoked or cancelled. Revoked tasks are those that were scheduled but have been explicitly removed from the queue and will not be executed.
celery -A project_name inspect stats --> This command provides statistics about the Celery workers, including information on their uptime, number of tasks processed, and other performance metrics. It helps in monitoring the overall health and activity of the worker processes.
celery -A project_name purge --> This command removes all messages from all queues in the specified Celery application, effectively clearing the entire message broker.
celery -A project_name purge -Q test --> This command removes all messages only from the specified queue (test in this case) while leaving messages in other queues intact.
celery -A project_name events --> This command starts the Celery events monitoring tool, which displays real-time events and status updates about tasks and workers. It provides a continuous stream of events such as task state changes, worker status updates, and more.
celery -A project_name control enable_events --> enables event monitoring for the Celery workers. Once enabled, workers will start sending event data (such as task state changes and worker status updates) to the message broker, which can then be viewed using the celery events command or integrated with monitoring tools.


Flower 3rd party tool to monitor celery process:
-------------------------------------------------
- Flower is a web-based tool for monitoring and administrating Celery clusters. It provides real-time information about task progress, 
worker status, and system performance, offering a user-friendly interface to manage and inspect Celery tasks.

Install Flower using "pip install flower"
Start Flower with your Celery application using "celery -A project_name flower"
Accessing Flower using "http://localhost:5555"