"""

    Helper functions for data loading and manipulation.

    Author: Explore Data Science Academy.

"""
# Data handling dependencies
import pandas as pd
import numpy as np

def load_movie_titles(path_to_movies):
    """Load movie titles from database records.

    Parameters
    ----------
    path_to_movies : str
        Relative or absolute path to movie database stored
        in .csv format.

    Returns
    -------
    list[str]
        Movie titles.

    """
    df = pd.read_csv(path_to_movies)
    df = df.dropna()
    movie_list = df['title'].to_list()
    return movie_list


def load_movie_genres(path_to_movies):
    df = pd.read_csv(path_to_movies)
    df = df.dropna()
    movie_list = df['genres'].dropna().str.split("|").to_list()
    new_list = []
    for item in movie_list:
        if item:
            for i in item:
                if i != '(no genres listed)':
                    new_list.append(i)
    new_list = list(set(new_list))

    return new_list
