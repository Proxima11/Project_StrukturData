import random
from questions import NodeQuestion
from questions import question

class Room:
    def __init__(self, level, index=0, previous= None):
        self.treasure = False
        self.Question : NodeQuestion
        self.Question = None
        self.powerUp = False
        self.powerUptype = 0
        self.level = level
        self.data = None
        self.index = index
        self.locked = True
        self.left = None
        self.right = None
        self.previous = previous
    
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
        self.root = Room(0,0)
        self.listquest = question()
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
                temp = random.randint(0,1)
                if temp==0:
                    queue.append(current.left)
                else:
                    queue.append(current.right)
            else:
                current.addRoom(Room(current.level+1,index, current))
                self.size +=1
                break

    def addTreasure(self):
        queue = []
        queue.append(self.root)
        current = None
        index = random.randint(31,self.size-1)
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
        print('room  :  ')
        while len(queue) !=0:
            current = queue.pop(0)
            print(current.index ,end = "  ->  ")
            if current.previous is None:
                print(-1)
            else:
                print(current.previous.index)
    
            # Enqueue left child
            if current.left is not None:
                queue.append(current.left)
    
            # Enqueue right child
            if current.right is not None:
                queue.append(current.right)


    def addQuestion(self):
        queue = []
        visited = []
        not_visited = []
        for i in range(len(self.listquest.arr_question)):
            not_visited.append(self.listquest.arr_question[i])
        queue.append(self.root.left)
        queue.append(self.root.right)
        current = None
        #bfs
        while len(queue) != 0:
            current = queue.pop(0)
            #ketika sudah semua pertanyaan terpakai maka diulangi kembali
            if len(visited) == len(self.listquest.arr_question):
                while len(visited) != 0:
                    not_visited.append(visited.pop(0))
            #isi dengan pertanyaan
            if current.Question is None:
                random_index = random.randint(0,len(not_visited)-1)
                if not_visited[random_index] not in visited:
                    current.Question = not_visited[random_index]
                    visited.append(not_visited[random_index])
                    del not_visited[random_index]
            #append child kiri jika ada
            if current.left is not None:
                queue.append(current.left)
            #append child kanan jika ada
            if current.right is not None:
                queue.append(current.right)

    def addPowerUp(self):
        # print('index room power up: ')
        current = self.root
        self.__addpowerup(current)
        print()

    def __addpowerup(self, current):
        if current is None:
            return

        random1 = random.randint(1,4)
        random2 = random.randint(1,4)
        # print(random1," ", random2)
        if random1 == random2:
            if current != self.root and current.treasure is False:
                current.powerUp = True
                randompower = random.randint(1,4)
                current.powerUptype = randompower
                print(current.index, end=' ')
        
        self.__addpowerup(current.left)
        self.__addpowerup(current.right)

    def poweruproot(self, current):
        queue = []
        queue.append(current)
        while len(queue) !=0:
            current = queue.pop(0)

            if current.treasure:
                return True

            # Enqueue left child
            if current.left is not None:
                queue.append(current.left)
    
            # Enqueue right child
            if current.right is not None:
                queue.append(current.right)
        return False
        # return self.__checkroot(current)

    # def __checkroot(self, current):
    #     if current is None:
    #         return

    #     if current.treasure is True:
    #         return True
        
    #     self.__checkroot(current.left)
    #     self.__checkroot(current.right)
    #     return False

    def poweruplevel(self) -> int:
        # current = self.root
        # return self.__searchlevel(current)
        queue = []
        queue.append(self.root)
        print('room  :  ')
        while len(queue) !=0:
            current = queue.pop(0)

            if current.treasure:
                return current.level

            # Enqueue left child
            if current.left is not None:
                queue.append(current.left)
    
            # Enqueue right child
            if current.right is not None:
                queue.append(current.right)
        return -1

    # def __searchlevel(self, current):
    #     if current is None:
    #         return

    #     if current.treasure is True:
    #         return current.level
        
    #     self.__searchlevel(current.left)
    #     self.__searchlevel(current.right)
    #     if
    #     return 0

    def poweruphint(self):
        pass

    def isAllAnswered(self):
        queue = []
        allAnswered = True
        queue.append(self.root.left)
        queue.append(self.root.right)
        while len(queue) != 0:
            current = queue.pop(0)
            if current.Question.isAnswered == False:
                allAnswered = False
                break
            if current.left is None:
                return 0
            else:
                queue.append(current.left)
            if current.right is None:
                return 0
            else:
                queue.append(current.right)
        return allAnswered