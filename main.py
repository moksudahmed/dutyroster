def calculate(a):
    count = 0
    for i in range(len(a)):
        if a[i] == 1:
            count +=1
    return count

def swap(arr,a,b, limit):
    for i in range(len(arr)):
        if calculate(arr[i]) >= limit:
            for j in range(len(arr[i])):
                if arr[i][j] == 1 and calculate(arr[i]) >limit:
                    arr[i][j] = 0
                    if j<=len(b):
                        arr[b[0][j]][j] = 1
           # print(arr[i], calculate(arr[i]), b[0][2])    
    return arr

limit = 3
a = [[1,3,5,6],[4,4,4,5]]
b = [[0,2,4],[2,2,2]]
arr = [[0,1,0,0,0,1,0,0,0,0],
       [0,1,0,1,0,1,0,0,0,1],
       [0,0,0,1,0,0,0,1,0,0],
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
