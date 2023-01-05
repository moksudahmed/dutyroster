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
def get_next_point(arr):
    for i in range(len(arr)):
        if arr[i] == 0:            
           return i
    return 0
def find(arr,y):
    for i in range(len(arr)):
        if arr[i][y] == 0:            
           return i
    return 0

def swap(arr,a,b, limit):
    twod_list = []    
    arr_sum = sum(list(map(sum, arr)))
    print("Before",arr_sum)    
    print(b)
    # Delete instance from extra entry
    for i in range(len(a)):
        
        for j in range(len(arr[a[i]])):
           if arr[a[i]][j] == 1: 
            if calculate(arr[a[i]]) > limit:
                arr[a[i]][j] = 0  
                twod_list.append(j)              
    pos = 0
    # Insert instance for shortage entry
   # print(twod_list)
    while pos < len(twod_list):
        for j in range(len(b)): 
            if arr[b[j]][twod_list[pos]] == 1:
                #print("Already Exist",arr[b[j]][twod_list[pos]],get_next_point(arr[b[j]]))            
                arr[b[j]][get_next_point(arr[b[j]])] = 1
                print("p1",b[j],twod_list[pos])
                pos +=1
            else:
                arr[b[j]][twod_list[pos]] = 1                
                print("p2",b[j],twod_list[pos])
                pos +=1
        if calculate([b[j]]) < limit:
            break
          #  if pos < len(twod_list):break   
    
    i = 0
    while pos < len(twod_list) and i<len(arr):        
        if arr[i][twod_list[pos]] == 1:            
            arr[i][get_next_point(arr[i])] = 1
          #  print("p1",i,twod_list[pos],get_next_point(arr[i]))
            pos +=1
        else:
            arr[i][twod_list[pos]] = 1            
        #    print("p2",i,twod_list[pos])
            pos +=1
        i +=1
    result = list(map(sum, arr))    
    print("After",sum(result))
   
    return arr

limit = 3
a = [3,5,6]
b = [0,2,4]
arr = [[0,0,0,0,1,1,0,0,0,0],
       [0,0,0,1,0,1,0,0,0,1],
       [0,0,0,1,0,0,0,1,0,0],
       [0,0,0,1,0,0,1,1,0,1],
       [0,0,0,0,0,1,0,0,0,0],
       [0,1,0,1,0,1,0,0,1,1],
       [1,0,0,1,0,1,0,1,0,1],]
for row in range(len(arr)):
    print(arr[row],calculate(arr[row]))
arr =  swap(arr,a,b, limit)
print("--------------")
for row in range(len(arr)):
    print(arr[row],calculate(arr[row]))
