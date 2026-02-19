import json
import os

from .. import generator
from ..model_dataclasses import Person, Workplace, Address

def write_people(people: list[Person],
                 path: str,
                 file_name: str = "people",
                 extension: str = ".json",
                 pretty: bool = True) -> None:
    with open(os.path.join(path, file_name + extension), "w") as file:
        people_data = []
        for person in people:
            person_dict = {
                "id": person.id,
                "name": person.name,
                "age": person.age,
                "male": person.male,
                "workplace": person.workplace.id if person.workplace else None,
                "address": person.address.id if person.address else None
            }
            people_data.append(person_dict)
        
        json.dump(people_data, file, indent=2 if pretty else 0)


def read_people(path: str,
                file_name: str = "people",
                extension: str = ".json") -> list[Person]:
    with open(os.path.join(path, file_name + extension)) as file:
        people = []
        objects = json.load(file)
        for obj in objects:
            person = Person(
                id=obj["id"], 
                name=obj["name"], 
                age=obj["age"],
                male=obj["male"],
                workplace=obj.get("workplace"),  
                address=obj.get("address")  
            )
            people.append(person)
        return people


def write_workplaces(workplaces: list[Workplace],
                     path: str,
                     file_name: str = "workplaces",
                     extension: str = ".json",
                     pretty: bool = True) -> None:
    with open(os.path.join(path, file_name + extension), "w") as file:
        workplaces_data = []
        for workplace in workplaces:
            workplace_dict = {
                "id": workplace.id,
                "name": workplace.name,
                "location": workplace.location,
                "employees": workplace.employees  
            }
            workplaces_data.append(workplace_dict)
        
        json.dump(workplaces_data, file, indent=2 if pretty else 0)


def read_workplaces(path: str,
                    file_name: str = "workplaces",
                    extension: str = ".json") -> list[Workplace]:
    with open(os.path.join(path, file_name + extension)) as file:
        workplaces = []
        objects = json.load(file)
        for obj in objects:
            workplace = Workplace(
                id=obj["id"],
                name=obj["name"],
                location=obj["location"],
                employees=obj.get("employees", [])  
            )
            workplaces.append(workplace)
        return workplaces


def write_addresses(addresses: list[Address],
                    path: str,
                    file_name: str = "addresses",
                    extension: str = ".json",
                    pretty: bool = True) -> None:
    with open(os.path.join(path, file_name + extension), "w") as file:
        addresses_data = []
        for address in addresses:
            address_dict = {
                "id": address.id,
                "street": address.street,
                "city": address.city,
                "country": address.country,
                "resident": address.resident.id if address.resident else None
            }
            addresses_data.append(address_dict)
        
        json.dump(addresses_data, file, indent=2 if pretty else 0)


def read_addresses(path: str,
                   file_name: str = "addresses",
                   extension: str = ".json") -> list[Address]:
    with open(os.path.join(path, file_name + extension)) as file:
        addresses = []
        objects = json.load(file)
        for obj in objects:
            address = Address(
                id=obj["id"],
                street=obj["street"],
                city=obj["city"],
                country=obj["country"],
                resident=obj.get("resident")  
            )
            addresses.append(address)
        return addresses


if __name__ == "__main__":
    import os
    from data.generator import generate_people, generate_workplaces, generate_addresses

    # Teszt könyvtár létrehozása
    test_dir = os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
        "data",
        "test_files"
    )
    os.makedirs(test_dir, exist_ok=True)

    # Tesztadatok generálása
    workplaces = generate_workplaces(2)
    addresses = generate_addresses(5)
    people = generate_people(5, workplaces.copy(), addresses.copy())

    # Emberek tesztelése
    write_people(people, test_dir, "json_test_people")
    loaded_people = read_people(test_dir, "json_test_people")
    print(f"Elmentve {len(people)} ember, beolvasva {len(loaded_people)} ember")
    print(f"Első beolvasott ember: {loaded_people[0] if loaded_people else 'Nincs adat'}")

    # Munkahelyek tesztelése
    write_workplaces(workplaces, test_dir, "json_test_workplaces")
    loaded_workplaces = read_workplaces(test_dir, "json_test_workplaces")
    print(f"Elmentve {len(workplaces)} munkahely, beolvasva {len(loaded_workplaces)} munkahely")
    print(f"Első beolvasott munkahely: {loaded_workplaces[0] if loaded_workplaces else 'Nincs adat'}")

    # Címek tesztelése
    write_addresses(addresses, test_dir, "json_test_addresses")
    loaded_addresses = read_addresses(test_dir, "json_test_addresses")
    print(f"Elmentve {len(addresses)} cím, beolvasva {len(loaded_addresses)} cím")
    print(f"Első beolvasott cím: {loaded_addresses[0] if loaded_addresses else 'Nincs adat'}")

