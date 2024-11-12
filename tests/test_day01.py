from unittest import TestCase
from Day01.Day01 import Main

class TestDay01(TestCase):


    def test_result(self):
        main = Main(input_data = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet""")
        assert main.get_result() == 142

    def test_with_real_data(self):
        main = Main()
        print(main.get_result())
        assert main.get_result() == 55621

    def test_part2(self):
        main = Main(input_data="""two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen""",part=2)
        assert main.get_result() == 281

    def test_with_real_data_part2(self):
        main = Main(part=2)
        print(main.get_result())
        assert main.get_result() == 53592
