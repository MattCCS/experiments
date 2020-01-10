
class CompanyId:
    def __init__(self, id: int):
        self.id = id


class Company:
    TYPES = {
        "id": CompanyId
    }

    def __init__(self, id: CompanyId, name: str):
        self.id = id
        self.name = name


class EmployeeId:
    def __init__(self, id: int):
        self.id = id


class Employee:
    TYPES = {
        "id": EmployeeId
    }

    def __init__(self, id: EmployeeId, name: str, company: Company):
        self.id = id
        self.name = name
        self.company = company


def query(table, column, key):
    column_type = table.TYPES[column]
    if not isinstance(key, column_type):
        print(f"Query key {repr(key)} is of type {type(key)}, but column {repr(column)} of table '{table.__name__}' requires type '{column_type}'!")
    else:
        print("Ok")
    print()


print("Bare id:")
query(Employee, "id", 5)

print("Good:")
query(Employee, "id", EmployeeId(5))

print("Bad:")
query(Employee, "id", CompanyId(5))

google = Company(CompanyId(1), "Google Inc.")
e1 = Employee(EmployeeId(1), "Joan", google)

print("Good nested:")
query(Company, "id", e1.company.id)

print("Bad nested:")
query(Employee, "id", e1.company.id)
