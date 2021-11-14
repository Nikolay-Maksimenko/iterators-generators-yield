def flat_generator(my_list):
	for element in my_list:
		if type(element) != list:
			yield element
		else:
			for item in flat_generator(element):
				yield item

nested_list = [['a', 'b', 'c'],['d', 'e', 'f'],['g', 'h', 'i']]
for item in flat_generator(nested_list):
	print(item)