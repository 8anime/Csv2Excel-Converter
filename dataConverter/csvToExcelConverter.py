
# Import the necessary modules
import os
import csv
import openpyxl

SCRIPT_LOC = os.path.abspath(__file__)     # Construct a path to get location of the current script(csvToExcel.py)
SCRIPT_DIR = os.path.dirname(SCRIPT_LOC)   # Get the directory where the script(csvToExcel.py) is located
ROOT_DIR = os.path.dirname(SCRIPT_DIR)     # Get the directory where the script directory is located, which is the root directory
CSV_FOLDER = 'csvFiles'                    # Name of the folder that contains csv data
EXCEL_FOLDER = 'excelFiles'                # Folder that will contain the csv data in excel format


def csvToExcel():
    """
    Convert data from a CSV file to an Excel file.

    This function reads data from a CSV file, creates a new Excel workbook,
    and writes the data to an Excel sheet. It is designed to be used with
    specific file paths and file names for both input and output.

    Args:
        None (Input file and output file paths are defined inside the function).

    Raises:
        FileNotFoundError: If the input CSV file is not found.
        PermissionError: If there are permission issues with file operations.
        Exception: For any other unexpected errors.

    Returns:
        None

    Note:
        - Make sure to set the 'CSV_FOLDER' and 'EXCEL_FOLDER' variables to
          the appropriate directory paths where CSV and Excel files are stored.
        - The function saves the Excel file in the 'EXCEL_FOLDER' directory.

    Example:
        csvToExcel()
    """
    try:
        cFile = 'supermarket_sales.csv'                  # Define the name of the CSV file
        csvFile = os.path.join(CSV_FOLDER, cFile)        # Construct the path to the CSV file in the CSV folder
    
        eFile = 'supermarket_sales.xlsx'                 # Define the name of the Excel file
        excelFile = os.path.join(EXCEL_FOLDER, eFile)    # Construct the path to the Excel file in the Excel folder
    
        # Try to open and read the CSV file
        with open(csvFile, 'r', encoding='utf-8') as readCsvFile:
            reader = csv.reader(readCsvFile)  # Create a reader object to read the csv file contents
            data = list(reader)               # Put the data read from the csv file into a list
    
        # Create a new Excel workbook and sheet
        wb = openpyxl.Workbook()
        sheet = wb.active
        sheet.title = 'Supermarket data'  # Title of the sheet
    
        # Write data to the Excel sheet
        for row in data:
            sheet.append(row)
    
        # Save the Excel workbook
        wb.save(excelFile)

        # Return True if both operations were successful
        return True
    
    except FileNotFoundError:
        print('File not found. Please check the file paths')
    except PermissionError:
        print('Permisson error: Make sure you have the necessary permissions')
    except Exception as e:
        print(e)

        # Return False if an error occured during the operations
        return False
    
    





