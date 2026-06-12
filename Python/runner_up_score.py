rray=[]
n_array = []

n = int(input())
array = list(map(int, input().split()))
l = array[0]
for num in array:
    if num>l :
        l = num
for num in array:
    if num!=l:
        n_array.append(num)
sl=n_array[0]
for a in n_array:
    if(sl<a):    
        sl=a
            
print(sl)

