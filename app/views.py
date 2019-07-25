from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.template.response import TemplateResponse

from app import models

# Create your views here.
def receipts(request):
    receipts = models.Receipt.objects.all()
    context = (
        RequestContext(
            request,
            {
                'receipts': receipts,
            }
        ).flatten()
    )
    return TemplateResponse(request, 'app/receipts.html', context=context)

def receipt(request, receipt_id):
    receipt = models.Receipt.objects.get(id=receipt_id)
    context = (
        RequestContext(
            request,
            {
                'receipt': receipt,
            }
        ).flatten()
    )
    return TemplateResponse(request, 'app/receipt.html', context=context)
