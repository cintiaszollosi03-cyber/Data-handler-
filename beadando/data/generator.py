from faker import Faker
from .model_dataclasses import Person, Workplace, Address
import random


def generate_people(n: int,
                    workplaces: list[Workplace] = None,
                    addresses: list[Address] = None,
                    male_ratio: float = 0.5,
                    locale: str = "hu_HU",
                    unique: bool = False,
                    min_age: int = 0,
                    max_age: int = 100) -> list[Person]:

    assert n > 0
    assert 0 <= male_ratio <= 1
    assert min_age >= 0
    assert min_age <= max_age <= 100


    people = []
    if workplaces is None:      
        workplaces = generate_workplaces(n=random.randint(1, n))
    if addresses is None or len(addresses) < n:
        addresses = generate_addresses(n)
    
    used_workplaces = []
    fake = Faker(locale)
    fake = fake if not unique else fake.unique
    
    for i in range(n):
        # munkahely hozzárendelés
        if len(workplaces) != 0:
            work = workplaces.pop(random.randrange(len(workplaces)))
            used_workplaces.append(work)
        else:
            work = used_workplaces[random.randrange(len(used_workplaces))]
        
        # cím hozzárendelés
        address = addresses[i] if i < len(addresses) else None
        
        # nem és név generálása
        male = random.random() < male_ratio
        person = Person(
            id=f"P-{str(i + 1).zfill(6)}",
            name=fake.unique.name_male() if male else fake.unique.name_female(),
            age=random.randint(min_age, max_age),
            male=male,
            workplace=work,
            address=address)
        
        # kapcsolatok beállítása
        work.employees.append(person.id)
        if address:
            address.resident = person
        people.append(person)

    return people

def generate_workplaces(n: int,
                       location: str = None,
                       unique: bool = True,
                       locale: str = "hu_HU") -> list[Workplace]:

    assert n > 0
    
    workplaces = []
    fake = Faker(locale)
    fake = fake if not unique else fake.unique
    for i in range(n):
        workplace = Workplace(
            id = f"WP-{str(i + 1).zfill(6)}",
            name = fake.company(),
            location=location if location else fake.city()
        )
        workplaces.append(workplace)
    
    return workplaces

def generate_addresses(n: int,
                      country: str = None,
                      unique: bool = True,
                      locale: str = "hu_HU") -> list[Address]:

    assert n > 0
    
    addresses = []
    fake = Faker(locale)
    fake = fake if not unique else fake.unique
    
    for i in range(n):
        address = Address(
            id=f"A-{str(i + 1).zfill(6)}",
            street=fake.street_address(),
            city=fake.city(),
            country=country if country else fake.country()
        )
        addresses.append(address)
    
    return addresses

if __name__ == "__main__":
    print("Testing generator with addresses...")
    workplaces = generate_workplaces(4)
    addresses = generate_addresses(6)
    people = generate_people(n=6, workplaces=workplaces.copy(), addresses=addresses)
    
    print("\nGenerated People:")
    for person in people:
        print(person)
    
    print("\nGenerated Workplaces:")
    for workplace in workplaces:
        print(workplace)
        
    print("\nGenerated Addresses:")
    for address in addresses:
        print(address)