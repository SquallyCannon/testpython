list1 = [1,2,3,4,5,6,7,8,9,0]

track = 0

def trackprintset(n):
    global track
    if isinstance(n, list):
        print(n)
        for _ in n:
            trackprintset(_)
    else:
        track +=1
    return track
def listmaker(n):
    global list1
    liste = 0
    for _ in range(1,n+1):
        if _ == 1:
            liste = list1.copy()
        else:
            liste2 = liste.copy()
            for __ in range(len(list1)):
                liste[__]= liste2
    return liste


#print(listmaker(5))
print(trackprintset(listmaker(5)))