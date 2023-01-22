# Artie Humphreys, bsg6vr

namestr = "What player would you like to calculate statistics for? "  # declaring strings for the inputs
name = str(input(namestr))  # implementing the inputs - using the right data types
opponentstr = "What team was the opponent in the game you would like to calculate statistics for? " #str at the end means string
opponent = str(input(opponentstr))
threeptattemptstr = "How many 3's did {} attempt this game? ".format(name) #three pointer attempts
threeptattempt = int(input(threeptattemptstr))
threeptmakestr = "How many 3's did {} make this game? ".format(name) #three pointers made
threeptmake = int(input(threeptmakestr))
twoptattemptstr = "How many 2's did {} attempt this game? ".format(name)
twoptattempt = int(input(twoptattemptstr))
twoptmakestr = "How many 2's did {} make this game? ".format(name)
twoptmake = int(input(twoptmakestr))
ftattemptstr = "How many free throws did {} attempt this game? ".format(name) # ft is free throw
ftattempt = int(input(ftattemptstr))
ftmakestr = "How many free throws did {} make this game? ".format(name)
ftmake = int(input(ftmakestr))
fgpct = (((twoptmake + threeptmake) / (twoptattempt + threeptattempt)) * 100) #field goal percentage
ftpct = ((ftmake / ftattempt) * 100) #free throw percentage

pctstr = "{} had a {}% field goal percentage and a {}% free throw percentage".format(name, fgpct, ftpct) #I previously didn't know how to put variable values into a string, so I used the following website (https://matthew-brett.github.io/teaching/string_formatting.html) to learn about the .format function as a way to insert values into strings. (No code was copied)
print(pctstr)

pttotal = ((threeptmake * 3) + (twoptmake * 2) + (ftmake)) #point total (3's, 2's, 1's)

ptstr = "{} scored {} points against {}. Wahoowa!".format(name, pttotal, opponent) #same .format function
print(ptstr)
