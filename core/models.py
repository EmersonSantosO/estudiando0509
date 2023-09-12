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

    def listAll(self):
        return self.tickets
    
    def searchTicket(self, id):
        for t in self.tickets:
            if id == t.id:
                return t
        return #Retorna None
    
    def create(self, ticket):
        resultado = self.searchTicket(ticket.id)
        if resultado is None:
            self.tickets.append(ticket)
            return 'Se agrego ticket'
        return 'Codigo ya existe'
    
    def edit(self, ticket):
        resultado = self.searchTicket(ticket.id)
        if(isinstance(resultado, Ticket)):
            resultado.name = ticket.name
            resultado.description = ticket.description
            resultado.tech = ticket.tech
            return 'Se ha modificado ticket'
        return 'No se ha podido modificar'

