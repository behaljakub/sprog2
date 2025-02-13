l = [2,3,1,0,5,6,4,2]

index = 6
misto = []

for i in l:
    if i == 1:
        misto.append(index)
    if index >= len(l):
        break

print(misto)