from datetime import timedelta
import datetime
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

# pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org pytz, colorama

colorama_init()

final_time = timedelta()

while(True): # Infinite loop, unless user doesn't put in anything
    
    c = str(input('Enter time (HH:MM): '))
    
    if len(c) < 1: # Final print-out
        s_hour, s_min = str(final_time).split(':')[:2]
        zero_added = ''
        if int(s_min)/60*100 < 10: zero_added = '0' # e.g. 5,05 SAP - zero added; 5,15 SAP - not zero added
        print(f"\n{Fore.BLUE}Total is {':'.join(str(final_time).split(':')[:2])} (HH:MM), {Fore.GREEN}{s_hour},{zero_added}{round(int(s_min)/60*100)} SAP time")
        exit()

    try: 
        p_hours, p_minutes = c.split(':')
        final_time += timedelta(seconds=(int(p_hours)*3600 + int(p_minutes)*60))

    except:
        print("An error occurred, use format HH:MM")
    