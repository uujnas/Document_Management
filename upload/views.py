import shutil

from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.views.generic import DetailView

from .forms import FileForm, AddUserForm, EditFileForm, ModifyForm, ContactForm, CreateUserForm, PhotoForm, File_Form, \
    UserdetailsForm, ProfileImage, DirectoryForm

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from .forms import SignUpForm,Create_folderForm
import os
from django.http import JsonResponse
import datetime
from datetime import date
from django.contrib import messages
from .models import Files, Profile, Contacts, Userdetails, Create_folder, Directory, Rename
from django.views import View  #from django.views.generic import UpdateView
from django.urls import reverse_lazy
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required

from django.core.exceptions import ValidationError


@login_required(login_url='accounts:login')
def file_upload(request):
    c=Files
    c.count_pdf=Files.objects.filter(title=1).count()
    c.count_doc=Files.objects.filter(title=2).count()
    c.count_excel=Files.objects.filter(title=3).count()
    c.count_img=Files.objects.filter(title=4).count()
    #aa=[7,8,9,]
    #print(aa)
    #u=request.user
    #r=AddDetails(user_id=u)
    #print(request.user.AddDetails.Gender)
    return render(request,"dash.html",{'c':c,
    #'u':u,
    })


@login_required(login_url='accounts:login')
def upload_files(request):
    #file_form=FileForm()
    a=[1,2,3,4,5]
    #print(a)
    if request.method == 'POST':
        file_form = FileForm(request.POST, request.FILES)
        #s=file_form
        #print(a)
        
        file_form.file=request.FILES['file']
        value=file_form.file
        ext = os.path.splitext(value.name)[1]
        if ext == '.pdf':
            file_form.title=1
        elif ext == '.doc' or ext=='.docx':
            file_form.title=2
        elif ext=='.xlsx' or ext=='.csv':
            file_form.title=3
        elif ext=='.jpg' or ext=='.png' or ext=='.bmp':
            file_form.title=4
        #print(ext)
        if file_form.is_valid():
            #print(file_form.title)
            s = file_form.save(commit=False)
            s.title = file_form.title
            s.user = request.user
            s.is_multiple = 0
            s.save()
            return redirect('upload:search_files')
            #return render(request, 'search.html',{'error':'File uploaded successfully'})
           #return render(request, 'home.html')#HttpResponseRedirect('success')
    else:
        file_form = FileForm()
        #print(a)
    #return HttpResponseRedirect('ok')
    #return HttpResponseRedirect('login')
    return render(request, 'upload_files.html',{'file_form':file_form})#HttpResponseRedirect('success')
    #return render(request,"create_folder.html")

@login_required(login_url='accounts:login')
def search_file(request):
    c=Files
    c=Files.objects.order_by('-uploaded_at')[:10] #.all #filter().all #order_by('-uploaded_at')[:10] #all

    # c.pdf=Files.objects.filter(title=1).count()
    # c.count_doc=Files.objects.filter(title=2).count()
    # c.count_excel=Files.objects.filter(title=3).count()
    # c.count_img=Files.objects.filter(title=4).count()
    return render(request, 'search.html',{'c':c})

                                                # class FileUpdateView(UpdateView):
                                                    # #context_object_name = pk
                                                    # model = Files
                                                    # form_class = FileForm
                                                    # #fields = ['Name', 'Description','File','uploaded_at']
                                                    # #print(model.id)
                                                    # template_name = "Files_form.html"
                                                    # success_url = reverse_lazy('upload:Editfiles_save') #,'model.id')

    

        
@login_required(login_url='accounts:login')
def Editfiles(request,pk):
    item = Files.objects.get(id=pk)
    aa=[7,8,9,]
    #print(aa)
    if request.method == 'POST':
        file_form = FileForm(request.POST, request.FILES,instance=item)
        file_form.user = request.user
        #print(aa)
        if file_form.is_valid():
            #print(aa)
            file_form.file=request.FILES['file']
            value=file_form.file
            ext = os.path.splitext(value.name)[1]
            if ext == '.pdf':
                file_form.title=1
            elif ext == '.doc' or ext=='.docx':
                file_form.title=2
            elif ext=='.xlsx' or ext=='.csv':
                file_form.title=3
            elif ext=='.jpg' or ext=='.png' or ext=='.bmp':
                file_form.title=4
            #print(ext)
            #print(file_form.title)
            s=file_form.save(commit=False)
            s.title=file_form.title
            #print(aa)
            s.id = item.id
            s.save()
            return redirect('upload:search_files')
            #return render(request, 'Files_form.html',{'error':'File uploaded successfully'})
           #return render(request, 'home.html')#HttpResponseRedirect('success')
    else:
        file_form = FileForm(instance=item)
        #a=item.File #request.FILES.get['File']
        args = {}
        args.update(csrf(request))
        args['file_form'] = file_form
        #print(item.Name)
        #print(aa)
    return render(request, 'Files_form.html',args,{'item':item})#HttpResponseRedirect('success')

