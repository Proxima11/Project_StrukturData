import random

class NodeQuestion:
    def __init__(self, question: str, answer_correct:str, answer2:str, answer3:str, answer4:str) -> None:
        self.answer = []
        self.question = question
        self.correct_answer = answer_correct
        self.count = 2
        self.answer.append(answer_correct)
        self.answer.append(answer2)
        if answer3 != "":
            self.answer.append(answer3)
            self.count+=1
        if answer4 != "":
            self.answer.append(answer4)
            self.count+=1
        self.correct = False
        self.isAnswered = False
        self.random_urutan_jawaban()
    
    def isCorrect(self, user_answer:str):
        if user_answer == self.correct_answer:
            self.correct = True
            return self.correct
        else:
            self.correct = False
            return self.correct
    
    def random_urutan_jawaban(self):
        for i in range(len(self.answer)):
            tukar = random.randint(0,len(self.answer)-1)
            self.answer[i], self.answer[tukar] = self.answer[tukar], self.answer[i]


class question:
    def __init__(self) -> None:
        self.arr_question = []
        self.add_all()

    def add_question(self, question: str, answer_correct:str, answer2:str, answer3:str, answer4:str):
        new_question = NodeQuestion(question, answer_correct, answer2, answer3, answer4)
        self.arr_question.append(new_question)
    
    def update_question(self, index:int):
        if index < len(self.arr_question):
            self.arr_question[index].isAnswered = True
    
    def add_all(self):
        self.add_question("Yang bukan istilah dalam Stack", "Rear", "IsFull", "Pop", "Push")#1
        self.add_question("Yang bukan istilah dalam Queue", "Pop", "Enqueue", "Dequeue", "IsFull")#2
        self.add_question("Kumpulan dari simpul dan busur disebut", "graph", "stack", "queue", "linked list")#3
        self.add_question("Jika sebuah undirected graph memiliki edge sebagai / berikut: (A,B), (B,C), (C,A), (D,E), (B,D) apakah graph / tersebut membentuk cycle graph?", "ya", "tidak", "", "")#4
        self.add_question("Istilah dalam graph jika ada sebuah edge yang ditulis / e = (v,w) dan w terletak pada e maka hal tersebut disebut", "incident", "outdegree", "degree", "adjacent")#5
        # self.add_question("Pada graph tak berarah, dua simpul disebut adjacent / ketika", "ada busur yang / menghubungkan kedua / simpul", "ada simpul yang / menghubungkan kedua / simpul", "tidak ada busur yang / menghubungkan kedua / simpul", "ada busur dan simpul / yang menghubungkan / kedua simpul")#6
        self.add_question("Beberapa algoritma yang dapat mencari shortest path / sebuah graph, kecuali", "max-sum", "warshall's algorithm", "MST", "djikstra algorithm")#7
        self.add_question("Penelusuran graph dengan mendahulukan arah kedalaman / disebut dengan", "DFS", "BFS", "Greedy", "Dynamic Programming")#8
        self.add_question("Dalam Single Linked List, ada tambahan data di dalam / node yang berfungsi untuk menyambungkan suatu node / dengan node lainnya agar tidak putus disebut", "pointer", "line", "number", "null")#9
        self.add_question("Kelebihan linked list daripada array adalah", "ukuran dinamis", "mudah dimengerti", "bisa mengakses index / langsung", "code sederhana")#10
        self.add_question("Fungsi atau prosedur yang dapat digunakan dalam sebuah / program disebut", "primitif", "abstrak", "kompleks", "variabel")#11
        self.add_question("Berikut adalah contoh tipe data sederhana tunggal, kecuali", "string", "integer", "boolean", "char")#12
        self.add_question("Ketika ada sebuah data set 3, 2, 1 dan dimasukkan ke / dalam stack secara berurutan namun menghasilkan hasil / ascending, berapakah jumlah dari stack melakukan fungsi push?", "6", "3", "2", "8")#13
        self.add_question("Double linked list memiliki 2 pointer, yaitu", "head & tail", "root & leaf", "top & bottom", "front & rear")#14
        self.add_question("Perintah yang tepat untuk menyatakan linked list yang / berada pada kondisi kosong adalah", "Head-Tail-Null", "Branch-Null", "Tail-Null", "Root-Null")#15
        self.add_question("Beikut ini adalah istilah umum dalam tree, kecuali", "Weight", "Level", "Leaf", "Root")#16
        self.add_question("Node yang mempunyai level sama pada tree disebut", "Sibling", "Parent", "Child", "Line")#17
        self.add_question("Tree yang pada tiap node nya memiliki 2 cabang saja disebut", "binary tree", "normal tree", "not tree", "graph tree")#18
        self.add_question("Simpul yang tidak mempunyai subordinat atau simpul yang / derajat masuknya = 1 dan keluarnya = 0 adalah", "Leaf", "Root", "Child", "Parent")#19
        self.add_question("Node yang berada di bawah node tertentu disebut juga dengan", "Successor", "Prodecessor", " Ancestor", "Descendant")#20
        self.add_question("Suatu kelompok data yang dapat dikarakteristikan oleh / organisasi serta operasi adalah", "Struktur data", "Kolom data", "Pengaturan data", "Tipe data")#21
        self.add_question("Struktur data standar yang digunakan dibawah ini adalah, kecuali", "Stuck", "Graph", "Queue", "Tree")#22
        self.add_question("Berapa macam Linked List", "2", "1", "3", "4")#23
        self.add_question("Prinsip kerja dari queue adalah", "last in last out", "first in last out", "sama dengan stack", "last in first out")#24
        self.add_question("Antrean yang dimanfaatkan berdasarkan kepentingan / penggunanya, disebut dengan", "priority queue", "performance queue", "input restricted queue", "output restricted queue")#25
        self.add_question("Apabila ada satu data yang keluar dari dalam queue, / maka posisi yang berubah adalah indikator (pointer)", "FRONT", "TOP", "BOTTOM", "REAR")#26
        self.add_question("Jika Suatu pohon binner memiliki simpul sebanyak 5, / maka ruasnya jumlahnya", "5", "4", "7", "6")#27
        self.add_question("Untuk menambahkan item pada posisi paling atas pada / stack adalah", "PUSH", "POP", "CLEAR", "ISFULL")#28
        self.add_question("Berapa macam Linked Listika pada stack terdapat kondisi / TOP of STACK = MAX_STACK - 1, maka stack berada dalam keadaan", "FULL", "Empty", "Half Empty", "ALMOST FULL")#29
        self.add_question("Jika saat ini elemen dalam sebuah antrian QUEUE adalah / B G F R T, dan diberikan operasi Dequeue(), Enqueue('P'), / Enqueue('H'), Dequeue(), Dequeue(). Maka elemen antrian / saat ini adalah", "(R T P H)", "(R T P)", "(T P H)", "(G F R T P H)")#30
        self.add_question("Jika saat ini elemen dalam sebuah antrian QUEUE adalah / A D C F I, dan diberikan operasi Enqueue('Z'), Dequeue(), / Enqueue('A'), Dequeue(), Dequeue(), Dequeue(). Maka elemen / antrian saat ini adalah", "(I Z A)", "(C F I Z A)", "()", "(Z)")#31
        self.add_question("Jika saat ini elemen dalam sebuah antrian QUEUE adalah / Z X W A, dan diberikan operasi Dequeue(), Dequeue(), / Enqueue('A'), Dequeue(), Dequeue(), Dequeue(). Maka elemen / antrian saat ini adalah", "()", "(A A)", "(A)", "(W A A)")#32
        self.add_question("Jika saat ini elemen dalam sebuah antrian QUEUE adalah / R S T N B, dan diberikan operasi Dequeue(), Dequeue(), / Enqueue('G'), Dequeue(), Enqueue('J), Enqueue('L). Maka / elemen antrian saat ini adalah", "(N B G J L)", "(B J)", "(B G J L)", "(T B L)")#33
        self.add_question("Untuk menambahkan item pada posisi paling belakang dalam / queue dilakukan", "Enqueue", "Dequeue", "Push", "Pop")#34
        self.add_question("Banyaknya simpul dari Graph dinamakan", "Order", "Size", "Vertex", "Ruas")#35
        self.add_question("Banyaknya ruas dari Graph dinamakan", "Size", "Ruas", "Vertex", "Order")#36
        self.add_question("Alur jalan mencetak isi node yang dikunjungi lalu melakukan / kunjungan ke subtree kiri dan selanjutnya ke subtree kanan disebut", "Preorder", "Lastorder", "Postorder", "Inorder")#37        
        self.add_question("Berat sebuah pohon biner adalah", "banyaknya daun", "banyaknya simpul", "tinggi left substree-nya", "tinggi right substree-nya")#38
        self.add_question("Struktur data apakah yang digunakan dalam proses hashing / untuk menyimpan informasi dalam waktu berkala", "Hash table", "1D Array", "2D Array", "Linked List")#39
        self.add_question("Hash table T memiliki 25 slot dan menyimpan 2000 element, / load factor α untuk T adalah", "80", "8000", "1.25", "0.0125")#40
        self.add_question("Hashing function pada memiliki beberapa macam, salah satunya", "Folding by shifting", "Folding by number", "Folding by block", "Folding by sorting")#41
        self.add_question("istilah dari hash table yang mencegah agar hanya dapat / ditempati maksimum oleh n record disebut", "blocking factor", "interrupt", "linked address", "record")#42
        self.add_question("Jika saat ini elemen dalam sebuah STACK adalah Y(top) H B C, / dan diberikan operasi pop(), push('V'), pop(), / pop(), push('O'), pop(). Maka elemen dalam stack saat ini adalah", "(B C)", "(H B C)", "(C)", "(O B C)")#43
        self.add_question("Jika saat ini elemen dalam sebuah STACK adalah X(top) U E, / dan diberikan operasi push('T'), push('V'), pop(), /  pop(), push('O'), pop(). Maka elemen dalam stack saat ini adalah", "(O X U E)", "(X U E)", "(V X U E)", "(U E)")#44
        self.add_question("Susunan preorder sebuah tranversal tree adalah 30, 20, 10, / 15, 25, 23, 39, 35, 42. Apakah susunan postorder /  tree yang sama?", "15, 10, 23, 25, 20, 35, 42, 39, 30", "10, 20, 15, 23, 25, 35, 42, 39, 30", "15, 10, 25, 23, 20, 42, 35, 39, 30", "15, 20, 10, 23, 25, 42, 35, 39, 30")#45
        self.add_question("Berapakah maksimum node dalam binary search tree dengan / height = 5?", "2^6-1", "2^5-1", "2^5", "2^6")#46
        self.add_question("Apakah Breadth-First-Search menggunakan stack atau dan queue?", "Queue saja", "Stack saja", "Keduanya", "Tidak keduanya")#47
        self.add_question("Tree yang balance memiliki jumlah item yang sama pada tiap / subtree", "Benar", "Salah", "", "")#48
        self.add_question("Metode transversal tree manakah yang digunakan untuk output / isi dari binary tree secara ascending?", "In-order", "Pre-order", "Post-order", "Monastic Orders")#49
        self.add_question("Sebuah tree terdiri dari ..... yang terhubung dengan garis", "Node", "Root", "Leaf", "Fruit")#50


# list_question = question()
# for i in range(len(list_question.arr_question)):
#     print(list_question.arr_question[i].answer)
