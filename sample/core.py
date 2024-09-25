# Function to swap the content in the answer choices A <-> E and B <-> D in a PDF text
def swap_options(text):
    # Swap the option A with E, and B with D using a placeholder
    text = text.replace("a)", "TEMP_A)")
    print("Conteudo de A ->" + text)
    text = text.replace("e)", "a)")
    print("Conteudo de E ->" + text)
    text = text.replace("TEMP_A)", "e)")

    text = text.replace("b)", "TEMP_B)")
    text = text.replace("d)", "b)")
    text = text.replace("TEMP_B)", "d)")

    return text


# Extract the text from the original PDF to modify
import io

from PyPDF2 import PdfReader, PdfWriter

reader = PdfReader("../main.pdf")
writer = PdfWriter()

for page in reader.pages:
    # Extract page text
    text = page.extract_text()
    print(text)

    # Apply the swap function to the text
    # modified_text = swap_options(text)
    #
    # # Create a new PDF page with the modified text
    writer.add_page(page)
    output_swapped_pdf_path = (
        "/home/vinicius/Projects/question_trader/output_file/out.pdf"
    )
    with open(output_swapped_pdf_path, "wb") as output_pdf_file:
        writer.write(output_pdf_file)
    exit()


# Save the modified PDF with swapped options
output_swapped_pdf_path = "/home/vinicius/Projects/question_trader/output_file/out.pdf"
with open(output_swapped_pdf_path, "wb") as output_pdf_file:
    writer.write(output_pdf_file)
