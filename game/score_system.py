import time

  
# Timer starts
round_start_time = time.time()
last_recorded_time = round_start_time
choice_number = 1
value = ""
turn = True
while turn == True:  
                

    # The current lap-time
    laptime = round((time.time() - last_recorded_time), 2)

    # Total time elapsed since the timer started
    totaltime = round((time.time() - round_start_time), 2)

    # Printing the lap number, lap-time, and total time
    print("Lap No. "+str(choice_number))
    print("Total Time: "+str(totaltime))
    print("Lap Time: "+str(laptime))
            
    print("*"*20)

    # Updating the previous total time and lap number
    last_recorded_time = time.time()
    choice_number += 1
  
