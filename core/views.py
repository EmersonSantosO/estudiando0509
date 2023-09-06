from django.shortcuts import render
from .models import Ticket, HelpDesk
# Create your views here.
h = HelpDesk()
def home(request):
    return render(request,"ticketList.html", context={"context":h.listAll()})

def createForm(request):
    return render(request,"ticketForm.html")