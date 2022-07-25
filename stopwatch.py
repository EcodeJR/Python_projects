import time
while True:
    try:
        input("Press Enter to continue and ctrl C to exit the stopwatch")
        start_time=time.time()
        print("Stopwatch has started")
        while True:
            print("Time elapsed:",round(time.time()-start_time,0),'secs',end='\n')
            time.sleep(1)
            
            
    except KeyboardInterrupt:
        print("Timer has stopped")
        end_time=time.time()
        print("The time elapsed:",round(time.time()-end_time,2),'secs')
        break