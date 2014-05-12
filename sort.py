'''
Quick sort,bubble sort and selection sort
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