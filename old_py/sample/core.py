import random
import re


def random_swap_options(text):
    # Use regex to match the options and their corresponding content
    options = re.findall(r"([a-e]\)) (.+)", text)

    # Extract only the content for shuffling
    contents = [content for _, content in options]

    # Shuffle the contents randomly
    random.shuffle(contents)

    # Reconstruct the text with the shuffled content
    swapped_text = text
    for i, (opt, _) in enumerate(options):
        # Escape the parentheses to avoid regex interpretation
        escaped_opt = re.escape(opt)
        swapped_text = re.sub(
            rf"{escaped_opt} .+", f"{opt} {contents[i]}", swapped_text
        )

    return swapped_text


# Extract the text from the original PDF to modify
import io

from PyPDF2 import PdfReader, PdfWriter

reader = PdfReader("main.pdf")
writer = PdfWriter()

for page in reader.pages:
    # Extract page text
    text = page.extract_text()

    # Apply the swap function to the text
    modified_text = random_swap_options(text)
    #
    # # Create a new PDF page with the modified text
    writer.add_page(page)
    output_swapped_pdf_path = (
        "/home/vinicius/Projects/question_trader/output_file/random.pdf"
    )
    with open(output_swapped_pdf_path, "wb") as output_pdf_file:
        writer.write(output_pdf_file)
    exit()


# Save the modified PDF with swapped options
output_swapped_pdf_path = "/home/vinicius/Projects/question_trader/output_file/out.pdf"
with open(output_swapped_pdf_path, "wb") as output_pdf_file:
    writer.write(output_pdf_file)
