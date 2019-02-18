from Classes import document
from Classes import document_writer

def export_document(document):
    document_writer.DocumentWriter(document).write_document()

