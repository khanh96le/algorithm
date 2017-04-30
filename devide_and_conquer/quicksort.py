import numpy as np

np.random.seed(3)
arr = np.random.permutation(20)

def quickSort(alist):
  quickSortHelper(alist, 0, len(alist) - 1)


def quickSortHelper(alist, first, last):
  if first < last:
    splitpoint = partition(alist, first, last)

    quickSortHelper(alist, first, splitpoint - 1)
    quickSortHelper(alist, splitpoint + 1, last)


def partition(alist, first, last):
  pivotvalue = alist[first]

  leftmark = first + 1
  rightmark = last

  done = False
  while not done:

    while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
      leftmark = leftmark + 1

    while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
      rightmark = rightmark - 1

    if rightmark < leftmark:
      done = True
    else:
      print "swap a[{0}] and a[{1}]".format(leftmark, rightmark)
      temp = alist[leftmark]
      alist[leftmark] = alist[rightmark]
      alist[rightmark] = temp
      print alist

  temp = alist[first]
  alist[first] = alist[rightmark]
  alist[rightmark] = temp

  return rightmark

print arr
quickSort(arr)

