from numpy import *
import numpy as np
import random
from copy import copy, deepcopy

def countNumber(a):
    count = 0
    for i in range(len(a)):
        if a[i] == 1:
            count += 1   
    return count

def chaeck_same(a,pos):
    if a[pos] == 1: 
        if a[pos-1]== 1 and a[pos-2]== 1:
            return True
    else:
        return False
           
def getNumber(limit, cols):
    n = cols
    a =[0] * n
    
    while True:
        for i in range(n):
           a[i] = random.randint(0,1)
           if chaeck_same(a,i):
                a[i] = 0
                #print(a,i,a[i],a[i-1], a[i-2],a[i-3], "Match")
        if countNumber(a) == limit:
            break
    return a
def getNumberCol(limit, n):
    a =[0] * n    
    while True:
        for i in range(n):
           a[i] = random.randint(0,1)
        if countNumber(a) == limit:
            break
    return a

def modify_array(arr, m, rows, cols):
    x =rows + 1
    y = cols + 1
    a = [[0]*y]*x
    a = deepcopy(arr)        
    a.append(m)
    column_to_add = np.array([[calculateTotalCol(a[j]) for i in range(1)] for j in range(x)])
    output = np.column_stack((a, column_to_add))
  #  total_rows = calculateTotalValue(output[rows:,]) 
    #print(output[:,cols])
    total_cols = calculateTotalValue(output[:,cols])
    output[rows:,cols] = total_cols
    return output
   
def calculateTotalInstanceinRow(a,rows,cols):
    arr = [0]*cols
    count = 0
    for col in range(cols):
        for row in range(rows):        
            count += a[row][col]
            arr[col] = count 
        count = 0
    
    return arr

def calculateTotalInstanceinCol(a,rows,cols):
    arr = [0]*cols
    count = 0
    for col in range(cols):
        for row in range(rows):        
            count += a[row][col]
            arr[col] = count 
        count = 0
    return arr

def calculateTotalInstanceinRow(a,rows,cols):
    count = 0
    for col in range(cols):
        for row in range(rows):        
            count += a[row][col]
    return count

def calculateTotalValue(a):
    count = 0
    for i in range(len(a)):         
         count += a[i]     
    return count

def calculateTotalCol(a):
    count = 0
    for i in range(len(a)):
        if a[i] == 1:
            count += 1               
    return count
    
def calculateTotalRow(a, row, col):
    count = 0
    for i in range(row):
        if a[i][col] == 1:
            count += 1               
    return count

def calculateTotal(a, row, col):
    count = 0
    for col in range(cols):    
        for row in range(rows):    
            if a[row][col] == 1:
                count += 1  
    return count

def draw(arr,rows,cols,limit):
    for row in range(rows):
        #while calculateTotalCol(arr[row]) != limit:            
            #for col in range(cols):
         #print(arr[row], getNumber(limit, cols))
         arr[row] = getNumber(limit, cols)
    return arr

def drawCol(arr,rows,cols, limit, individual):
    a = [0]*cols   
    for col in range(cols):
        #if countNumber(arr[row][col]) != limit:    
            a = getNumberCol(limit[col],rows)
            
            for row in range(rows):
                arr[row][col] = a[row]
             #   arr = draw(arr,rows,cols,individual) 
    return arr

def swap(arr, a, pos, b, pos2, cols, individual):    
    print("Befor",a)
    print("Befor",b)
    print(pos, pos2)
    for i in range(0, cols):
        if a[i] == 1 and calculateTotalCol(a) >= individual and calculateTotalCol(b) <= individual :
            if len(b) >i:
                print(a[i], b[i])
                b[i] = 1
                a[i] = 0
                arr[pos] = a
                arr[pos2] = b     
    print("re a",arr[pos])
    print("re b",arr[pos2])
    return arr

def find_higher_value(arr, rows, cols, individual):
    a = [] 
    a1 = []
    a2 = []  
    for row in range(rows):
        if arr[row][cols] > individual:
            a1.append(row)
            a2.append(arr[row][cols])
    a.insert(0,a1)
    a.insert(1,a2)
    return a
def find_lower_value(arr, rows, cols, individual):
    a = [] 
    a1 = []
    a2 = []  
    for row in range(rows):
        if arr[row][cols] < individual:
            a1.append(row)
            a2.append(arr[row][cols])
    a.insert(0,a1)
    a.insert(1,a2)
    return a
def rearangeRow(arr,rows,cols, shifts, individual):
    a = [] 
    b = []
    a = find_higher_value(arr, rows, cols, individual)
    b = find_lower_value(arr, rows, cols, individual)
    
    print("High:", a)    
    print("Low:", b)
    print(a[0][0],":",a[1][0], b[0][0],":",b[1][0])
    print("a:", arr[a[0][0]])
    print("b:",arr[b[0][0]])
    print("---",len(a[0]), len(b[0]))
   
    if len(a[0]) > len(b[0]):
        for c in range(0,1):
            for r in range(len(a[c])):            
               # print(arr[a[0][r]], end = " ")
               if r < len(b[0]):
                arr = swap(arr,arr[a[0][r]],a[0][r],arr[b[0][r]],b[0][r],cols, individual)    
   
                print()
    else:
        for c in range(0,1):
            for r in range(len(b[c])):            
                print(b[0][r],b[1][r], end = " ")
                print()
    
    print("a:",arr[a[0][0]])
    print("b:",arr[b[0][0]])
    
    return arr

total_person = 20
pershift_instance = 8
total_shits = 8
total_instance = pershift_instance * total_shits
individual = round(total_instance / total_person)
array_size_x = total_person
array_size_y = total_shits
print(total_person,individual, total_instance)
# Python 3 program to demonstrate working
# of method 1 and method 2.
rows, cols = (array_size_x, array_size_y)
# method 2 1st approach

arr = [[0]*cols]*rows
# lets change the first element of the
# first row to 1 and print the array
shifts = [8,7,6,6,10,8,8,7]

x = 0

total_cols = 0
while True:
    arr = [[random.randint(0,1) for i in range(cols)] for j in range(rows)]

    #arr = draw(arr,rows,cols,individual)
    #a = calculateTotalInstanceinCol(arr,rows,cols)
    #arr = modify_array(arr, a, rows, cols)

   # print(np.matrix(arr))

    arr = drawCol(arr,rows,cols,shifts, individual) #pershift_instance
    col_total = calculateTotalInstanceinCol(arr,rows,cols)
    row_total =  calculateTotalInstanceinRow(arr,rows,cols)
    arr = modify_array(arr, col_total, rows, cols)
    
    total = row_total + arr[rows:,cols]
    
    total_cols = arr[rows:,cols]
    print(np.matrix(arr))
    print(rearangeRow(arr,rows,cols, shifts, individual))
    
    #print(np.matrix(arr))
    if total_cols <= total:
        break
    
#print(np.matrix(arr))
