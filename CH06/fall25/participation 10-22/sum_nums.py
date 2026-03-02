def sum_numbers_from_file(filename):
    total = 0

    try:
        # TODO: open the file here (use a with statement)
        # Example: with open(filename, "r") as infile:
        with open(filename, "r") as inp:
            for line in inp:
                try:
                    total += int(line)
                except:
                    print("error with line: ", line)
        
            # TODO: loop through each line in the file
            # Try to convert each line to an int and add to total
            

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    
    except PermissionError:
        print(f"Error: You do not have permission to read '{filename}'.")
    
    # Optional: handle any other unexpected exceptions
    except Exception as e:
        print("Unexpected error:", e)

    # Return the final total
    return total


def main():
    filename = input("Enter the filename to sum: ")
    result = sum_numbers_from_file(filename)

    print(f"The total sum is: {result}")

if __name__=="__main__":
    main()