@login_required(login_url='accounts:login')
def Viewfiles(request,pk):
    item = Files.objects.get(id=pk)
    item.name=item.name
    item.uploaded_at=item.uploaded_at
    item.description=item.description
    item.file=item.file
    return render(request, 'Viewfiles.html',{'item':item})

@login_required(login_url='accounts:login')
def Downloadfiles(request,pk):
    item = Files.objects.get(id=pk)
    item.file=item.file
    return render(request, 'Downloadfiles.html',{'item':item})

# def signup(request):
    # if request.method == 'POST':
        # usr = Profile()
        # form_adduser= CreateUserForm(request.POST or None)
        # try:
            # user = User.objects.get(username=request.POST['username'])
            # return render(request, 'signup1.html', {'error':'Username is already taken'})
        # except User.DoesNotExist:
            # User.username = request.POST['username']
            # #User.first_name = request.POST['first_name']
            # #User.last_name = request.POST['last_name']
            # #User.email = request.POST['email']
            # print(User.email)
            # User.password = 'Pro123!@#'
            # user = User.objects.create_user(User.username, User.password)
            # #User.save()
            # s = form_adduser.save(commit = False)
            # s.user = User
            # s.save()
            # return render(request, 'manage_user.html') #return redirect('upload/manage_user')


        # # else:
            # # return render(request, 'signup1.html', {'error':'Password doesn\'t matched'})

    # else:
        # form_adduser= CreateUserForm(request.POST or None)
        # return render(request, 'signup1.html',{'form_adduser':form_adduser})
@login_required(login_url='accounts:login')
def signup(request):
    #a=[1,2,3,4,5,6,7]
    if request.method == 'POST':
        form = SignUpForm(request.POST or None)
        form.password1 = request.POST.get('password1')
        print(form.password1)
        if form.is_valid(): # and form_adduser.is_valid():
            
            user = form.save()
            user.refresh_from_db()
            user.profile.Gender = form.cleaned_data.get('Gender')
            user.profile.Role = form.cleaned_data.get('Role')
            username = form.cleaned_data.get('username')
            #user.set_password('Pro123!@#')
            user.save() 
            #raw_password = form.password1   user.set_password(self.cleaned_data['new_password1'])
            #print(raw_password)
             
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            messages.success(request, ('New user successfully created!'))
            
            return redirect('upload:user_list_new')
        
    else:
        form = SignUpForm()
        #form_adduser= CreateUserForm()
    return render(request, 'signup.html', {'form': form}) #,'form_adduser': form_adduser})

@login_required(login_url='accounts:login')
def manage_user(request):
    
    return render(request, 'manage_user.html')
    
@login_required(login_url='accounts:login')
def user_list_new(request):
    us_er=User
    us_er.total = us_er.objects.all
    return render(request, 'user_list_new.html',{'us_er':us_er})

@login_required(login_url='accounts:login')
def modify_user(request,pk):
    usr=User.objects.get(id=pk)                          #form['fieldname'].field.widget.attr['readonly'] = 'readonly'
    usr.ID = usr.id
    usr.Name= usr.username
    usr.first_name=usr.first_name
    usr.last_name=usr.last_name
    usr.email=usr.email
    #usr.Role=usr.Profile.Role
    #print(usr.Role)
    if request.method == 'POST':
        #file_form = FileForm(request.POST, request.FILES)
        form_adduser= AddUserForm(request.POST, request.FILES)
        #form_adduser.user = usr.id
        if form_adduser.is_valid():
            #form_adduser.Img = request.FILES['Img']            
            #print(a)
            s=form_adduser.save(commit = False)
            s.user = usr
            s.save()
            messages.success(request, ('User successfully updated!'))
            return render(request, 'manage_user.html')
        
    else:
        #form = ModifyForm(instance=usr)
        form_adduser= AddUserForm()
        #form_adduser['Us_er'].field.widget.attr['readonly'] = usr.id
        # args = {}
        # args.update(csrf(request))
        # args['form'] = form
    return render(request, 'modify_user.html', {'form_adduser': form_adduser,'usr':usr}) #,'form_adduser': form_adduser})

