import spacy

# Load a pre-trained language model
nlp = spacy.load("en_core_web_md")

# Define the description of the watched movie
movie = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."

# Convert the description to a spacy document
movie_doc = nlp(movie)

# Open the movies.txt file for reading
file_path = "movies.txt"
with open(file_path, "r") as file:
    # Initialize an empty list to store the movie titles and similarities
    movies = []
    # Iterate over each line in the file
    for line in file:
        # Split the line by ":" to get the movie title and description
        title, description = line.split(":")
        # Convert the description to a spacy document
        description_doc = nlp(description)
        # Compute the similarity between the watched movie and the current movie
        similarity = movie_doc.similarity(description_doc)
        # Append a tuple of title and similarity to the movies list
        movies.append((title, similarity))
    # Sort the movies list by similarity in descending order
     movies.sort(reverse=True)
    # Print the most similar movie title
    print(f"The most similar movie to our chosen movie is: {movies[0][0]}")