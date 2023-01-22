def fine(speed_limit, my_speed, zone = "default"):
    """
    Determine how much a driver will have to pay based on their speed over the speed in and in which zone they committed the infraction
    :param speed_limit: The speed limit on the road
    :param my_speed: How fast the person was going
    :param zone: What zone was it in? (residential, school, etc.)
    :return: an amount of money (the fine)
    """
    speed_over = my_speed - speed_limit #calculating how much the driver went over the speed limit
    fine = 0
    if(speed_over < -10): #first case (very exclusive case)
        fine = 30
    elif(speed_over >= 20): #the wreckless driving case
        fine = 350
    elif (zone == "residential" and speed_over > 0): #residential area case (8 times the speed over plus 200) (using speed_over > 0 to make sure that no negative cases happen)
        fine = ((8 * speed_over) + 200)
    elif(zone == "default" and speed_over > 0): #the case for when there is no zone given
        fine = 6 * speed_over
    elif(zone == "work" or "school" and speed_over > 0): #work or school zone case
        fine = 7 * speed_over #formula given

    return fine

def demerits(speed_limit, my_speed):
    """
    calculates the number of demerits given based on the offense
    :param speed_limit: The speed limit on the road
    :param my_speed: How fast the person was going
    :return: The number of demerits they will receive
    """
    speed_over = my_speed - speed_limit #same calculation as the last time
    demerit = 0
    if (speed_over >= 20): #first case (easiest one)
        demerit = 6
    elif (10 <= speed_over <= 19): #4 demerit case
        demerit = 4
    elif(1 <= speed_over <= 9): #3 demerit case
        demerit = 3
    return (demerit) #number of demerits
