from copy import deepcopy
from random import randint
from secrets import choice
from time import time

from sqlalchemy.orm import Session

from numbergame.models.level import Level
from numbergame.settings import engine


class LevelGenerator:
    def __init__(self):
        self.session = Session(engine)

    @staticmethod
    def generator(max_num: int):
        number_list = [randint(8, max_num) for _ in range(4)]
        number_list.append(randint(1, 9))
        number_list.append(randint(1, 9))
        print(number_list)
        tmp_list = deepcopy(number_list)
        result_list = []
        solution_list = []
        func_list = ["+", "-", "/", "*", "*", "*"]
        for num_steps in range(3):
            item1 = choice(tmp_list)
            tmp_list.remove(item1)
            item2 = choice(tmp_list)
            tmp_list.remove(item2)
            func = choice(func_list)
            func_list.remove(func)
            first_num = max(item1, item2)
            second_num = min(item1, item2)

            if func == "/" and first_num % second_num != 0:
                func = "+"
            equation = f"{first_num}{func}{second_num}"
            res = eval(equation)
            if res != 0:
                result_list.append(res)
                solution_list.append(f"{equation}={res}")
            else:
                result_list.append(first_num)
            print(equation, result_list, res)

        item1 = max(result_list)
        result_list.remove(item1)
        item2 = choice(result_list)
        result_list.remove(item2)
        first_num = max(item1, item2)
        second_num = min(item1, item2)
        func = choice(["+", "*", "-", "/", "*"])
        if func == "/" and first_num % second_num != 0:
            func = "+"
        equation = f"{first_num}{func}{second_num}"
        res = eval(equation)
        if 50 <= res <= 500:
            solution_list.append(f"{equation}={res}")
            if result_list:
                equation = f"{res}+{pow(-1, randint(1, 2)) * choice(result_list)}"
                res = eval(equation)
                solution_list.append(f"{equation}={res}")

        solution_list = [x.replace("--", "+").replace("+-", "-").replace(".0", "") for x in solution_list]
        return number_list, int(res), solution_list

    def start(self, num_levels: int = 100):
        n: int = 0
        while n < num_levels:
            list_numbers, goal, solution = self.generator(10)
            if 100 < goal < 500:
                new_level = Level()
                new_level.numbers = list_numbers
                new_level.goal = goal
                new_level.solution = solution
                self.session.add(new_level)
                self.session.commit()
                n += 1


lg = LevelGenerator()
lg.start()
