from datetime import datetime, timedelta, date
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from django.utils.safestring import mark_safe
import calendar
from django.shortcuts import redirect
from .models import *
from .utils import Calendar
from .forms import EventForm
from django.contrib.auth.decorators import login_required
#from braces.views import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

def index(request):
    return HttpResponse('hello')
	
@login_required(login_url='accounts:login')
def checkin(request):
    att=Event()
    current_time = datetime.now()
    att.start_time = current_time
    att.user = request.user
    att.save()
    #messages.success(request, 'You are checked in Successfully')
    return HttpResponseRedirect(reverse('cal:calendar')) #return redirect(calendar)  #return HttpResponse('You are checked in') leave

@login_required(login_url='accounts:login')
def checkout(request,pk):
    att=Event.objects.get(id=pk)
    current_time = datetime.now()
    att.end_time = current_time
    att.save()
    return HttpResponseRedirect(reverse('cal:calendar'))
 
#@login_required 
class CalendarView(generic.ListView):
    model = Event#(user=request.user)
    #queryset = Event.objects.filter(user=request.user)
    template_name = 'cal/calendar.html'
    def get_queryset(self):
        return Event.objects.filter(user=self.request.user)
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #owner = Event(user=self.request.user)
        d = get_date(self.request.GET.get('month', None))
        cal = Calendar(d.year, d.month) #,owner)
        html_cal = cal.formatmonth(withyear=True)
        #Event.objects.filter(user=self.request.user)
        today = date.today()
        check_in_user = Event.objects.filter(user=self.request.user)
        #print(check_in_user)
        checkin_date = ''
        if not check_in_user.filter(start_time__year=today.year, start_time__month=today.month, start_time__day=today.day).exists():
            #Event.objects.filter(user=self.request.user).exists():
            checkin_date = None
        else:
            #checkin_date = Event(user=self.request.user)
            checkin_date = Event.objects.get(user=self.request.user,start_time__year=today.year, start_time__month=today.month, start_time__day=today.day)
            checkin_date.user = self.request.user         #(Q(start_time__year=today.year, start_time__month=today.month, start_time__day=today.day)| Q(user = self.request.user))
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        context['checkin_date'] = checkin_date
        return context
    


def get_date(req_month):
    if req_month:
        year, month = (int(x) for x in req_month.split('-'))
        return date(year, month, day=1)
    return datetime.today()

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month

def event(request, event_id=None):
    instance = Leave()
    if event_id:
        instance = get_object_or_404(Leave, pk=event_id)
    else:
        instance = Leave()

    form = EventForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        s = form.save(commit = False)
        s.user = request.user
        s.save()
        return HttpResponseRedirect(reverse('cal:calendar'))
    return render(request, 'cal/event.html', {'form': form})

@login_required(login_url='accounts:login')
def view_attendance(request,pk):
    attendance = Event.objects.filter(user_id = pk)
    usr = User.objects.get(id = pk)
    return render(request, 'view_attendance.html',{'att':attendance,'usr':usr})

@login_required(login_url='accounts:login')    
def view_leave(request,pk):
    attendance = Leave.objects.filter(user_id = pk)
    usr = User.objects.get(id = pk)
    return render(request, 'view_leave.html',{'att':attendance,'usr':usr})