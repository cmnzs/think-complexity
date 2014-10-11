import string
# def alphabet_cycle():
#     while True:
#         for c in string.lowercase:
#             yield c
def alphanum():
	count = 1
	while True:
		for c in string.lowercase:
			yield c + str(count)
		count+= 1

def main(script, *args):

	iter = alphanum()
	print iter
	for i in range(29):
		print iter.next()


if __name__ == '__main__':
    import sys
    main(*sys.argv)
