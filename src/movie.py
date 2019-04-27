class Movie:
	def __init__(self,m_id,actors = [], director=None, genres = [],tags=[],ratings=[], users=[]):
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
	
	def to_dict(self):
		return {'id':self.id,'actors':self.actors,'director':self.director,'genres':self.genres,'tags':self.tags, 'ratings':self.ratings}

	@staticmethod
	def from_dict(movie_dict):
		return Movie(movie_dict['id'],movie_dict['actors'],movie_dict['director'],movie_dict['genres'],movie_dict['tags'],movie_dict['ratings'])