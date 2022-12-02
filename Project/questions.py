class NodeQuestion:
    def __init__(self, question: str, answer:str) -> None:
        self.isAnswered : bool
        self.question = question
        self.answer = answer
        self.isAnswered = False

class question:
    arr_question = []

    def add_question(self, question: str, answer:str):
        new_question : NodeQuestion
        new_question = NodeQuestion(question, answer)
        self.arr_question.append(new_question)
    
    def update_question(self, index:int):
        if index < len(self.arr_question):
            self.arr_question[index].isAnswered = True
    
