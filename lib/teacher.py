#!/usr/bin/env python

from user import User

import random

# define the list of knowledge for the teachers
knowledge = [
    "str is a data type in Python",
    "programming is hard, but it's worth it",
    "JavaScript async web request",
    "Python function call definition",
    "object-oriented teacher instance",
    "programming computers hacking learning terminal",
    "pipenv install pipenv shell",
    "pytest -x flag to fail fast",
]

class Teacher(User):
    
    # initialize variables
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = knowledge

    def teach(self):
        
        # get a random integer
        random_index = random.randint(0, len(self.knowledge))
        
        # return the knowledge at that index
        return self.knowledge[random_index]