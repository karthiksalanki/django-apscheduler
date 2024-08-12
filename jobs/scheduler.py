from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from apscheduler.triggers.interval import IntervalTrigger
from django.utils.timezone import now
from apscheduler.events import EVENT_JOB_EXECUTED, EVENT_JOB_ERROR
from django.utils import timezone
from .models import Job
from django.core.mail import send_mail

def scheduled_task():

    receiver_email = "karthiksalanki99@gmail.com"
    message = "Testing"
    subject = 'Email To Test The Background Task'
    send_mail(
        subject=subject,
        message=message,
        from_email='karthiksalanki1999@gmail.com',
        recipient_list=[receiver_email],
        fail_silently=False,
    )

scheduler = BackgroundScheduler()

def start_scheduler():
    scheduler.start()

def schedule_job(job_id, schedule_type, schedule_details):
    job = Job.objects.get(id=job_id)
    if schedule_type == 'cron':
        trigger = CronTrigger(**schedule_details)
    elif schedule_type == 'interval':
        trigger = IntervalTrigger(**schedule_details)
    # Add other types of triggers if needed

    scheduler.add_job(scheduled_task, trigger, id=str(job.id))
    
    job.next_run = trigger.get_next_fire_time(None, now())
    job.save()

# To check whether scheduled_task task executed successfully or not
def job_listener(event):
    if event.exception:
        print(f"Scheduled task failed with error: {event.exception}")
    else:
        print("Scheduled task executed successfully.")

scheduler.add_listener(job_listener, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)


# 2nd Implementation

# scheduler = BackgroundScheduler()

# def start_scheduler():
#     scheduler.start()

# def dummy_job():
#     # Logic for the job
#     print("Executing job")

# def job_listener(event):
#     try:
#         print(event)
#         job = Job.objects.get(id=event.job_id)
#         if event.exception:
#             print(f"The job {job.name} failed.")
#         else:
#             print(f"The job {job.name} was executed successfully.")
#             job.last_run = timezone.now()
#             job.next_run = event.scheduled_run_time
#             job.save()
#     except Job.DoesNotExist:
#         print(f"Job with ID {event.job_id} not found.")

# def add_job(job_id, schedule_type, schedule_details):
#     job = Job.objects.get(id=job_id)
    
#     if schedule_type == 'cron':
#         trigger = CronTrigger(**schedule_details)
#     elif schedule_type == 'interval':
#         trigger = IntervalTrigger(**schedule_details)
#     else:
#         raise ValueError("Invalid schedule_type provided")

#     scheduler.add_job(dummy_job, trigger, id=str(job.id))
#     job.next_run = trigger.get_next_fire_time(None, timezone.now())
#     job.save()

# # Add the listener to track job executions
# scheduler.add_listener(job_listener, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)
