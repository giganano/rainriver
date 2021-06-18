r""" 
Global variables to the migration simulations and plot analysis. 
""" 

END_TIME = 13.2 # total simulation time in Gyr 

# Width of each annulus in kpc 
# This needs modified *only* if running the plotting scripts. If you're running 
# a simulation of a model, the zone_width should be speicified via 
# --zonewidth=XXX on the command line when running the simulations.py file. 
ZONE_WIDTH = 0.1 

MAX_SF_RADIUS = 15.5 # Radius in kpc beyond which the SFR = 0 

# Stellar mass of Milky Way (Licquia & Newman 2015, ApJ, 806, 96) 
M_STAR_MW = 5.17e10 

COLORMAP = "winter" 


def vrad(radius, time): 
	r""" 
	Inward radial flow velocity of the ISM in km/s as a function of radius 
	and simulation time. 

	Parameters 
	----------
	radius : float 
		Galactocentric radius in kpc 
	time : float 
		Simulation time in Gyr 

	Returns 
	-------
	vrad : float 
		The magnitude of the velocity vector pointing inward in km/s 
	""" 
	return 0.7 

