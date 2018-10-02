# writing a python script to use pandas for the first time

import pandas as pd

# let's create a list of songs
songs = ['NY State of Mind', 'Warning', 'One More Chance', 'Headlines']

# list of corresponding artists
artists = ['Nas', 'Biggie', 'MJ', 'Drake']

# dictionary of artists and songs
song_arts = {'Nas': 'NY State of Mind', 'Biggie': 'Warning', 'MJ': 'One More Chance', 'Drake': 'Headlines'}

# pd.Series() creates a series object from the data, and you have
# to define the data as a parameter. we will create one from the songs list
ser_num = pd.Series(data=songs)


# now make the artist names the indexes
ser_art = pd.Series(data=songs, index=artists)


# now create a series from a dictionary 
series_dictionary = pd.Series(song_arts)
print(series_dictionary)

