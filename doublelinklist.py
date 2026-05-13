class DoubleLinkedList:

    def __init__(self):

        self.head = None
        self.tail = None

    # Agregar nodo al final
    def append(self, new_node):

        # Lista vacía
        if self.head is None:

            self.head = new_node
            self.tail = new_node

        else:

            # Conectar nodos
            new_node.prev = self.tail
            self.tail.next = new_node

            # Actualizar tail
            self.tail = new_node

    # Agregar hijo a un nodo
    def add_child(self, parent, child):

        # Si no tiene sublista
        if parent.sub_list is None:

            sub_list = DoubleLinkedList()

            sub_list.head = child
            sub_list.tail = child

            parent.sub_list = sub_list

        else:

            current = parent.sub_list.tail

            current.next = child
            child.prev = current

            parent.sub_list.tail = child

    # Mostrar multilista
    def print_multilist(self, level=0):

        current = self.head

        while current:

            print("   " * level + str(current))

            # Si tiene hijos
            if current.sub_list:
                current.sub_list.print_multilist(level + 1)

            current = current.next