import random as r

role =[]
look = ['看起來','感覺']
adverb = ['很','非常','有點']
adj = ['漂亮','帥','可愛','醜']


role.append(input("請輸入名字 : "))

def S():
    return  ROLE() + '你今天' + LOOK() + ADVERB() + ADJ()

def ROLE():
    return r.choice(role)

def LOOK():
    return r.choice(look)

def ADVERB():
    return r.choice(adverb)

def ADJ():
    return r.choice(adj)


print(S())
