#!/usr/bin/env python3

from faker import Faker
import random

from connect import Session

from models import Facility, Dog, Adopter

if __name__ == "__main__":
    session = Session()

    session.query(Adopter).delete()
    session.query(Dog).delete()
    session.query(Facility).delete()

    fake = Faker()

    facilities = []
    for i in range(10):
        facility = Facility(
            name=fake.unique.name(),
        )

        # add and commit individually to get IDs back
        session.add(facility)
        session.commit()

        facilities.append(facility)

    adopters = []
    for i in range(10):
        adopter = Adopter(
            first_name=fake.unique.first_name(),
            last_name=fake.unique.last_name(),
        )

        # add and commit individually to get IDs back
        session.add(adopter)
        session.commit()

        adopters.append(adopter)

    dogs = []
    for i in range(10):
        dog = Dog(
            name=fake.unique.name(),
            facility_id=random.randint(1, 10),
            adopter_id=random.randint(1, 10),
        )

        dogs.append(dog)

    session.bulk_save_objects(dogs)
    session.commit()
    session.close()