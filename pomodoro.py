
# --------------
#  pomodoro.py 
#  13 Feb 2021 
# --------------

import time
import os

# optional: user-set parameters

try: # focus time [ minutes ]
    focus_time = float(input("Focus time (min): "))
except ValueError:
    focus_time = 0.1
try: # short break time [ minutes ]
    short_break = float(input("Break time (min): "))
except ValueError:
    short_break = focus_time
try: # target number of pomodoros [ unitless ]
    reps_goal = int(input("Number of intervals: "))
except ValueError:
    reps_goal = 10 
    
# misc settings
reps_done = 0 # number of pomodoros done [ unitless ]
N_chime = 3 # number of chimes at the end of an interval
t_0 = time.time() # set zero time [ seconds, float ]
focus_state = True # current state of timer [ Boolean ]
chime_path = 'Ping.aiff'


def chime(N):
    for i in range(N):
        os.system('afplay '+chime_path)
        time.sleep(0.05)

def interval(time_period, focus_state, t_0, reps_done, N_chime):
    # time_period:    length of interval in minutes
    # t_0:            starting time
    
    
    print("Focus", reps_done, end="   \n") if focus_state else print("Break", reps_done, end="   \n")
    
    for j in range(int(60*time_period)):

        delta_t = time.strftime("%H:%M:%S", time.gmtime(time.time() - t_0 + 1))
        print(delta_t, end="\r")
        time.sleep(1)
        
    chime(N_chime)

    return not(focus_state), reps_done+1, time.time()


print("""
Pomodoro starting:
[ {} min focus, {} min break, {} reps ]
""".format(focus_time,short_break,reps_goal))
for i in range(reps_goal):

    # focus interval
    focus_state, reps_done, t_0 = interval(focus_time, focus_state, t_0, reps_done, N_chime)

    #break interval
    focus_state, reps_done, t_0 = interval(short_break, focus_state, t_0, reps_done - 1, N_chime)

print("Done")
    

    
        
