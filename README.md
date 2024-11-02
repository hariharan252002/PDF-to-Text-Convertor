This Python script automates the process of converting PDF files into plain text files. It uses the PyPDF2 library to read and extract text from PDF documents and saves the extracted content into a specified .txt file. The script also allows users to specify custom file paths for both the PDF input and the text output, and if no output path is provided, it stores the result in a temporary directory.

Key Features:

	•	PDF to Text Conversion: Extracts text from each page of a given PDF file.
	•	File Handling: Prompts users for the input PDF file path and output text file path, with a fallback to a default temporary directory.
	•	Text File Output: Stores the extracted text in a .txt file.
	•	User-Friendly: Prints extracted text to the console for quick review and logs the output to a file.
	•	Cross-Platform Compatibility: Supports different file systems by handling file paths dynamically.

How it Works:

	1.	The script prompts the user to enter the path to the PDF file and the desired output location for the text file.
	2.	If the output file path is not provided, the script creates a temporary folder (temp) to store the result.
	3.	It reads each page of the PDF and writes the extracted text into the specified .txt file.

This script is useful for automating the extraction of textual data from PDF files for further analysis or record-keeping.
