import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

data = {
    "Movie": [
        "Inception","Titanic","Avatar","Interstellar","The Dark Knight",
        "The Matrix","Avengers","Iron Man","Gravity","The Notebook",
        "Mad Max","Joker","Doctor Strange","Spider-Man","Black Panther"
    ],

    "Action":  [1,0,1,1,1,1,1,1,0,0,1,0,1,1,1],
    "Romance": [0,1,0,0,0,0,0,0,0,1,0,0,0,0,0],
    "SciFi":   [1,0,1,1,0,1,1,1,1,0,0,0,1,0,0],
    "Drama":   [0,1,0,0,1,0,0,0,1,1,0,1,0,0,0]
}

df = pd.DataFrame(data)

df.set_index("Movie", inplace=True)

similarity = cosine_similarity(df)

similarity_df = pd.DataFrame(similarity, index=df.index, columns=df.index)

def recommend(movie_name):

    if movie_name not in similarity_df.index:
        print("Movie not found in database.")
        return

    print(f"\nMovies similar to '{movie_name}':\n")

    scores = similarity_df[movie_name].sort_values(ascending=False)

    for movie in scores.index[1:6]:
        print(movie)


movie = input("Enter a movie name: ")
recommend(movie)