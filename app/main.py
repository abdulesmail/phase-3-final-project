#!/usr/bin/env python3

from validaters import validate_choice
from cli.cls_facility import interact_with_facilities
from cli.cls_adopters import interacting_with_adopters
from cli.cls_dogs import interacting_with_dogs


def main():
    choice = 1
    while choice != 4:
        print("=" * 10 + " Running Dog Adoption App " + "=" * 10)
        print("1) Interact with Facilities")
        print("2) Interact with Adopters")
        print("3) Interact with Dogs")
        print("4) quit!")

        choice = int(validate_choice(input(">>>> "), 5))

        if choice == 1:
            interact_with_facilities()
        elif choice == 2:
            interacting_with_adopters()
        elif choice == 3:
            interacting_with_dogs()


if __name__ == "__main__":
    main()