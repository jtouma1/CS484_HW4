import pandas as pd


def get_dataframes():
	mov_actor_file = open("../additional_files/movie_actors.dat", encoding = "ISO-8859-1").readlines()
	mov_directors_file = open("../additional_files/movie_directors.dat", encoding = "ISO-8859-1").readlines()
	mov_genres_file = open("../additional_files/movie_genres.dat", encoding = "ISO-8859-1").readlines()
	mov_tags_file = open("../additional_files/movie_tags.dat", encoding = "ISO-8859-1").readlines()
	tags_file = open("../additional_files/tags.dat", encoding = "ISO-8859-1").readlines()
	test_file = open("../additional_files/test.dat", encoding = "ISO-8859-1").readlines()
	train_file = open("../additional_files/train.dat", encoding = "ISO-8859-1").readlines()
	user_tagged_file = open("../additional_files/user_taggedmovies.dat", encoding = "ISO-8859-1").readlines()

	actor_data = pd.DataFrame(data = [x.strip("\n").split("\t") for x in mov_actor_file])
	director_data = pd.DataFrame(data = [x.strip("\n").split("\t") for x in mov_directors_file])
	genre_data = pd.DataFrame(data = [x.strip("\n").split("\t") for x in mov_genres_file])
	tags_data = pd.DataFrame(data = [x.strip("\n").split("\t") for x in mov_tags_file])

	actor_data.columns = actor_data.loc[0].tolist()
	actor_data.drop([0],inplace = True)
	
	director_data.columns = director_data.loc[0].tolist()
	director_data.drop([0],inplace = True)

	genre_data.columns = genre_data.loc[0].tolist()
	genre_data.drop([0],inplace = True)

	tags_data.columns = tags_data.loc[0].tolist()
	tags_data.drop([0],inplace = True)

	return actor_data,director_data,genre_data,tags_data

def main():
	actor_data,director_data,genre_data,tags_data = get_dataframes()

	print(actor_data.head())
	print(director_data.head())
	print(genre_data.head())
	print(tags_data.head())



if __name__ == '__main__':
	main()