from linkedQFile import LinkedQ
  

q = LinkedQ()
q1 = [7, 1, 12, 2, 8, 3, 11, 4, 9, 5, 13, 6, 10]
q2 = input().split()


for i in range(len(q2)):
  q.enqueue(int(q2[i]))

a = []


for i in range(len(q2)):
  y = q.dequeue() 
  q.enqueue(y)  # tar nollte elementet och stoppar in den längst bak
  x = q.dequeue()# tar bort nollte elementet och sparar in den i a
  a.append(x) 
   
print(a)
