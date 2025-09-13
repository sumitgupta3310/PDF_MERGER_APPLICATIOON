import os
from PyPDF2 import PdfMerger

user_input = input("Enter file path: ")
print("Merging PDF Files")
directory = user_input
merger = PdfMerger()
for filename in os.listdir(directory):
    if filename.endswith(".pdf"):
        merger.append(os.path.join(directory, filename))
merger.write("C:/Users/Sumit Gupta -SSD PC/Downloads/Ravi/pdfs/merged_output.pdf")
print("files merged successfully")
merger.close()