@login_required(login_url='accounts:login')
def UserContacts(request):
    #contact=Contacts
    c = Contacts.objects.all
    return render(request,'contacts.html',{'c':c})
                                        # def ADDContacts(request):
                                            # #obj = Contacts
                                            # if request.method == 'POST':
                                                # if request.POST['Name'] and request.POST['Office_name']: # and request.POST['Mobile_no1']: 
                                                    # obj = Contacts
                                                    # obj.Name = request.POST['Name']
                                                    # obj.Office_name = request.POST['Office_name']
                                                    # obj.Description = request.POST['Description']
                                                    # obj.Address = request.POST['Address']
                                                    # #obj.ename = User.objects.get(username=request.user.username)
                                                    # obj.Mobile_no1=request.POST['Mobile_no1']
                                                    # obj.Mobile_no2=request.POST['Mobile_no2']
                                                    # obj.landline_no=request.POST['landline_no']
                                                    # obj.email = request.POST['email']
                                                    # #print(c.Office_name)
                                                    # #if obj.is_valid():
                                                    # c = obj.save()
                                                    # # e.obj.ename=ename
                                                    # # e.save()
                                                    # return render(request, 'contacts.html',{'c':c})
                                        
                                                # else:
                                                    # return render(request, 'contacts.html', {'error':'please fill all the fields'})
                                            # else:
                                                # return render(request,'add_contacts.html')
                                                
@login_required(login_url='accounts:login')
def ADDContacts(request):
    #a=[1,2,3,4,5,6,7]
    if request.method == 'POST':
        contact_form= ContactForm(request.POST or None)
        #print(a)
        if contact_form.is_valid():
            #print(a)
            contact_form.save()
            messages.success(request, ('User successfully updated!'))
            return redirect('upload:Contacts') # return render(request, 'contacts.html') #,{'c':c})
        
    else:
        #form = ModifyForm(instance=usr)
        contact_form= ContactForm()
        #print(a)
    return render(request, 'add_contact.html', {'contact_form': contact_form})

@login_required(login_url='accounts:login')
def Search_Contact(request):
    a=[1,2,3,4,5,6,7]
    errors = []
    if 'Name' in request.GET or 'office_name' in request.GET:
        Name = request.GET['Name']
        Office_name = request.GET['office']
        print(a)
        #field3 = request.GET['field3']
        if not (Name or Office_name):# or field3):
            errors.append('search item didn''t matched')
        else:
            results = Contacts.objects.filter(
                Name__icontains=Name
            ).filter(
                Office_name__icontains=Office_name
            )#.filter(
             #   field3__icontains=field3            )
            query = "Field 1: %s, Field 2: %s" % (Name, Office_name)
            return render_to_response('search_contact.html',
                    {'results': results, 'query': query})
    return render_to_response('search_contact.html',
            {'errors': errors})

@login_required(login_url='accounts:login')
def Search_File_New(request):
    a=[1,2,3,4,5,6,7]
    errors = []
    if 'Name' in request.GET:
        Name = request.GET['Name']
        #from_date = request.GET['from_date']
        #to_date = request.GET['to_date']
        #from_date=int(from_date)
        #to_date = int(to_date)
        ##from_date = datetime.datetime.strptime(from_date, "%Y-%m-%d") # %H:%M:%S")
        ##to_date = datetime.datetime.strptime(to_date, "%Y-%m-%d") # %H:%M:%S")
        #print(from_date)
        #field3 = request.GET['field3']
        if not (Name): # or from_date or to_date):# or field3):
            errors.append('search item didn''t matched')
        else:
            results = Files.objects.filter(
                name__icontains=Name
            )#.filter(uploaded_at=(date(from_date), date(to_date))
            #)#.filter(
             #   field3__icontains=field3            )
            query = "Field 1: %s" % (Name)
            return render_to_response('Search_File_New.html',
                    {'results': results, 'query': query})
    elif 'from_date' in request.GET or 'to_date' in request.GET:
        from_date = request.GET['from_date']
        to_date = request.GET['to_date']
        if not (from_date):
            errors.append('search item didn''t matched')
        elif not (to_date):
            errors.append('search item didn''t matched')
        else:
            results = Files.objects.filter(uploaded_at__range=(date(from_date), date(to_date))
            )#.filter(
             #   field3__icontains=field3            )
            query = "Field 2: %s, Field 3: %s" % (from_date, to_date)
            return render(render,'Search_File_New.html',
                    {'results': results, 'query': query})
    
    return render(request,'Search_File_New.html',
            {'errors': errors})

