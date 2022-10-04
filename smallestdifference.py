import random
import time


def alg1(maximum, lis):
    start = time.time()

    smallest = maximum
    for a in lis:
        for b in lis:
            if a != b:
                difference = abs(a - b)
                if smallest > difference:
                    smallest = difference

    end = time.time()
    return [smallest, end - start]


def alg2(rand_lis):
    start = time.time()
    differences = []
    for a in rand_lis:
        for b in rand_lis:
            if a != b:
                differences.append(abs(a - b))
    differences.sort()
    end = time.time()
    return [differences[0], end - start]


def main():

    print('''This program finds the smallest difference between any two elements in a
randomly generated list of integers, using two different algorithms with
different Big-O efficiency.''', '\n')

    min_range = int(input('Enter random min range: '))
    max_range = int(input('Enter random max range: '))
    length = int(input('Enter length of list: '))

    random_list = []
    for i in range(length):
        random_list.append(random.randrange(min_range, max_range))

    print()
    print('Smallest difference:', alg1(max_range, random_list)[0])
    print('List: ', random_list)
    print('List length: ', length)
    print('Algorithm 1 Time: ', alg1(max_range, random_list)[1])
    print('Algorithm 2 Time: ', alg2(random_list)[1])


main()
