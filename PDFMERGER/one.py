import PyPDF2

def merge_pdfs(files_list, output):
    merger = PyPDF2.PdfMerger()
    
    for file in files_list:
        merger.append(file)
    
    merger.write(output)
    merger.close()

if __name__ == "__main__":
    # List of PDF files to merge
    files = ['file1.pdf', 'file2.pdf']
    output = 'merged_files.pdf'
    
    merge_pdfs(files, output)
