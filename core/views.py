from django.shortcuts import render, redirect
from core.models import Ticket, HelpDesk

h = HelpDesk()

def home(request):
    return render(request, 'core/ticketList.html', context={'context':h.list_all()})


def create_ticket(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        name = request.POST.get('name')
        description = request.POST.get('description')
        tech = request.POST.get('tech')

        if not (id.strip() and name.strip() and description.strip() and tech.strip()):
            # Si faltan datos, puedes manejar el error aquí
            context = {'mensaje': 'No se puede agregar un ticket sin datos'}
        else:
            try:
                h.create_ticket(id, name, description, tech)
                return redirect('ticketList')  # Redirigir a la lista de tickets
            except:
                context = {'mensaje': 'Se ha producido un error'}

    return render(request, 'core/ticketForm.html', context={})

def edit_ticket(request, id):
    ticket = h.search_ticket(id)
    
    if not ticket:
        error_message = "Ticket no encontrado"
        return render(request, 'ticketList.html', {'error_message': error_message})
    
    if request.method == 'POST':
        new_name = request.POST.get('new_name')
        new_description = request.POST.get('new_description')
        new_tech = request.POST.get('new_tech')

        result = h.edit_ticket(id, new_name, new_description, new_tech)
        
        if result:
            return redirect('ticketList')
    
    return render(request, 'edit_ticket.html', {'ticket': ticket})
def remove_ticket(request, id):

    ticket = h.search_ticket(id)

    if ticket:
        
        h.remove_ticket(id)
        return redirect('ticketList')  
    else:
      
        error_message = "Ticket no encontrado"
        return render(request, 'ticketList.html', {'error_message': error_message})

