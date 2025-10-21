"""
pdf_resumen
"""

#!/usr/bin/env python
# coding: utf-8

# In[1]:


import fitz  # PyMuPDF
from docx import Document
from gensim.summarization import summarize

def pdf_to_word_summary(pdf_path, word_path):
    # Abrir el documento PDF
    pdf_document = fitz.open(pdf_path)
    text = ""

    # Leer cada página del documento PDF
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        text += page.get_text()

    # Usar gensim para generar un resumen del texto
    summary = summarize(text)

    # Crear un nuevo documento Word
    doc = Document()
    doc.add_paragraph(summary)

    # Guardar el documento Word
    doc.save(word_path)

    # Cerrar el documento PDF
    pdf_document.close()

# Uso del programa
pdf_path = 'ruta/a/tu/documento.pdf'
word_path = 'ruta/donde/guardar/documento.docx'
pdf_to_word_summary(pdf_path, word_path)


# In[ ]:






if __name__ == "__main__":
    pass
