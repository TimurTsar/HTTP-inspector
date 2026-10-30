#lab1, HTTP-inspector
#this lab asks user URL-address, then it shows status code, headers and the operation time
#if it's error, it will show error in terminal

#This lab requires "Requests" and "time" library

import requests
import time
################


url = input('Type your URL-address here: ') #asking user a URL

#starting time
time_start = time.perf_counter()

try:
    response = requests.get(url=url, timeout=5) #sending request with user's inputed URL
    print('Request was successfully sent!')
    print('') #just for some space in terminal. Looks good
    print('Your URL: '+url)
    print(f'Status code: '+str(response.status_code))
    print(f'Headers: '+str(response.headers))
    
    #ending time counting
    time_end = time.perf_counter()
    print(f'Time: '+str(time_end-time_start)+' seconds.') #time = time_end - time_start 

except requests.exceptions.RequestException as e: #this part of code shows an error in "e" variable
    print('') #it's for space in terminal too
    print('Error! Something went wrong. Please, try again!')
    print(f'Error code: '+str(e))