from array import array

class ArrayQ():
  def __init__(self):
    self._lista=[]   

  def enqueue(self, x):
      """lägger in self längst back i listan """
      self._lista.append(x)  


  def dequeue(self):
    temp = self._lista[0]
    self._lista.pop(0)
    return temp #tar ut element 0 ur listan och returnar

  def isEmpty(self):
      """Returnerar True om listan är tom, False annars"""
      if self._lista == []: 
         return True
      else: 
         return False 
  
if __name__ == "__main__":
    q = ArrayQ()
    q.enqueue(1)
    q.enqueue(2)
    print(q)
    x = q.dequeue()
    y = q.dequeue()
    if (x == 1 and y == 2):
        print("OK")
    else:
        print("FAILED")