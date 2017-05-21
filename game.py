import sys

import pygame
import numpy
import pygame.surfarray as surfarray

"""
Rules:
1. Any live cell with fewer than two live neighbours dies, as if caused by underpopulation.
2. Any live cell with two or three live neighbours lives on to the next generation.
3. Any live cell with more than three live neighbours dies, as if by overpopulation.
4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
"""

WHITE = (255,255,255)
BLACK = (0,0,0)

def main(width, height):

	pygame.init()
	allCells = numpy.zeroes((width,height)) #make the board with the input width/height

	display = pygame.display.set_mode((width, height), 0, 32)
	display.fill(WHITE) #TODO why isn't this working?

	#displays a surface using allCells
	surfarray.blit_array(display, allCells)
	pygame.display.flip()
	pygame.display.set_caption("Game of Life")

	# Game loop
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
		pygame.display.update() #TODO add sleep here





main(int(sys.argv[1]), int(sys.argv[2]))