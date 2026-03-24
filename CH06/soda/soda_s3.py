


def main():
    try:
        infile = open("orders.txt", "r")
    except FileNotFoundError:
        print("Could not find file")
        exit()

    total_cases = 0

    max_soda_count = 0
    max_soda_name = ""
    while True:
        soda_name = infile.readline()
        if soda_name == "":
            break

        soda_count = infile.readline()
        if soda_count == "":
            break

        print(f"{soda_name.strip()}, {soda_count.strip()}")

        total_cases += int(soda_count)
        if int(soda_count) > max_soda_count:
            max_soda_count = int(soda_count)
            max_soda_name = soda_name

    print(f"Total Cases Ordered: {total_cases}")
    print(f"Max soda {max_soda_name} with {max_soda_count} cases")



main()