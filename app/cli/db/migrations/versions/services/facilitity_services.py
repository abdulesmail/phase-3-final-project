from db.connect import Session
from db.models import Facility


class FacilityService:
    @classmethod
    def get_facility_by_id(cls, facility_id):
        """
        Returns facility by id
        """
        session = Session()
        facility = session.query(Facility).filter_by(id=facility_id).first()
        session.close()
        return facility

    @classmethod
    def get_all_facilities(cls):
        """
        Returns all facilities in the system
        """
        session = Session()
        all_facilities = session.query(Facility).all()
        session.close()
        return all_facilities

    @classmethod
    def create_facility(cls, name):
        """
        Creates new facility
        """
        facility = Facility(name=name)
        session = Session()
        session.add(facility)
        session.commit()
        session.close()

    @classmethod
    def update_facility(cls, facility_id, new_name):
        """
        Updates facility details
        """
        session = Session()
        facility = session.query(Facility).filter_by(id=facility_id).first()
        facility.name = new_name
        session.commit()
        session.close()

    @classmethod
    def delete_facility(cls, facility_id):
        """
        Removes facilities from the system
        """
        session = Session()
        facility = session.query(Facility).filter_by(id=facility_id).first()
        session.delete(facility)
        session.commit()
        session.close()

    @classmethod
    def get_all_facility_dogs(cls, facility_id):
        """
        Returns all dogs in the facility
        """
        session = Session()
        facility = session.query(Facility).filter_by(id=facility_id).first()
        dogs = facility.get_facility_dogs()
        return dogs

    @classmethod
    def get_facility_adopters(cls, facility_id):
        """
        Returns all users(adopters) under that facility
        """
        session = Session()
        facility = session.query(Facility).filter_by(id=facility_id).first()
        adopters = facility.get_adopters()
        return adopters