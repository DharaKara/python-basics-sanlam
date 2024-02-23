movies = [
    {"title": "Inception", "ratings": [5, 4, 5, 4, 5]},
    {"title": "Interstellar", "ratings": [5, 5, 4, 5, 4]},
    {"title": "Dunkirk", "ratings": [4, 4, 4, 3, 4]},
    {"title": "The Dark Knight", "ratings": [5, 5, 5, 5, 5]},
    {"title": "Memento", "ratings": [4, 5, 4, 5, 4]},

]

# dont use normal for loop or list comprehension
# final output should include a new keyvalue in list of dictionary
# Task 1.1: find average for all - map, filter, all, ...
# titles
# titles=map(lambda movie: movie['title'],movies)
# print(list(titles))

# average
# avg_rating=map(lambda movie: sum(movie["ratings"]) / len(movie["ratings"]),movies)
# print(list(avg_rating))

# function
def average_rating(movie):
    return sum(movie["ratings"]) / len(movie["ratings"])
   
# movies_with_average = list(map(calculate_average_rating, movies))
# print(movies_with_average)

# Task 1.2: Lambda average of all
# movies_with_average = list(map(lambda movie: {**movie, "average_rating": average_rating(movie)}, movies))
# print(movies_with_average)

# Task 2: Find the top-rated movie using lambda function (key is what to compare by)
# top_rated_movie = max(movies, key=lambda movie: average_rating(movie))
# print(f"The top rated movie is {top_rated_movie['title']}.")

# Task 3: Movies with ratings more than 4.6
more_than = list(filter(lambda movie: average_rating(movie) >= 4.6, movies))
mapped = list(map(lambda movie: movie['title'], more_than))
print(mapped)

# Task 4: Movie names in order of their rating
# output = ['The Dark Night','Inception','Interstellar','Memto','Dunkrik']
# sorted_movies = sorted(movies, key=lambda movie: average_rating(movie), reverse = True)
# output = [movie["title"] for movie in sorted_movies]
# print(output)