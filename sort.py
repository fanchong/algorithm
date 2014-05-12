#--coding:utf-8 --
'''
Quick sort,bubble sort,selection sort and heapsort
'''
import random



#bubble sort
def bubble_sort(seq):
	length = len(seq) - 1
	for i in xrange(length):
		for j in xrange(length-i):
			if seq[j] >= seq[j+1]:
				seq[j], seq[j+1] = seq[j+1], seq[j]


#selection sort

def select_sort(seq):
	length = len(seq) - 1
	for i in xrange(length):
		minone = i
		for j in xrange(i, length):
			if seq[j] < seq[minone]:
				minone = j
		seq[i], seq[minone] = seq[minone], seq[i]



#quick sort
def depart(seq, left, right):
	flag = seq[left]
	while left < right:
		while (left < right and seq[right] >= flag):
			right -= 1
		seq[left] = seq[right]
		while (left < right and seq[left] <= flag):
			left += 1
		seq[right] = seq[left]

	seq[left] = flag
	return left

def quick_sort(seq, left, right):
	if left < right:
		middle = depart(seq, left, right)
		quick_sort(seq, left, middle)
		quick_sort(seq, middle+1, right)

#heapsort
def heap_sort(seq):
	build_heap(seq)

	length = len(seq)
	for i in reversed(range(1, length)):
		swap(seq, 0, i)
		heapify(seq, 0, i-1)

def swap(arr, indexone, indexanother):
	arr[indexone], arr[indexanother] = arr[indexanother], arr[indexone]

def build_heap(seq):
	length = len(seq)
	for i in reversed(range(0, (length-1)/2)):
		heapify(seq, i, length-1)

def heapify(seq, low, high):
	left = low * 2 + 1
	right= left + 1
	current = low

	tmp = seq[low]
	while left <= high:
		if right <= high:
			if seq[left] < seq[right]:
				next = right
			else:
				next = left
		else:
			next = left

		if tmp < seq[next]:
			seq[current] = seq[next]
			current = next
			left = current * 2 + 1
			right = left + 1
		else:
			break
	seq[current] = tmp


#main
if __name__ == '__main__':
	print "------quick sort-----"
	data = [x for x in range(20)]
	random.shuffle(data)
	print "before:",data
	quick_sort(data, 0, len(data)-1)
	print "after:",data
	print "------bubble sort----"
	data = [6,5,4,3,2,1]
	print "before:", data
	bubble_sort(data)
	print "after:",data
	print "------selection sort---"
	data = [x for x in range(10)]
	random.shuffle(data)
	print "before:", data
	select_sort(data)
	print "after:",data

	print "-----heapsort-----"
	data = [x for x in range(5)]
	random.shuffle(data)
	print "before:", data
	heap_sort(data)
	print "after:",data

