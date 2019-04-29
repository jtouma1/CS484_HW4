class Movie:

	#arbitrary static weights for similarities, genre holds more weight than directors, which holds more weight than actors
	actor_sim = 3
	director_sim = 7
	genre_sim = 10

	def __init__(self,m_id):
		self.id = m_id
		#{ActorID : (actor_name, actor_rank)}
		self.actors = dict()
		#{directorID : director_name}
		self.director = dict()
		#{genre : None}
		self.genres = dict()
		#{tagID : tag_weight}
		self.tags = dict()
		#list of tuples (user_id, rating)
		self.ratings = []

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

	#counts the number of matches between this movie and other (actors, directors, genres, tags) multiplied by the weights at top of this file and weights given to tags
	def compare(self, other):
		similarities = 0
		#compare actors
		for key, val in self.actors.items():
			if key in other.actors:
				similarities += 1 * self.actor_sim

		#compare directors
		for key, val in self.director.items():
			if key in other.director:
				similarities += 1 * self.director_sim

		#compare genres
		for key, val in self.genres.items():
			if key in other.genres:
				similarities += 1 * self.director_sim

		#compare tags 
		for key, val in self.tags.items():
			if key in other.tags:
				similarities += min(val, other.tags.get(key)) * self.tags[key]

		return similarities
