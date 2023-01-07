from numpy import *
import numpy as np
import random

def combiend(arr, n=30):
    val = [0]*n
    for i in range (len(arr)):
            val[i] = arr[i]
          #  print(val)
    return val


def find(shits, days, n):
    val = [0] * n
    x=0
    for i in range (len(shits)):
        val[x] = shits[i] + str(days)
        x = x + 1
    return val

def _next(l, target):
    return next((i for i in l if i == target), None)

def get_random(list, n):
    val =[0] * n
    i = 0
    l = -0
    val[0] = random.choice(list)
    for i in range(0,n):
        l = random.choice(list)
        if _next(val, int(l)) == None:
            val[i] = 1
            l = -0
        else:
            val[i] = 0
        i +=1                    
   # val.sort()    
    return val

def get_random2(list, n):
    val =[0] * n
    i = 0
    l = -0
    val[0] = random.choice(list)
    for i in range(0,n):
        l = random.choice(list)
        if _next(val, int(l)) == None:
            val[i] = 1
            l = -0
        else:
            val[i] = 0
        i +=1                    
   # val.sort()    
    return val

def countNumber(a):
    count = 0
    for i in range(len(a)):
        if a[i] == 1:
            count += 1    
    return count

def countNumberRow(a):
    count = 0
    for i in range(len(a)):
        if a[i] == 1:
            count += 1    
    return count

def calculateTotalCol(a):
    n = 30
    count = 0          
    for i in range(len(a)):
        if a[i] == 1:
            count += 1               
    return count

def clculateColumn(a):
    count = 0
    n = 30
    val =[0] * n    
    i = 0
    for row in range(30):        
        for col in range(10):
            count = a[row,col] + count                 
       # print("Row",count)    
        val[i] = count
        i = i+1        
        count = 0
    return val

# Function for calculate Total Number of instance in a coloumn and insert in the last row #
    
def clculateRow(a):
    count = 0
    n = 10
    val =[0] * n    
    i = 0
    for col in range(10):
        for row in range(30):        
            count = a[row,col] + count                 
       # print("Row",count)    
        val[i] = count
        i = i+1        
        count = 0
    return val

# Function for Re-arrange thr every column of the matrix with define limits 
  
def rearangeRow(a, limit):
    n = 30   
    for col in range(10):
        val =[0] * n    
        if countNumberRow(a[:,col]) != limit:
            while countNumberRow(val) != limit:
                for i in range(30):
                    val[i] = random.randint(0,1)
            for row in range(30):
                    a[row:,col] = val[row]
    return a


def getNumber(limit):
    n = 10
    a =[0] * n
    #for i in range(10):
    #    a[i] = random.randint(0,1)
    length = 0
    #if countNumber(a) < 5:
    while countNumber(a) != limit:
        for i in range(10):
           a[i] = random.randint(0,1)
    return a

# Function for Re-arrange thr every row of the matrix with define limits 
def rearangeColumn(arr, limit):
    for row in range(30):
            val = getNumber(limit)
            for col in range(10):
                arr[row:,col] = val[col]         
            col = col+1
            arr[row:,col] = calculateTotalCol(val)
            #print(calculateTotalCol(val))
        #print(clculateRow(arr))
    return arr
        
def get_matrix(arr, row_size, col_size,total_instance, perday, individual):
    n = col_size
    val =[0] * n
    x = 1
    for x in range(col_size):
        arr = np.insert(arr, x, 1 , axis=1)
    #arr = np.insert(a, 1, 5, axis=1)
    for x in range(row_size):
        arr[x][0] = random.randint(0,row_size)
    
    total = 0
    while total_instance!= total:
        # Re-arrange thr every column of the matrix with define limits 
        arr = rearangeRow(arr, perday)
    
        # Re-arrange thr every row of the matrix with define limits 
        arr = rearangeColumn(arr, individual)
        
        # Calculate Total Number of instance in a coloumn and insert in the last row #
        temp = clculateRow(arr)
        total_row = 0
        for x in range(col_size):
            arr[row_size:,x] = temp[x]
            total_row += temp[x]
        
        # Calculate Total Number of instance in every row and insert in the last column #
        temp = clculateColumn(arr)
        total_col = 0
        for x in range(row_size):
            arr[x:,col_size] = temp[x]
            total_col += temp[x]

        # Calculate Total Number of instance in the Matrix#
        total = total_row + total_col
    
    arr[row_size:,col_size] = total
    print(arr)
    return arr


# All the required parameter values
total_instance = 200
perday_instance = 25
individual = total_instance / perday_instance
array_size_x = 30
array_size_y = 10


n = 12
m = 6
val = [0] * n

days = [12,14,16,18,20,22]
evendays = [13,15,17,19,21,23]
threeshifts = ['Mor','Eve','Night'] 
twoshifts = ['Mor','Eve']
alldays = [12,13,14,15,16,17,18,19,20,21,22,23]

for i in range(len(alldays)):
    if (i % 2 == 0):
        val[i] = find(threeshifts, alldays[i], 3)
    else:
        val[i] = find(twoshifts, alldays[i], 2)

b = np.hstack(val)
h = 10
#matrix = 5*[5*[0]]
arr = np.matrix(31*[1*[0]])
#print(arr)
#matrix[0] = b 


print(individual)

print(get_matrix(arr, array_size_x, array_size_y,total_instance, perday_instance, individual))

list1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40]

"""
for row in range(1, 5):
    for col in range(10):
        matrix[row][col] = get_random(list1, 5) 
"""
#random_list = get_random(list1, 10)
#arr = np.insert(arr, 0, range(1,31) , axis=1)
"""arr = np.insert(arr, 1, get_random(list1, 30) , axis=1)
arr = np.insert(arr, 2, get_random(list1, 30) , axis=1)
arr = np.insert(arr, 3, get_random(list1, 30) , axis=1)
arr = np.insert(arr, 4, get_random(list1, 30) , axis=1)
arr = np.insert(arr, 5, get_random(list1, 30) , axis=1)
"""
"""if (row % 2 == 0):
                if (col % 2 == 0):            
                    arr[row:,col] = 1
                else:
                    arr[row:,col] = 0            
            else:
                if (col % 2 == 0):            
                    arr[row:,col] = 0
                else:
                    arr[row:,col] = 1"""
#print(arr)