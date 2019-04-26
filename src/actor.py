class Actor:
	def __init__(self,name,a_id,rank):
		self.name = name
		self.a_id = a_id
		self.rank = rank

	def __str__(self):
		return "Name: " + str(self.name) + " / ID: " + str(self.a_id) + " / Rank: " + str(self.rank)