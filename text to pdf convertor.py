# Install fpdf package if not installed
# pip install fpdf

from fpdf import FPDF


def txt_to_pdf(txt_file_path, pdf_file_path):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)

    # Open the text file and add each line to the PDF
    with open(txt_file_path, "r") as file:
        for line in file:
            pdf.cell(0, 10, txt=line.strip(), ln=True)

    # Save the PDF file
    pdf.output(pdf_file_path)
    print(f"PDF created successfully at {pdf_file_path}")



# Install fpdf package if not installed
# pip install fpdf

from fpdf import FPDF


def txt_to_pdf(txt_file_path, pdf_file_path):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)

    # Open the text file and add each line to the PDF
    with open(txt_file_path, "r") as file:
        for line in file:
            pdf.cell(0, 10, txt=line.strip(), ln=True)

    # Save the PDF file
    pdf.output(pdf_file_path)
    print(f"PDF created successfully at {pdf_file_path}")


# Example usage
txt_file_path = "C:\\Users\\hp\\OneDrive\\Desktop\\Types of Machine Learning Algorithms"  # path to your text file
pdf_file_path = "C:\\Users\\hp\\OneDrive\\Desktop\\certificates\\output.pdf"  # desired output path for the PDF

txt_to_pdf(txt_file_path, pdf_file_path)

