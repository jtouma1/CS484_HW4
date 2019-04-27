import pandas as pd
import numpy as np
import threading
from movie import *


#helper function that puts all data into pandas dataframes with correct headers
def get_dataframes():
	#load in files
	mov_actor_file = open("../additional_files/movie_actors.dat", encoding = "ISO-8859-1").readlines()
	mov_directors_file = open("../additional_files/movie_directors.dat", encoding = "ISO-8859-1").readlines()
	mov_genres_file = open("../additional_files/movie_genres.dat", encoding = "ISO-8859-1").readlines()
	mov_tags_file = open("../additional_files/movie_tags.dat", encoding = "ISO-8859-1").readlines()
	tags_file = open("../additional_files/tags.dat", encoding = "ISO-8859-1").readlines()
	test_file = open("../additional_files/test.dat", encoding = "ISO-8859-1").readlines()
	train_file = open("../additional_files/train.dat", encoding = "ISO-8859-1").readlines()
	user_tagged_file = open("../additional_files/user_taggedmovies.dat", encoding = "ISO-8859-1").readlines()

	#put raw data into files, removing newlines at end of strings and splitting at every \t
	actor_data = pd.DataFrame(data = [x.strip("\n").split("\t") for x in mov_actor_file])
	director_data = pd.DataFrame(data = [x.strip("\n").split("\t") for x in mov_directors_file])
	genre_data = pd.DataFrame(data = [x.strip("\n").split("\t") for x in mov_genres_file])
	tags_data = pd.DataFrame(data = [x.strip("\n").split("\t") for x in mov_tags_file])
	user_tag_data = pd.DataFrame(data = [x.strip("\n").split(" ") for x in user_tagged_file])
	test_data = pd.DataFrame(data = [x.strip("\n").split(" ") for x in test_file])
	train_data = pd.DataFrame(data = [x.strip("\n").split(" ") for x in train_file])

	#replace header indexs with header labels in data
	actor_data.columns = actor_data.loc[0].tolist()
	actor_data.drop([0],inplace = True)
	actor_data = actor_data.astype({'movieID':int, 'actorID':str, 'actorName':str, 'ranking':int})

	director_data.columns = director_data.loc[0].tolist()
	director_data.drop([0],inplace = True)
	director_data = director_data.astype({'movieID':int,'directorID':str,'directorName':str})

	genre_data.columns = genre_data.loc[0].tolist()
	genre_data.drop([0],inplace = True)
	genre_data = genre_data.astype({'movieID':int,'genre':str})

	tags_data.columns = tags_data.loc[0].tolist()
	tags_data.drop([0],inplace = True)
	tags_data = tags_data.astype({'movieID':int,'tagID':int,'tagWeight':int})

	user_tag_data.columns = user_tag_data.loc[0].tolist()
	user_tag_data.drop([0],inplace = True)
	user_tag_data = user_tag_data.astype({'userID':int, 'movieID':int, 'tagID':int})

	train_data.columns = train_data.loc[0].tolist()
	train_data.drop([0],inplace = True)
	train_data = train_data.astype({'userID':int, 'movieID':int, 'rating':float})

	test_data.columns = test_data.loc[0].tolist()
	test_data.drop([0],inplace = True)
	test_data = test_data.astype({'userID':int, 'movieID':int})

	return actor_data,director_data,genre_data,tags_data,user_tag_data,train_data,test_data

def get_movies():
	actor_data,director_data,genre_data,tags_data,user_tag_data,train_data,test_data = get_dataframes()
	#print(director_data.dtypes)
	#print(genre_data.dtypes)
	#print(tags_data.dtypes)
	#print(user_tag_data.dtypes)

	#main idea that I want to do:
	#For each movie in the dataset 
	#	For each user who reviewed it 
	#		For each other movie reviewed by that customer 
	#			Record the user's review

	#movie has:
		#actors
			#each with a ranking 
		#director
		#tags
			#each with a weight
		#user ratings
			#between 1-5
		#genres

	#all ids added to movies list so now we can make that many movie objects (should be 10174)
	movies_ids = []
	for movie_id in actor_data.itertuples():
		if movie_id[1] not in movies_ids:
			movies_ids.append(movie_id[1])
	print("finished finding IDs")
	#grabs each movie id and makes a Movie object with all attributes associated with the movie id
	#last movie id is 65133
	movies = []
	for movie_id in movies_ids:
		#make movie
		movie = Movie(movie_id)
		for actor in actor_data.query('movieID == @movie_id').itertuples():
			movie.actors.append(actor[2:])
		for director in director_data.query('movieID == @movie_id').itertuples():
			movie.director = director[2:]
		for tags in tags_data.query('movieID == @movie_id').itertuples():
			movie.tags.append(tags[2:])
		for genre in genre_data.query('movieID == @movie_id').itertuples():
			movie.genres.append(genre[2])
		for rating in train_data.query('movieID == @movie_id').itertuples():
			movie.ratings.append((rating[1],rating[3]))
		print("adding movie " + str(movie_id)+" to list")
		movies.append(movie)
	return movies
