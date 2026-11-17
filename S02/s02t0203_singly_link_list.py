#importando clase node
from s02t0107_1d_linked_list import Node 

#creando la clase de una lista enlazada
class Singly_Linked_List:
  #cosntructor
  def  __init__(self):
    self.head=None
    #metodo de insercion de nodo en lista
  def append(self,data):
    #creo el nodo
    new_node = Node(data)
    #si la lista esta vacia 
    #apuntamos el head al nueva nodo
    #que se creo
    if not self.head:
      self.head=new_node
      return
    #Si la lista no esta vacia, hay
    #que recorrer el nodo hasta llegar
    #al final de ña lista
    
    current_node = self.head
    while current_node.next:
      current_node=current_node.next
    current_node.next= new_node



def main():
  my_list = Singly_Linked_List()
  #agregar elementos a la lista
  my_list.append(30)
  my_list.append(59)
  my_list.append(80)
  my_list.append(100)
  #recorrer la lista
  for value in my_list.head.iter():
    print(f" {value}, ",end=" ")

#1 creo funcion principal
# def main():
#  #2coloco el codigo ejecutable
#  test_node = Node("prueba")
#  print(f"valor del nodo: {test_node.data}")

 #evaluo el valor name __name__
if __name__ == "__main__":
   main()
  























































































  