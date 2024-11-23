my_dict = {'Mary': 2010, 'Kate': 1998, 'Anna': 2012}
print(my_dict)
print(my_dict.get('Mary'))
print(my_dict.get('Amina'))
my_dict.update({'Alex':2009, 'Kitty':2001})
my_dict.pop('Kitty')
print(my_dict)


my_set = {1, 2, 3, True, 'String', False, 3, 2, 1, True, 'String', 6, 6, 6, 7, 7, 8}
print(my_set)
my_set.add((0,0,9,8,9))
my_set.add('String2')
my_set.discard('String2')
print(my_set)
