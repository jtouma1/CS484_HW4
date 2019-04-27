class User:
	def __init__(self,u_id, movies=[]):
		self.id = u_id
		#list of tuples of movie objects with the rating the user has provided
		self.movies = movies

	def __hash__(self):
		return hash(self.id)

	def __eq__(self, other):
		return self.id == other.id
