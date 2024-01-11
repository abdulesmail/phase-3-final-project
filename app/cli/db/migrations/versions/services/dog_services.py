from db.connect import Session
from db.models import Dog


class DogService:
    @classmethod
    def get_dog_by_id(cls, dog_id):
        """
        Returns dog with provided id
        """
        session = Session()
        dog = session.query(Dog).filter_by(id=dog_id).first()
        return dog

    @classmethod
    def get_all_dogs(cls):
        """
        Returns all dogs in the system
        """
        session = Session()
        dogs = session.query(Dog).all()
        session.close()
        return dogs

    @classmethod
    def create_dog(cls, name, facility_id, adopter_id):
        """
        Registers new dog
        """
        dog = Dog(name=name, facility_id=facility_id, adopter_id=adopter_id)
        session = Session()
        session.add(dog)
        session.commit()
        session.close()

    @classmethod
    def update_dog(cls, dog_id, name):
        """
        Updates dog details
        """
        session = Session()
        dog = session.query(Dog).filter_by(id=dog_id).first()
        dog.name = name
        session.commit()
        session.close()

    @classmethod
    def delete_dog(cls, dog_id):
        """
        Removes dog from the system
        """
        session = Session()
        dog = session.query(Dog).filter_by(id=dog_id).first()
        session.delete(dog)
        session.commit()
        session.close()