class BaseClass:

    def __init__(self, text: str):
        self.text = text

    def __str__(self):
        return "question with text:" + self.text


class ChoiceQuestions(BaseClass):

    def __init__(self,text: str, answer: list ,rightone: int):
        super (ChoiceQuestions, self). __init__(text)
        self.answer = answer
        self.rightone = rightone


class MultipleQuestions(BaseClass):

    def __init__(self, text: str, answer: list ,rightanswers: list):
        super (MultipleQuestions, self). __init__(text)
        self.answer = answer
        self.rightanswers = rightanswers


class QuestionList:

    def __init__(self,title: str, questions):
        self.title = title
        self.questions = questions









