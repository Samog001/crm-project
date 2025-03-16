from django.db import models

from crmapp.models import BaseClass,District

class AcademicAdvisors(BaseClass):


    profile = models.OneToOneField('authentication.Profile',on_delete=models.CASCADE)

    first_name = models.CharField(max_length=25)

    last_name = models.CharField(max_length=25)

    employee_id = models.CharField(max_length=10)

    photo = models.ImageField(upload_to='trainers')

    email = models.EmailField()

    contact = models.CharField(max_length=12)

    house_name = models.CharField(max_length=25)

    post_office = models.CharField(max_length=25)

    district = models.CharField(max_length=20,choices=District.choices)

    pincode = models.CharField(max_length=6)

    qualification = models.CharField(max_length=10)
    
    stream = models.CharField(max_length=25)

    id_proof = models.FileField(upload_to='academic_counselor/idproof')
    

def str(self):

        return f'{self.first_name} {self.last_name}'
    
class Meta:

        verbose_name = 'Academic Counsellors'

        verbose_name_plural ='Academic Counsellors'