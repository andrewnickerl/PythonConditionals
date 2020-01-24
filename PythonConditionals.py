def main():
    x, y = 1000, 100

    if (x < y):
        st = "x is less than y"
    elif (x > y):  #Python equivalent of "else if"
        st = "x is greater than y"
    else:
        st = "x is the same as y"
        #NOTE: there is no switch construct in Python, only if/else
    print(st) 

if __name__ == "__main__":
    main()