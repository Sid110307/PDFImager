import os
from tkinter import Tk, filedialog, ttk

from PyPDF2 import PdfFileReader
from wand.image import Image

root = Tk()
root.title("PDF to Image Converter")


def pdf_to_image():
    file_path = filedialog.askopenfilename(
        title="Select input file", filetypes=[("PDF files", "*.pdf")])
    if not file_path:
        return

    save_directory = filedialog.askdirectory(
        title="Select the directory to save the images")
    if not save_directory:
        return

    pdf = PdfFileReader(file_path, strict=False)

    for page in range(len(pdf.pages)):
        with Image(filename=f"{file_path}[{str(page)}]", resolution=300) as img:
            img.save(filename=os.path.join(
                save_directory, f"page_{str(page)}.jpg"))


convert_button = ttk.Button(
    root, text="Convert PDF to Image", command=pdf_to_image)
convert_button.pack(side="top", fill="both", expand=True, padx=10, pady=10)

if __name__ == "__main__":
    root.mainloop()
