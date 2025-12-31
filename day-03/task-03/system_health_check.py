import psutil

def get_cpu_threshold():
    try:
        threshold = int(input("Enter the CPU threshold (0-100): "))
        if threshold <0 or threshold >100:
            raise ValueError("Threshold must be between 0-100")
        return threshold
    except ValueError as e:
        print(f"Invalid Input: {e}" )
        return None
        
def check_cpu_usage(threshold):
    try:
        cpu_usage = psutil.cpu_percent(interval=1)
        print(f"current cpu usage: {cpu_usage}%")

        if cpu_usage > threshold:
            print("⚠️ Warning: CPU usage is above threshold. Admin notification triggered.")
        else:
            print("CPU usage is within normal limits.")
    except Exception as e:
        print(f"Error while checking CPU usage : {e} ")

def main():
    threshold = get_cpu_threshold()
    
    if threshold is not None:
        check_cpu_usage(threshold)
    else:
        print("Script Exit safely due to invalid input.")

if __name__ == "__main__":
    main()
    