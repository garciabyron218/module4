#Byron Garcia
# This program will give you the time an alarm will go off based on the initial time and wait time
time_now_str = input("What time is it now? ")
time_wait_str = input("What is the number of hours to wait? ")
time_now_int = int(time_now_str)
time_wait_int = int(time_wait_str)

time_alarm: int = time_now_int + time_wait_int
print('Alarm will go off at ', time_alarm)
