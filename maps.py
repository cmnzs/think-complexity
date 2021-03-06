# Chapter 3.4 - Implementing maps and then Hashtables

class LinearMap(object):

	def __init__(self):
		self.items = []

	def add(self, k, v):
		self.items.append((k,v))

	def get(self, k):
		for key, val in self.items:
			if key == k:
				return val
		raise KeyError

class BetterMap(object):

	def __init__(self, n=100):
		self.maps = []
		for i in range(n):
			self.maps.append(LinearMap())

	def __len__(self):
		return len(self.maps)

	def find_map(self, k):
		index = hash(k) % len(self.maps)
		return self.maps[index]

	def add(self, k, v):
		m = self.find_map(k)
		m.add(k,v)

	def get(self, k):
		m = self.find_map(k)
		return m.get(k)
	
	def iteritems(self):
		for x in self.maps:
			yield x


class HashMap(object):

	def __init__(self):
		self.maps = BetterMap(2)
		self.num = 0

	def add(self, k, v):
		if self.num == len(self.maps.maps):
			self.resize()
		self.maps.add(k,v)
		self.num += 1

	def get(self, k):
		return self.maps.get(k)

	def resize():
		new_maps = BetterMap(self.num * 2)

		for m in self.maps.iteritems():
			for k,v in m.items:
				new_maps.add(k,v)
		self.maps = new_maps


def main(script, *args):

    # lm = LinearMap()
    # lm.add("a","linmapval")
    # print lm.get("a")

    # bm = BetterMap()
    # bm.add("a","bettermapval")
    # print bm.get("a")    

    hm = HashMap()
    hm.add("hashingkey","hashvalue")
    print hm.get("hashingkey")

if __name__ == '__main__':
    import sys
    main(*sys.argv)
