from preprocessor import *

def main():
	movies = None
	with open('movie_cache/movies.json') as json_file:  
		movies = json.load(json_file)

	print(movies)

if __name__ == '__main__':
	main()