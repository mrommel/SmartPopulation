import unittest

from map.map import Map, HexPoint, HexDirection


class TestHexPoint(unittest.TestCase):
	
	def test_neighbor(self):
		# GIVEN
		hex_point = HexPoint(x=5, y=5)
		
		# WHEN
		neighbor = hex_point.neighbor_in(direction=HexDirection.north, distance=1)
		
		# THEN
		self.assertEqual(neighbor.x, 4)
		self.assertEqual(neighbor.y, 4)
	
	def test_neighbors(self):
		# GIVEN
		hex_point = HexPoint(x=5, y=5)
		
		# WHEN
		neighbors = hex_point.neighbors()
		
		# THEN
		self.assertEqual(len(neighbors), 6)
		self.assertEqual(HexPoint(x=4, y=4), neighbors[0])
		self.assertEqual(HexPoint(x=5, y=4), neighbors[1])
		self.assertEqual(HexPoint(x=6, y=5), neighbors[2])
		self.assertEqual(HexPoint(x=5, y=6), neighbors[3])
		self.assertEqual(HexPoint(x=4, y=6), neighbors[4])
		self.assertEqual(HexPoint(x=4, y=5), neighbors[5])
	
	def test_distance(self):
		# GIVEN
		hex_point = HexPoint(x=5, y=5)
		distant_point = HexPoint(x=13, y=7)
		
		# WHEN
		distance = hex_point.distance_to(distant_point)
		
		# THEN
		self.assertEqual(distance, 9)
	
	def test_is_neighbor(self):
		# GIVEN
		hex_point = HexPoint(x=5, y=5)
		neighbor_point = HexPoint(x=4, y=4)
		
		# WHEN
		is_neighbor = hex_point.is_neighbor_of(neighbor_point)
		
		# THEN
		self.assertEqual(is_neighbor, True)


class TestMap(unittest.TestCase):
	
	def test_get(self):
		# GIVEN
		hex_map = Map(width=5, height=5)
		
		# WHEN
		is_inside = hex_map.valid(2, 2)
		is_outside = hex_map.valid(5, 2)
		
		# THEN
		self.assertEqual(is_inside, True)
		self.assertEqual(is_outside, False)


if __name__ == '__main__':
	unittest.main()
