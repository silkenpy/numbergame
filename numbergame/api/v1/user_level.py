import json
import re
from copy import deepcopy
from random import randint
from secrets import choice
from typing import List

import falcon

from numbergame.models.level import Level
from numbergame.models.users import User


class UserLevels(object):
    @staticmethod
    def check(list_numbers: List, goal: int, solution: List[str]) -> bool:
        solution = [step.split("=")[0] for step in solution]
        print(solution)
        for step in solution:
            matched = re.match("\d+[+*/-]\d+", step)

            if not matched:
                return False

            for func in ["+", "-", "*", "/"]:
                parts = step.split(func)
                if len(parts) == 2:
                    first_num, second_num = parts
                    if int(first_num) not in list_numbers or int(second_num) not in list_numbers:
                        return False

                    res = eval(step)
                    if not isinstance(res, int):
                        return False

                    if res == goal:
                        return True

                    list_numbers.remove(int(first_num))
                    list_numbers.remove(int(second_num))
                    list_numbers.append(res)
                    break
        return False

    def on_post(self, req, resp):
        data = json.loads(req.bounded_stream.read())
        user = self.session.query(User).filter(User.uuid == data["uuid"]).first()
        if user:
            level = self.session.query(Level) \
                .filter(Level.id == data["level"]) \
                .first()
            if level:
                done = self.check(level.numbers, level.goal, data["solution"])
                if done:
                    user.completed = list(user.completed)
                    if level.id not in user.completed:
                        user.completed.append(level.id)
                        self.session.add(user)
                        self.session.commit()

                    resp.status = falcon.HTTP_200
                    return
        resp.status = falcon.HTTP_404
