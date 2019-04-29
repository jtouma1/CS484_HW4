from preprocessor import *
import time 

def main():
	s = time.time()
	#grab data from files
	actor_data,director_data,genre_data,tags_data,user_tag_data,train_data,test_data = get_dataframes()
	#generate movie and user objects
	movies,users = get_movies(actor_data,director_data,genre_data,tags_data,user_tag_data,train_data,test_data)

	print('Number of users: {}'.format(len(users)))
	print('Number of movies: {}'.format(len(movies)))

	#populate final_ratings with ratings using User.get_rating(movie dictionary, movie to get rating for)
	final_ratings = []
	counter = 0
	#model creation
	for test in test_data.itertuples():
		#get ids from current test
		u_id = test[1]
		mov_id = test[2]
		#get movie & user 
		movie = movies.get(mov_id)
		#some movies aren't in the initial grab of movies
		if movie is None:
			print('couldnt find movie {}'.format(str(mov_id)))
		user = users.get(u_id)
		#gets predicted rating of movie from this user
		pred_rating = user.get_rating(movies, movie)
		final_ratings.append(pred_rating)
		if (counter % 100) == 0:
			print('done with {}'.format(counter))
		counter += 1
	#write predicted ratings out to file
	with open('output1.txt', 'w') as f:
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

if __name__ == '__main__':
	main()