from enum import Enum

class QuestionOrder(Enum):
    increasing = 1
    decreasing = -1

    @staticmethod
    def values():
        return [(k.value, k.name) for k in QuestionOrder]


class Gender(Enum):
    male = 'Male'
    female = 'Female'

    @staticmethod
    def values():
        return [(k.value, k.name) for k in Gender]
