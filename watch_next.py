import spacy  # importing spacy
nlp = spacy.load('en_core_web_md') 

# define a class 
class Movie:
    #initialise the attributes
    def __init__(self, title, description):
        self.title = title
        self.description = description


description_to_compare = 'Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the illuminatr trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator.'
movie_list = [] #store a list of movies

# define a function which takes in the description as a parameter
def movie_recommend(d_to_compare):
    f = open('movies.txt', 'r') #open and read the file movies.txt
    line = f.readline() #read the  line
    line_list = line.split(':') #split the  line

    while len(line_list)  > 1 : #until reading empty line
        try: 
            title = line_list[0]
            description = line_list[1].strip('\n')
            #create an object of movie
            movie = Movie(title,description)
            #append an object to list 'movie_list'
            movie_list.append(movie)
            #read the next line
            line = f.readline()
            line_list = line.split(':') 

        except  ValueError:
            print("Something went wrong.")
        except FileNotFoundError:
            print("The file does not exist.")

    f.close()

    d_token = nlp(d_to_compare)
    # create a list to store 'title' & 'similarity'
    title_similarity_list = []
    # create a list to store 'similarity'
    similarity_list = []

    # loop through every movie and obtain the extent of similarity with the description to compare
    for movie in movie_list:
        token = nlp(movie.description)
        similarity = (token.similarity(d_token))
        title_similarity_list.append([movie.title,similarity])
        similarity_list.append(similarity)
    # loop through every movie to find the title of the most similar movie
    for movie in title_similarity_list:
        if movie[1] == max(similarity_list):
            movie_to_recommned = movie[0]
        
    return print(f"The title of the most similar movie is '{movie_to_recommned}'.")

movie_recommend(description_to_compare)


