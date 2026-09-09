import os
from PyPDF2 import PdfReader, PdfWriter

def split_pdf(input_pdf, output_folder, pages_per_file):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)  # Create output folder if not exists

    reader = PdfReader(input_pdf)
    total_pages = len(reader.pages)
    file_count = 1

    for start_page in range(0, total_pages, pages_per_file):
        end_page = min(start_page + pages_per_file, total_pages)
        writer = PdfWriter()

        for page_num in range(start_page, end_page):
            writer.add_page(reader.pages[page_num])

        output_pdf = os.path.join(output_folder, f"split_{file_count}.pdf")
        with open(output_pdf, 'wb') as out_file:
            writer.write(out_file)
        print(f"✅ Created: {output_pdf} (Pages {start_page+1}-{end_page})")
        file_count += 1

    print(f"\n✅ Total {file_count-1} PDF file(s) created successfully!")

if __name__ == "__main__":
    input_pdf = input("Enter the input PDF file path: ").strip()
    output_folder = input("Enter the output folder path: ").strip()
    pages_per_file = int(input("Enter number of pages per file: "))
    split_pdf(input_pdf, output_folder, pages_per_file)
