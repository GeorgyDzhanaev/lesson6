#my_dict = {'George':1995, 'Evgeniy': 1997, 'Bogdan': 1997}
#print(my_dict)
#my_dict['George'] = 1995
#my_dict['Evgeniy'] = 1997
#print(my_dict.values)
#my_dict.update({'Anton':1995, 'Misha':1998})
#my_dict.pop('Anton')
#print(my_dict)
#del my_dict['Misha']
#print(my_dict)
my_dict = {'George':1995, 'Evgeniy': 1997, 'Bogdan': 1997}
print('Dict:', my_dict)
my_dict['George'] = 1995
my_dict['Evgeniy'] = 1997
my_dict['Bogdan'] = 1997
print('Existing value:',1995)
print('Not Existing value:', None)
print('Deleted Value;', 1997)
my_dict.update({'Anton':1995, 'Misha':1998})
my_dict.pop('Anton')
del my_dict['Misha']
print('Modified dictionary:', my_dict)
my_set = ['George',1995,2211,'Ne znau pravilno li',2211,1995,'George']
print(set(my_set))
my_set = set(my_set)
print('Set:', my_set)
my_set.discard('George')
print('Modified set:', my_set)