#Artie Humphreys
#bsg6vr

cs111x_enrollments = [[614, 88, 144],
 [534, 59, 148],
 [0, 0, 0],
 [682, 77, 146],
 [501, 93, 136],
 [44, 0, 0]]

def mean_all(table):
    """

    :param table: takes in a table of values (assuming each inner list has the same length)
    :return: the average of all of the terms in the list
    """
    sum = 0
    average = 0
    count = 0
    for i in range (0,len(table)):
        for j in range (0, len(table[0])): #nested loop for all terms
            sum += table[i][j] #running sum
            count += 1
    average = sum / count
    return (average)

def mean_by_row(table):
    """

    :param table: takes in a table of values (assuming each inner list has the same length)
    :return: a list of the mean of each row of data
    """
    average = []
    for row in range (0,len(table)): #(0,6) -> isolating each row
        sum1 = 0 #calling it here so that it resets after each iteration
        for col in range(0, len(table[0])): #(0,3)
            sum1 += (table[row][col])
        average.append(sum1 / len(table[0])) #using append so that we don't have to specify the length of the list at the beginning
    return(average)

def mean_by_col(table):
    """

    :param table: takes in a table of values (assuming each inner list has the same length)
    :return: a list of the mean of each column of data
    """
     #same as mean by row function, but a different length
    sum1 = 0
    average = []
    for i in range (0,len(table[0])): #(0,3) -> isolating each column
        sum1 = 0 #calling sum here since I was getting int not iterable error and just adding each list value onto it and resetting it after every iteration
        for j in range (0,len(table)): #(0,6) -> for adding all of the values in the column
            sum1 += (table[j][i]) #first index changes while the second remains the same
        average.append(sum1 / len(table)) #appending to the end of the list
    return(average)




