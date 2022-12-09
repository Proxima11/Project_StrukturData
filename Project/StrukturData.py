import random

class Room:
    def __init__(self, level, index=0):
        self.treasure = False
        self.indexQuestion = random.randint(0,99)                   #100 question
        self.powerUp = False
        self.level = level
        self.data = None
        self.index = index
        self.locked = True
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
        if self.left == None:
            self.left= room
        elif self.right == None:
            self.right = room
            

class Cave:
    def __init__(self):
        self.root = Room(0,0)
        self.root.locked = False
        self.size = 1
    

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
                self.size +=1
                break

    def addTreasure(self):
        queue = []
        queue.append(self.root)
        current = None
        index = random.randint(0,self.size-1)
        count = 0
        while len(queue) != 0:
            current = queue.pop(0)
            
            if current.left != None:
                queue.append(current.left)

            if current.right != None:
                queue.append(current.right)
            
            if count==index:
                current.treasure= True
                print()
                print(current.index,"->", current.level)
                break
            count +=1
            

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
        print()
    