@login_required(login_url='accounts:login')
def filterfiles(request):
    #a=[1,2,3,4,5,6,7]
    errors = []
    filetype = request.GET['filterfiles']
    #print(filetype)
    #print(a)
    if filetype == 'pdf':
        results = Files.objects.filter(title = 1)
        return render(request,'Search_File_New.html',{'results': results})
    elif filetype == 'word':
        results = Files.objects.filter(title = 2)
        return render(request,'Search_File_New.html',{'results': results})
    elif filetype == 'image':
        results = Files.objects.filter(title = 4)
        return render(request,'Search_File_New.html',{'results': results})
    elif filetype == 'excel':
        results = Files.objects.filter(title = 3)
        return render(request,'Search_File_New.html',{'results': results})
    elif filetype == 'all':
        results = Files.objects.all
        return render(request,'Search_File_New.html',{'results': results})
    else:
        errors.append('search item didn''t matched')
    return render(render,'Search_File_New.html',{'errors': errors})
            
@login_required(login_url='accounts:login')    
def multipleupload(request):
    a=[1,2,3,4,5,6,7,8,9,10]
    form_name = File_Form(request.POST)
    if form_name.is_valid():
            form_name.name = request.POST['name']
            form_name.description = request.POST['description']
            #multi.id = multi.id
            #print(a)
            if Files.objects.filter(name__isnull=True).exists():
                #cc = Files.objects.filter(file_name_id__isnull=True)
                cc = Files.objects.filter(name__isnull=True)
                print(a)
                print(cc.count())
                for c in cc:
                    #mupl = Files.objects.get(file_name_id__isnull=True)
                    #print(c.id)
                    c.name = form_name.name
                    c.description = form_name.description
                    c.is_multiple = 1
                    c.save()
                    #print(a)
                    
    return redirect('upload:search_files') #return render(request,'photos/uploaded.html')  

    
class BasicUploadView(View):
    a=[1,2,3,4,5,6,7,8,9,10]
    def get(self, request):
        a=[1,2,3,4,5,6,7,8,9,10]
        #print(a)
        Filess_list = Files.objects.filter(name__isnull=True) #Files.objects.all()
        form_name = File_Form()
        return render(self.request, 'photos/basic_upload/index.html', {'Filess': Filess_list,'form_name': form_name })

    def post(self, request):
        form = PhotoForm(self.request.POST, self.request.FILES)
        form.file = self.request.FILES.get('file')
        value=form.file
        ext = os.path.splitext(value.name)[1]
        if ext == '.pdf':
            form.File_type=1
        elif ext == '.doc' or ext=='.docx':
            form.File_type=2
        elif ext=='.xlsx' or ext=='.csv':
            form.File_type=3
        elif ext=='.jpg' or ext=='.png' or ext=='.bmp':
            form.File_type=4
        print(ext)
        if form.is_valid():
            Files = form.save(commit = False)
            Files.title = form.File_type
            Files.user = request.user
            Files.save()
            #a=[1,2,3,4,5,6,7,8,9,10]
            #print(a)
            data = {'is_valid': True, 'name': Files.file.name, 'url': Files.file.url}
        else:
            data = {'is_valid': False}
        return JsonResponse(data)



class ProgressBarUploadView(View):
    def get(self, request):
        Filess_list = Files.objects.all()
        return render(self.request, 'photos/progress_bar_upload/index.html', {'Filess': Filess_list})

    def post(self, request):
        time.sleep(1)  # You don't need this line. This is just to delay the process so you can see the progress bar testing locally.
        form = PhotoForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            Files = form.save()
            data = {'is_valid': True, 'name': Files.file.name, 'url': Files.file.url}
        else:
            data = {'is_valid': False}
        return JsonResponse(data)



class DragAndDropUploadView(View):
    def get(self, request):
        Filess_list = Files.objects.all()
        form_name = File_Form()
        return render(self.request, 'photos/drag_and_drop_upload/index.html', {'Filess': Filess_list, 'form_name':form_name})

    def post(self, request):
        form = PhotoForm(self.request.POST, self.request.FILES)
        form.file = self.request.FILES.get('file')
        value=form.file
        ext = os.path.splitext(value.name)[1]
        if ext == '.pdf':
            form.File_type=1
        elif ext == '.doc' or ext=='.docx':
            form.File_type=2
        elif ext=='.xlsx' or ext=='.csv':
            form.File_type=3
        elif ext=='.jpg' or ext=='.png' or ext=='.bmp':
            form.File_type=4
        print(ext)
        if form.is_valid():
            Files = form.save(commit = False)
            Files.title = form.File_type
            Files.user = request.user
            Files.save()
            data = {'is_valid': True, 'name': Files.file.name, 'url': Files.file.url}
        else:
            data = {'is_valid': False}
        return JsonResponse(data)


def clear_database(request):
    for Files in Files.objects.all():
        Files.file.delete()
        Files.delete()
    return redirect(request.POST.get('next'))

