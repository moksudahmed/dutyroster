def calculate(a):
    count = 0
    for i in range(len(a)):
        if a[i] == 1:
            count +=1
    return count

def swap(arr,a,b, limit):
    pos = 0
    for i in range(len(arr)):
        if calculate(arr[i]) >= limit:
            for j in range(len(arr[i])):
                if arr[i][j] == 1 and calculate(arr[i]) >limit:                    
                    if j<=len(b):                
                        arr[a[0][j]][a[0][j]] = 0
                        arr[b[0][j]][a[0][j]] = 1
                        print(i,j)
           
    return arr

limit = 3
a = [[3,5,6],[4,4,5]]
b = [[0,4],[2,2]]
arr = [[0,1,0,0,0,1,0,0,0,0],
       [0,0,0,1,0,1,0,0,0,1],
       [0,1,0,1,0,0,0,1,0,0],
       [0,0,0,1,0,0,1,1,0,1],
       [0,0,0,1,0,1,0,0,0,0],
       [0,0,0,1,0,1,0,0,1,1],
       [1,0,0,1,0,1,0,1,0,1],
    ]
for row in range(len(arr)):
    print(arr[row],calculate(arr[row]))
arr =  swap(arr,a,b, limit)
print("--------------")
for row in range(len(arr)):
    print(arr[row],calculate(arr[row]))
