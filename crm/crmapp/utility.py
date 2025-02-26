import uuid

import string

import random

from .models import students

def get_adm_num():
    
    while True:
        
    
     pattern = str(uuid.uuid4().int)[:7]
    
     adm_num = f'LM-{pattern}'
     
     if not  students.objects.filter(adm_number=adm_num).exists():
         
         return adm_num
     
def get_password():
    
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    
    return password
    
    
    
    