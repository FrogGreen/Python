# Enum, Generator

from enum import Enum


class Cost(Enum):
    LOW = 5
    MEDIUM = 10
    HIGH = 15

    def getCost(self):
        return self.value

def generator():
    n = 1
    print("First")
    yield n

    n += 1
    print("Second")
    yield n

    n += 1
    print("Third")
    yield n


print("Enum:")
Low = Cost.LOW
Medium = Cost.MEDIUM
High = Cost.HIGH

for cost in Cost:
    print(cost)

print(Low.getCost())
print(Medium.getCost())
print(High.value)

print("\nGenerator:")
generator = generator()

print(next(generator))
print(next(generator))
print(next(generator))


# End of file
print()
input("Press Enter to continue...")