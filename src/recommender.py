from preprocessor import *
import time 
import json

def main():
	s = time.time()
	actor_data,director_data,genre_data,tags_data,user_tag_data,train_data,test_data = get_dataframes()
	movies,users = get_movies(actor_data,director_data,genre_data,tags_data,user_tag_data,train_data,test_data)
	#prints out the users dictionary
	#for key,val in users.items():
	#	print('Key: {}   UserID: {}'.format(key, val.id))
	#	for movie,rating in val.movies:
	#		print('\tMovieID: {}   Rating: {}'.format(movie, rating))
	print('Number of users: {}'.format(len(users)))
	print('Number of movies: {}'.format(len(movies)))

	#populate final_ratings with ratings using User.get_rating(movie dictionary, movie to get rating for)
	final_ratings = []
	counter = 0
	for test in test_data.itertuples():
		u_id = test[1]
		mov_id = test[2]
		#print('Predicting {}, {}'.format(u_id, mov_id))
		movie = movies.get(mov_id)
		if movie is None:		#some movies aren't found for some reason
			print('couldnt find movie {}'.format(str(mov_id)))
		user = users.get(u_id)
		pred_rating = user.get_rating(movies, movie)		#gets predicted rating of movie from this user
		final_ratings.append(pred_rating)
		if (counter % 100) == 0:
			print('done with {}'.format(counter))
		counter += 1
	with open('output1.txt', 'w') as f:		#write predicted ratings out to file
		for rating in final_ratings:
			f.write("%s\n" % str(rating))

#before changing movie attributes to dicts
#runtime 6748 seconds
#score 1.13
#rank 40

#after changing attributes to dicts
#rutnime 685 seconds
#score 1.14
#rank 42

	e = time.time()
	#takes about 3.5 minutes rn
	print("runtime = " + str(e-s) + " seconds")

	#ideas about what we can do:
	#1: item item collab
		#create distance measures between each and every movie and store them with every movie 
		#furthest points away are least similar and closest are most similar
		#very taxing on processor/memory
		#slow first time through
		#
	#2: user user collab
		#instead of using every feature possible, only use user ratings from train data and movie ids to find movies that are similar based on user preferences
		#this is more like clustering users together and putting movies into the system to see how each user would like it

if __name__ == '__main__':
	main()