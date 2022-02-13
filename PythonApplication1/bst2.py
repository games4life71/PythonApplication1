from object import objectClass


class Node:
   def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data
   

   def insert(self, data):
       if self.data:
           if data < self.data:
               if self.left is None:
                   self.left = Node(data)
               else:
                   self.left.insert(data)
           else:
               if self.right is None : 
                   self.right = Node(data)
               else:
                   self.right.insert(data)
       else : 
         self.data = data 


   def inorder(self):
        if self.left is not None : 
            self.left.inorder()
        print(self.data)
        if self.right is not None :
            self.right.inorder()

root = Node(1)
root.insert(2)
root.insert(3)
root.insert(4)
root.insert(65)
root.insert(12)
#root.inorder()

Obj1 = objectClass('static' , 11213121)
Obj1.typeof = 3121212
obj2  = objectClass()

print(obj2.serialNO , " " , obj2.typeof)
obj2.serialNO = input('Specify the serial no of the number {} object'.format(int(objectClass.numberOfinstances)))
print('The new serial number for the object is {}'.format(obj2.serialNO))