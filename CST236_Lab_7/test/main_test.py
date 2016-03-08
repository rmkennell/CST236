from source.main import Interface
from unittest import TestCase
from test.plugins.ReqTracer import requirements
from source.shape_checker import get_triangle_type, get_quadrilateral_type, get_quadrilateral_point_type

import sys


class TestGetShapes(TestCase):


    # Testing Question Validity

    # 0007 The system shall answer questions that begin with one of the following valid question keywords: "How", "What", "Where", "Why" and "Who"

    # what
    @requirements(['#0001', '#0002', '#0006', '#0007', '#0010', '#0013'])
    def test_ask_triangle_isosceles_what(self):
        obj = Interface()
        result = obj.ask('What type of triangle is 5.5 2 5.5?')
        self.assertEqual(result, 'isosceles')

    @requirements(['#0001', '#0002', '#0006', '#0007', '#0010', '#0013'])
    def test_ask_triangle_invalid_shape_what(self):
        obj = Interface()
        result = obj.ask('What type of triangle is -10 2 5.5?')
        self.assertEqual(result, 'invalid')

    # who
    @requirements(['#0006', '#0007', '#0010', '#0014'])
    def test_ask_valid_question_who(self):
        obj = Interface()
        result = obj.ask('Who is the president of the USA?')
        self.assertEqual(result, 'I don\'t know, please provide the answer')

    # where
    @requirements(['#0006', '#0007', '#0010', '#0014'])
    def test_ask_valid_question_where(self):
        obj = Interface()
        result = obj.ask('Where did they go?')
        self.assertEqual(result, 'I don\'t know, please provide the answer')

    # why
    @requirements(['#0006', '#0007', '#0010', '#0014'])
    def test_ask_valid_question_why(self):
        obj = Interface()
        result = obj.ask('Why did they let the dogs out?')
        self.assertEqual(result, 'I don\'t know, please provide the answer')

    # how
    @requirements(['#0006', '#0007', '#0010', '#0014' ])
    def test_ask_valid_question_how(self):
        obj = Interface()
        result = obj.ask('How did the dogs get out?')
        self.assertEqual(result, 'I don\'t know, please provide the answer')



    # 0008 If the system does not detect a valid question keyword it shall return "Was that a question?"
    @requirements(['#0006', '#0008', '#0010'])
    def test_ask_invalid_when(self):
        obj = Interface()
        result = obj.ask('When were the dogs let out?')
        self.assertEqual(result, 'Was that a question?')

    #0009 If the system does not detect a question mark at end of the string it shall return "Was that a question?"
    @requirements(['#0006', '#0008', '#0009', '#0010'])
    def test_ask_invalid_punctuation(self):
        obj = Interface()
        result = obj.ask('Find my dogs')
        self.assertEqual(result, 'Was that a question?')


    # Determining Answers

    #0010 The system shall break a question down into words separated by space
    @requirements(['#0006', '#0007', '#0008', '#0009', '#0010', '#0014'])
    def test_ask_invalid_spacing(self):
        obj = Interface()
        result = obj.ask('Whowas the first president of the USA?')
        self.assertEqual(result, 'Was that a question?')

    #0011 The system shall determine an answer to a question as a correct if the keywords provide a 90% match and return the answer
    @requirements(['#0001', '#0002', '#0006', '#0007', '#0010', '#0011', '#0013'])
    def test_ask_triangle_percentage(self):
        obj = Interface()
        result = obj.ask('What type of triangle 4 3 5?')
        self.assertEqual(result, 'scalene')

    #0012 The system shall exclude any number value from match code and provide the values to generator function (if one exists)
    @requirements(['#0001', '#0002', '#0006', '#0007', '#0010', '#0011', '#0012', '#0013'])
    def test_ask_triangle_number_match(self):
        obj = Interface()
        result = obj.ask('What 5 type 5 of triangle 5 is?')
        self.assertEqual(result, 'equilateral')


    # Providing Answers

    #0015 The system shall provide a means of providing an answer to the previously asked question.
    @requirements(['#0006', '#0007', '#0010', '#0015', '#0016'])
    def test_ask_teach_provide_answer(self):
        obj = Interface()
        obj.ask('Who let the dogs out, yesterday?')
        obj.teach('James let the dogs out')
        result = obj.ask('Who let the dogs out, yesterday?')
        self.assertEqual(result, 'James let the dogs out')


    #0016 The system shall accept and store answers to previous questions in the form of a string or a function pointer and store it as the generator function.
    @requirements(['#0006', '#0007', '#0010', '#0012', '#0013', '#0015', '#0016'])
    def test_ask_store_previous_answer(self):
        obj = Interface()
        obj.ask('What t o t is 5 5 5?')
        obj.teach(get_triangle_type)
        result = obj.ask('What type of triangle is 5 5 5?')
        self.assertEqual(result, 'equilateral')

    #0017 If no previous question has been asked the system shall respond with "Please ask a question first"
    @requirements(['#0006', '#0017'])
    def test_ask_no_previous_question(self):
        obj = Interface()
        result = obj.teach('hello')
        self.assertEqual(result, 'Please ask a question first')

    #0018 If an attempt is made to provide an answer to an already answered question the system shall respond with "I don\'t know about that. I was taught differently" and not update the question
    @requirements(['#0006', '#0007', '#0010', '#0015', '#0016', '#0018'])
    def test_teach_modify_answer(self):
        obj = Interface()
        obj.ask('What color is the sky?')
        obj.teach('The sky is blue')
        result = obj.teach('The sky is green')
        self.assertEqual(result, 'I don\'t know about that. I was taught differently')

    @requirements(['#0006', '#0007', '#0010', '#0015', '#0016', '#0018'])
    def test_teach_same_answer(self):
        obj = Interface()
        obj.ask('What color is the sky?')
        obj.teach('The sky is blue')
        result = obj.teach('The sky is blue')
        self.assertEqual(result, 'I don\'t know about that. I was taught differently')


    # Correcting Answers

    #0019 The system shall provide a means of updating an answer to the previously asked question.
    @requirements(['#0006', '#0007', '#0010', '#0015', '#0016', '#0019'])
    def test_provide_answer_corrected(self):
        obj = Interface()
        obj.ask('What color is the sky?')
        obj.teach('The sky is blue')
        obj.correct('The sky is a multitude of colors typically ranging from turquoise to indigo')
        result = obj.ask('What color is the sky?')
        self.assertEqual(result, 'The sky is a multitude of colors typically ranging from turquoise to indigo')

    #0020 The system shall accept and store answers to previous questions in the form of a string or a function pointer and store it as the generator function.
    @requirements(['#0006', '#0007', '#0010', '#0015', '#0016', '#0020'])
    def test_provide_answer_corrected_strings(self):
        obj = Interface()
        obj.ask('Why did ancient egyptians build the pyramids?')
        obj.teach('To honor their royalty in tombs')
        obj.correct('Aliens')
        result = obj.ask('Why did ancient egyptians build the pyramids?')
        self.assertEqual(result, 'Aliens')

    @requirements(['#0003', '#0006', '#0007', '#0010', '#0015', '#0016', '#0020'])
    def test_provide_answer_corrected_fptr(self):
        obj = Interface()
        obj.ask('What shape is 2 5 2 5?')
        obj.teach(get_triangle_type)
        obj.correct(get_quadrilateral_type)
        result = obj.ask('What shape is 2 5 2 5?')
        self.assertEqual(result, 'rectangle')

    #0021 If no previous question has been asked the system shall respond with "Please ask a question first"
    @requirements(['#0006', '#0007', '#0010', '#0013', '#0016', '#0017', '#0021'])
    def test_correct_no_previous_question(self):
        obj = Interface()
        result = obj.correct('9-11, inside job')
        self.assertEqual(result, 'Please ask a question first')

    # main.py tests
    def test_ask_invalid_string(self):
        obj = Interface()
        result = obj.ask(5)
        self.assertEqual(result, 'Not A String!')

    def test_demand_invalid_string(self):
        obj = Interface()
        result = obj.demand(2)
        self.assertEqual(result, 'Not A String!')

    def test_demand_unknown(self):
        obj = Interface()
        result = obj.demand('Give me a soda')
        self.assertEqual(result, 'I don\'t know how to do that')



