from django import forms

from .models import students,District,CourseChoices,Batch,TrainerName

from batches.models import Batches

from courses.models import Courses

from trainers.models import Trainers

class StudentRegisterForm(forms.ModelForm):
    
    class Meta:
        
        model = students
    
    # fields = ['first_name','last_name','photo','email','contact_num','house_name','post_office','district','pincode','course','batch','batch_date','trainer_name']
    
    # if all fields are needed, use fields = '__all__'
    
    # fields = '__all__'
    
        exclude = ['adm_number','Join_date','uuid','active_status','profile']
        
        widgets = { 
                   'first_name':forms.TextInput(attrs={'class':"block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input",
                                                       'required':'required'}),
                   
                   'last_name':forms.TextInput(attrs={'class':"block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input",
                                                       'required':'required'}),
                   'photo':forms.FileInput(attrs={'class':"block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input"
                                                  }),
                   'email':forms.EmailInput(attrs={'class':"block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input",
                                                       'required':'required'}),
                   'contact_num':forms.TextInput(attrs={'class':"block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input",
                                                       'required':'required'}),
                   'house_name':forms.TextInput(attrs={'class':"block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input",
                                                       'required':'required'}), 
                    'post_office':forms.TextInput(attrs={'class':"block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input",
                                                       'required':'required'}),
                    'pincode':forms.TextInput(attrs={'class':"block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input",
                                                       'required':'required'}),
                    'batch_date':forms.DateInput(attrs={'type': 'date',
                                                        'class':"block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input",
                                                        'required':'required'}),
            
        }
        
    
    district = forms.ChoiceField(choices=District.choices,widget=forms.Select(attrs={
                                                                                 'class':"block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input",
                                                                                 'required':'required'}))
    
    # Course = forms.ChoiceField(choices=CourseChoices.choices,widget=forms.Select(attrs={
    #                                                                              'class':"block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input",
    #                                                                              'required':'required'}))
    
    course = forms.ModelChoiceField(queryset=Courses.objects.all(),widget=forms.Select(attrs={
                                                                                 'class':"block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input",
                                                                                 'required':'required'}))
    
    # Batch = forms.ChoiceField(choices=Batch.choices,widget=forms.Select(attrs={
    #                                                                              'class':"block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input",
    #                                                                              'required':'required'}))
    
    batch = forms.ModelChoiceField(queryset=Batches.objects.all(),widget=forms.Select(attrs={
                                                                                 'class':"block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input",
                                                                                 'required':'required'}))
    
    # trainer_name = forms.ChoiceField(choices=TrainerName.choices,widget=forms.Select(attrs={
    #                                                                              'class':"block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input",
    #                                                                              'required':'required'}))
    
    trainer = forms.ModelChoiceField(queryset=Trainers.objects.all(),widget=forms.Select(attrs={
                                                                                 'class':"block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input",
                                                                                 'required':'required'}))
    
    
    def clean(self):
        
        cleaned_data = super().clean()
        
        pincode = cleaned_data.get('pincode')
        
        email = cleaned_data.get('email')
       
        if students.objects.filter(profile__username = email).exists():
           
           self.add_error('email','This email is already registerd')
        
        if len(str(pincode))<6:
            self.add_error('pincode','Pincode should be 6 digits')
            
        return cleaned_data
    
        
    def __init__(self,*args,**kwargs):
        
        super(StudentRegisterForm,self).__init__(*args,**kwargs)
        
        if not self.instance:
            
            self.fields.get('photo').widget.attrs['requred'] = 'required'