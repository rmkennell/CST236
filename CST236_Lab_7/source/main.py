from source.question_answer import QA
from source.shape_checker import get_triangle_type, get_quadrilateral_type
from source.math_questions import  fibonacci, pi, unitConvert, romanNumeralConversion, randomNumberRange
from source.demands import  dateTime, openDoor, dogsOut

import difflib
NOT_A_QUESTION_RETURN = "Was that a question?"
UNKNOWN_QUESTION = "I don't know, please provide the answer"
UNKNOWN_DEMAND = "I don't know how to do that"
NO_QUESTION = 'Please ask a question first'
NO_TEACH = 'I don\'t know about that. I was taught differently'
NOT_A_STRING = "Not A String!"


class Interface(object):
    def __init__(self):
        self.how_dict = {}
        self.what_dict = {}
        self.where_dict = {}
        self.who_dict = {}

        self.keywords = ['How', 'What', 'Where', 'Who', "Why"]
        self.question_mark = chr(0x3F)

        self.question_answers = {
            'What type of triangle is ': QA('What type of triangle is ', get_triangle_type),
            'What type of quadrilateral is ': QA('What type of quadrilateral is ', get_quadrilateral_type),
            'What is the digit of fibonacci?' : QA('What is the digit of fibonacci?', fibonacci),
            'What is the digit of pi?' : QA('What is the digit of pi?', pi),
            'What time is it?' : QA('What time is it', dateTime),
            'What is the date?' : QA('What si the date' , dateTime),
            'Open the door hal': QA('Open the door hal', openDoor),
            'Convert to ': QA('Convert to ', unitConvert),
            'Who let the dogs out?' : QA('Who let the dogs out', dogsOut),
            'Convert to number' : QA('Convert to number', romanNumeralConversion),
            'Give me a number between and ' : QA('Give me a number between and  ', randomNumberRange),

        }
        self.last_question = None

    def ask(self, question=""):
        if not isinstance(question, str):
            self.last_question = None
            return NOT_A_STRING
        if question[-1] != self.question_mark or question.split(' ')[0] not in self.keywords:
            self.last_question = None
            return NOT_A_QUESTION_RETURN
        else:
            parsed_question = ""
            args = []
            for keyword in question[:-1].split(' '):
                try:
                    args.append(float(keyword))
                except:
                    parsed_question += "{0} ".format(keyword)
            parsed_question = parsed_question[0:-1]
            self.last_question = parsed_question
            for answer in self.question_answers.values():
                if difflib.SequenceMatcher(a=answer.question, b=parsed_question).ratio() >= .90:
                    if answer.function is None:
                        return answer.value
                    else:
                        try:
                            return answer.function(*args)
                        except:
                            raise Exception("Too many extra parameters")
            else:
                return UNKNOWN_QUESTION

    def demand(self, question=""):
        if not isinstance(question, str):
            self.last_question = None
            return NOT_A_STRING
        else:
            parsed_question = ""
            args = []
            for keyword in question[:].split(' '):
                try:
                    args.append(float(keyword))
                except:
                    parsed_question += "{0} ".format(keyword)
            parsed_question = parsed_question[0:-1]
            self.last_question = parsed_question
            for answer in self.question_answers.values():
                if difflib.SequenceMatcher(a=answer.question, b=parsed_question).ratio() >= .90:
                    if answer.function is None:
                        return answer.value
                    else:
                        try:
                            return answer.function(*args)
                        except:
                            raise Exception("Too many extra parameters")
            else:
                return UNKNOWN_DEMAND


    def teach(self, answer=""):
        if self.last_question is None:
            return NO_QUESTION
        elif self.last_question in self.question_answers.keys():
            return NO_TEACH
        else:
            self.__add_answer(answer)

    def correct(self, answer=""):
        if self.last_question is None:
            return NO_QUESTION
        else:
            self.__add_answer(answer)

    def __add_answer(self, answer):
        self.question_answers[self.last_question] = QA(self.last_question, answer)

    def delete(self):
        self.question_answers = {}
        return "clear"

    def checkIfClear(self):
        if self.question_answers == {}:
            return "clear"
        return "Not Clear"
