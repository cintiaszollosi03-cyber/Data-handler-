from functools import total_ordering

@total_ordering
class Person:
    id: str
    name: str
    age: int
    male: bool
    workplace: 'Workplace'
    address: 'Address'

    def __init__(self, id: str, name: str, age: int, workplace: 'Workplace', address: 'Address', male: bool = True) -> None:
        self.id = id
        self.name = name
        self.age = age
        self.male = male
        self.workplace = workplace
        self.address = address

    def __str__(self) -> str:
        return "#{id}: {name} ({age}, {male}, {workplace}, {address})".format(
            id=self.id,
            name=self.name,
            age=self.age,
            male=self.male,
            workplace=(self.workplace.id, self.workplace.name, self.workplace.location),
            address=(self.address.id, self.address.street, self.address.city, self.address.country)
        )

    def __eq__(self, o: object) -> bool:
        return isinstance(o, Person) and self.id == o.id

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Person):
            return NotImplemented
        return self.id < other.id

    def __hash__(self) -> int:
        return self.id.__hash__()
    
@total_ordering
class Workplace:
    id: str
    name: str
    location: str
    employees: list[Person]

    def __init__(self, id: str, name: str, location: str, employees: list[Person] = None) -> None:
        self.id = id
        self.name = name
        self.location = location
        self.employees = employees
    
    def __str__(self) -> str:
        employee_info = []
        for emp in self.employees:
            employee_info.append(emp.id+', '+emp.name+', '+str(emp.age)+', '+str(emp.male))
        return "#{id}: {name} ({location}, {employees})".format(
            id=self.id,
            name=self.name,
            location=self.location,
            employees=", ".join(employee_info)
        )
    
    def __eq__(self, other: object) -> bool:
        return isinstance(other, Workplace) and self.id == other.id

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Workplace):
            return NotImplemented
        return self.id < other.id

    def __hash__(self) -> int:
        return self.id.__hash__()

@total_ordering
class Address:
    id: str
    street: str
    city: str
    country: str
    resident: Person

    def __init__(self, id: str, street: str, city: str, country: str, resident: Person = None) -> None:
        self.id = id 
        self.street = street
        self.city = city
        self.country = country
        self.resident = resident

    def __str__(self) -> str:
        return "{street}, {city}, {country}, {resident}".format(
            street=self.street,
            city=self.city,
            country=self.country,
            resident=self.resident
        )

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Address) and self.id == other.id

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Address):
            return NotImplemented
        return self.id < other.id

    def __hash__(self) -> int:
        return self.id.__hash__()

if __name__ == "__main__":
    wp1 = Workplace(id="WP-000001", name="Lipóti pékség", location="Debrecen")
    wp2 = Workplace(id="WP-000002", name="Molnár autoszerelő és pizzéria", location="Baktalórántháza")
    a1 = Address(id="A-000001", street="Fő utca 1.", city="Debrecen", country="Magyarország")
    a2 = Address(id="A-000002", street="Petőfi utca 3.", city="Debrecen", country="Magyarország")
    a3 = Address(id="A-000003", street="Kossuth utca 2.", city="Baktalórántháza", country="Magyarország")
    p1 = Person(id="P-000001", name="Lajos", age=30, workplace=wp1, address=a1)
    p2 = Person(id="P-000002", name="Péter", age=18, workplace=wp1, address=a2)
    p3 = Person(id="P-000003", name="Eszter", age=32, male=False, workplace=wp2, address=a3)
    
    # cím és személy közötti kapcsolat beállítása
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
    
    print("Address:")
    for address in [a1, a2, a3]:
        print(address)
        print('Address of '+address.resident.id)
    
    print("Comparison:")
    print('p1 == p2 :', p1 == p2)
    print('p2 < p3 :', p2 < p3)
    print('wp != wp2 :', wp1 != wp2)
    print('a1 > a2 :', a1 > a2)