#
# python3 merge_pdf.py file_name1.pdf file_name2.pdf file_name3.pdf file_name4.pdf ....
#
# Final output: merged_result.pdf
#
from PyPDF2 import PdfMerger
import sys

n_files = len(sys.argv)
files = []
for i in range(1, n_files):
    files.append(sys.argv[i])

merger = PdfMerger()
for fname in files:
    print("Appending ", fname)
    merger.append(fname)

merger.write("merged_result.pdf")
merger.close()
