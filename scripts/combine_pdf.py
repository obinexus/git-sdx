#!/usr/bin/env python3
import os
import argparse
from PyPDF2 import PdfMerger

# Set up argument parser
parser = argparse.ArgumentParser(description="Combine all PDFs in a directory (recursively) into one PDF.")
parser.add_argument("directory", help="Path to the root directory containing PDFs")
args = parser.parse_args()

# Define the root directory and output path
root_dir = args.directory
output_dir = os.path.join(root_dir, "merge")
os.makedirs(output_dir, exist_ok=True)
output_file = os.path.join(output_dir, "obiai-merged.pdf")

# Create the PDF merger object
merger = PdfMerger()

# Walk through all subdirectories and find .pdf files
for subdir, _, files in os.walk(root_dir):
    for file in sorted(files):
        if file.lower().endswith(".pdf"):
            pdf_path = os.path.join(subdir, file)
            print(f"Adding: {pdf_path}")
            merger.append(pdf_path)

# Write out the merged PDF
merger.write(output_file)
merger.close()
print(f"Merged PDF saved to: {output_file}")
