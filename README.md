DOCX to PDF Conversion Script
This repository contains a Python script for converting .docx files to .pdf format using Microsoft Word. 
It's designed to automate the conversion process and save you time when dealing with large numbers of documents.

Why Use This Script?
If you frequently work with .docx documents and need them converted to .pdf format for sharing, archiving, or printing, this script automates the entire process. 
Instead of manually opening each document in Microsoft Word and saving it as a PDF, this script does it for you — saving you time and effort. 
Plus, it automatically deletes the original .docx files after conversion (based on personal preference), keeping your folder clean and organized.

This script is especially useful for:
  Batch converting multiple .docx files to .pdf in one go.
  Automating repetitive tasks without needing to open each document.
  Saving time on document conversion, especially when dealing with large numbers of files.

Pre-requisite (for Windows)
  You need to have Microsoft Word installed on your system.

Steps to Use:
  -->Copy the script to the folder where your .docx file(s) are saved.
  -->Paste your folder path into the script (instructions provided in the script).
  -->Open a terminal (command prompt) in the folder.
  -->Run the following command to install the required package:
      pip install docx2pdf
  -->Run the Python script with:
      python convert.py
    
Note: The script will automatically delete the .docx files after converting them to .pdf (this is a personal preference, but feel free to modify it to suit your needs!).

License
This project is open-source and free to use for personal or commercial purposes.
