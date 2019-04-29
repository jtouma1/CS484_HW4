import pandas as pd
import numpy as np
import threading
import time
from movie import *
from user import *


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
	print("finished getting data")

	return actor_data,director_data,genre_data,tags_data,user_tag_data,train_data,test_data

def get_movies(actor_data,director_data,genre_data,tags_data,user_tag_data,train_data,test_data):

	#main idea:
	#For each movie in the dataset 
	#	For each user who reviewed it 
	#		For each other movie reviewed by that customer 
	#			Record the user's review

	#all ids added to movies list so now we can make that many movie objects (should be 10174)
	movies_ids = []
	for movie_id in actor_data.itertuples():
		if movie_id[1] not in movies_ids:
			movies_ids.append(movie_id[1])
	print("finished finding IDs")
	#grabs each movie id and makes a Movie object with all attributes associated with the movie id similarly with users
	results = [None,None,None]
	#threading out this process because neither are dependent on eachother's outcomes
	t_movies_fronthalf = threading.Thread(target = make_movies, args = (movies_ids[int(len(movies_ids)/2):],actor_data,director_data,genre_data,tags_data,train_data,results,0))
	t_movies_backhalf = threading.Thread(target = make_movies, args = (movies_ids[:int(len(movies_ids)/2)],actor_data,director_data,genre_data,tags_data,train_data,results,1))
	t_users = threading.Thread(target = make_users, args = (train_data,results))
	t_movies_fronthalf.start()
	t_movies_backhalf.start()
	t_users.start()
	t_movies_fronthalf.join()
	t_movies_backhalf.join()
	t_users.join()

	#print(results[0],results[1])
	#print(type(results[0]),type(results[1]),type(results[2]))
	results[0].update(results[1])
	return results[0],results[2]

#populate movies dictionary
def make_movies(movies_ids,actor_data,director_data,genre_data,tags_data,train_data,result,num):
	s = time.time()
	movies = dict()
	for movie_id in movies_ids:
		#make movie
		movie = Movie(movie_id)
		for actor in actor_data.query('movieID == @movie_id').itertuples():
			movie.actors.update({actor[2] : actor[3:]})
		for director in director_data.query('movieID == @movie_id').itertuples():
			movie.director.update({director[2] : director[3]})
		for tags in tags_data.query('movieID == @movie_id').itertuples():
			movie.tags.update({tags[2] : tags[3]})
		for genre in genre_data.query('movieID == @movie_id').itertuples():
			movie.genres.update({genre[2] : None})
		for rating in train_data.query('movieID == @movie_id').itertuples():
			movie.ratings.append((rating[1],rating[3]))
		movies.update({movie_id: movie})
	result[num] = movies
	e = time.time() 
	if num == 1:
		print("finished making movies, took: "+ str(e-s) +" sec")


#populate users dictionary
def make_users(train_data,result):
	s = time.time()
	users = dict()
	for user_data in train_data.itertuples():
		if users.get(user_data[1]) is None:
			users.update({user_data[1] : User(user_data[1], [(user_data[2],user_data[3])])})
		else:
			user = users.get(user_data[1])
			user.movies.append((user_data[2],user_data[3]))
			users.update({user_data[1] : user})
	result[2] = users
	e = time.time() 
	print("finished making users, took:"+ str(e-s) +" sec")

