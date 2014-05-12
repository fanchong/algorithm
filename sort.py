'''
Quick sort and bubble sort
'''


def bubble_sort(seq):
	length = len(seq)
	for i in xrange(length):
		for j in xrange(i, length):
			if seq[i] >= seq[j]:
				seq[i], seq[j] = seq[j], seq[i]


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
	data = [10,39,2,33,4,45]
	quick_sort(data, 0, len(data)-1)
	print data
	print "------bubble sort----"
	data = [10,39,2,33,4,45]
	bubble_sort(data)
	print data