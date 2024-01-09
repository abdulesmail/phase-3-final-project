from services.facilitity_services import FacilityService
from validaters import validate_choice
from .utils import print_facilities


def check_if_facility_present(facilities, id):
    facilities_ids = [facility.id for facility in facilities]
    return id in facilities_ids


def facility_id_choice_is_numeric(id):
    return id.isnumeric()


def fetch_facility_from_list(facilities, id):
    return [facility for facility in facilities if facility.id == id][0]


def list_facilities():
    try:
        facilities = FacilityService.get_all_facilities()
        print_facilities(facilities)
    except:
        print("Error printing facilities")


def creating_new_facility():
    name = input("Facility name: ")
    try:
        if not (name.isnumeric() or name.strip() == ""):
            r = FacilityService.create_facility(name)
            if r == None:
                print("Done!")
        else:
            print("Not created!")
    except:
        print("Error creating facility")


def updating_facility():
    list_facilities()
    print("-" * 50)
    id = input("Select facility by id: ")
    name = input("Facility new name: ")

    try:
        facilities = FacilityService.get_all_facilities()
        if (id.isnumeric()) and (not name.isnumeric()):
            id = int(id)
            is_present = check_if_facility_present(facilities, id)
            if is_present:
                FacilityService.update_facility(id, name)
                print("Facility Updated")
            else:
                print("No facility with that Id")
        else:
            print("Invalid input!")

    except:
        print("Error occured while updating facility!")


def print_facility_dogs(dogs, facility):
    print("\n-" * 3 + f" Listing Facility- {facility.name} Dogs" + "-" * 50)
    print()
    print("-" * 5 + " Id " + "-" * 10 + " Name " + "-" * 5)
    print("\n")
    for dog in dogs:
        print(" " * 5 + f" {dog.id}" + " " * 5 + f"{dog.name}" + " " * 5)


def print_adopters_in_facility(adopters, facility):
    print("\n-" * 3 + f" Listing Facility- {facility.name} Adopters" + "-" * 50)
    print()
    print("-" * 5 + " Id " + "-" * 10 + " Name " + "-" * 5)
    print("\n")
    for adopter in adopters:
        print(
            " " * 5
            + f" {adopter.id}"
            + " " * 5
            + f"{adopter.get_full_name()}"
            + " " * 5
        )


def list_facility_dogs():
    list_facilities()
    print("-" * 50)
    try:
        id = input("Select facility by id: ")
        id = int(id)
        facilities = FacilityService.get_all_facilities()
        facility = fetch_facility_from_list(facilities, id)
        dogs = FacilityService.get_all_facility_dogs(facility.id)
        print_facility_dogs(dogs, facility)
    except:
        print("Wrong choice!")


def list_adopters_in_facility():
    list_facilities()
    print("-" * 50)
    try:
        id = input("Select facility by id: ")
        id = int(id)
        facilities = FacilityService.get_all_facilities()
        facility = fetch_facility_from_list(facilities, id)
        adopters = FacilityService.get_facility_adopters(facility.id)
        print_adopters_in_facility(adopters, facility)
    except:
        print("Wrong choice!")


def delete_facility():
    list_facilities()
    print("-" * 50)
    id = input("Delete facility by id: ")
    try:
        facilities = FacilityService.get_all_facilities()
        if id.isnumeric():
            id = int(id)
            is_present = check_if_facility_present(facilities, id)
            if is_present:
                FacilityService.delete_facility(id)
                print("Facility Deleted!")
            else:
                print("No facility with that Id")
        else:
            print("Invalid input!")

    except:
        print("Error occured while deleting facility!")


def interact_with_facilities():
    choice = 1

    while choice != 7:
        print("*" * 100)
        print("*" * 10 + " Now interacting with Facilities " + "*" * 10)
        print("1) Print all facilities")
        print("2) Create new facility")
        print("3) Update facility")
        print("4) List facility dogs")
        print("5) List adopters in a facility")
        print("6) Delete facility!!")
        print("7) Quit interacting with facilities!")

        choice = int(validate_choice(input(">>>> "), 7))

        if choice == 1:
            list_facilities()
        elif choice == 2:
            creating_new_facility()
        elif choice == 3:
            updating_facility()
        elif choice == 4:
            list_facility_dogs()
        elif choice == 5:
            list_adopters_in_facility()

        elif choice == 6:
            delete_facility()

        else:
            print("Quiting facilities!")