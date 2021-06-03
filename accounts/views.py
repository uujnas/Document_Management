from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm  #,SignUpForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

# def base(request):
	# if request.session.get("islogin"):
		# return render(request,"dashboard.html")
	# else:
	#	return render(request,"login.html")

def log_in(request):
	if request.method == 'POST':
		form = LoginForm(request.POST or None)
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		# if user.last_login is None:
		    # return redirect('accounts:change_password')
		if user is not None:
			login(request, user)
			return redirect('upload:file_upload') #render(request, "dash.html")
		else:
			form = LoginForm()
			return render(request, 'login_mine.html',{'error':'username or password is incorrect!','form':form})
	else:
		form = LoginForm()
		return render(request, 'login_mine.html',{'form':form})
def log_out(request):
		#request.session.flush()
	if request.method=='GET':	#why POST method is not working i don't know need to find it out
		
		logout(request)
		
		#mykey=request.session['mykey']
		#del request.session['mykey']
	return redirect('accounts:login')

@login_required(login_url='accounts:login')
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('upload:view_profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {
        'form': form
    })