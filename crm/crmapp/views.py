from django.views import View
from .models import District,CourseChoices,Batch,TrainerName
from django.shortcuts import render,redirect,get_object_or_404
from .utility import get_adm_num,get_password
from .forms import StudentRegisterForm 
from .models import students
from django.db.models import Q
from authentication.models import Profile
from django.db import transaction
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from authentication.permission import permission_roles



class GetStudentObject:
    
    def get_student(self,request,uuid):
        
        try:
            
            student = students.objects.get(uuid=uuid)
            
            return student
        
        except:
            
            return render(request,'errorpages/error404.html')
        
class Home(View):
    
    def get(self,request,*args,**kwargs):
        
        return render(request,'crmapp/home.html')
    
# @method_decorator(login_required(login_url='login'),name='dispatch')

@method_decorator(permission_roles(roles=['Admin','Sales']),name='dispatch')
class DashboardView(View):
    
    
    
    def get(self,request,*args,**kwargs):
        
        return render(request,'crmapp/dashboard.html')
    
@method_decorator(permission_roles(roles=['Admin','Sales','Trainer','Academic counselor']),name='dispatch')             
class StudentsView(View):
    
    def get(self,request,*args,**kwargs):
        
        query = request.GET.get('query')
        
        student = students.objects.filter(active_status=True)

        
        if query:
            
            student = students.objects.filter(Q(active_status=True)&(Q(first_name__icontains = query)|Q(last_name__icontains=query)|Q(contact_num__icontains=query)|Q(house_name__icontains=query)|Q(post_office__icontains=query)|Q(pincode__icontains=query)|Q(course__name__icontains=query)|Q(batch__name__icontains=query)|Q(trainer__first_name__icontains=query)))
            
        
        return render(request,'crmapp/students.html',context={'students':student,'query':query})
        
        # all_students = students.objects.all()
        
        
        # print(all_students)
               
class CoursesView(View):
    
    def get(self,request,*args,**kwargs):
        
        return render(request,'crmapp/courses.html')
    
class BatchView(View):
    
    def get(self,request,*args,**kwargs):
        
        return render(request,'crmapp/batch.html')
    
@method_decorator(permission_roles(roles=['Admin','Sales']),name='dispatch')
class RegistrationView(View):
    
    def get(self,request,*args,**kwargs):
        
        form = StudentRegisterForm()
        
        
        # data ={'number=[1,2,3,4,5]'}

        
        # data = {'districts': District,'courses':CourseChoices,'batches':Batch,'trainers':TrainerName,'form':form}

        data = {'form':form}
        
        return render (request,'crmapp/registration.html',context=data) 
    
    def post (self,request,*args,**kwargs):
        
        form = StudentRegisterForm(request.POST,request.FILES)
        
        for error in form.errors:
            
            print(error)
             
             
        
        if form.is_valid():
            
            with transaction.atomic():
            
             student=form.save(commit=False)
            
             student.adm_number = get_adm_num()
            
             username = student.email
            
             password = get_password()
             
             print(password)
            
             profile=Profile.objects.create_user(username=username,password=password,role='Student')
            
             student.profile = profile
            
             student.save()
            
            return redirect('students')
        
        else:
            
            return render(request,'crmapp/students.html',context={'form':form})    

    # def post(self,request,*args,**kwargs):

    #     form_data = request.POST
        
    #     first_name = form_data.get('first_name')
    #     print(first_name)
    #     last_name = form_data.get('last_name')
    #     print(last_name)
    #     photo = request.FILES.get('photo')
    #     print(photo)
    #     email = form_data.get('email')
    #     print(email)
    #     contact_number= form_data.get('contact_number')
    #     print(contact_number)
    #     house_name = form_data.get('house_name')
    #     print(house_name)
    #     district = form_data.get('district')
    #     print(district)
    #     pincode = form_data.get('pincode')
    #     print(pincode)
    #     course = form_data.get('course')
    #     print(course)
    #     batch = form_data.get('batch')
    #     print(batch)
    #     batch_date = form_data.get('batch_date')
    #     print(batch_date)
    #     trainer = form_data.get('trainer')
    #     print(trainer)
        
    #     adm_number = get_adm_num()
        
    #     print(adm_number)
        
 #     return render(request,'crmapp/students.html')
 
@method_decorator(permission_roles(roles=['Admin','Sales','Trainer','Academic counselor']),name='dispatch')

class StudentDetailView(View):
    
    def get(self,request,*args,**kwargs):
        
        uuid = kwargs.get('uuid')
        
        # student = get_object_or_404(students,pk=pk)
        
        student = GetStudentObject().get_student(uuid,request)
        
        return render(request,'crmapp/student-detail.html',context={'student':student})
    

# class Error404View(View):
    
#     def get(self,request,*args,**kwargs):
        
#         return render(request,'crmapp/error404.html')
    
@method_decorator(permission_roles(roles=['Admin','Sales']),name='dispatch')
class StudentDeleteView(View):
    
    def get(self,request,*args,**kwargs):
        
        uuid = kwargs.get('uuid')
        
        # try:
            
        #    student = students.objects.get(pk=pk)
            
        # except:
            
        #     return redirect('student-delete')
        
        student = GetStudentObject().get_student(uuid,request)
        
        # student.delete()
        student.active_status = False
        
        student.save()
        
        return redirect('students')
    
@method_decorator(permission_roles(roles=['Admin','Sales']),name='dispatch')
class StudentUpdateView(View):
    
    def get(self,request,*args,**kwargs):
        
        uuid = kwargs.get('uuid')
        
        student = GetStudentObject().get_student(uuid,request)
        
        form = StudentRegisterForm(instance=student)
        
        data = {'form':form}
        
        return render(request,'crmapp/student-update.html',context=data)
   
    def post(self,request,*args,**kwargs):
        
        uuid = kwargs.get('uuid')
        
        student = GetStudentObject().get_student(uuid,request)
        
        form = StudentRegisterForm(request.POST,request.FILES,instance=student)
        
        if form.is_valid():
            
            form.save()
            
            return redirect('students')
        
        else:
        
            return render(request,'crmapp/student-update.html',context={'form':form})
        
        
        
        