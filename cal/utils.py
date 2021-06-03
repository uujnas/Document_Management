from datetime import datetime, timedelta
from calendar import HTMLCalendar
from .models import Event
#from request_middlware.middleware import get_request
#from .current_user import user_from_session_key
import calendar
from django_currentuser.middleware import (
    get_current_user, get_current_authenticated_user)

class Calendar(HTMLCalendar):
    calendar.setfirstweekday(calendar.SUNDAY)
    def __init__(self, year=None, month=None): #,owner
        self.year = year
        self.month = month
        calendar.setfirstweekday(calendar.SUNDAY)
        #Event.objects.filter(user=self.request.user)
        super(Calendar, self).__init__()
    
    # formats a day as a td
    # filter event by day
    def formatday(self, day, events):
        usr = get_current_user() 
		#user=current_user(request) # user_id = bundle.request.user.id 
        #print(usr)
        events_per_day = events.filter(start_time__day=day,user=usr) #,user=self.request.user)   ,user=current_user
        #events_per_day = events_per_day.filter(user=current_user)
        #Event.objects.filter(user=self.request.user)
        d = ''
        for event in events_per_day:
            #print(event.user)
            #if event.user==current_user(event.user): 
                #print(event.user)           
            cin = ''
            if event.start_time is not None:
                cin = event.start_time
                cin = cin.strftime('%H:%M:%S')
                d += f'<li>In time: {cin} </li>' #|date:"H:i"
                #d += f'<li>In time: {event.user} </li>'
                                   
            cout = ''
            if event.end_time is not None:
                cout = event.end_time
                cout = cout.strftime('%H:%M:%S')
                d += f'<li>Out time: {cout} </li>'
                        
        if day != 0:
            return f"<td><span class='date'>{day}</span><ul> {d}</ul></td>"
        return '<td></td>'
       
           
    # formats a week as a tr
    def formatweek(self, theweek, events):
        week = ''
        for d, weekday in theweek:
            week += self.formatday(d, events)
        return f'<tr> {week} </tr>'

    # formats a month as a table
    # filter events by year and month
    def formatmonth(self, withyear=True):
        events = Event.objects.filter(start_time__year=self.year, start_time__month=self.month)

        cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
        cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
        cal += f'{self.formatweekheader()}\n'
        for week in self.monthdays2calendar(self.year, self.month):
            cal += f'{self.formatweek(week, events)}\n'
        return cal
