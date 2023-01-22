#Artie Humphreys, bsg6vr

college = {'Virginia': 13,
 'Ohio': 18,
 'Minnesota': 10,
 'Alabama': 9,
 'Maine' : 4}

state_votes = {} #global dict with the format {state name: candidate}

def add_state(name, votes):
    """

    :param name: the name of a state that you would like to add to the voting dictionary
    :param votes: a dictionary of how many votes each candidate obtained
    :return: nothing (lol), just updates the global state_votes dictionary
    """
    global state_votes
    min = 0 #for looping through each state and finding the highest number of votes
    for key in votes:
        if votes[key] > min: #if the amount of votes this candidate is > the current highest
            min = votes[key]
    state_votes[name] = list(votes.keys())[list(votes.values()).index(min)] #declaring that the candidate for the given state is the value of the key with the index of the winning candidate (inspired by stack exchange: https://stackoverflow.com/questions/8023306/get-key-by-value-in-dictionary)

def winner(college):
    """

    :param college: the dictionary including the states in the electoral college and how many votes they get each
    :return: the winning candidate or "No Winner." if a candidate didn't recieve 50% or more of the votes
    """
    global state_votes
    candidate_votes = {} #new dict with the format: {candidate : electoral votes}
    sum_of_votes = 0 #initializing of the running sum for tallying the total number of votes
    winner = ""
    for states in state_votes.keys(): #looping through each state in state_votes ({state: candidate})
        if not states in college: #if the state isn't in the college (kind of a base case)
            college[states] = 0
        else:
            candidate_votes[state_votes[states]] = college[states] + candidate_votes.get(state_votes[states], 0) #using state_votes[states] to access the name of each candidate, I set the value associated with the key of the candidates name in the new dictionary to the amount of electoral votes it gets plus any previous votes.
    for votes in state_votes.keys(): #looping through each state again
        sum_of_votes = sum_of_votes + college[votes] #adding the amount of electoral votes each state has and adding it to the total
    for candidates in candidate_votes.keys():
        if candidate_votes[candidates] >= (sum_of_votes / 2): #to see if a candidate got more than half of the votes
            winner = candidates
    if winner == "":
        return("No Winner")
    else:
        return(winner) #i did this if else statement to avoid errors with for loops only running once after return is called
def clear():
    """

    :return: resets the state votes dictionary (allowing for new votes to come in from the states)
    """
    global state_votes
    state_votes = {}