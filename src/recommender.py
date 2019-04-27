from preprocessor import *
import time 
import json
def main():
	s = time.time()
	#just so you have access to all the data
	actor_data,director_data,genre_data,tags_data,user_tag_data,train_data,test_data = get_dataframes()
	#all movie objects
	movies = get_movies()
	e = time.time()
	#takes about 3.5 minutes rn
	print("runtime = " + str(e-s) + " seconds")
	with open('outputfile.json', 'w') as fout:
		json.dump([x.to_dict() for x in movies], fout)

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


	print(movies[0],movies[1])
if __name__ == '__main__':
	main()