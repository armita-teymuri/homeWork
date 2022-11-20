l=[1,2,3,4,"armita"]
print(l,"\n",type(l))
# [1, 2, 3, 4, 'armita']
#  <class 'list'>

str=list("armita")
print(str)
#['a', 'r', 'm', 'i', 't', 'a']

s="armita teymuri"
s=s.split(" ")
print(s)
#['armita', 'teymuri']

print(l[3])
#4
print(l[:])
#[1, 2, 3, 4, 'armita']
print(l[1:3])
#[2, 3]
print(l[::2])
#[1, 3, 'armita']

print(l*2)
#[1, 2, 3, 4, 'armita', 1, 2, 3, 4, 'armita']
print(l+["arash","arsham"])
#[1, 2, 3, 4, 'armita', 'arash', 'arsham']


#list is mutable
l[3]="arash"
print(l)
#[1, 2, 3, 'arash', 'armita']


print (l==str)
# False
print("armita" in l)
# True


l1=[1,2,3]
l2=l1
print(id(l1),"\n",id(l2))
# [1, 2, 3]
#  [1, 2, 3]
l2[0]=100
print(l1,"\n",l2)
# [100, 2, 3]
#  [100, 2, 3]
l2=l1[:]
l2[0]=1
print(l1,"\n",l2)
# [100, 2, 3]
#  [1, 2, 3]
l2=l1.copy()
l2[0]=200
print(l1,"\n",l2)
# [100, 2, 3]
#  [200, 2, 3]



x=[1,2,['armita','teymouri'],3]
print(x[2][1][-1])
# i


y1=[1,2,['a','b'],3]
y2=y1.copy()
print(id(y1),"\n",id(y2))
y2[2][0]="c"
print(y1,"\n",y2)
# 2493768296512
#  2493768296704
# [1, 2, ['c', 'b'], 3]
#  [1, 2, ['c', 'b'], 3]


import copy
z1=[1,2,['a','b'],3]
z2=copy.deepcopy(z1)
print(id(z1),"\n",id(z2))
z2[2][0]="c"
print(z1,"\n",z2)
# 1998382656128 
#  1998382656000
# [1, 2, ['a', 'b'], 3]
#  [1, 2, ['c', 'b'], 3]



e=[1,2,3,4]
e.append(10)
print(e)
# [1, 2, 3, 4, 10]
e.append([100,200,300])
print(e)
# [1, 2, 3, 4, 10, [100, 200, 300]]

del e[1]
print(e)
#[1, 3, 4, 10, [100, 200, 300]]
del e[2:5]
print(e)
# [1, 3]
del e


r=[1,2,3,4,5,6]
print(len(r))
# 6
print(r[:len(r)])
# [1, 2, 3, 4, 5, 6]
print(r[len(r)-1])
# 6



a,b,c=[1,2,3]
print("a:",a,"b:",b,"c:",c)
# a: 1 b: 2 c: 3

*a,b,c=[1,2,3,4,5,6,7]
print("a:",a,"b:",b,"c:",c)
# a: [1, 2, 3, 4, 5] b: 6 c: 7

a,*b,c=[1,2,3,4,5,6,7]
print("a:",a,"b:",b,"c:",c)
# a: 1 b: [2, 3, 4, 5, 6] c: 7

a,b,*c=[1,2,3,4,5,6,7]
print("a:",a,"b:",b,"c:",c)
# a: 1 b: 2 c: [3, 4, 5, 6, 7]



# lists method
li=[1,2,3,4,5]
li.append(6)
print(li)
# [1, 2, 3, 4, 5, 6]
li[len(li):]=[7]
print(li)
#appent item from len li to end
# [1, 2, 3, 4, 5, 6, 7]


li.clear()
print(li)
# []   ===> del li[:]



li = [1,2,3,4,5,2,2,2]
print(li.count(2))
# 4


li.extend([10,11,12,13])
print(li)
# [1, 2, 3, 4, 5, 2, 2, 2, 10, 11, 12, 13]
p=[100,200,300]
li[len(li):]=p
print(li)
# [1, 2, 3, 4, 5, 2, 2, 2, 10, 11, 12, 13, 100, 200, 300]



print(li.index(2))
# 1 ====> frist index fo 2
print(li.index(2,3))
# 5 ====> first index for 2 from 3 index
print(li.index(2,3,7))
# 5 ====> first index for 2 from 3 index to 7


li.insert(3,"armita")
print(li)
# [1, 2, 3, 'armita', 4, 5, 2, 2, 2, 10, 11, 12, 13, 100, 200, 300]



print(li.pop())
print(li)
# 300
# [1, 2, 3, 'armita', 4, 5, 2, 2, 2, 10, 11, 12, 13, 100, 200]
# remove and return last item from list
print(li.pop(3))
print(li)
# armita
# [1, 2, 3, 4, 5, 2, 2, 2, 10, 11, 12, 13, 100, 200]



li.remove(2)
print(li)
# [1, 3, 4, 5, 2, 2, 2, 10, 11, 12, 13, 100, 200]
# remove frist item equl with 2


li.reverse()
print(li)
# [200, 100, 13, 12, 11, 10, 2, 2, 2, 5, 4, 3, 1] ===> print(li[::-1])
# reverse lest and save in list
k=reversed(li)
print(list(k))
print(li)
# [1, 3, 4, 5, 2, 2, 2, 10, 11, 12, 13, 100, 200]
# [200, 100, 13, 12, 11, 10, 2, 2, 2, 5, 4, 3, 1]



li.sort()
print(li)
# [1, 2, 2, 2, 3, 4, 5, 10, 11, 12, 13, 100, 200]
li.sort(reverse=True)
print(li)
# [200, 100, 13, 12, 11, 10, 5, 4, 3, 2, 2, 2, 1]


