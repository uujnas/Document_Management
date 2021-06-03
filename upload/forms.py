from django import forms
from django.forms import ClearableFileInput

from .models import Files, Profile, Contacts, Userdetails, Create_folder, Directory
from django.contrib.auth.models import User,Group
from django.contrib.auth.forms import UserCreationForm
from django.forms.fields import MultipleChoiceField #,ModelChoiceField

#GENDER = (('M','M'), ('F','F'), ('other','other'))
class FileForm(forms.ModelForm):
    #employee_id = forms.IntegerField(widget=forms.HiddenInput())
    class Meta:
        model = Files
        fields = ('name','description','file','title')  #,'uploaded_by')
        widgets = {
            'title': forms.HiddenInput(),
            'description':forms.Textarea(attrs={'rows': 5, 'cols': 40})
        }
        # widgets = {
            # 'description': Textarea(attrs={
                # 'cols': 80,
                # 'rows': 4,
                # 'class': 'form-control'
            # }),
class PhotoForm(forms.ModelForm):
    class Meta:
        model = Files
        fields = ('file','title' )
        
class File_Form(forms.ModelForm):
    class Meta:
        model = Files
        fields = ('name','description')
        widgets = {
            #'title': forms.HiddenInput(),
            'description':forms.Textarea(attrs={'rows': 1, 'cols': 20})
        }
class AddUserForm(forms.ModelForm):
    #employee_id = forms.IntegerField(widget=forms.HiddenInput())
    class Meta:
        model = Profile
        fields = ('Gender','Role') #,'Img') 
        # widgets = {
            # 'Us_er': forms.HiddenInput(),'Us_er',
            
        # } 

class EditFileForm(forms.ModelForm):
    #employee_id = forms.IntegerField(widget=forms.HiddenInput())
    class Meta:
        model = Files
        fields = ('name','description','file')  #,'uploaded_by')
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        Files.id=self.name

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=120,required=False, help_text='Optional.')# help_text='Required. Inform a valid email address.')
    Role=forms.ModelChoiceField(queryset = Group.objects.all())
    GENDER = (('M','M'), ('F','F'), ('other','other'))
    Gender = forms.ChoiceField(choices=GENDER)
    # Img = models.ImageField(upload_to= 'images/')
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email','Gender','Role') #,'Img' ) , 'password1', 'password2'
        # widgets = {
            # 'password1': forms.HiddenInput(),
            # 'password2': forms.HiddenInput(),
        # }
    
    def __init__(self, *args, **kwargs):
       super(SignUpForm, self).__init__(*args, **kwargs)
       del self.fields['password1']
       del self.fields['password2']
    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password('Pro123!@#')
        if commit:
            user.save()
        return user
    
class CreateUserForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ('Role', 'Gender')

class ModifyForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')       
        
class ContactForm(forms.ModelForm):
    #employee_id = forms.IntegerField(widget=forms.HiddenInput())
    class Meta:
        model = Contacts        
        fields = ('Name','Office_name','Description','Address','Mobile_no1','Mobile_no2','landline_no','email')

class UserdetailsForm(forms.ModelForm):
    class Meta:
        model = Userdetails
        fields = ('Img','father_name','mother_name','grandfather_name',
		'spouse_name','citizenship_no','issued_district','issue_date','temporary_address',
		'permanent_address','Mobile_no','landline','secondary_school','passed_year1',
		'division_percentage1','intermediate_school','passed_year2','division_percentage2',
		'Bachelor','passed_year3','division_percentage3','Masters',
		'passed_year4','division_percentage4')
  
class ProfileImage(forms.ModelForm):
    class Meta:
        model = Userdetails
        fields = ('Img',)


class Create_folderForm(forms.ModelForm):
    class Meta:
        model = Create_folder
        fields =('dir','file',)
        widgets = {
            'file':ClearableFileInput(attrs={'multiple':True}),
        }

class DirectoryForm(forms.ModelForm):
    class Meta:
        model = Directory
        fields ="__all__"