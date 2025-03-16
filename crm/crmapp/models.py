from django.db import models

import uuid

class BaseClass(models.Model):
    
    uuid = models.SlugField(unique=True,default= uuid.uuid4)
    
    active_status = models.BooleanField(default=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        
        abstract = True
    
class CourseChoices(models.TextChoices):
    
    PY_DJANGO = 'PY-DJANGO','PY-DJANGO'
    MEARN = 'MEARN','MEARN'
    DATA_SCIENCE = 'DATA-SCIENCE','DATA-SCIENCE'
    SOFTWARE_TESTING = 'SOFTWARE_TESTING','SOFTWARE_TESTING'
    
class Batch(models.TextChoices):
    
    PY_NOV_2024 = 'PY-NOV-2024','PY-NOV-2024'
    MEARN_NOV_2024 = 'MEARN-NOV-2024','MEARN-NOV-2024'
    PY_JAN_2025 = 'PY-JAN-2025','PY-JAN-2025'
    DS_JAN_2025 = 'DS-JAN-2025','DS-JAN-2025'
    ST_JAN_2025 = 'ST-JAN-2025','ST-JAN-2025'
    MEARN_JAN_2025 = 'MEARN-JAN-2025','MEARN-JAN-2025'
    
class TrainerName(models.TextChoices):
    
    JOHN_DOE = 'JOHN_DOE','JOHN_DOE'
    JAMES = 'JAMES','JAMES'
    PETER = 'PETER','PETER'
    ALEX = 'ALEX','ALEX'
   
class District(models.TextChoices):
    
    ALAPPUZHA = 'ALAPPUZHA', 'Alappuzha'
    ERNAKULAM = 'ERNAKULAM', 'Ernakulam'
    IDUKKI = 'IDUKKI', 'Idukki'
    KANNUR = 'KANNUR', 'Kannur'
    KASARAGOD = 'KASARAGOD', 'Kasaragod'
    KOLLAM = 'KOLLAM', 'Kollam'
    KOTTAYAM = 'KOTTAYAM', 'Kottayam'
    KOZHIKODE = 'KOZHIKODE', 'Kozhikode'
    MALAPPURAM = 'MALAPPURAM', 'Malappuram'
    PALAKKAD = 'PALAKKAD', 'Palakkad'
    PATHANAMTHITTA = 'PATHANAMTHITTA', 'Pathanamthitta'
    THIRUVANANTHAPURAM = 'THIRUVANANTHAPURAM', 'Thiruvananthapuram'
    THRISSUR = 'THRISSUR', 'Thrissur'
    WAYANAD = 'WAYANAD', 'Wayanad'
    
class students(BaseClass):
    
    profile=models.OneToOneField('authentication.Profile',on_delete=models.CASCADE)
    
    first_name = models.CharField (max_length=50)
    
    last_name = models.CharField (max_length=50)
    
    photo = models.ImageField(upload_to='student')
    
    email = models.EmailField (unique=True)
    
    contact_num = models.CharField (max_length=10)

    house_name = models.TextField(max_length=500)
    
    post_office = models.CharField (max_length=50)
    
    district = models.CharField (max_length=30,choices = District.choices)
    
    pincode = models.CharField (max_length=6)
    
    # course details field
    
    adm_number = models.CharField (max_length=50)

    #Course = models.CharField (max_length=30,choices = CourseChoices.choices)
    
    course = models.ForeignKey('courses.Courses',null=True,on_delete=models.SET_NULL)

    #Batch = models.CharField(max_length=50,choices=Batch.choices)
    
    
    batch = models.ForeignKey('batches.Batches',null=True,on_delete=models.SET_NULL)
    
    #batch_date = models.DateField ()
    
    Join_date = models.DateField (auto_now_add=True)

    #trainer_name = models.CharField(max_length=30,choices = TrainerName.choices)
    
    trainer = models.ForeignKey('trainers.Trainers',null=True,on_delete=models.SET_NULL)
    
    
    def __str__(self):
        
        return f'{self.first_name} {self.last_name} {self.batch}'
    
    class Meta:
        
        verbose_name = 'students'
        
        verbose_name_plural = 'students'
        
        ordering = ['-id']
        
