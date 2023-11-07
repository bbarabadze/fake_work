from faker import Faker
from random import randrange

from utils.decorators.main import file_exists_decorator


def generate_random_gender(*genders: str) -> str:

    random_gender = randrange(0, len(genders))
    return genders[random_gender]


def generate_jobs(filename: str) -> None:

    fake = Faker()
    with open(filename, "w") as f:
        for idx in range(10000):

            ssn = fake.ssn()
            name = fake.name()
            job = fake.job()
            gender = generate_random_gender("male", "female")

            f.write(f"{ssn}|{name}|{job}|{gender}\n")


def append_to_file(filename: str, record: str) -> None:

    with open(filename, "a") as f:
        f.write(f"{record}\n")


@file_exists_decorator
def read_and_count(filename: str) -> None:

    with open(filename, "r") as f:

        for idx, record in enumerate(f):
            try:
                record = record.strip()
                ssn, name, job, gender = record.split("|")
            except ValueError:
                print(f"Error with splitting line {idx}")
                continue

            #  job.lower() ჯობია თუ ეს მიდგომა გასატესტია
            if gender == 'female' and ('Programmer' in job or 'programmer' in job):
                append_to_file("female programmers.txt", record.strip())

generate_jobs("jobs.txt")
read_and_count("jobs.txt")