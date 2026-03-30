

def count_capitals(sentence):
    i = 1
    count = 0
    for x in sentence:
        i +=1
        if x.isupper():
            print(f"letter {i} is {x} is capital")
            count +=1
        else:
            print(f"letter {i} is {x} is not capital")
    return count

def main():
    sentence = input("enter a sentence ")
    caps = count_capitals(sentence)
    print(caps)
    

main()