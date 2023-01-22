#Artie Humphreys, bsg6vr
#3 inputs: a random number, a birth year, and a semi-random number
#2 outputs: the magic number and the age

random_num = int(input("Pick a number between 1 and 10: ")) #input for picking a random number
if random_num > 10 or random_num < 0: #just for fun
    print("Not a valid input")
    exit()
birth_this_year = int(input("If you've already had a birthday this year, enter 1772. Otherwise, enter 1771: ")) #part of the math
if 1771 < birth_this_year < 1772:
    print("Not a valid input")
    exit()
born = int(input("Enter the year that you were born: ")) #birth year input

magic_num = (((((random_num*2)+5)*50)+birth_this_year)-born) #math given to us. Sorry about the number of parentheses

age = magic_num - (random_num*100) #finding the age from the magic number

print(('The magic number is "{}". That means you are {}!').format(magic_num, age)) #return statement