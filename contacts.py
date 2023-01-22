def update(contactDict, list_of_values):
    """

    :param contactDict: a dictionary of the name of a disney character and their contact info (email)
    :param list_of_values: a list of tuples containing an action, the name of the character, and their email
    :return:
    """
    error = 0 #initializing the error count
    #i used elifs and put an else at the end to avoid repeated counting
    for tup in range(len(list_of_values)): # for the number of tuples in the list of tuples (using in range for indexing pruposes)
        if list_of_values[tup][0] == '+' and not list_of_values[tup][1] in contactDict: #addition case (if the action is + and the name is not in the contact dict)
            contactDict[list_of_values[tup][1]] = list_of_values[tup][2] #setting new dict value
        elif list_of_values[tup][0] == '/' and list_of_values[tup][1] in contactDict: #division case (if the action is / and the name is in the contact dict)
            contactDict[list_of_values[tup][1]] = list_of_values[tup][2]
        elif list_of_values[tup][0] == '-' and list_of_values[tup][1] in contactDict: #subtraction case (if the action is - and the name is in the contact dict)
            del contactDict[list_of_values[tup][1]] #we discussed del in our lecture, but we're deleting the key:value pair from the contact dict
        elif not list_of_values[tup][0] == '-' or not list_of_values[tup][0] == '+' or not list_of_values[tup][0] == '/': #if the action isn't one of the three from earlier
            error= error + 1
        else:
            error = error + 1 #if these cases fail

    return(error)
