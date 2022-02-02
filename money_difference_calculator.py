
def price_calculator(persons, cost):
    sumPays = 0
    for p in persons:
        if p.maxVal == -1:
            p.maxVal = cost
        sumPays += p.maxVal

    print(sumPays)
    if sumPays >= cost:
        c = cost/sumPays
        for p in persons:
            p.payVal = c*p.maxVal
    else:
        print("There is not enough money, try again.")
    return persons

class Person:
    def __init__(self, name, maxVal):
        self.name = name
        self.maxVal = maxVal
        self.payVal = 0
        


def main():
    persons = []
    print(f"Money difference calculator, Python edition\nVersion0.1\nCopyright Didrik NL 2022")
    inp = ""
    while inp != "N":
        name = ""
        maxVal = 0.0
        name = input("Type in name: ")
        maxVal = float(input("Type that persons max payment, (-1 for total cost): "))
        persons.append(Person(name, maxVal))
        inp = input("Add another person? ")
    cost = float(input("Type in the cost to calculate: "))
    
    persons = price_calculator(persons, cost)
    
    for p in persons:
        print(f"{p.name} has to pay: {p.payVal}")
    #print(persons)


if __name__ == "__main__":
    main()