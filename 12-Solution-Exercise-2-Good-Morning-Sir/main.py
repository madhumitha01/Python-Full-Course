import time

# Get the current hour as an integer
current_hour = int(time.strftime('%H'))

# Greet based on the hour
if 5 <= current_hour < 12:
    print("Good Morning, Sir!")
elif 12 <= current_hour < 17:
    print("Good Afternoon, Sir!")
elif 17 <= current_hour < 21:
    print("Good Evening, Sir!")
else:
    print("It's late, Sir. Good Night!")
