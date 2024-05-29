currentTime=int(input('Enter the current time in hours as an integer ranging form 0-23\n'))
waitHours = int(input('Enter the number of hours before you want the alarm to go off as a positive integer\n'))
endTime = currentTime + waitHours
alarmTime= endTime%24
print('The time on the 24 hour clock when the alarm will ring is {}'.format(alarmTime))