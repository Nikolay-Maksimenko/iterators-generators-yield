class FlatIterator():

	def __init__(self, my_list):
		self.my_list = my_list

	def create_flat_list(self, current_list, new_list):
		"""Преобразование списка списков с любым уровнем вложенности в плоский список"""
		for element in current_list:
			if type(element) != list:
				new_list.append(element)
			else:
				self.create_flat_list(element, new_list)
		return new_list

	def __iter__(self):
		self.count = -1
		return self

	def __next__(self):
		new_list = []
		self.count += 1
		flat_list = self.create_flat_list(self.my_list, new_list)
		if self.count == len (flat_list):
			raise StopIteration
		return flat_list[self.count]

nested_list = [['a', 'b', 'c'],['d', 'e', 'f'],['g', 'h', 'i']]
for item in FlatIterator(nested_list):
	print(item)