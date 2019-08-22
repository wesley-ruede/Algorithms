'Original highly inefficent bucket sort'

DEFAULT_BUCKET_SIZE = 5

def bucket_sort(my_list, bucket_size=DEFAULT_BUCKET_SIZE):
    # if the len of arg my list is eactly 0
    if len(my_list) == 0:
        # display an error
        raise Exception("Please add some elements in the array.")
    
    # applying min and max aggregate funcs to my list and store as new var
    min_value, max_value = (min(my_list), max(my_list))
    # var equals min minus max of my_list with floor division of bucket_size
    # that has a default value of DEFAULT_BUCKET_SIZE equal to 5 plus 1
    # remember order of operations as the plus 1 occurs after floor division
    bucket_count = ((max_value - min_value) // bucket_size + 1)
    # create empty lists for the value in the range of bucket_count
    buckets = [[] for _ in range(int(bucket_count))]
    # iterate through the entirety of my_list
    for i in range(len(my_list)):
        # this is fancy indexing
        # passing a list of elements to access the index of bucket at
        # the designated positions as integer values
        # access the elements of my list and minus the min value with
        # floor division by bucket_size finally add the element 
        # to my list in the place of the list being accessed
        buckets[int((my_list[i] - min_value) // bucket_size)
                ].append(my_list[i])
    # return the sorted bucket values indexed in bucket one and two
    # in the length of the buckets for the length of the buckets elements
    return sorted([buckets[i][j] for i in range(len(buckets))
    # iterate for the element in lenght of buckets index      
                   for j in range(len(buckets[i]))])

# if the root of the programs name is main the begin the program
if __name__ == "__main__":
    # take input and remove the whitespace
    user_input = input('Enter numbers separated by a comma:').strip()
    unsorted = [float(n) for n in user_input.split(',') if len(user_input) > 0]
    print(bucket_sort(unsorted))


'A  higly efficient bucket sort'

def bucket_sort(L: list, num_buckets=4):
    buckets = [[] for _ in range(num_buckets)]

    bucket_range = [int(item * (len(L) / num_buckets)) for item in range(1, num_buckets + 1)]

    for item in L:
        for i, _max in enumerate(bucket_range):
            if item <= _max:
                buckets[i].append(item)
            break
        print(buckets)

import random
array = [random.randint(0, 100) for i in range(50)]
#print(bucket_sort(array, num_buckets=4))
print(bucket_sort(array, num_buckets=4))

'tA highly efficent and recursive bucket sort'

def recursive_bucket_sort(L: list, num_buckets=4):
    # Using set because we don't want to try and bucket sort [10, 10, 10] for example
    if len(set(L)) == 1:
        return L
    elif len(L) == 0:
        return None

    _min = min(L)
    _max = max(L)

    # Create bins
    #print(_min, _max, num_buckets)
    bins = [_max - ((_max - _min) / num_buckets) * i for i in list(range(num_buckets)[::-1])]
    # range(0,100), 5 --> [20.0, 40.0, 60.0, 80.0, 100.0]

    # Create empty buckets
    buckets = [[] for b in range(num_buckets)]
    # [[], [], [], [], []]

    # Fill buckets
    for n in L:
        for i, b in enumerate(bins):
            if n <= b:
                buckets[i].append(n)
                break

    result = []

    # Recursively bucket_sort
    for bucket in buckets:
        if len(set(bucket)) > 1:
            for n in recursive_bucket_sort(bucket, num_buckets):
                result.append(n)
        elif len(set(bucket)) == 1:
            for n in bucket:
                result.append(n)

     return result


import random
array = [random.randint(0, 100) for i in range(25)]
print(array)
array = recursive_bucket_sort(array, num_buckets=4)
print(array)


def bucket_sort(L: list, num_buckets=4):
    buckets = [[] for _ in range(num_buckets)]

    bucket_range = [int(item * (len(L) / num_buckets)) for item in range(1, num_buckets + 1)]

    for item in L:
        for i, _max in enumerate(bucket_range):
            if item <= _max:
                buckets[i].append(item)
            break
        print(buckets)

import random
array = [random.randint(0, 100) for i in range(50)]
#print(bucket_sort(array, num_buckets=4))
print(bucket_sort(array, num_buckets=4))
