
from dataConverter.csvToExcelConverter import csvToExcel

status = csvToExcel()
if status:
    print('Data transfer successful')
else:
    print('An error occured during the data conversion')


