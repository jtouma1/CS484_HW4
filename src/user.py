from recommender import *

class User:
	def __init__(self, u_id, movies):
		self.id = u_id
		#list of tuples of movie objects with the rating the user has provided
		self.movies = movies

	#given a movie ID, find the most similar movie that the user has already rated and return its rating
	def get_rating(self, movies, movie):
		closest_movie = None
		max_sim = 0
		for mov in self.movies:
			mov_obj = movies.get(mov[0])
			if mov_obj is None or movie is None:
				continue
			sim = movie.compare(mov_obj)
			if sim > max_sim:
				closest_movie = mov
				max_sim = sim
		if closest_movie is None:
			print('no movie similarties')
			return 2.5
		return closest_movie[1]

	def __eq__(self, other):
		return self.id == other.id
