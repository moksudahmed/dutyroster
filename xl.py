import xlsxwriter
import swaparray

def export_to_xl(content, rows, cols, col_total):
    workbook = xlsxwriter.Workbook('duty_roster.xlsx')
    worksheet = workbook.add_worksheet()
       
    for i in range(rows):
        for j in range(cols):
           worksheet.write(i, j, content[i][j]) #(row, column, content) 

        # incrementing the value of row by one with each iterations.     
    for k in range(rows):        
        worksheet.write(k, cols, swaparray.calculate(content[k])) #(row, column, content) 
    
    for i in range(len(col_total)):
        worksheet.write(rows, i, col_total[i]) #(row, column, content)         
    result = list(map(sum, content))    
    worksheet.write(rows, cols, sum(result)) #(row, column, content)         
    
    workbook.close()
