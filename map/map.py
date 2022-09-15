"""map main module."""
from ctypes import Union
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
		pass


class HexCube:
	
	def __init__(self, q: int, r: int, s: int):
		self.q = q
		self.r = r
		self.s = s
	
	"""def __init__(self, q: int, s: int):
		self.q = q
		self.s = s
		self.r = -q - s"""
	
	def distance_to(self, cube):
		return max(abs(self.q - cube.q), abs(self.r - cube.r), abs(self.s - cube.s))
	
	def __add__(self, other):
		# if isinstance(other, HexDir):
		#	other = other.value
		return HexCube(q=self.q + other.q, r=self.r + other.r, s=self.s + other.s)
	
	def __mul__(self, factor: int):
		return HexCube(q=self.q * factor, r=self.r * factor, s=self.s * factor)


@dataclass(frozen=True)
class HexDirection(Enum):
	north = 0
	northeast = 1
	southeast = 2
	south = 3
	southwest = 4
	northwest = 5
	
	def cube_direction(self):
		if self.value == HexDirection.north.value:
			return HexCube(q=0, r=1, s=-1)
		elif self.value == HexDirection.northeast.value:
			return HexCube(q=1, r=0, s=-1)
		elif self.value == HexDirection.southeast.value:
			return HexCube(q=1, r=-1, s=0)
		elif self.value == HexDirection.south.value:
			return HexCube(q=0, r=-1, s=1)
		elif self.value == HexDirection.southwest.value:
			return HexCube(q=-1, r=0, s=1)
		elif self.value == HexDirection.northwest.value:
			return HexCube(q=-1, r=1, s=0)
		else:
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
			self.x = cube.q + (cube.s + (cube.s & 1)) / 2
			self.y = cube.s
		else:
			raise ValueError(f"unsupported format: {x}")
		
	def is_neighbor_of(self, point):
		return self.distance_to(hexagon=point) == 1
	
	def neighbor_in(self, direction: HexDirection, distance: int = 1):
		cube_neighbor = self.to_cube() + (direction.cube_direction() * distance)
		return HexPoint(x=cube_neighbor)
	
	def neighbors(self):
		neighboring = [
			self.neighbor_in(direction=HexDirection.north),
			self.neighbor_in(direction=HexDirection.northeast),
			self.neighbor_in(direction=HexDirection.southeast),
			self.neighbor_in(direction=HexDirection.south),
			self.neighbor_in(direction=HexDirection.southwest),
			self.neighbor_in(direction=HexDirection.northwest)
		]
		
		return neighboring
	
	
	def distance_to(self, hexagon):
		self_cube = self.to_cube()
		hex_cube = hexagon.to_cube()
		return self_cube.distance_to(cube=hex_cube)
	
	
	def distance_to(self, x: int, y: int):
		self_cube = self.to_cube()
		hex_cube = HexPoint(x=x, y=y).to_cube()
		return self_cube.distance_to(cube=hex_cube)
	
	
	def to_cube(self):
		# return HexCube(q: hex.x - (hex.y - (hex.y&1)) / 2, s: hex.y) # odd-q
		r = -int(self.x - (self.y + (self.y & 1)) / 2) - self.y
		return HexCube(q=int(self.x - (self.y + (self.y & 1)) / 2), r=r, s=self.y)  # even-q
	
	
	# def areaWith(self, radius: int):
	#	return HexArea(center: self, radius: radius)


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
