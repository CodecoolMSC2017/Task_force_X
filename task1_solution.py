import random


def sum_of_nums(table):
    sums = 0
    for elem in table:
        sums += elem
    return sums


def sum_of_many_nums(table, table2):
    sums = []
    sums1 = 0
    sums2 = 0
    for i in table:
        sums1 += i
    for i in table2:
        sums2 += i
    sums.append(sums1)
    sums.append(sums2)
    return sums


def find_all_uppers(table):
    uppers = 0
    for elem in table:
        elem = str(elem)
        for char in elem:
            if char.isupper():
                uppers += 1
    return uppers


def isPrime(x):
    if x < 2:
        return False
    for i in range(2, x):
        if not x % i:
            return False
    return True


def find_all_none_primes(n):
    nonprimes = []
    for i in range(n):
        if isPrime(i):
            continue
        else:
            nonprimes.append(i)
    return nonprimes


def find_the_odd_one_out(table):
    finaltable = []
    ints = []
    strings = []
    for elem in table:
        if str(elem).isdigit():
            ints.append(elem)
        elif elem == str(elem):
            strings.append(elem)
    if len(ints) > len(strings):
        return ([ints, strings])
    else:
        return ([strings, ints])


def many_whelps_handle_it(table):
    raid_members = 0
    whelps = 0
    for elem in table:
        if elem == "W":
            whelps += 1
        elif elem == "R":
            raid_members += 1
    if whelps > raid_members:
        return "LEEEEEEROY JENNNKINS"
    if whelps == raid_members:
        return "dunno"
    if whelps < raid_members:
        return "Hit it like you mean it"


def generate_random_table():
    table = []
    for i in range(0, 10):
        a = "".join(random.choice("RW") for k in range(1))
        table.append(a)
    return table


def handle_menu():
    while True:
        print("--- Functions ---")
        print("1. Sum of nums")
        print("2. Sum of many nums")
        print("3. Find all uppers")
        print("4. Find all non primes")
        print("5. Find the odd one out")
        print("6. Many whelps, can't handle it")
        print("0. Exit")
        choice = input("Select a function to test: ")
        if choice == "1":
            a = []
            table_items = " "
            print("Give the numbers you would like to add: ")
            while table_items != "":
                table_items = input()
                if table_items == "":
                    break
                table_items = int(table_items)
                a.append(table_items)

            print("Sum of given nums:", sum_of_nums(a))
        
        elif choice == "2":
            a = []
            b = []
            a_items = " "
            b_items = " "
            print("Please provide numbers for first table: ")
            while a_items != "":
                a_items = input()
                if a_items == "":
                    break
                else:
                    a_items = int(a_items)
                    a.append(a_items)

            print("Please provide numbers for second table: ")
            while b_items != "":
                b_items = input()
                if b_items == "":
                    break
                else:
                    b_items = int(b_items)
                    b.append(b_items)

            print("Sum of many nums:", sum_of_many_nums(a, b))

        elif choice == "3":
            listitems = []
            item = " "
            print("Please provide list items: ")
            while item != "":
                item = input()
                listitems.append(item)

            print("Number of uppercase letters: ", find_all_uppers(listitems))

        elif choice == "4":
            a = int(input("Provide maximum: "))
            print(find_all_none_primes(a))

        elif choice == "5":
            table = []
            print("Provide list items: ")
            list_items = " "
            while list_items != "":
                list_items = input()
                if list_items == "":
                    break
                else:
                    table.append(list_items)
            print(find_the_odd_one_out(table))

        elif choice == "6":
            table = generate_random_table()
            whelps = 0
            raid_members = 0
            for i in table:
                if i == "W":
                    whelps += 1
                elif i == "R":
                    raid_members += 1
            print("Randomly generated table:", table)
            print("Number of whelps:", whelps)
            print("Number of raid members:", raid_members)
            print(many_whelps_handle_it(table))

        elif choice == "0":
            exit()
        
        else:
            print("Not a valid option")
            continue


def main():
    handle_menu()


if __name__ == '__main__':
    main()
