# cron to send remainder emails to customers\
    
from .models import Payment

from django.utils import timezone

import threading

from crmapp.utility import send_email

from apscheduler.schedulers.background import BackgroundScheduler

def remainder_email():
    
    current_date = timezone.now().date()
    
    five_days_before_date = current_date - timezone.timedelta(days=5)
    
    pending_payments=Payment.objects.filter(status='Pending',student__Join_date__lte=five_days_before_date)
    
    if pending_payments.exists():
        
        for payment in pending_payments:
        
            subject = 'Payment Reminder'

                # sender = settings.EMAIL_HOST_USER

            recepients = [payment.student.email]

            template = 'email/payment-remainder.html'

            context = {'name' : f'{payment.student.first_name} {payment.student.last_name}'}

            thread = threading.Thread(target=send_email,args=(subject,recepients,template,context))

            thread.start()
            
        print('all emails sent')
            
def scheduler_start():
    
    scheduler = BackgroundScheduler()
    
    scheduler.add_job(remainder_email, 'cron',hour=10,minute=0)
    
    scheduler.start()
    
    