@login_required(login_url='accounts:login')    
def view_profile(request):
    instance = request.user
    a=[1,2,3,4,5,6,7]
    if request.method == 'POST':
        userdetail_form= UserdetailsForm(request.POST, request.FILES)
        #print(a)
        if userdetail_form.is_valid():
            #print(a)
            #userdetail_form.father_name = request.POST['father_name']
            #print(userdetail_form.father_name)
            s = userdetail_form.save(commit = False)
            s.user = request.user
            s.save()
            return redirect('upload:view_profile') # return render(request, 'contacts.html') #,{'c':c})
        
    else:
        if Userdetails.objects.filter(user=request.user).exists():
            return render(request, 'view_profile.html')
        else:
            userdetail_form= UserdetailsForm()#print(a)
    return render(request, 'update_profile.html',{'userdetail_form':userdetail_form}) #,{'item':item})

@login_required(login_url='accounts:login')
def update_profile_image(request):
    #instance = request.user
    a=[1,2,3,4,5,6,7]
    if request.method == 'POST':
            image_form = ProfileImage(request.FILES)
            if image_form.is_valid():
                image_form.Img = request.FILES['Img']#s = image_form.save(commit = False)
                #instance = request.user
                s = image_form.save(commit = False)
                s.user = request.user
                s.save()
            return redirect('upload:view_profile') # return render(request, 'contacts.html') #,{'c':c})
        
    else:
        image_form = ProfileImage()
    return render(request, 'update_profile_image.html',{'image_form':image_form})    
    

@login_required(login_url='accounts:login')
def view_user_profile(request,pk):
    usr = User.objects.get(id = pk)
    if usr==request.user:
        return redirect('upload:view_profile')
    else:
        usr_profile = Userdetails.objects.filter(user_id = pk)
        usr = User.objects.get(id = pk)
    return render(request, 'view_user_profile.html',{'usr_profile':usr_profile,'usr':usr})


def create_folder(request):
    # folder = Create_folder.objects.all()
    if request.method == 'POST':
        dir = request.POST['directory']

        dir_1 = Directory(directory=dir)
        dir_1.save()

        parent_dir = "E:/testsql/testsql/media"
        path = os.path.join(parent_dir,dir)
        os.mkdir(path)
        print("Directory is created ")
        arr = os.listdir("E:/testsql/testsql/media")
        print(arr)

    return redirect('/upload/add_file/')

def add_file(request):
    list_folder = Directory.objects.all()
    form=Create_folderForm()
    if request.method == "POST":
        form = Create_folderForm(request.POST,request.FILES)
        files = request.FILES.getlist('file')
        directory = request.POST.get('dir')
        print(directory)
        try:
            directory = Directory.objects.get(id=directory)

            if form.is_valid():
                for f in files:
                    file_instance = Create_folder(file=f)
                    file_instance.dir = directory
                    print(file_instance)
                    file_instance.save()
                    form.save()
            else:
                form = Create_folderForm()
        except:
            print('no directory found')
            messages.error(request, 'Folder isn''t chosen!! First choose folder and upload file')

    context = {'form':form,'folder':list_folder}
    return render(request, "create_folder.html",context)
def clean(self):
    file_path = "your folder/" + self.cleaned_data.get('file')
    if os.path.isfile(file_path):
        raise ValidationError('File already exists')
    return self.cleaned_data
def remove_folder(request,id):
    context={}
    try:
        obj = Directory.objects.get(id=id)
        path=os.path.join('E:/testsql/testsql/media/',obj.directory)
        shutil.rmtree(path)
        obj.delete()
    except:
        print('folder not found')
        messages.error(request,'Note: No more folder')

        # return redirect('upload:folder')

    return render(request,'remove_folder.html',context)

def folder_detail(request,id):
    detail = Directory.objects.get(id=id)
    file = Create_folder.objects.filter(dir=detail.id)
    print(file)
    context = {'detail':detail,'file':file}
    return render(request,'folder_detail.html',context)


def rename_folder(request,id):
    rename_folder = Directory.objects.get(id=id)
    form = DirectoryForm(request.POST,instance = rename_folder)
    direct = request.POST.get('directory')
    print(direct)

    if form.is_valid():
        obj = Directory.objects.get(id=id)
        src = os.path.join('E:/testsql/testsql/media/', obj.directory)
        print(src)
        dst1 = os.path.join('E:/testsql/testsql/media/', direct)
        print(dst1)
        os.rename(src, dst1)
        form.save()

        return redirect('upload:folder')
    return render(request,'rename_folder.html',{'form':form})
