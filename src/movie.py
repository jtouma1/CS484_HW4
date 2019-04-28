class Movie:

	#arbitrary static weights for similarities
	actor_sim = 3
	director_sim = 10
	genre_sim = 2

	def __init__(self,m_id):
		self.id = m_id
		#list of tuples (actor_id, actor name, rank)
		self.actors = []
		#tuple (director_id, director name)
		self.director = []
		#list of strings
		self.genres = []
		#list of tuples (tag_id, tag weight)
		self.tags = []
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

	def compare(self, other):
		similarities = 0
		#compare actors
		for actor in self.actors:
			for other_actor in other.actors:
				#print('comparing actors {} and {}'.format(actor[0], other_actor[0]))
				#if actor ids match, movies contain same actor
				if actor[0] == other_actor[0]:
					similarities += 1 * self.actor_sim
		#print('finished actors')

		#compare directors
		for dirc in self.director:
			for other_dirc in other.director:
				if dirc[0] == other_dirc[0]:
					similarities += 1 * self.director_sim

		#compare genres
		for gen in self.genres:
			for other_gen in other.genres:
				if gen == other_gen:
					similarities += 1 * self.genre_sim
		#print('finished genres')
		#compare tags
		for tag in self.tags:
			for other_tag in other.tags:
				if tag[0] == other_tag[0]:
					similarities += min(tag[1], other_tag[1])
		#print('finihsed tags')
		return similarities
