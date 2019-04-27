from preprocessor import *
import time 
def main():
	s = time.time()
	#just so you have access to all the data
	actor_data,director_data,genre_data,tags_data,user_tag_data,train_data,test_data = get_dataframes()
	#all movie objects
	movies = get_movies()
	e = time.time()
	#takes about 3.5 minutes rn
	print("runtime = " + str(e-s) + " seconds")
if __name__ == '__main__':
	main()