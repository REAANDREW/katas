import unittest

class FizzBuzzPrinter:

    def __init__(self, output):
        self.output = output

    def print_to_output(self, number):
        result = self.fizz_buzz_print(number)
        self.output.print_to_output(result)

    def fizz_buzz_print(self, number):
        if number % 5 == 0 and number % 3 == 0:
            return 'FizzBuzz'

        if number % 5 == 0:
            return 'Buzz'

        if number % 3 == 0:
            return 'Fizz'

        return str(number)

class FizzBuzzGame:

    def __init__(self, printer):
        self.printer = printer

    def execute(self):
        for i in range(1,101):
            self.printer.print_to_output(i)

class TestOutputPrinter:

    def __init__(self):
        self.outputPrinted = None
        self.numberOfTimesPrintWasCalled = 0

    def print_to_output(self, data):
        self.outputPrinted = data
        self.numberOfTimesPrintWasCalled += 1

class TestFizzBuzz(unittest.TestCase):

    '''
    Write a program that prints the numbers from 1 to 100. But for multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz?".
    '''

    def testShouldReturnFizzWhenNumberIsDivisbleBy3(self):
        output = TestOutputPrinter()
        printer = FizzBuzzPrinter(output)
        number = 3
        result = printer.print_to_output(number)
        self.assertEquals('Fizz', output.outputPrinted)

    def testShouldReturnBuzzWhenNumberIsDivisibleBy5(self):
        output = TestOutputPrinter()
        printer = FizzBuzzPrinter(output)
        number = 5
        result = printer.print_to_output(number)
        self.assertEquals('Buzz', output.outputPrinted)

    def testShouldReturnFizzBuzzWhenNumberIsDivisibleBy3And5(self):
        output = TestOutputPrinter()
        printer = FizzBuzzPrinter(output)
        number = 15
        result = printer.print_to_output(number)
        self.assertEquals('FizzBuzz', output.outputPrinted)

    def testShouldReturnNumberWhenNumberIsNotDivisibleBy3Or5(self):
        output = TestOutputPrinter()
        printer = FizzBuzzPrinter(output)
        number = 7
        result = printer.print_to_output(number)
        self.assertEquals('7', output.outputPrinted)

    def testShouldPrintNumbersFrom1to100WithTheFizzBuzzRules(self):
        output = TestOutputPrinter()
        printer = FizzBuzzPrinter(output)
        game = FizzBuzzGame(printer)
        game.execute()
        self.assertEquals(100, output.numberOfTimesPrintWasCalled)

