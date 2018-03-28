# -*- coding:utf-8 -*-

import  random
def bubblesort(array):
    """冒泡排序算法"""
    for i in range(len(array)-1):
        for j in range(len(array)-1):
            if array[j] > array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]
    return array
r = random.Random()
newarray = []
for i in range(10):
    newarray.append(r.randint(0, 100))
if __name__ == '__main__':
    print("排序前")
    print(newarray)
    print("排序后")
    print(bubblesort(newarray))
