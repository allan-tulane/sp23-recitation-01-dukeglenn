"""
CMPS 2200  Recitation 1
"""

### the only imports needed are here
### import tabulate
import time
###

def linear_search(mylist, key):
  """ done. """
  for i,v in enumerate(mylist):
    if v == key:
      return i
  return -1

def test_linear_search():
  """ done. """
  assert linear_search([1,2,3,4,5], 5) == 4
  assert linear_search([1,2,3,4,5], 1) == 0
  assert linear_search([1,2,3,4,5], 6) == -1

def binary_search(mylist, key):
  return _binary_search(mylist, key, 0, len(mylist)-1)

def _binary_search(mylist, key, left, right):
	
  if left<=right:
    mid = (left+right)//2
    
    if mylist[mid] == key:
      mid+1
      return mid

    elif key < mylist[mid]:
      return _binary_search(mylist, key, left, mid-1)

    elif key > mylist[mid]:
      return _binary_search(mylist, key, mid+1, right)

  else:
    return -1
      
	###


def test_binary_search():

  assert binary_search([1,2,3,4,5], 5) == 4
  assert binary_search([1,2,3,4,5], 1) == 0
  assert binary_search([1,2,3,4,5], 6) == -1
  
  assert binary_search([1,2,3,4,5], 0) == -1
  assert binary_search([1,2,3,4,5], 3) == 2
	###


def time_search(sort_fn, mylist, key):
	### TODO
  firstTime = time.time() * 1000
  mylist.sort_fn
  lastTime = time.time() * 1000
  totalTime = lastTime-firstTime
  return totalTime
	###

def compare_search(sizes=[1e1, 1e2, 1e3, 1e4, 1e5, 1e6, 1e7]):
  nList = []
  linearSearchTimes = []
  binarySearchTimes = []
  for size in sizes:
    nList.append(size)
    linearSearchTime = time_search(linear_search, size, -1)
    linearSearchTimes.append(linearSearchTime)
    binarySearchTime = time_search(binary_search, size, -1)
    binarySearchTimes.append(binarySearchTime)

  data = list(zip(nList, linearSearchTimes, binarySearchTimes))
  return data

def print_results(results):
	""" done """
	print(tabulate.tabulate(results,
							headers=['n', 'linear', 'binary'],
							floatfmt=".3f",
							tablefmt="github"))

def test_compare_search():
	res = compare_search(sizes=[10, 100])
	print(res)
	assert res[0][0] == 10
	assert res[1][0] == 100
	assert res[0][1] < 1
	assert res[1][1] < 1
