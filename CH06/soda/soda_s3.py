


def main():
    try:
        infile = open("orders.txt", "r")
    except FileNotFoundError:
        print("Could not find file")
        exit()

    total_cases = 0

    while True:
        soda_name = infile.readline()
        if soda_name == "":
            break

        soda_count = infile.readline()
        if soda_count == "":
            break

        print(f"{soda_name.strip()}, {soda_count.strip()}")

        total_cases += int(soda_count)

    print(f"Total Cases Ordered: {total_cases}")



main()