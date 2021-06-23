from pprint import pprint


def get_payment_to_this_person(paid_m: (float, int), amount_p: int) -> float:
    return round(paid_m / amount_p, 2)


def get_payment_to_others(name_from: str, others_dept: float, payment_ttp: dict) -> dict:
    payment = {}

    for name_to, dept in payment_ttp.items():
        if name_to == name_from:
            continue
        payment[name_to] = round(dept - others_dept, 2) if dept > others_dept else 0

    return payment


def divide(paid_by_person: dict):
    amount_persons = len(paid_by_person)
    payment_to_this_person = {}
    payment_to_others = {}

    for name, paid_money in paid_by_person.items():
        payment_to_this_person[name] = get_payment_to_this_person(paid_money, amount_persons)

    for name, others_debt in payment_to_this_person.items():
        payment_to_others[name] = get_payment_to_others(name, others_debt, payment_to_this_person)

    return payment_to_others


def collect_info() -> dict:
    persons = {}
    amount_persons = int(input("How many persons paid?\n"))

    for i in range(amount_persons):
        while True:
            name = input(f"Enter {i+1}th person\n")
            if name in persons.keys():
                print("This name is already counted")
                continue
            break
        while True:
            paid_sum = input("Enter sum paid by this person:\n")
            if not paid_sum.isdigit():
                print("It must be a number!")
                continue
            persons[name] = float(paid_sum)
            break

    return persons


def main():
    pprint(divide(collect_info()))


if __name__ == "__main__":
    main()

