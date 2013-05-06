import unittest

class DigitTranslator:
    digit_1 = '     |  |'
    digit_2 = ' _  _||_ '
    digit_3 = ' _  _| _|'
    digit_4 = '   |_|  |'
    digit_5 = ' _ |_  _|'
    digit_6 = ' _ |_ |_|'
    digit_7 = ' _   |  |'
    digit_8 = ' _ |_||_|'
    digit_9 = ' _ |_| _|'

    def __init__(self):
        self.digits = dict()
        self.digits[DigitTranslator.digit_1] = 1
        self.digits[DigitTranslator.digit_2] = 2
        self.digits[DigitTranslator.digit_3] = 3
        self.digits[DigitTranslator.digit_4] = 4
        self.digits[DigitTranslator.digit_5] = 5
        self.digits[DigitTranslator.digit_6] = 6
        self.digits[DigitTranslator.digit_7] = 7
        self.digits[DigitTranslator.digit_8] = 8
        self.digits[DigitTranslator.digit_9] = 9

    def parse_digit(self, data):
        if data in self.digits:
            return self.digits[data]
        else:
            #This is not a requirement but not sure what else to use 
            #apart from an exception to ensure the test fails until it is correct
            return 1

class DigitParser:

    def parse_digits(self, data):
        lines = data.split('\n')
        data = []
        for i in range(3,28,3):
            digit = ''
            for line in range(0,3):
                for digitChar in range(i-3,i):
                    digit = digit + lines[line][digitChar]
            data.append(digit)
        return data


class AccountNumberParser:

    def __init__(self):
        self.digit_parser = DigitParser()
        self.digit_translator = DigitTranslator()

    def parse(self, data):
        digits = self.digit_parser.parse_digits(data)
        return int(''.join((str(self.digit_translator.parse_digit(x)) for x in digits)))

class TestKataBankOCR(unittest.TestCase):

    def setUp(self):
        self.input = "    _  _     _  _  _  _  _ \n" +\
                     "  | _| _||_||_ |_   ||_||_|\n" +\
                     "  ||_  _|  | _||_|  ||_| _|\n" +\
                     "                           \n"
        self.digit_translator = DigitTranslator()

    def testParseDigitPartOfInputString(self):
        digit_parser = DigitParser()
        expected = DigitTranslator.digit_1
        digits = digit_parser.parse_digits(self.input)
        self.assertEquals(expected, digits[0])

    def testShouldParseTheCorrectNumberOfDigits(self):
        digit_parser = DigitParser()
        expected_length = 9
        digits = digit_parser.parse_digits(self.input)
        self.assertEquals(expected_length, len(digits))

    def testShouldParseARepresentationOfa_1(self):
        expected = DigitTranslator.digit_1
        self.assertEquals(1, self.digit_translator.parse_digit(expected))

    def testShouldParseARepresentationOfa_2(self):
        expected = DigitTranslator.digit_2
        self.assertEquals(2, self.digit_translator.parse_digit(expected))

    def testShouldParseARepresentationOfa_3(self):
        expected = DigitTranslator.digit_3
        self.assertEquals(3, self.digit_translator.parse_digit(expected))

    def testShouldParseARepresentationOfa_4(self):
        expected = DigitTranslator.digit_4
        self.assertEquals(4, self.digit_translator.parse_digit(expected))

    def testShouldParseARepresentationOfa_5(self):
        expected = DigitTranslator.digit_5
        self.assertEqual(5, self.digit_translator.parse_digit(expected))

    def testShouldParseARepresentationOfa_6(self):
        expected = DigitTranslator.digit_6
        self.assertEquals(6, self.digit_translator.parse_digit(expected))

    def testShouldParseARepresentationOfa_7(self):
        expected = DigitTranslator.digit_7
        self.assertEquals(7, self.digit_translator.parse_digit(expected))

    def testShouldParseARepresentationOfa_8(self):
        expected = DigitTranslator.digit_8
        self.assertEquals(8, self.digit_translator.parse_digit(expected))

    def testShouldParseARepresentationOfa_9(self):
        expected = DigitTranslator.digit_9
        self.assertEquals(9, self.digit_translator.parse_digit(expected))

    def testShouldParsePipesAndUnderscoreCharactersIntoTheirIntendedNumericalValues(self):
        """
        Each entry is 4 lines long, and each line has 27 characters. The first 3 lines of each entry contain an account number written using pipes and underscores, and the fourth line is blank. Each account number should have 9 digits, all of which should be in the range 0-9. A normal file contains around 500 entries.
        """
        account_number_parser = AccountNumberParser()
        self.assertEquals(123456789, account_number_parser.parse(self.input))
