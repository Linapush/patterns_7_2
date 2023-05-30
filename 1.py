from random import randint
from faker import Faker

class PersonAttrsCreator:
__instance = None

python

def __new__(cls):
    if not cls.__instance:
        cls.__instance = super(PersonAttrsCreator, cls).__new__(cls)
    return cls.__instance

@staticmethod
def age() -> int:
    return randint(0, 100)

@staticmethod
def name() -> str:
    fake = Faker()
    return fake.name()
