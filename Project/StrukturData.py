import random

class Room:
    def __init__(self, level, index=0):
        self.treasure = False
        self.indexQuestion = random.randint(0,99)                   #100 question
        self.powerUp = False
        self.level = level
        self.data = None
        self.index = index
        self.left = None
        self.right = None
    
    def isFull(self):
        if (self.left!=None and self.right!=None):
            return True
        else :
            return False

    def isEmpty(self):
        if (self.left==None and self.right==None):
            return True
        else :
            return False
    
    def addRoom(self, room):
        if (self.isEmpty()==True):
            temp = random.randint(0,1)
            if temp==0:
                self.left = room
            else:
                self.right = room
        elif self.left == None:
            self.left= room
        elif self.right == None:
            self.right = room
            

class Cave:
    def __init__(self):
        self.root = Room(0)
    

    def height(self):
        # Compute the height of each subtree
        lheight = self.height(self.root.left)
        rheight = self.height(self.root.right)

        # Use the larger one
        if lheight > rheight:
            return lheight+1
        else:
            return rheight+1
    
    def addRoomCave(self,index):
        queue = []
        queue.append(self.root)
        while len(queue) != 0:
            current = queue.pop(0)
            if current.isFull():
                queue.append(current.left)
                queue.append(current.right)
                
            else:
                current.addRoom(Room(current.level+1,index))
                print(current.level+1, end=" ")
                break

    def printRoom(self):
        queue = []
        queue.append(self.root)
        while len(queue) !=0:
            current = queue.pop(0)
            print(current.index , end = " ")
    
            # Enqueue left child
            if current.left is not None:
                queue.append(current.left)
    
            # Enqueue right child
            if current.right is not None:
                queue.append(current.right)
    

        


cave = Cave()
print("level: ",0,end=' ')
cave.addRoomCave(1)
cave.addRoomCave(2)
cave.addRoomCave(3)
cave.addRoomCave(4)
cave.addRoomCave(5)
cave.addRoomCave(6)
cave.addRoomCave(7)
cave.addRoomCave(8)
cave.addRoomCave(9)
print()
print("index: ",end=" ")
cave.printRoom()
