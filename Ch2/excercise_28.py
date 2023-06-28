"""
Using a Dictionary to Store a Movie Record
"""
movie = {
    'title': 'The Godfather',
    'director': 'Francis Ford Cappola',
    'year': 1972,
    'rating': 9.2
}

print(movie['year'])

# updating dictionary value
movie['rating'] = (movie['rating'] + 9.3) / 2
print(movie['rating'])

# constructing a movie dictionary from scratch, and extending it
movie = {}
movie['title'] = 'The Godfather'
movie['director'] = 'Francis Ford Cappola'
movie['year'] = 1972
movie['rating'] = 9.2

# storing a list inside a dictionary, storing a dictionary within a dictionary
movie['actors'] = ['Marlon Brando', 'Al Pacino', 'James Caan']

movie['other details'] = {
    'runtime': 175,
    'language': 'English'
}
print(movie)
