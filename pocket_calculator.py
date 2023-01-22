#Artie Humphreys
#bsg6vr

global curr_val
curr_val = 0
most_rec_opp = ''
most_rec_arg = int
full_express = '0'
eval_num = 0 #used to keep track of how many times the step function is run (for get_expres function)
last_eval_num = 0 #to make sure there are no repeats of the most recent argument and operator in the get_expres string since I call the function inside of step

def get_value():
    """

    :return: returns the current value stored in the calculator
    """
    global curr_val
    return(curr_val)

def clear(arg = 0):
    """

    :param arg: A number that defaults to zero when the calculator clears (doesn't have to be zero)
    :return:
    """
    global most_rec_arg
    global most_rec_opp
    global curr_val
    global full_express
    global eval_num
    most_rec_arg = 0
    most_rec_opp = ''
    curr_val = arg
    full_express = str(arg)
    eval_num = 0
    return(arg)

def step(op, arg):
    """

    :param op: the operater (+,-,*,//)
    :param arg: the argument (integer)
    :return: A new value for the calculator
    """

    global eval_num
    global most_rec_arg
    global most_rec_opp
    global curr_val
    current = int(get_value())
    if op == '+':
        current += arg
    elif op == '-':
        current = current - arg
    elif op == '*':
        current = current * arg
    elif op == '//':
        current = current // arg
    most_rec_arg = arg
    most_rec_opp = op
    curr_val = current
    eval_num+=1
    get_expr()
    return (current)
def repeat():
    """

    :return: the new value of the calculator after repeating the most recent operation
    """
    val = step(most_rec_opp, most_rec_arg)
    return (val)
def get_expr():
    """

    :return: A new string of all of the operations. Since I call it in the step function, I have to make sure that I'm not repeating any expressions.
    """
    global full_express
    global most_rec_arg
    global most_rec_opp
    global eval_num
    global last_eval_num

    if eval_num == 0: #base case
        return('0')
    elif last_eval_num == eval_num: #If the expression has already been added to full_express
        return (full_express)
    else: #addition statements
        full_express = '(' + full_express + ')' + most_rec_opp + str(most_rec_arg)
        last_eval_num = eval_num
        return(full_express)

