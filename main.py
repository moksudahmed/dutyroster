from numpy import *
import numpy as np
import random


def find(shits, days, n):
    val = [0] * n
    x=0
    for i in range (len(shits)):
        val[x] = shits[i] + str(days)
        x = x + 1
    return val

def _next(l, target):
    return next((i for i in l if i == target), None)


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
   # print(a)
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
  
def rearangeRow(a,row_size, col_size,limit):
    n = row_size   
    for col in range(col_size):
        val =[0] * n    
        if countNumberRow(a[:,col]) != limit:
            while countNumberRow(val) != limit:
                for i in range(row_size):
                    val[i] = random.randint(0,1)
            for row in range(row_size):
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
def rearangeColumn(arr,row_size, col_size, limit):
    for row in range(row_size):
            val = getNumber(limit)
            for col in range(col_size):
                arr[row:,col] = val[col]         
            col = col+1
            arr[row:,col] = calculateTotalCol(val)
            #print(calculateTotalCol(val))
        #print(clculateRow(arr))
    return arr
        
def getRowTotal(arr, row_size, col_size):
    temp = clculateRow(arr)
    total_row = 0
    for x in range(col_size):
        arr[row_size:,x] = temp[x]
        total_row += temp[x]
    return total_row

def getColoumnTotal(arr, row_size, col_size):
    temp = clculateColumn(arr)
    total_col = 0
    for x in range(row_size):
        arr[x:,col_size] = temp[x]
        total_col += temp[x]
    return total_col

def draw_matrix(a,perday, individual):
    getNumber(individual)

def get_matrix(arr, row_size, col_size,total_instance, perday, individual):
    n = col_size
    val =[0] * n
    x = 1
    for x in range(col_size):
        arr = np.insert(arr, x, random.randint(0,1) , axis=1)
    
    #arr = np.insert(a, 1, 5, axis=1)
    print("A",arr[0][0])
    count = 0
    for i in range(len(arr[0])):
        if arr.any == 1:
            count += 1   
    
    for i in range(len(arr[1][0])):
        print("Test")
    for x in range(row_size):
        while True:            
            for y in range(col_size):
                arr[x:,y] = random.randint(0,1)    
            if calculateTotalCol(arr[0:,0]) != individual:
                break
    print(calculateTotalCol(arr[:,2]))
    
    #for x in range(row_size):
    #rearangeRow(arr,row_size, col_size,perday)
    #rearangeColumn(arr,row_size, col_size, individual)
    total_col = getColoumnTotal(arr, row_size, col_size)    
    total_row = getRowTotal(arr, row_size, col_size)

    total = total_row + total_col
    arr[row_size:,col_size] = total          
    print(arr)          
    #total_col = getColoumnTotal(arr, row_size, col_size)    
    #total_row = getRowTotal(arr, row_size, col_size)
    
    #total = total_row + total_col
        
        # Calculate Total Number of instance in every row and insert in the last column #
    #print(total_col, total_row)
        # Calculate Total Number of instance in the Matrix#
    #arr[row_size:,col_size] = total   
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

get_matrix(arr, array_size_x, array_size_y,total_instance, perday_instance, individual)
