def main():
    file_input = open("test",'r')
    file_list = []
    running_total = 0
    count = 1
    third_number_total = 0
    for line in file_input:
        if (count) % 3 == 0:
            running_total += int(line.rstrip('\n'))
            third_number_total += 1
            print(running_total)
        count += 1
    print("hello world")
main()