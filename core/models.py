from django.db import models

class Ticket:
    def __init__(self, id, name, description, tech):
        self.id = id
        self.name = name
        self.description = description
        self.tech = tech

class HelpDesk:
    def __init__(self):
        
        t1 = Ticket(12345, 'Ticket 1', 'Esto es una descripcion', 'Perico Los Palotes')
        t2 = Ticket(54321, 'Ticket 2', 'Esto es un clon', 'Perico Los Palotes')

        self.tickets = [t1, t2]

    def list_all(self):
        return self.tickets
    
    
    def create_ticket(self,id, name, description, tech):
        newTicket = Ticket(id, name, description, tech)
        self.tickets.append(newTicket)
        return 


            
    def remove_ticket(self, id):
        ticket = self.search_ticket(id)
        if ticket:
            self.tickets.remove(ticket)
        else:
            return "Ticket no encontrado"

    def search_ticket(self, id):
        for ticket in self.tickets:
            if ticket.id == id:
                return ticket
        return 
    
    def edit_ticket(self, id, new_name, new_description, new_tech):      
        ticket = self.search_ticket(id)     
        if ticket:
            ticket.name = new_name
            ticket.description = new_description
            ticket.tech = new_tech
            return f"Ticket {ticket.name} editado correctamente"
        else:
            return "Ticket no encontrado"