#importando clase node
from s02t0107_1d_linked_list import Node 

#1 creo funcion principal
def main():
 #2coloco el codigo ejecutable
 test_node = Node("prueba")
 print(f"valor del nodo: {test_node.data}")

#evaluo el valor name __name__
if __name__ == "__main__":
  main()