# Pomodoro-Timer

The pomodoro timer will follow the classic pattern of 4 rounds of 25 minutes with a 3-5 minute break and then after 4
rounds a break of 15-30 minutes. 

The application allows the User to:
1. Start the timer.
2. Alerts the user when there is no more time left on the timer.
3. Allows the user to view the remaining time of the timer.

General Algorithm:
1. The user is provided the option to start the timer.
2. The user is provided the option to display the remaining time.
3. The timer function for each Pomodoro cycle is called from the main function. 
4. After 4 cycles of the timer, the timer function for the break period is called .
5. The timer function for the next 4 cycles of the Pomodoro timer is called again.
6. The User is provided the option to restart the whole process again or exit. 
