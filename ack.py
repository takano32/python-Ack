


def ack(m, n):
	if m == 0:
		return n + 1
	elif n == 0:
		return ack(m - 1, 1)
	else:
		return ack(m - 1, ack(m, n - 1))


if __name__ == '__main__':
	# print "A(2, 2) = %d" % ack(2, 2)
	print "A(4, 1) = %d" % ack(4, 1)



