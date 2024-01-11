from db.connect import Session
from db.models import Adopter


class AdopterService:
    @classmethod
    def get_adopter_by_id(cls, adopter_id):
        session = Session()
        adopter = session.query(Adopter).filter_by(id=adopter_id).first()
        session.close()
        return adopter

    @classmethod
    def get_all_adopters(cls):
        """
        Returns all adopters in the system
        """
        session = Session()
        adopters = session.query(Adopter).all()
        session.close()
        return adopters

    @classmethod
    def register_adopter(cls, first_name, last_name):
        """
        Registers a new user(adopter) in the system
        """
        adopter = Adopter(first_name=first_name, last_name=last_name)
        session = Session()
        session.add(adopter)
        session.commit()
        session.close()

    @classmethod
    def update_adopter(cls, adopter_id, first_name, last_name):
        """
        Updates adopter details
        """
        session = Session()
        adopter = session.query(Adopter).filter_by(id=adopter_id).first()
        adopter.first_name = first_name
        adopter.last_name = last_name
        session.commit()
        session.close()

    @classmethod
    def delete_adopter(cls, adopter_id):
        """
        Removes adopter from the system
        """
        session = Session()
        adopter = session.query(Adopter).filter_by(id=adopter_id).first()
        session.delete(adopter)
        session.commit()
        session.close()

    @classmethod
    def get_adopted_dogs(cls, adopter_id):
        """
        Returns all adopter dogs
        """
        session = Session()
        adopter = session.query(Adopter).filter_by(id=adopter_id).first()
        dogs = adopter.get_adopter_dogs()
        return dogs

    @classmethod
    def get_facilities(cls, adopter_id):
        """
        Returns facilities associated with adopter
        """
        session = Session()
        adopter = session.query(Adopter).filter_by(id=adopter_id).first()
        facilities = adopter.get_facilities()
        return facilities