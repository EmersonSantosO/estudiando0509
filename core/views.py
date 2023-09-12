from django.shortcuts import render
from core.models import Ticket, HelpDesk

h = HelpDesk()

def home(request):
    return render(request, 'core/ticketList.html', context={'context':h.listAll()})

def createForm(request):
    return render(request, 'core/ticketForm.html')

def addTicket(request): 
    #Capturamos datos desde formulario que se encuentran en request
    id = request.POST.get('id')
    name = request.POST.get('name')
    description = request.POST.get('description')
    tech = request.POST.get('tech')

    if(id == '' or name.replace(' ', '') == '' or description.strip(' ') == '' or tech == ''):
        context = {'mensaje':'No se puede agregar un ticket sin datos'}
    else:
        #Instanciamos objeto tipo TICKET 
        try:
            t = Ticket(int(id), name, description, tech)
            #Llamos a nuestro objeto HelpDesk para usar su metodo create
            #y aniadir un nuevo tick
            resultado = h.create(t)
            context = {'mensaje': resultado}
        except:
            context = {'mensaje': 'Se ha producido un error'}
    #Retornamos la vista
    return render(request, 'core/created.html', context)

def editForm(request):
    id = int(request.POST.get('id'))
    ticket = h.searchTicket(id)
    if ticket is not None:
        context = {'ticket':ticket}
    else:
        context = {}
    return render(request, 'core/ticketEditForm.html', context)

def editTicket(request):
    id = request.POST.get('id')
    name = request.POST.get('name')
    description = request.POST.get('description')
    tech = request.POST.get('tech')

    if(id == '' or name.replace(' ', '') == '' or description.strip(' ') == '' or tech == ''):
        context = {'mensaje':'No se puede agregar un ticket sin datos'}
    else:
        try:
            t = Ticket(int(id), name, description, tech)
            resultado = h.edit(t)
            context = {'mensaje': resultado}
        except:
            context = {'mensaje': 'Se ha producido un error'}
    #Retornamos la vista
    return render(request, 'core/edited.html', context)

