t=(1,2,3,"armita",['a','b','c'],(1,2,3),4,5)
print(type(t))
# <class 'tuple'>


t=1,2,3,4
print(type(t))
print(t)
# <class 'tuple'>
# (1, 2, 3, 4)


t=(1,2,3,[1,2,3],4)
t[3][0]=0
print(t)
# (1, 2, 3, [0, 2, 3], 4)


t=()
print(type(t))
t=(1)
print(type(t))
t=(1,)
print(type(t))
# <class 'tuple'>
# <class 'int'>
# <class 'tuple'>



t="armita"
t=tuple(t)
print(t)
# ('a', 'r', 'm', 'i', 't', 'a')


t=1,2,3,4
l=list(t)
l[3]=100
t=tuple(l)
print(t)
# (1, 2, 3, 100)
