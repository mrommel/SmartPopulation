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


class TestMap(unittest.TestCase):
	
	def test_get(self):
		# GIVEN
		hex_map = Map(width=5, height=5)
		
		# WHEN
		is_inside = hex_map.valid(x=2, y=2)
		is_outside = hex_map.valid(x=5, y=2)
		
		# THEN
		self.assertEqual(is_outside, False)
		self.assertEqual(is_inside, True)


if __name__ == '__main__':
	unittest.main()
