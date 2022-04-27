#!/usr/bin/python3
from abc import ABC, abstractmethod
class Human:
    def __init__(Self, name, age):
        Self.name=name
        Self.age=age
    
    def name(Self):
        return Self.name
    def age(Self):
        return Self.age
    @abstractmethod
    def education(Self):
        pass
person = Human("John", "18")
print(person)
print(person.education)
class student(Human):
    def __init__(Self, name, age, education):
        Self.name=name
        Self.age=age
        Self.education = education

    def name(Self):
        return Self.name
    def age(Self):
        return Self.age
    def education(Self):
        return ecucation
        
enjineer=student("James", "20", "bachelor")
print(enjineer.education)



