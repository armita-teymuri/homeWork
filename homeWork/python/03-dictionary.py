d={}
print(type(d))
# <class 'dict'>


d={"a":5,"b":10}
print(d["b"])
# 10


d={(1,2,3):1,"b":2}
print(d[(1,2,3)])
# 1


d={"a":1,"b":2,"c":3,"a":10}
print(d)
# {'a': 10, 'b': 2, 'c': 3}    cant duplicate key

d["a"]=5
print(d)
# {'a': 5, 'b': 2, 'c': 3}   change dict item value

d["d"]=200
print(d)
# {'a': 5, 'b': 2, 'c': 3, 'd': 200}   add to dict

# print(d["f"])
# error
print(d.get("f"))
# None


print(d.keys())
# dict_keys(['a', 'b', 'c', 'd'])

print(d.values())
# dict_values([5, 2, 3, 200])

print(d.items())
# dict_items([('a', 5), ('b', 2), ('c', 3), ('d', 200)])
print(list(d.items()))
# [('a', 5), ('b', 2), ('c', 3), ('d', 200)]

del d["b"]
print(d)
# {'a': 5, 'c': 3, 'd': 200}
del d


# change dict key!
d={"a":1,"b":2,"c":3}
x=d["c"]
del d["c"]
d["f"]=x
print(d)
# {'a': 1, 'b': 2, 'f': 3}


l=[1,2,3,4,8,3,5,0]
l=sorted(l,reverse=True)
print(l)
# [8, 5, 4, 3, 3, 2, 1, 0] list sorted

d={"e":1,"a":5, "b":2}
print(sorted(d.keys()))
# ['a', 'b', 'e']
print(sorted(d.values()))
# [1, 2, 5]