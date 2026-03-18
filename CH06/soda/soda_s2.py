
def get_total_cases(infile):
    total_cases = 0
    while True:
        soda_type = infile.readline()
        if soda_type == "":
            break

        soda_count = infile.readline()
        if soda_count == "":
            break

        print(f"soda: {soda_type.strip()}, {soda_count.strip()}")

        total_cases += int(soda_count)
    return total_cases

def main():
    try:
        infile = open("orders.txt", "r")
    except FileNotFoundError:
        print("Could not find file")
        exit()

    total_cases = get_total_cases(infile)
    infile.close()
    print(f"Total Cases Ordered: {total_cases}")
main()