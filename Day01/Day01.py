import re
import os
from collections import OrderedDict

class Main:
    _sum = 0
    def __init__(self, input_data: list[str] = None, part: int = 1):
        self.part = part
        if input_data:
            self.input_data = input_data
        else:
            dir_path = os.path.dirname(os.path.abspath(__file__))
            with open(f"{dir_path}/input_data.txt") as f:
                self.input_data = f.read()


    def words_to_numbers(self, line):
        # this only applies to part 2
        if self.part == 2:
            
            str_map = {
                "one": 1,
                "two": 2,
                "three": 3,
                "four": 4,
                "five": 5,
                "six": 6,
                "seven": 7,
                "eight": 8,
                "nine": 9,

            }

            number_dict = {str(i): i for i in range(1, 10)}
            str_map.update(number_dict)
            print(str_map)
            data = {}
            for x in str_map.keys():
                for index in [i for i in range(len(line)) if line.startswith(x, i)]:
                    data[index] = x
            if len(data) >0:
                indexed = dict(sorted(data.items()))
                first_string_number = indexed[min(iter(indexed))]
                last_string_number = indexed[max(iter(indexed))]
                new_line = line.replace(first_string_number, str(str_map[first_string_number]), 1) # replace first number text
                new_line = new_line.replace(last_string_number, str(str_map[last_string_number]), -1) # replace last number text

                return new_line
            
        return line


    def get_result(self):
        self._sum = 0
        lines = self.input_data.split()
        for line in lines:
            line = self.words_to_numbers(line)
            numbers = re.findall(r"\d+", line)
            res = int(f"{str(numbers[0])[0]}{str(numbers[-1])[-1]}" )
            self._sum += res
        return self._sum
    
