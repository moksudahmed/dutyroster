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
                            print("Found",a[x])
                    #    print(i)
                    #if j<=len(b):                
                    #    arr[a[0][j]][a[0][j]] = 0
                    #    arr[b[0][j]][a[0][j]] = 1
                        
           
    return arr
def swap(arr,a,b, limit):
    print(b)    
    twod_list = []    
    print("============")
    for i in range(len(a)):
        
        for j in range(len(arr[a[i]])):
           if arr[a[i]][j] == 1: 
            if calculate(arr[a[i]]) > limit:
                arr[a[i]][j] = 0  
                twod_list.append(j)              
                print("F",arr[a[i]][j],"{",a[i],"C",j,"}",arr[a[i]])
    count = 0
    print("Test",twod_list)
    for j in range(len(b)):       
        for i in range(len(twod_list)):                        
           # if i == twod_list[i]:                                
                if arr[b[j]][twod_list[i]] != 1 and calculate(arr[b[j]]) <= limit:                    
                    arr[b[j]][twod_list[i]] = 1
                    count +=1                
                else:    
                    arr[b[j]][twod_list[i]+1] = 1
                    count +=1                
          #  print(twod_list[i], end=' ')
           # print()
            #print(i)
    print(count)
 #   for i in range(count):
 #        print(twod_list[i+count])
  #       arr[i][i+count] = 1
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
