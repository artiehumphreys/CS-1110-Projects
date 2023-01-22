#Artie Humphreys, bsg6vr

import urllib.request
#url = 'http://arcanum.cs.virginia.edu/cs1110/files/louslist/CS'
#lous_list = urllib.request.urlopen(url)


def instructor_lectures(dept, instructor):
    """

    :param dept: a string containing which department in Lou's list you want to explore (gets added to the lou's list url)
    :param instructor: a string containing the name of the desired instructor
    :return: a list of the classes that the specified instructor teaches in that department
    """
    url = 'http://arcanum.cs.virginia.edu/cs1110/files/louslist' + '/' + dept
    lous_list = urllib.request.urlopen(url)
    everything = [] #a list of every single element in the specific web page (everything in between '|')
    classes = [] #for the return statement
    for rows in lous_list: #for each row in the web page
        rows = rows.decode('utf-8') #decoding
        elements = rows.strip().split('|')
        everything.append(elements) #adding every point of information to everything (a nested list to keep each row in its own list)
    for lists in range(len(everything)): #for each nested list in everything
        if (instructor == everything[lists][4] or instructor+"+1" == everything[lists][4]) and everything[lists][3] not in classes and everything[lists][5] == 'Lecture':  #if the instructor in the row is the same as the given one and the class isn't already in the list
            classes.append(everything[lists][3])
    lous_list.close()
    return(classes)

def compatible_classes(first_class, second_class, needs_open_space=False):
    """

    :param first_class: A string containing the first class that the user wants to compare to see if its compatible (in the form dept number-class number)
    :param second_class: A string containing the second class that the user wants to compare to see if its compatible (in the form dept number-class number)
    :param needs_open_space: A boolean used only if its set to True. If true, each class needs at least one open spot.
    :return:
    """
    extension1 = first_class.split(' ')[0] #the department of the first class (splitting it assuming the put a space between the department and the class number)
    extension2 = second_class.split(' ')[0] #the department of the second class
    everything = [] #same everything as before

    #first class

    url = 'http://arcanum.cs.virginia.edu/cs1110/files/louslist' + '/' + extension1
    lous_list = urllib.request.urlopen(url)
    for rows in lous_list: #same for loop as first function
        rows = rows.decode('utf-8')
        elements = rows.strip().split('|')
        everything.append(elements)
    for lists in range (len(everything)): #same bounds as first function
        if (str(everything[lists][0]) + " " + str(everything[lists][1]) + "-" + str(everything[lists][2])) == first_class: #formatting the list so that it's in the form "dept number-class number" and comparing it to the input
            start_time1 = int(everything[lists][12]) #sorry for the hard coding, but this is for making comparison a lot easier
            end_time1 = int(everything[lists][13])
            monday1 = everything[lists][7]
            tuesday1 = everything[lists][8]
            wednesday1 = everything[lists][9]
            thursday1 = everything[lists][10]
            friday1 = everything[lists][11]
            seats_taken1 = int(everything[lists][15])
            seats_available1 = int(everything[lists][16])
    lous_list.close()

    #second class

    url = 'http://arcanum.cs.virginia.edu/cs1110/files/louslist' + '/' + extension2 #doing the same thing for the second class
    lous_list = urllib.request.urlopen(url)
    for rows in lous_list:
        rows = rows.decode('utf-8')
        elements = rows.strip().split('|')
        everything.append(elements)
    for lists in range (len(everything)):
        if (str(everything[lists][0]) + " " + str(everything[lists][1]) + "-" + str(everything[lists][2])) == second_class:
            start_time2 = int(everything[lists][12])
            end_time2 = int(everything[lists][13])
            monday2 = everything[lists][7]
            tuesday2 = everything[lists][8]
            wednesday2 = everything[lists][9]
            thursday2 = everything[lists][10]
            friday2 = everything[lists][11]
            seats_taken2 = int(everything[lists][15])
            seats_available2 = int(everything[lists][16])
    lous_list.close()

    compatibility = True
    if start_time1 <= start_time2 <= end_time1 or start_time2 <= start_time1 <= end_time2:
        if monday1 == monday2 or tuesday1 == tuesday2 or wednesday1 == wednesday2 or thursday1 == thursday2 or friday1 == friday2:
            if monday1 == 'true' and monday2 == 'true' or tuesday1 == 'true' and tuesday2 == 'true' or wednesday1 == 'true' and wednesday2 == 'true' or thursday1 == 'true' and thursday2 == 'true' or friday1 == 'true' and friday2 == 'true':
                compatibility = False

    if needs_open_space == True: #case for is classes are full
        if seats_available1 <= seats_taken1 or seats_available2 <= seats_taken2:
            compatibility = False

    return(compatibility)