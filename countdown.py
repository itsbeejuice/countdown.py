import time

def countdown(t):
    while t>0:
        mins,secs=divmod(t,60)
        timer='{:02d}:{:02d}'.format(mins,secs)
        print(timer+"\r",end="")
        time.sleep(1)
        t-=1
    print("Timer is done")

print("How many seconds should i count down?: ")
sec=input()
countdown(int(sec))

# websites used:
# https://junilearning.com/blog/coding-projects/make-countdown-timer-python/ 
# https://www.codespeedy.com/how-to-create-a-countdown-in-python/
# https://www.wikihow.com/Make-a-Countdown-Program-in-Python