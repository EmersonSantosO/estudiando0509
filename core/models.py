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
        self.tickets.append(ticket)
    
    def searchTicket(self,id):
        for t in self.tickets:
            if t.id == id:
                return t 
        return
    def listAll(self):
        return self.tickets