import os
from PyPDF2 import PdfMerger

continue_input = "Y"

while continue_input.casefold() == "y":
    user_input = input("Enter directory path: ")
    print("Merging PDF Files")
    directory = user_input

    merger = PdfMerger()
    for filename in os.listdir(directory):
        if filename.endswith(".pdf"):
            merger.append(os.path.join(directory, filename))

    output_path = os.path.join(directory, "merged_output.pdf")
    merger.write(output_path)
    merger.close()

    print(f"Files merged successfully into {output_path}")
    continue_input = input("Do you wish to continue Y/N: ")
