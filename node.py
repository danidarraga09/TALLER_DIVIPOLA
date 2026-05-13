class Node:

    def __init__(self, id, name):

        self.id = id
        self.name = name

        # Nodo siguiente
        self.next = None

        # Nodo anterior
        self.prev = None

        # Sublista (hijos)
        self.sub_list = None

    def __str__(self):
        return f"{self.id} - {self.name}"