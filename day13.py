INPUT = """0: 4
1: 2
2: 3
4: 4
6: 8
8: 5
10: 6
12: 6
14: 10
16: 8
18: 6
20: 9
22: 8
24: 6
26: 8
28: 8
30: 12
32: 12
34: 12
36: 12
38: 10
40: 12
42: 12
44: 14
46: 8
48: 14
50: 12
52: 14
54: 14
58: 14
60: 12
62: 14
64: 14
66: 12
68: 12
72: 14
74: 18
76: 17
86: 14
88: 20
92: 14
94: 14
96: 18
98: 18"""

TEST_INPUT = """0: 3
1: 2
4: 4
6: 4"""

class Layer:
	def __init__(self, depth, range):
		self.depth = depth
		self.range = range
		self.scanner_location = 0
		self.up = lambda x: x + 1
		self.down = lambda x: x - 1
		self.scanner_move = self.up
	
	def bump_scanner(self):
		self.scanner_location = self.scanner_move(self.scanner_location)
		if self.scanner_location == 0:
			self.scanner_move = self.up
		if self.scanner_location == self.range - 1:
			self.scanner_move = self.down

class Firewall:
	def __init__(self, text):
		self.layers = {}
		self.packet = -1
		for line in text.splitlines():
			depth, range = [int(part.strip()) for part in line.split(":")]
			self.layers[depth] = Layer(depth, range)
			self.last = depth
	
	def move_scanners(self):
		for layer in self.layers.values():
			layer.bump_scanner()
	
	def move_packet(self):
		self.packet += 1
		layer = self.layers.get(self.packet)
		if layer and layer.scanner_location == 0:
			return layer.depth * layer.range
		return 0

	def cross(self):
		severity = 0
		for i in range(self.last + 1):
			severity += self.move_packet()
			self.move_scanners()
		return severity
	
f = Firewall(TEST_INPUT)
assert f.cross() == 24

f = Firewall(INPUT)
print("result", f.cross())
















