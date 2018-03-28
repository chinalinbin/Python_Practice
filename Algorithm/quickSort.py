# -*- coding：utf-8 -*-

def quicksort(array):
    '''使用递归思想进行快速排序'''
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)
if __name__ == '__main__':
    print(quicksort([3,1,2,10,8]))