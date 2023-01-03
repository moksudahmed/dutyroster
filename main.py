import numpy as np

def calculate(a):
    count = 0
    for i in range(len(a)):
        if a[i] == 1:
            count +=1
    return count

def swap2(arr,a,b, limit):
    pos = 0
    print(a)
    for i in range(len(arr)):
        if calculate(arr[i]) >= limit:
            for j in range(len(arr[i])):
                if arr[i][j] == 1 and calculate(arr[i]) > limit:
                    for x in range(len(a)):
                        if arr[a[x]][j] == 1 and calculate(arr[i]) <= limit:
                            arr[a[x]][j] = 0 
                            arr[b[x]][j] = 1
                    #    print(i)
                    #if j<=len(b):                
                    #    arr[a[0][j]][a[0][j]] = 0
                    #    arr[b[0][j]][a[0][j]] = 1
                        
           
    return arr

def find(arr,y):
    for i in range(len(arr)):
        if arr[i][y] == 0:            
           return i
    return 0

def swap(arr,a,b, limit):
    twod_list = []    
    for i in range(len(a)):
        
        for j in range(len(arr[a[i]])):
           if arr[a[i]][j] == 1: 
            if calculate(arr[a[i]]) > limit:
                arr[a[i]][j] = 0  
                twod_list.append(j)              
    pos = 0

    for j in range(len(b)):       
        arr[b[j]][twod_list[pos]] = 1
        pos +=1
    i = 0
    
    if pos < len(twod_list):
        while True:
            if pos >= len(twod_list):
                break
            else:
                if calculate(arr[pos]) <= limit:
    #                print("F",pos, twod_list[pos],find(arr,twod_list[pos]))
                    arr[find(arr,twod_list[pos])][twod_list[pos]] = 1
                print(pos,twod_list[pos])
                pos +=1 
                i +=1
    return arr

limit = 3
a = [3,5,6]
b = [0,4]
arr = [[0,0,0,0,0,1,0,0,1,0],
       [0,0,0,1,0,1,0,0,0,1],
       [0,1,0,1,0,0,0,1,0,0],
       [0,0,0,1,0,0,1,1,0,1],
       [0,0,0,1,0,1,0,0,0,0],
       [0,1,0,1,0,1,0,0,1,1],
       [1,0,0,1,0,1,0,1,0,1],]
for row in range(len(arr)):
    print(arr[row],calculate(arr[row]))
arr =  swap(arr,a,b, limit)
print("--------------")
for row in range(len(arr)):
    print(arr[row],calculate(arr[row]))
