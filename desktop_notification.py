from win10toast import ToastNotifier
import datetime

self_note = ToastNotifier()

def __main__():
    a_event, message = set_notevalues()
    a_year, a_month, a_date, a_hour, a_minute = set_datevalues()
    to_display = set_time(a_year,a_month,a_date,a_hour,a_minute)
    display_note(to_display,a_event,message)



def set_notevalues():
    a_event = input('Title for the notification?  ')
    message = input('A description of the notification? ')
    return a_event, message
   
def set_datevalues():
    a_year = int(input('In which year should the notification display? '))
    a_month = int(input('In which month should the notification display?(enter as a number)'))
    a_date = int(input('On which date should the notification display? '))
    a_hour = int(input('At what hour should do the notification display?'))
    a_minute = int(input('At how many minutes? '))
    return a_year, a_month, a_date, a_hour, a_minute


def set_time(a_year,a_month,a_date,a_hour,a_minute):
    to_display = datetime.datetime(a_year,a_month,a_date,a_hour,a_minute)
    to_display = str(to_display)
    return to_display

def display_note(to_display,a_event,message):
    while True:
        current_time = datetime.datetime.now()
        c_t = current_time.strftime("%Y-%m-%d %H:%M:%S")
        if c_t == to_display:
            self_note.show_toast(a_event, message, duration = 20, icon_path =None)
            break

__main__()
   


