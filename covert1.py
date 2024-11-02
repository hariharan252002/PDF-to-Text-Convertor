# -*- coding: utf-8 -*-
import PyPDF2
import os

# Create 'temp' directory if it doesn't exist
if not os.path.isdir("temp"):
    os.mkdir("temp")
    
# Prompt user for PDF and output file paths
pdfpath = input("Enter the full path of your PDF file (use double backslash or raw string for path): ")
txtpath = input("Enter the output TXT file path (use double backslash or raw string for path): ")

# Set the base directory for temp files if output path is not provided
BASEDIR = os.path.realpath("temp")
print(f"Base directory: {BASEDIR}")

# Use default path in 'temp' directory if no specific output path is provided
if len(txtpath) == 0:
    txtpath = os.path.join(BASEDIR, os.path.basename(pdfpath).replace(".pdf", "") + ".txt")

# Open the PDF file in binary mode
with open(pdfpath, 'rb') as pdfobj:
    # Create PDF reader object
    pdfread = PyPDF2.PdfReader(pdfobj)
    
    # Get the total number of pages
    x = len(pdfread.pages)
    
    # Loop through each page and extract text
    for i in range(x):
        pageObj = pdfread.pages[i]
        with open(txtpath, 'a+', encoding='utf-8') as f:  # Ensure proper encoding for text
            text = pageObj.extract_text()
            f.write(text)
            print(text)  # Show extracted text on console