# -*- coding:utf-8 -*-

def findsmallest(array):
    '''查找最小的值'''
    smallest = array[0]
    smallest_index = 0
    for i in range(1,len(array)):
        if array[i] <= smallest:
            smallest = array[i]
            smallest_index = i
    return smallest_index
def selectionsort(data):
    '''选择排序'''
    newarray = []
    for i in range(len(data)):
        newsmallest = findsmallest(data)
        newarray.append(data.pop(newsmallest))
    return newarray
if __name__ == '__main__':
    print(selectionsort([2,10,6,9,1]))