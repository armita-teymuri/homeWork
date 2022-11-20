from random import random,seed,uniform,randint,randrange,choice,sample,shuffle
seed(5)
print(random())
print(random())
# 0.6229016948897019
# 0.7417869892607294
print(random())
print(random())
# 0.6229016948897019
# 0.7417869892607294


#min + (random() * (max-min)) == uniform() (create rando number between 2 num)
for _ in range(3):
    print(5+(random()* (10-5)))
# 8.699492873699654
# 9.611624983327085
# 5.145026141418073
for _ in range(3):
    print(uniform(5,10))
# 7.328113271890526
# 9.716783584991568
# 8.24487276568462


print(randint(5,10))
# 6


#with step
print(randrange(5,10,2))
#5


#choice ==>  x[randint(0,len(x)-1)]
x=["a","b","c","d"]
print(x[randint(0,len(x)-1)])
#c
print(choice(x))
#d


print(sample(x,3))
#['b', 'd', 'a']



shuffle(x)
print(x)
#['d', 'c', 'a', 'b']


#tamrin shir ya khat
coin = ["shir", "khat", "khat"]
shir = 0
khat = 0
for _ in range(1000):
    r = choice(coin)
    if r == "shir":
        shir +=1
    else:
        khat +=1
print("shir:" ,shir)
print("khat:" , khat)
# shir: 337
# khat: 663


#tamrin shabih sazi tas
tas = {1:0,2:0,3:0,4:0,5:0,6:0}
for _ in range(1000):
    tas[randint(1,6)]+=1
print (tas)
#{1: 188, 2: 152, 3: 154, 4: 178, 5: 165, 6: 163}



#tamrin tyabdil adad 3 raghami be horoof
se = {1:"sad",2:"devist",3:"sisad",4:"chaharsad",5:"punsad",6:"shishsad",7:"haftsad",8:"hashtsad",9:"nohsad"}
do = {0:"",1:"sad",2:"bist",3:"si",4:"chehel",5:"panjah",6:"shast",7:"hafad",8:"hashtad",9:"navad"}
yek =  {0:"",1:"yek",2:"do",3:"se",4:"chahar",5:"panj",6:"shish",7:"haft",8:"hasht",9:"noh"}
yazdah = {
    1:"yazdah",2:"davazdah",
3:"sizdah",4:"chahardah",5:"panzdah",6:"shanzdah",7:"hefdah",8:"hejdah",9:"noozdah",0:"dah"}
i=input("enter number:")
if int(len(i))!=3 or int(i[0])==0 :
    print("out of range")
else:
    i=list(i)
    sadgan = i[0]
    dahgan = i[1]
    yekan = i[2]
    if int(i[1])==1 :
        print(se[int(sadgan)],"o",yazdah[int(yekan)])
    elif int(i[1])==0 :
        print(se[int(sadgan)],"o",yek[int(yekan)])
    else:
        print(se[int(sadgan)],"o",do[int(dahgan)],"o",yek[int(yekan)])
    