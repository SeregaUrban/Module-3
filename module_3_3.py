def print_params(a=1, b='строка', c=True):
    print(a,b,c)
print_params(b = 25)
print_params(c = [1,2,3])
value_list = [4 , 'Urban',False]
value_dict = {'a':19 , 'b':'Urban' ,'c': False}
print_params(*value_list)
print_params(**value_dict)
value_list2 = ['Car',True]
print_params(*value_list2,42)