class Node:

   def __init__(self, x, next = None):
      self.value = x
      self.next = next
      
class LinkedQ:
    
    def __init__(self): 
       self.first = None
       self.last = None
       
    def enqueue(self,x):
        """Stoppar in x sist i kön """
        ny = Node(x)
        if self.first == None:
            self.first=ny
            self.last=ny
            # Om kön är tom blir det på ett sätt...
                            # ...som du får tänka ut själv.
        else:      
            self.last=ny
            x= self.first
            y= x.next     # x = nuvarande objekt, y = nuvarande objekts pekare
            
            while y != None: # om den föregåendes objektets pekare var skillt från None,
                # uppdatera då tills du får fram den pekare vars värde är None
                # sätt om den så att den pekar på den nya objektet
                x=x.next
                y=x.next
            x.next=ny # sätter värdet på None pekare till det nya objektet

    def dequeue(self):
        """Plockar ut och returnerar det som står först i kön """
        temp = self.first.value # kanske skicka tillbaka hela noden
        self.first=self.first.next
        return temp

    def isEmpty(self):
        """Returnerar True om kön är tom, False annars """
        if self.first == None:
            return True
        else: 
            return False
    def size(self):
        size=1
        y = self.first.next
        while y != None:
            self.first=self.first.next
            y = self.first.next
            size=size+1
        return size    
          

import unittest
from linkedQFile import LinkedQ

class TestQueue(unittest.TestCase):

    def test_isEmpty(self):
        #isEmpty ska returnera True för tom kö, False annars
        q = LinkedQ()
        self.assertTrue(q.isEmpty(), "isEmpty på tom kö")
        q.enqueue(17)
        self.assertFalse(q.isEmpty(), "isEmpty på icke-tom kö")

    def test_order(self):
        #Kontrollerar att kö-ordningen blir rätt
        q = LinkedQ()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        self.assertEqual(q.dequeue(), 1)
        self.assertEqual(q.dequeue(), 2)
        self.assertEqual(q.dequeue(), 3)

if __name__ == "__main__":
    unittest.main()