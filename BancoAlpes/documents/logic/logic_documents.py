from ..models import Documento

def get_document(document_pk):
    document = Documento.objects.get(pk=document_pk)
    return document

def get_documents():
    documents = Documento.objects.all()
    return documents
