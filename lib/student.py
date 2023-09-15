#!/usr/bin/env python

from user import User

class Student(User):
    
    # initialize attributes
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = []
    
    def learn(self, knowledge_str):
        self.knowledge.append(knowledge_str)