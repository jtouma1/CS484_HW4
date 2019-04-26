import pandas as pd
from actor import *

def make_movie(actors,directors,genre,tags):
	movies = {}
	current_mov_id = 0
	for line in actors:
		line = line.split("\t")
		#print(line[0],type(line[0]))
		if line[0] not in movies.keys():
			#print("adding movie " + line[0])
			current_mov_id = line[0]
			movies[line[0]] = [Actor(line[2],line[1],line[3])]
		elif line[0] == current_mov_id:
			actor = Actor(line[2],line[1],line[3])
			movies[line[0]].append(actor)
			#print("adding actor" + str(actor))
	for movie in movies.keys():
		print("*****************************\n")
		print("Movie:" + movie)
		for actor in movies[movie]:
			print(actor)

def main():
	movie_data = pd.DataFrame()

	mov_actor_file = open("../additional_files/movie_actors.dat", encoding = "ISO-8859-1")
	mov_directors_file = open("../additional_files/movie_directors.dat", encoding = "ISO-8859-1")
	mov_genres_file = open("../additional_files/movie_genres.dat", encoding = "ISO-8859-1")
	mov_tags_file = open("../additional_files/movie_tags.dat", encoding = "ISO-8859-1")
	tags_file = open("../additional_files/tags.dat", encoding = "ISO-8859-1")
	test_file = open("../additional_files/test.dat", encoding = "ISO-8859-1")
	train_file = open("../additional_files/train.dat", encoding = "ISO-8859-1")
	user_tagged_file = open("../additional_files/user_taggedmovies.dat", encoding = "ISO-8859-1")

	mov_actors = mov_actor_file.readlines()
	mov_directors = mov_directors_file.readlines()
	mov_genres = mov_genres_file.readlines()
	mov_tags = mov_tags_file.readlines()
	make_movie(mov_actors,mov_directors,mov_genres,mov_tags)



if __name__ == '__main__':
	main()