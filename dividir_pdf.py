import PyPDF2
import os
from tkinter import Tk, filedialog

def abrir_janela_arquivo():
    root = Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(title="Selecione o arquivo PDF")
    root.destroy()

    return file_path

def abrir_janela_pasta():
    root = Tk()
    root.withdraw()
    folder_path = filedialog.askdirectory(title="Selecione a pasta de destino")
    root.destroy()

    return folder_path

def dividir_pdf(input_pdf_path, output_directory):
    with open(input_pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)

        total_pages = len(pdf_reader.pages)


        if not os.path.exists(output_directory):
            os.makedirs(output_directory)

        for page_number in range(total_pages):
            pdf_writer = PyPDF2.PdfWriter()
            pdf_writer.add_page(pdf_reader.pages[page_number])

            output_file_path = os.path.join(output_directory, f'page_{page_number + 1}.pdf')

            with open(output_file_path, 'wb') as output_file:
                pdf_writer.write(output_file)

            print(f'Página {page_number + 1} dividida e salva em {output_file_path}')


if __name__ == "__main__":
    pdf_path = abrir_janela_arquivo()
    if not os.path.exists(pdf_path):
        print("O arquivo PDF não foi encontrado.")
    else:
        output_dir = abrir_janela_pasta()

        dividir_pdf(pdf_path, output_dir)
