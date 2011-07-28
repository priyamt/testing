class Stack:
   def __init__(self):
       self.storage = []

   def push(self, p):
       self.storage.append(p)
       print 'push',p
   def pop(self):
       try:
     
           i= self.storage.pop()
           print i
           return i
       except(IndexError):
           print "An exception, \"IndexError\", because stack is now empty"
   def is_empty(self):
       return (self.storage == [])
if __name__ == "__main__":
    
     a = Stack()
     a.push(10)
     a.push(20)
     i = a.pop()
     i = a.pop()
     k = a.is_empty()
     i = a.pop()
