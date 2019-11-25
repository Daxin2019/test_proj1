import operator

def print_dict(dic):
    for key in dic:
        print (key)
        print (dic.get(key))

dict1 = dict({'a':5, 'b':3, 'c':4,'e':111, 'f':45.79})

print (dict1)
print_dict(dict1)


dict2 = dict(sorted(dict1.items(),key=operator.itemgetter(1),reverse=True)[:2])

print (dict2)
print_dict(dict2)

def print_dict(dic):
    for key in dic:
        print (key)
        print ("\n")
        print (dic.get(key))