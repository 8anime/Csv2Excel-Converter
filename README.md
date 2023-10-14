# csvToExcel Function

The `csvToExcel` function is a Python script that converts data from a CSV file into an Excel file. It reads data from a CSV file, creates a new Excel workbook, and writes the data to an Excel sheet. This function is designed to be used with specific file paths and file names for both input and output.

## Prerequisites

Before using this function, ensure that you have the following prerequisites:

- Python installed on your system.
- The `openpyxl` library, which can be installed using `pip`


## Usage

To use the `csvToExcel` function, follow these steps:

1. Clone or download the project folder to your local machine.

2. Modify the `CSV_FOLDER` and `EXCEL_FOLDER` variables to set the appropriate directory paths where CSV and Excel files will be stored.

3. Ensure that the input CSV file is placed in the `CSV_FOLDER` directory. The default input file name is 'supermarket_sales.csv,' but you can modify it as needed.

4. Run the main.py script in your Python environment:

5. If the data transfer is successful, the Excel file will be saved in the `EXCEL_FOLDER` directory with the name 'supermarket_sales.xlsx.' You can modify the output file name if necessary.

6. If any errors occur during the process, the script will display appropriate error messages.

## Error Handling

The `csvToExcel` function handles several exceptions, including:

- `FileNotFoundError`: If the input CSV file is not found.
- `PermissionError`: If there are permission issues with file operations.
- `Exception`: For any other unexpected errors.

## Example

Here's an example of how to use the `csvToExcel` function:

```python
from dataConverter.csvToExcelConverter import csvToExcel

status = csvToExcel()
if status:
    print('Data transfer successful')
else:
    print('An error occurred during the data conversion')
