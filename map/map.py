"""map main module."""
from dataclasses import dataclass
from enum import Enum


class Tile:
	"""
		class that encapsulates single map tile
	"""
	
	def __init__(self):
		"""
			default constructor
		"""
		self.dummy = 0


class HexCube:
	"""
		class that represents a HexPoint in cube coordinates
	"""
	
	def __init__(self, q: int, r: int, s: int):
		"""
			value constructor
		
			:param q: q coord of HexCube
			:param r: r coord of HexCube
			:param s: s coord of HexCube
		"""
		self.q_val = q
		self.r_val = r
		self.s_val = s
	
	def distance_to(self, cube):
		"""
			calculate the distance in points (int)
		
			:param cube: cube the distance should be evaluated
			:return: distance to cube
		"""
		return max(abs(self.q_val - cube.q_val), abs(self.r_val - cube.r_val), abs(self.s_val - cube.s_val))
	
	def __add__(self, other):
		"""
			+ operator to add two HexCube
		
			:param other: HexCube to add
			:return: sum of two HexCubes
		"""
		if isinstance(other, HexCube):
			return HexCube(q=self.q_val + other.q_val, r=self.r_val + other.r_val, s=self.s_val + other.s_val)

		raise Exception(f'not a valid type: {other}')
	
	def __mul__(self, factor: int):
		"""
			scale HexCube with factor
		
			:param factor: factor to scale the HexCube
			:return: scaled
		"""
		if isinstance(factor, int):
			return HexCube(q=self.q_val * factor, r=self.r_val * factor, s=self.s_val * factor)

		raise Exception(f'not a valid type: {factor}')


@dataclass(frozen=True)
class HexDirection(Enum):
	"""
		enum that represents all 6 possible directions (n, ne, se, s, sw, nw)
	"""
	north = 0
	northeast = 1
	southeast = 2
	south = 3
	southwest = 4
	northwest = 5
	
	def cube_direction(self):
		"""
			get a HexCube value for each of the enum directions
		
			:return: HexCube in the values direction
		"""
		if self.value == HexDirection.north.value:
			return HexCube(q=0, r=1, s=-1)
		
		if self.value == HexDirection.northeast.value:
			return HexCube(q=1, r=0, s=-1)
		
		if self.value == HexDirection.southeast.value:
			return HexCube(q=1, r=-1, s=0)
		
		if self.value == HexDirection.south.value:
			return HexCube(q=0, r=-1, s=1)
		
		if self.value == HexDirection.southwest.value:
			return HexCube(q=-1, r=0, s=1)
		
		if self.value == HexDirection.northwest.value:
			return HexCube(q=-1, r=1, s=0)

		raise Exception(f'not a valid direction: {self.value}')


class HexPoint:
	"""
		class that encapsulates a hexagonal location / point
	"""
	
	def __init__(self, x: int, y: int = -1):
		"""
			hexagonal point constructor
		
			:param x: x coord or HexCube
			:param y: y coord
		"""
		if isinstance(x, int) and isinstance(y, int):
			self.x = x
			self.y = y
		elif isinstance(x, HexCube) and y == -1:
			# self.init(x: cube.q + (cube.s - (cube.s & 1)) / 2, y: cube.s) // odd - q
			# even - q
			cube = x
			self.x = int(cube.q_val + (cube.s_val + (cube.s_val & 1)) / 2)
			self.y = int(cube.s_val)
		else:
			raise ValueError(f"unsupported format: {x}")
		
	def is_neighbor_of(self, point):
		"""
			check if given point is a direct neighbor
			
			:param point: point to check if it is a direct neighbor
			:return: true if point is direct neighbor
		"""
		return self.distance_to(point) == 1
	
	def neighbor_in(self, direction: HexDirection, distance: int = 1):
		"""
			get neighbor in direction (and distance)
		
			:param direction: direction the neighbor is in
			:param distance: distance the neighbor is in
			:return: get the neighbor in given direction and given distance (default: 1)
		"""
		cube_neighbor = self.to_cube() + (direction.cube_direction() * distance)
		return HexPoint(x=cube_neighbor)
	
	def neighbors(self):
		"""
			get all 6 neighbors of the point
		
			:return: all 6 neighbors of the point
		"""
		neighboring = [
			self.neighbor_in(direction=HexDirection.north),
			self.neighbor_in(direction=HexDirection.northeast),
			self.neighbor_in(direction=HexDirection.southeast),
			self.neighbor_in(direction=HexDirection.south),
			self.neighbor_in(direction=HexDirection.southwest),
			self.neighbor_in(direction=HexDirection.northwest)
		]
		
		return neighboring

	def distance_to(self, x, y: int = -1):
		"""
			get the distance to
			a) point with (x,y) coord
			b) other HexPoint
		
			:param x: x coord or HexPoint
			:param y: y coord or not provided (defaults to -1)
			:return: distance to point
		"""
		if isinstance(x, int) and isinstance(y, int):
			self_cube = self.to_cube()
			hex_cube = HexPoint(x=x, y=y).to_cube()
			return self_cube.distance_to(cube=hex_cube)
		
		if isinstance(x, HexPoint) and y == -1:
			hexagon = x
			self_cube = self.to_cube()
			hex_cube = hexagon.to_cube()
			return self_cube.distance_to(cube=hex_cube)

		raise ValueError(f"unsupported format: {x}")
	
	def to_cube(self):
		"""
			converts HexPoint to HexCube representation
		
			:return: HexCube representation of current point
		"""
		# return HexCube(q: hex.x - (hex.y - (hex.y&1)) / 2, s: hex.y) # odd-q
		r = -int(self.x - (self.y + (self.y & 1)) / 2) - self.y
		return HexCube(q=int(self.x - (self.y + (self.y & 1)) / 2), r=r, s=self.y)  # even-q
	
	# def areaWith(self, radius: int):
	#	return HexArea(center: self, radius: radius)
	
	def __str__(self):
		"""
			string representation
			
			:return: string representation
		"""
		return f'HexPoint({self.x}, {self.y})'
	
	def __repr__(self):
		"""
			string representation

			:return: string representation
		"""
		return f'HexPoint({self.x}, {self.y})'
	
	def __eq__(self, other):
		"""
			compares current to other HexPoint
		
			:param other: other HexPoint
			:return: true, if equal (x == x and y == y) - false, otherwise
		"""
		if isinstance(other, HexPoint):
			return self.x == other.x and self.y == other.y

		raise Exception(f'unsupported comparison type {type(other)}')


class Map:
	"""
		class that encapsulates a map
	"""
	
	def __init__(self, width: int, height: int):
		"""
			value constructor
			
			:param width: width of map
			:param height: height of map
		"""
		self.width = width
		self.height = height
		self.tiles = [[Tile() for x in range(width)] for y in range(height)]
	
	def get(self, x: int, y: int):
		"""
			get tile at coord (x, y)
		
			:param x: x coord of tile ot return
			:param y: y coord of tile ot return
			:return: tile at coord (x, y) or None if coord (x, y) is not valid
		"""
		if not self.valid(x, y):
			return None
		
		return self.tiles[x][y]
	
	def valid(self, x: int, y: int):
		"""
			checks if coord (x, y) is valid
			
			:param x: x coord to check
			:param y: y coord to check
			:return: true, if coord (x, y) is valid - false, otherwise
		"""
		return 0 <= x < self.width and 0 <= y < self.height
