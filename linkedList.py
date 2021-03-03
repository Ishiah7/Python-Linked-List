class Node:
  def __init__(self, data):
    self.data = data
    self.next = None


class LinkedList:
  head = None

  # Add Node to end of Linked List.

  def addAtBack(self, node):
    if self.head == None:
      self.head = node

    else:
      second_head = self.head

      while second_head.next != None:
        second_head = second_head.next

      second_head.next = node


  # Display Linked List Size.

  def size(self):
    count = 0

    if self.head == None:
      print(count) # could also return count instead of printing/ idea.

    else:
      count_pointer = self.head
      count += 1

      while count_pointer.next != None:
        count_pointer = count_pointer.next
        count += 1
      
      print(count)

  # Check if Linked List is empty or not
    
  def isEmpty(self):
    if self.head == None:
      return True

    else:
      return False


  # Delete Node at end of Linked List.

  def deleteFromBack(self):
    if self.head == None:
      print("Linked List is empty.")
    
    else:
      second_head = self.head
      prev_node = None

      while second_head.next != None:
        prev_node = second_head
        second_head = second_head.next

      if prev_node == None:
        self.head  = None
      
      else:
        prev_node.next = None


  # Search for data in the Linked List

  def search(self, data):
    if self.isEmpty():
      print('Empty Linked List contains no data!')
      return

    else:
      second_head = self.head

      while second_head.next != None:

        if data == second_head.data:
          print(f'{data} found!')
          return

        second_head = second_head.next

      if data == second_head.data:
        print(f'{data} found!')
        return

      else:
        print(f'{data} not found.')
        return










  


    




