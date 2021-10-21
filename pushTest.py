li=[3,8,2,1,6]
for i in range(len(li)-1):
    for j in range(len(li)-i-1):
        if li[j]>li[j+1]:
            li[j],li[j+1]=li[j+1],li[j]
print(li)
