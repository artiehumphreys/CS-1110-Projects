#Artie Humphreys, bsg6vr
def maxServed(fptr, year, served):
    """

    :param fptr: a file containing all of the data from the VA state food bank
    :param year: a parameter used to fetch only the data from a certain year
    :param served: a parameter used to determine which category they want to analyze (0 for households, 1 for individuals, 2 for children)
    :return: the name of the county with the most of the set paramter during the given year
    """

    if not year in [2019, 2020, 2021]:
        return ("")  # no instructions are given for how to handle an incorrect input
    if served == 0: #for households
        num = 3 #index in the list
    if served == 1: #for individuals
        num = 4
    curmax = 0 #a current maximum integer for determining the most (Food)
    for line in fptr: #for each line in the file
        if line[0] == "Y": #a case for the very first line where instead of data its headers
            pass
        else:
            line = line.strip()
            line = line.split(",") #making a list of everything
            if int(line[0]) == year:
                if served == 2: #for the children
                    if line[6] == "":
                        food1 = 0
                    else:
                        food1 = int(line[6])
                    if line[7] == "":
                        food2 = 0
                    else:
                        food2 = int(line[7])
                    food = food1
                elif not line[num] == "":
                    food = int(line[num])
                else: #for empty submissions
                    food = 0
                if food >= curmax: #to see if its the most
                    county = str(line[2])
                    curmax = food
                    print(curmax)
    return (county)

