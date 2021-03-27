"""
Plotting parameters
"""

# Seed for reproducibility
SEED: int = 100

# Number of frames to render
FRAMES: int = 100

# X, Y, Z noise shape 
SHAPE = [600, 400, FRAMES]

# Number of periods of noise to generate along each axis
# RESOLUTION must be multiple of SHAPE
RESOLUTION = [5, 5, 1]

# Number of particles to move through the field
N_PARTICLES: int = 10

# Color the particle traces make
TRACE_COLOR = 'grey'