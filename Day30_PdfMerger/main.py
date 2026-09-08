import os
from PyPDF2 import PdfMerger

def merge_pdfs(pdf_folder, output_pdf):
    # Collect all PDF files from the folder
    pdf_files = [f for f in os.listdir(pdf_folder) if f.lower().endswith('.pdf')]

    if not pdf_files:
        print("❌ No PDF files found in the folder!")
        return

    pdf_files.sort()  # Sort to maintain order
    merger = PdfMerger()

    try:
        for file in pdf_files:
            file_path = os.path.join(pdf_folder, file)  # corrected path join
            merger.append(file_path)

        merger.write(output_pdf)
        print(f"✅ PDF merged successfully: {output_pdf}")

    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        merger.close()  # Close the merger object 

if __name__ == "__main__":
    folder = input("Enter the path of PDF folder: ").strip()
    output = input("Enter output PDF file name (e.g., merged.pdf): ").strip()
    merge_pdfs(folder, output)
