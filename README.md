# DOCX to PDF Conversion Script

This repository contains a Python script for converting `.docx` files to `.pdf` format using Microsoft Word. It's designed to automate the conversion process, saving you time when working with large numbers of documents.

## Why Use This Script?

If you frequently work with `.docx` documents and need them converted to `.pdf` format for sharing, archiving, or printing, this script automates the entire process. Instead of manually opening each document in Microsoft Word and saving it as a PDF, this script does it for you — saving you time and effort.

### Key Features:
- **Batch Conversion:** Convert multiple `.docx` files to `.pdf` in one go.
- **Automation:** No need to manually open each document; the script handles it automatically.
- **Clean Organization:** The script deletes the original `.docx` files after conversion (this is optional and can be modified based on your preference).

## Pre-requisite (for Windows)

- **Microsoft Word** must be installed on your system.

## Steps to Use

1. **Copy the script** to the folder where your `.docx` files are saved.
2. **Edit the script:** Paste your folder path into the script (instructions are provided in the script).
3. **Open a terminal** (Command Prompt) in the folder where the script is saved.
4. **Install the required package** by running the following command:
   ```bash
   pip install docx2pdf
5. Run the script by executing:
   ```bash
   python convert.py

## Notes
The script automatically deletes the .docx files after converting them to .pdf. This is a personal preference, but you can modify the script to suit your needs if you don't want to delete the .docx files.
