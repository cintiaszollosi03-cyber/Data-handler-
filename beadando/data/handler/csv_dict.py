import csv
import os

from ..generator import generate_people, generate_workplaces, generate_addresses
from ..model_dataclasses import Person, Workplace, Address


def write_people(people: list[Person],
                 path: str,
                 file_name: str = "people",
                 extension: str = ".csv",
                 heading: bool = True,
                 delimiter: str = ";") -> None:
    with open(os.path.join(path, file_name + extension), "w",
              newline="\n", encoding="utf-8") as file:
        writer = csv.DictWriter(file, delimiter=delimiter,
                    fieldnames=["id", "name", "age", "male", "workplace", "address"])
        if heading:
            writer.writeheader()
        for person in people:
            row_data = {
                "id": person.id,
                "name": person.name,
                "age": person.age,
                "male": person.male,
                "workplace": str(person.workplace) if person.workplace else "",
                "address": person.address.id if person.address else ""
            }
            writer.writerow(row_data)

def read_people(path: str,
                 file_name: str = "people",
                 extension: str = ".csv",
                 delimiter: str = ";") -> None:
    with open(os.path.join(path, file_name + extension),
              newline="\n", encoding="utf-8") as file:
        rows = csv.DictReader(file, delimiter=delimiter)
        people = []
        for row in rows:
            people.append(
                Person(
                    id=row["id"],
                    name=row["name"],
                    age=int(row["age"]),
                    male=row["male"].lower() == 'true',
                    workplace=row.get("workplace") if row.get("workplace") else None,
                    address=row.get("address") if row.get("address") else None
                )
            )
        return people

def write_workplaces(workplaces: list[Workplace],
                     path: str,
                        file_name: str = "workplaces",
                        extension: str = ".csv",
                        heading: bool = True,
                        delimiter: str = ";") -> None:
    with open(os.path.join(path, file_name + extension), "w",
              newline="\n", encoding="utf-8") as file:
        writer = csv.DictWriter(file, delimiter=delimiter,
                                fieldnames=["id", "name", "location", "employees"])
        if heading:
            writer.writeheader()
        for workplace in workplaces:
            writer.writerow({"id": workplace.id, "name": workplace.name, "location": workplace.location, "employees": ",".join(workplace.employees)})

def read_workplaces(path: str,
                   file_name: str = "workplaces",
                   extension: str = ".csv",
                   delimiter: str = ";") -> list[Workplace]:
    with open(os.path.join(path, file_name + extension),
              newline="\n", encoding="utf-8") as file:
        rows = csv.DictReader(file, delimiter=delimiter)
        workplaces = []
        for row in rows:
            employees = row["employees"].split(",") if row["employees"] else []
            employees = [emp.strip() for emp in employees if emp.strip()]
            workplaces.append(
                Workplace(row["id"], row["name"], row["location"], employees)
            )
        return workplaces

def write_addresses(addresses: list[Address],
                    path: str,
                    file_name: str = "addresses",
                    extension: str = ".csv",
                    heading: bool = True,
                    delimiter: str = ";") -> None:
    with open(os.path.join(path, file_name + extension), "w",
              newline="\n", encoding="utf-8") as file:
        writer = csv.DictWriter(file, delimiter=delimiter,
                                fieldnames=["id", "street", "city", "country", "resident"])
        if heading:
            writer.writeheader()
        for address in addresses:
            writer.writerow({
                "id": address.id,
                "street": address.street,
                "city": address.city,
                "country": address.country,
                "resident": address.resident.id if address.resident else ""
            })

def read_addresses(path: str,
                   file_name: str = "addresses",
                   extension: str = ".csv",
                   delimiter: str = ";") -> list[Address]:
    with open(os.path.join(path, file_name + extension),
              newline="\n", encoding="utf-8") as file:
        rows = csv.DictReader(file, delimiter=delimiter)
        addresses = []
        for row in rows:
            addresses.append(
                Address(
                    id=row["id"],
                    street=row["street"],
                    city=row["city"],
                    country=row["country"],
                    resident=row.get("resident") if row.get("resident") else None
                )
            )
        return addresses

if __name__ == "__main__":
    print("Teszt indul...")

    # Teszt könyvtár létrehozása
    output_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
        "data",
        "test_files"
    )
    os.makedirs(output_path, exist_ok=True)

    # Tesztadatok generálása
    workplaces = generate_workplaces(4)
    addresses = generate_addresses(6)
    people = generate_people(6, workplaces.copy(), addresses.copy())

    # People teszt
    write_people(people, output_path, "csv_test_people")
    loaded_people = read_people(output_path, "csv_test_people")
    print(f"Elmentve: {len(people)} ember, beolvasva: {len(loaded_people)} ember")
    print(f"Első beolvasott ember: {loaded_people[0] if loaded_people else 'Nincs adat'}")

    # Workplaces teszt
    write_workplaces(workplaces, output_path, "csv_test_workplaces")
    loaded_workplaces = read_workplaces(output_path, "csv_test_workplaces")
    print(f"Elmentve: {len(workplaces)} munkahely, beolvasva: {len(loaded_workplaces)} munkahely")
    print(f"Első beolvasott munkahely: {loaded_workplaces[0] if loaded_workplaces else 'Nincs adat'}")

    # Addresses teszt
    write_addresses(addresses, output_path, "csv_test_addresses")
    loaded_addresses = read_addresses(output_path, "csv_test_addresses")
    print(f"Elmentve: {len(addresses)} cím, beolvasva: {len(loaded_addresses)} cím")
    print(f"Első beolvasott cím: {loaded_addresses[0] if loaded_addresses else 'Nincs adat'}")

