import os
from docx2pdf import convert

# Define the folder path (use raw string `r""` to avoid escape issues in Windows paths)
folder_path = r"paste the local path here"

# Convert all .docx files to .pdf
for file in os.listdir(folder_path):
    if file.endswith(".docx"):
        docx_file = os.path.join(folder_path, file)
        
        # Convert .docx to .pdf
        convert(docx_file)  

        # Get the corresponding PDF filename
        pdf_file = os.path.splitext(docx_file)[0] + ".pdf"

        # Check if the PDF was successfully created before deleting .docx
        if os.path.exists(pdf_file):
            os.remove(docx_file)  # Delete the original .docx file

print("Conversion completed! All .docx files have been converted and deleted.")

