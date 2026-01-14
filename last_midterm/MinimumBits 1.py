#Phanthira Kositjaroenkul u6630003

B=int(input("Number of bits used for encoding data: "))
N=int(input("Input the number of different bit-encoded:"))
Arr=[]
for i in range(N):
    Arr.append(list(input("Input number of each bits:")))

print(B)
print(N)
print(len(Arr))
count=0
min_num=0
for x in range(0,N):
    for y in range(0,B):
        if Arr[x][y]==Arr[x+1][y+1]:
            count+=1
        if count==N:
            min_num+=1


print(min_num)
