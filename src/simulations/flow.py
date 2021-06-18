r""" 
This file implements radial gas flows in the milky way model 
""" 

from .._globals import vrad 
import numbers 

class flow: 

	r""" 
	Per VICE's requirements for gas migration, this object computes the 
	mass *fraction* of an individual ring which migrates inward as a function 
	of time. 
	""" 

	def __init__(self, zone, dr = 0.1, dt = 0.01): 
		self.zone = zone 
		self.dr = dr 
		self.dt = dt 

	def __call__(self, time): 
		radius = self.dr * (self.zone + 0.5) # middle of the zone in kpc 
		inner = self.dr * self.zone # inside edge of the zone in kpc 
		outer = self.dr * (self.zone + 1) # outer edge of the zone in kpc 
		v = vrad(radius, time) * 1.023 # km/s -> kpc/Gyr 
		return (0.01 / self.dt) * (
			2 * inner * v * self.dt + v**2 * self.dt**2) / (
			outer**2 - inner**2
			) 

	@property 
	def zone(self): 
		r""" 
		Type : float 

		The integer index of the zone this flow object corresponds to. 
		""" 
		return self._zone 

	@zone.setter 
	def zone(self, value): 
		if isinstance(value, int): 
			if value >= 0: 
				self._zone = value 
			else: 
				raise ValueError("Zone index must be non-negative.") 
		else: 
			raise TypeError("Zone must be an integer. Got: %s" % (type(value))) 

	@property 
	def dr(self): 
		r""" 
		Type : float 

		The width of each zone in kpc. 
		""" 
		return self._dr 

	@dr.setter 
	def dr(self, value): 
		if isinstance(value, numbers.Number): 
			if value > 0: 
				self._dr = float(value) 
			else: 
				raise ValueError("Zone width must be non-negative.") 
		else: 
			raise TypeError("Zone width must be a numerical value. Got: %s" % (
				type(value))) 

	@property 
	def dt(self): 
		r""" 
		Type : float 

		The timestep size of the model in Gyr. 
		""" 
		return self._dt 

	@dt.setter 
	def dt(self, value): 
		if isinstance(value, numbers.Number): 
			if value > 0: 
				self._dt = float(value) 
			else: 
				raise ValueError("Timestep size must be positive.") 
		else: 
			raise TypeError("""Timestep size must be a numerical value. \
Got: %s""" % (type(value))) 



