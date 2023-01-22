#Artie Humphreys
#bsg6vr

endgame = ["Avengers: Endgame", 2.797, 2019, 8.2, 532]
infwar = ["Avengers: Infinity War", 2.048, 2018, 7.6, 474]
avengers = ["The Avengers", 1.518, 2012, 8.0, 358]
age = ["Avengers: Age of Ultron", 1.405, 2015, 6.8, 370]
bp = ["Black Panther", 1.346, 2018, 8.3, 515]
incredible = ["Incredibles 2", 1.242, 2018, 7.84, 379]
iron = ["Iron Man 3", 1.214, 2013, 7.0, 325]

movie = [endgame, infwar, avengers, age, bp, incredible, iron]

def get_name(movie):
    """

    :param movie: the movie
    :return: The name of the movie
    """
    return (movie[0]) #first position of the list (the name of the movie)

def get_gross(movie):
    """

    :param movie: a given movie
    :return: The gross income for the movie
    """
    return (movie[1]) #second position of the list (the gross income of the movie)

def get_rating(movie):
    """

    :param movie: a given movie
    :return: the rating for the given movie
    """
    return (movie[3]) #fourth position of the list (the average rating of the movie)

def get_num_ratings(movie):
    """

    :param movie: a given movie
    :return: the rating of the movie
    """
    return (movie[4]) #fifth position of the list (the amount of ratings of the movie)

def better_movies(movie_name, movies_list):
    """

    :param movie_name: the name of a given movie
    :param movies_list: a list of all of the movies
    :return: a list of movies with a better rating
    """
    return_val = []
    for i in range (len(movies_list)):
        if movies_list[i][0] == movie_name:
            base_rating = movies_list[i][3]
    for j in range(len(movies_list)):
        if movies_list[j][3] > base_rating: #comparison of the rating of the given movie
            return_val.append(movies_list[j][0:5])
    return(return_val)


def average(category, movies_list):
    """

    :param category: a given category (str)
    :param movies_list: a list of all of the movies
    :return: an average value of the given catergory across all of the movies
    """
    sum = 0
    type(movies_list)
    if category == "rating":
        num = 3
    if category == "gross":
        num = 1
    if category == "number of ratings":
        num = 4
    for j in range (len(movies_list)):
        sum += movies_list[j][num] #running sum
    avg = sum / len(movies_list)
    return (avg)
