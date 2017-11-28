import time

# Timer for each pomodoro cycle each of length 25 minutes
def timer_25min_(disp):
    # count for minute total
    mins = 60*25
    while mins > 0:
        # converting the minute total to minutes and seconds for displaying the remaining time
        quot = mins/60
        rem = mins%60
        # displaying the remaining time if requested by user
        if disp=="Y" or disp=="y" :
            print "Remaining time in current cycle: "+str(quot)+" : "+str(rem)
        # count of one second
        time.sleep(1)
        # Decrementing the minute total
        mins -= 1
    return 0       
 

# Timer for the break periods 
def break_(mins,disp):
    while mins >0:
        quot = mins/60
        rem = mins%60
        if disp=="Y" or disp=="y":
            print "Remaining break time "+str(quot)+" : "+str(rem)
        time.sleep(1)
        mins -= 1
    return 0

# Function to start the timer 
def start_timer(disp):
    # count of the cycles for the pomodoro timer
    rounds = 0
    while rounds != 4:
        print "Current pomodoro cycle : ",rounds+1
        # calling the pomodoro timer function
        timer_25min_(disp)
        # Incrementing the number of cycles each time 
        rounds = rounds + 1

    # minute total for the first break  
    mins = 60*5
    print "break time of 5 minutes"
    #calling the timer for breaks with the minute total, and the option of displaying
    #the timer
    break_(mins,disp)
    rounds = 0
    #resuming the pomodoro timer after the first break
    while rounds != 4:
        print "Current pomodoro cycle : ",rounds+1
        timer_25min_(disp)
        rounds = rounds + 1

    # minute total for the second break--15 minutes
    mins = 60*15
    print "break time of 15 minutes"
    break_(mins,disp)
    # end of timer
    print "end of timer"
    return 0



# Start the timer
run = raw_input("Start the timer? Y/N:  ")

if run=="Y" or run=="y":
    # Option to display the remaining time 
    disp = raw_input("Would you like the time to be displayed? Y/N : ")

    start_timer(disp)

# option to restart the timer
ans = raw_input("Would you like to restart the timer? Y / N : ")
if ans =="Y" or ans=="y":
    disp = raw_input("Would you like the time to be displayed? Y/N : ")
    start_timer(disp)







    
