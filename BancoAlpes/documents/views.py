import os
from .logic import logic_documents as vl
from django.http import FileResponse, HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def documents_view(request):
    if request.method == 'GET':
        id = request.GET.get("id", None)
        if id:
            documents_dto = vl.get_document(id)
            documents = serializers.serialize('json', [documents_dto,])
            return HttpResponse(documents, 'application/json')
        else:
            documents_dto = vl.get_documents()
            documents = serializers.serialize('json', documents_dto)
            return HttpResponse(documents, 'application/json')

    if request.method == 'POST':
        documents_dto = vl.create_documents(json.loads(request.body))
        documents = serializers.serialize('json', [documents_dto,])
        return HttpResponse(documents, 'application/json')

@csrf_exempt
def document_view(request, pk):
    if request.method == 'GET':
        documents_dto = vl.get_document(pk)
        documents = serializers.serialize('json', [documents_dto,])
        return HttpResponse(documents, 'application/json')

    if request.method == 'PUT':
        documents_dto = vl.update_document(pk, json.loads(request.body))
        documents = serializers.serialize('json', [documents_dto,])
        return HttpResponse(documents, 'application/json')

def pdf_view(request):
    filepath = os.path.join('BancoAlpes', 'documents', 'yourfile.pdf')  # Update 'yourfile.pdf' to your PDF's name
    return FileResponse(open(filepath, 'rb'), content_type='application/pdf')    
    
