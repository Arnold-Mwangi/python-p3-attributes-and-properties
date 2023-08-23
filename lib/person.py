#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]
BREEDS=["Mastif", "Chihuahua", "Corgi", "Shar Pei", "Beagle", "FRench Bulldog", "Pug", "Pointer"]

class Person:
    def __init__(self, name="Grace", job="ITC"):
        self._name = name
        self._job = job

    def get_name(self):
        print("Retrieving name")
        return self._name

    def get_job(self):
        print("Retrieving job")
        return self._job

    def set_name(self, name_value):
        if not isinstance(name_value, str) and (1 <= len(str(name_value)) <25):
            print( "Name must be string under 25 characters.")
        else:
            print(F"SETTING NAME TO {name_value}")
            self._name = name_value.title()
    name = property(get_name, set_name)

    def set_job(self, job_name):
        if job_name not in APPROVED_JOBS:
            print("Job must be in list of approved jobs.")
        else:
            print(f"Setting Job to: {job_name}")
            self._job = job_name
    job = property(get_job, set_job)



p1 = Person("Arnoh","ITC")
p1.name ="DEDEDEDEDEDEDE"
print(p1.name)

print("#################################")

p1.job = "ITC"
p1.job
print(p1.job)
