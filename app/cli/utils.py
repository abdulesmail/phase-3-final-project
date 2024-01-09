def print_facilities(facilities):
    print("\n-" * 3 + " Listing all facilities" + "-" * 50)
    print()
    print("-" * 5 + " Id " + "-" * 10 + " Name " + "-" * 5)
    print("\n")
    for facility in facilities:
        print(" " * 5 + f" {facility.id}" + " " * 5 + f"{facility.name}" + " " * 5)


def print_adopters(adopters):
    print("\n-" * 3 + " Listing all adopters" + "-" * 50)
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


def print_dogs(dogs):
    print("\n-" * 3 + " Listing all dogs" + "-" * 50)
    print()
    print("-" * 5 + " Id " + "-" * 10 + " Name " + "-" * 5)
    print("\n")
    for dog in dogs:
        print(" " * 5 + f" {dog.id}" + " " * 5 + f"{dog.get_dog_name()}" + " " * 5)


def is_valid_name(name):
    if name.isnumeric() or name.strip() == "":
        return False
    else:
        return True