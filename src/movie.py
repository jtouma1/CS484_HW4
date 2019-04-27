class Movie:
	def __init__(self,m_id,actors = [], director=None, genres = [],tags=[],ratings=[]):
		self.id = m_id
		#list of tuples (actor_id, actor name, rank)
		self.actors = actors
		#tuple (director_id, director name)
		self.director = director
		#list of strings
		self.genres = genres
		#list of tuples (tag_id, tag weight)
		self.tags = tags
		#list of tuples (user_id, rating)
		self.ratings = ratings

	#overwritten string method omitts ratings for space sake
	def __str__(self):
		return "ID: "  + str(self.id) + "\nActors: " + str(self.actors) + "\nDirector: "+str(self.director) + "\nGenres: " + str(self.genres) + "\n Tags: " + str(self.tags)

	#makes dictionary from movie object
	def to_dict(self):
		return {'id':self.id,'actors':self.actors,'director':self.director,'genres':self.genres,'tags':self.tags, 'ratings':self.ratings}

	#creates movie object from
	@staticmethod
	def from_dict(movie_dict):
		return Movie(movie_dict['id'],movie_dict['actors'],movie_dict['director'],movie_dict['genres'],movie_dict['tags'],movie_dict['ratings'])