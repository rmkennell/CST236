from source.main import Interface
from unittest import TestCase
from test.plugins.ReqTracer import story
from source.math_questions import  unitConvert, conversionVariations, pi, fibonacci, romanNumeralConversion, checkLegalAge, randomNumberRange
import time
import getpass
from source.demands import contactLookup, phoneLookup
import sys


def output_to_file(question, result):
    start_time = time.time()
    f = open('output.txt', 'a+')
    f.write("Question: {0}"  .format(question) )
    f.write("\n")
    f.write("Result: {0}"  .format(result) )
    f.write("\n")
    end_time = (time.time() - start_time)
    f.write("Output time: {}" .format(end_time))
    f.write("\n \n")
    f.close()


class TestQuestionAnswer(TestCase):

    @story('When I ask "What time is it?" I want to be given the current date/time so I can stay up to date')
    def test_ask_what_time(self):
        obj = Interface()
        question = 'What time is it?'
        result = obj.ask(question)
        output_to_file(question, result)
        self.assertEqual(result, time.strftime("%c"))


    @story('When I ask "What is the n digit of fibonacci" I want to receive the answer so I don\'t have to figure it out myself')
    def test_ask_fibonacci(self):
        obj = Interface()
        question = 'What is the 4 digit of fibonacci?'
        result = obj.ask(question)
        output_to_file(question, result)
        self.assertEqual(result, 3)


    def test_ask_fibonacci_2(self):
        obj = Interface()
        question = 'What is the 5 digit of fibonacci?'
        result = obj.ask(question)
        output_to_file(question, result)
        self.assertEqual(result, 5)

    def test_ask_fibonacci_invalid_int(self):
        obj = Interface()
        question = 'What is the -6 digit of fibonacci?'
        result = obj.ask(question)
        output_to_file(question, result)
        self.assertEqual(result, 'invalid')

    def test_fibonacci_invalid_string(self):
        result = fibonacci("a")
        self.assertEqual(result, 'invalid')

    @story('When I ask "What is the n digit of pi" I want to receive the answer so I don\'t have to figure it out myself')
    def test_ask_pi(self):
        obj = Interface()
        question = 'What is the 6 digit of pi?'
        result = obj.ask(question)
        output_to_file(question, result)
        self.assertEqual(result, 5)


    def test_ask_pi_invalid_int(self):
        obj = Interface()
        question = 'What is the -6 digit of pi?'
        result = obj.ask(question)
        output_to_file(question, result)
        self.assertEqual(result, 'invalid')

    def test_pi_invalid_string(self):
        result = pi("a")
        self.assertEqual(result, 'invalid')

    @story('When I ask "Please clear memory" I was the application to clear user set questions and answers so I can reset the application')
    def test_ask_clear_memory(self):
        obj = Interface()
        result = obj.delete()
        self.assertEqual(result, obj.checkIfClear())

    def test_ask_check_if_memory_clearedfalse(self):
        obj = Interface()
        self.assertEqual(obj.checkIfClear(), "Not Clear")


    @story('When I say "Open the door hal", I want the application to say "I\'m afraid I can\'t do that <user name> so I know that is not an option')
    def test_ask_open_door(self):
        obj = Interface()
        question = 'Open the door hal'
        result = obj.demand(question)
        output_to_file(question, result)
        self.assertEqual(result, 'I\'m afraid I can\'t do that ' + getpass.getuser())


    @story('When I ask "Convert <number> <units> to <units>" I want to receive the converted value and units so I can know the answer.')
    def test_ask_convert_units_km_to_cm(self):
        result = unitConvert(5, 'km', 'm')
        self.assertEqual(result, 5000)

    def test_ask_convert_units_km_to_mi(self):
        result = unitConvert(5, 'km', 'mi')
        self.assertEqual(result, 3.11)

    def test_ask_convert_units_m_to_in(self):
        result = unitConvert(3, 'm', 'in')
        self.assertEqual(result, 118.11)

    def test_ask_convert_units_yd_to_in(self):
        obj = Interface()
        result = unitConvert(2, 'yd', 'in')
        self.assertEqual(result, 72)

    def test_ask_convert_units_ft_to_cm(self):
        obj = Interface()
        result = unitConvert(2, 'ft', 'cm')
        self.assertEqual(result, 60.96)

    def test_ask_convert_units_mm_to_nm(self):
        obj = Interface()
        result = unitConvert(5, 'mm', 'nm')
        self.assertEqual(result, 5000000)


    @story('When I ask for a numberic conversion I want at least 10 different units I can convert from/to.')
    def test_ask_numberic_conversion(self):
        obj = Interface()
        result = conversionVariations()
        self.assertEqual(result, 'nm, mm, cm, m, km, in, ft, yd, mi')


    @story('When I ask "What is the date?" I want to be given the current date/time so I can stay up to date')
    def test_ask_what_date(self):
        obj = Interface()
        question = 'What is the date?'
        result = obj.ask(question)
        output_to_file(question, result)
        self.assertEqual(result, time.strftime("%c"))


    @story('When I ask "Who let the dogs out?" I want the application to say "<user name> let the dogs out" so I know that who did it')
    def test_ask_who_let_dogs_out(self):
        obj = Interface()
        question = 'Who let the dogs out?'
        result = obj.ask(question)
        output_to_file(question, result)

        self.assertEqual(result, getpass.getuser() + ' let the dogs out')




    @story('When I ask "Convert <roman numeral> to number" I want to recieve the converted value so I know what year Super Bowl it is.')
    def test_convert_roman_num_to_number1(self):
        result = romanNumeralConversion('CMIX')
        self.assertEqual(result, 909)

    def test_convert_roman_num_to_number2(self):
        result = romanNumeralConversion('CDIV')
        self.assertEqual(result, 404)

    def test_convert_roman_num_to_number3(self):
        result = romanNumeralConversion('XCXL')
        self.assertEqual(result, 130)

    def test_convert_roman_num_invalid(self):
        result = romanNumeralConversion('ABC')
        self.assertEqual(result, 'Invalid input')

    @story('When I give a date, I want the system to return whether somebody born on that date is legal to drive')
    def test_legal_age_checker_not_legal(self):
        question = '2012-02-10'
        result = checkLegalAge(question)
        output_to_file(question, result)
        self.assertEqual(result, 'Not legal to drive')

    def test_legal_age_checker_legal(self):
        question = '1980-01-01'
        result = checkLegalAge(question)
        output_to_file(question, result)
        self.assertEqual(result, 'Legal to drive')

    def test_legal_age_checker_invalid(self):
        result = checkLegalAge('2020-01-01')
        self.assertEqual(result, 'Invalid')

    @story('When I say "Give me a random number between <int> and <int>" the system will return a random number in that range so I dont need a die for a game')
    def test_random_number_range_greater(self):
        obj = Interface()
        question  = 'Give me a number between 1 and 6'
        result = obj.demand(question)
        output_to_file(question, result)
        self.assertGreaterEqual(result, 1)

    def test_random_number_range_less(self):
        obj = Interface()
        question = 'Give me a number between 1 and 10'
        result = obj.demand(question)
        output_to_file(question, result)
        self.assertLessEqual(result, 10)

    def test_random_number_range_invalid(self):
        obj = Interface()
        question = 'Give me a number between 10 and 10'
        result = obj.demand(question)
        output_to_file(question, result)
        self.assertLessEqual(result, "Invalid range")

    @story('When I ask "What is the phone number of <name> I want to be given their phone number so I can call them')
    def test_contact_lookup(self):
        question = 'Jason'
        result = contactLookup(question)
        output_to_file(question, result)
        self.assertEqual(result, '971-359-7954')

    def test_contact_no_contact(self):
        question = 'Bob'
        result = contactLookup(question)
        output_to_file(question, result)
        self.assertEqual(result, 'No contact for Bob')

    def test_contact_invalid_input(self):
        result = contactLookup(5)
        self.assertEqual(result, 'Invalid input')

    @story('When I ask "Whose phone number is <phoneNumber> I want to be given their name so I know who has been prank calling me')
    def test_phone_number_lookup(self):
        question = '503-879-6375'
        result = phoneLookup(question)
        output_to_file(question, result)
        self.assertEqual(result, 'Thomas')

    def test_phone_number_invalid(self):
        question = '503-879-0000'
        result = phoneLookup(question)
        output_to_file(question, result)
        self.assertEqual(result, 'No name for 503-879-0000')

    def test_phone_number_invalid_input(self):
        result = phoneLookup(1)
        self.assertEqual(result, 'Invalid input')
