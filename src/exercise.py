def main():
    #write your code below this line
    numbers = []
    while True:
        num = int(input())
        if (num == -1):
            break
        else:
            numbers.append(num)
    start = int(input("From where?"))
    end  = int(input("To where?"))
    i = start
    while (i <= end):
        print(numbers[i])
        i += 1

if __name__ == '__main__':
    main()