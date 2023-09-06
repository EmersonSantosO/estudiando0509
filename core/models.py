from django.db import models

class Ticket:
    def __init__(self,id,name,description,tech) -> None:
        self.id = id
        self.name = name
        self.description = description
        self.tech = tech

class HelpDesk:
    def __init__(self) -> None:
        t1 = Ticket(1,"Ticket 1","This is a ticket", "Tech 1")
        self.tickets = [t1]


    def create(self,ticket):
        result = self.searchTicket(ticket.id)
        if result is None:
            self.tickets.append(ticket)
            return f"Ticket {ticket.name}added"
        else:
            return "ID already added"

    def searchTicket(self,id):
        for t in self.tickets:
            if t.id == id:
                return t 
        return 
    
    def listAll(self):
        return self.tickets
    
    def edit(self,ticket):
        result = self.searchTicket(ticket.id)
        if isinstance(result,Ticket):
            result.description = ticket.description
            result.name = ticket.name
            result.tech = ticket.tech
            return f"Modified Ticket {result.id}"
    
    def remove(self,ticket):
        result = self.searchTicket(ticket.id)
        if isinstance(result,Ticket):
            self.tickets.remove(result)
            return f"Removed Ticket {result.id}"
        else:
            return "Ticket not found"