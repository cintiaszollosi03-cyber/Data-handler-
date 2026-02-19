from dataclasses import dataclass, field
from functools import total_ordering
from typing import List


@dataclass(unsafe_hash=True)
@total_ordering
class Person:
    id: str = field(hash=True)
    name: str = field(compare=False)
    age: int = field(compare=False)
    male: bool = field(compare=False,
                       default=True)
    workplace: 'Workplace' = field(compare=False, default=None)
    address: 'Address' = field(compare=False, default=None)

    def __lt__(self, o: object) -> bool:
        if not isinstance(o, Person):
            return NotImplemented

        return self.id < o.id

@dataclass(unsafe_hash=True)
@total_ordering
class Workplace:
    id: str = field(hash=True)
    name: str = field(compare=False)
    location: str = field(compare=False)
    employees: List['Person'] = field(compare=False, default_factory=list)

    def __lt__(self, o: object) -> bool:
        if not isinstance(o, Workplace):
            return NotImplemented
        return self.id < o.id

@dataclass(unsafe_hash=True)
@total_ordering
class Address:
    id: str = field(hash=True)
    street: str = field(compare=False)
    city: str = field(compare=False)
    country: str = field(compare=False)
    resident: 'Person' = field(compare=False, default=None)

    def __lt__(self, o: object) -> bool:
        if not isinstance(o, Address):
            return NotImplemented
        return self.id < o.id

if __name__ == "__main__":
    wp1 = Workplace(id="WP-000001", name="Lipóti pékség", location="Debrecen")
    wp2 = Workplace(id="WP-000002", name="Molnár autoszerelő és pizzéria", location="Baktalórántháza")
    a1 = Address(id="A-000001", street="Fő utca 1.", city="Debrecen", country="Magyarország")
    a2 = Address(id="A-000002", street="Petőfi utca 3.", city="Debrecen", country="Magyarország")
    a3 = Address(id="A-000003", street="Kossuth utca 2.", city="Baktalórántháza", country="Magyarország")
    p1 = Person(id="P-000001", name="Lajos", age=30, workplace=wp1, address=a1)
    p2 = Person(id="P-000002", name="Péter", age=18, workplace=wp1, address=a2)
    p3 = Person(id="P-000003", name="Eszter", age=32, male=False, workplace=wp2, address=a3)

    # kapcsolatok beállítása
    a1.resident = p1
    a2.resident = p2
    a3.resident = p3
    wp1.employees = [p1, p2]
    wp2.employees = [p3]

    print("Person:")
    for person in [p1, p2, p3]:
        print(person)
        for workplace in [wp1, wp2]:
            if(person in workplace.employees):
                print(person.name+' workplace: '+workplace.name)

    print("Workplaces:")
    for wp in [wp1, wp2]:
        print(wp)
        for person in [p1, p2, p3]:
            if(person in workplace.employees):
                print('Employees at '+workplace.name+': '+person.name)

    print("Addresses:")
    for address in [a1, a2, a3]:
        print(address)
        if address.resident:
            print(f'Address of {address.resident.name}: {address.street}, {address.city}')

    print("Comparison:")
    print('p1 == p2 :', p1 == p2)
    print('p2 < p3 :', p2 < p3)
    print('wp != wp2 :', wp1 != wp2)
    print('a1 > a2 :', a1 > a2)