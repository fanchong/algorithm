

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

def sort(seq, left, right):
	if left < right:
		middle = depart(seq, left, right)
		sort(seq, left, middle)
		sort(seq, middle+1, right)

if __name__ == '__main__':
	data = [10,39,2,33,4,45]
	sort(data, 0, len(data)-1)
	print data