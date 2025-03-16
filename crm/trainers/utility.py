import uuid
import string
import random

from .models import Trainers

def get_trainer_id():
    """Generate a unique Trainer ID."""
    while True:
        pattern = str(uuid.uuid4().int)[:7]  # Generate a 7-digit unique number
        trainer_id = f'TR-{pattern}'  # Prefix it with 'TR-'
        
        if not Trainers.objects.filter(employee_id=trainer_id).exists():
            return trainer_id

def get_trainer_password():
    """Generate a random 8-character password."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=8))