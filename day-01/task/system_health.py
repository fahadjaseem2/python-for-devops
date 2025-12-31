import psutil # Importing the psutil library to monitor system performance

# Function to check CPU usage   
#def system_thershold():
    user_usage = int(input("Enter CPU usage percentage threshold (0-100) ;"))

    # getting the current cpu usage
    cpu_usage = psutil.cpu_percent(interval=1)
    print ("Current CPU usage: ", cpu_usage)

    #compare current cpu usage to user defined threshold
    if cpu_usage > user_usage:
        print ("Warning: CPU usage is above the threshold and mailed to admin.")
    else:
        print ("CPU is operating within normal parameters.")

# Calling the function to check system health
#system_thershold()