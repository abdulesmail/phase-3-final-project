from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, backref
from sqlalchemy import ForeignKey


class Base(DeclarativeBase):
    pass


class Facility(Base):
    __tablename__ = "facilities"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    dogs = relationship("Dog", backref=backref("facility"), cascade="all, delete")

    def __repr__(self):
        return "Facility<{0}>".format(self.name)

    def get_facility_dogs(self):
        """
        Returns all dogs in the facility
        """
        return self.dogs

    def get_adopters(self):
        """
        Returns facility adopters
        """
        adopters = set([dog.adopter for dog in self.dogs])
        return list(adopters)


class Adopter(Base):
    __tablename__ = "adopters"
    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(nullable=False)
    last_name: Mapped[str] = mapped_column(nullable=False)
    dogs = relationship("Dog", backref=backref("adopter"))

    def get_full_name(self):
        """
        Returns full name
        """
        return f"{self.first_name} {self.last_name}"

    def get_adopter_dogs(self):
        """
        Returns all adopted dogs
        """
        return self.dogs

    def get_facilities(self):
        """
        Returns facility adopter own dogs
        """
        facilities = set([dog.facility for dog in self.dogs])
        return list(facilities)

    def __repr__(self):
        return "Adopter<{0} {1}>".format(self.first_name, self.last_name)


class Dog(Base):
    __tablename__ = "dogs"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    facility_id: Mapped[int] = mapped_column(ForeignKey(Facility.id), nullable=False)
    adopter_id: Mapped[int] = mapped_column(ForeignKey(Adopter.id))

    def get_dog_name(self):
        return self.name

    def get_adopter(self):
        return self.adopter

    def get_facility(self):
        return self.facility

    def __repr__(self):
        return "Dog<{0} adopted by {1}>".format(self.name, self.get_adopter())