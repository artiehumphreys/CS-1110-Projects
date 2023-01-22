#bsg6vr, Artie Humphreys


def gellish2 (age):
    """

    :param age: the user will input an age
    :return: the maximum (healthy) heartrate obtained by someone of the given age
    """
    maxhr = float(191.5-(0.007*age**2)) #formula given
    return (maxhr)

def in_target_range (hr, age):
    """

    :param hr: Heartrate -> used to see if it is within the target heartrate
    :param age: Used for the calculation of the max heart rate
    :return: a boolean (if the heartrate given is within the target heart rate [65% to 85% of max], it returns true. Else false)
    """
    max_bound = 0.85*gellish2(age) #calling the previous function to get the upper bound heart rate for that age
    min_bound = 0.65*gellish2(age) #same but lower bound
    return(min_bound <= hr <= max_bound) #return statement using relational operators to determine if the heartrate is within the range
