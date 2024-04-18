my_list = ['яблоко', 'банан', 'груша', 'персик', 'лимон']
print(my_list)
print(my_list[0], my_list[-1])
print(my_list[2:5])
my_list[2] = 'ананас'
print(my_list)

my_dict = {'apple': 'яблоко', 'banana': 'банан', 'pear': 'груша', 'peach': 'персик', 'lemon': 'лимон'}
print(my_dict)
print(my_dict['pear'])
my_dict['pear'] = 'грушевый'
print(my_dict)
my_dict.update({'pineapple': 'ананас'})
print(my_dict)