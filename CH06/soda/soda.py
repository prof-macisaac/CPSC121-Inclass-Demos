
SODA_FILE = "orders.txt"

def get_case_count_2(infile):
    total_cases = 0

    is_name = True
    for line in infile:
        if is_name:
            is_name = False
        else:
            is_name = True
            total_cases += int(line)

def get_case_count_1(infile):
    total_cases = 0

    while True:
        soda_name =  infile.readline()
        if soda_name == "":
            print("end of file")
            break
        soda_count = infile.readline()
        if soda_count == "":
            print("end of file")
            break

        soda_count = int(soda_count)
        total_cases += soda_count
        
    return total_cases

def main():
    try:
        infile = open(SODA_FILE, "r")
    except:
        print("File not found")
        exit()
    
    
    total_cases = get_case_count_1(infile)
    infile.close()
    print(f"Total Cases Ordered: {total_cases}")

main()