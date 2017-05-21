"""
Rules for a cell:
1. Any live cell with fewer than two live neighbours dies, as if caused by underpopulation.
2. Any live cell with two or three live neighbours lives on to the next generation.
3. Any live cell with more than three live neighbours dies, as if by overpopulation.
4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

Each cell holds:
1. Its position on the map
2. Its current status
"""

int x
int y
bool isAlive


# Check surrounding cells for the current number of live neighbors
def checkNumNeighbors():
	"""
	TODO This needs knowledge of the whole map
	"""

# Check rules above and change isAlive status accordingly
def updateStatus(int numNeighbors):
	if isAlive && (numNeighbors < 2 || numNeighbors > 3):
		isAlive = false
	elif !isAlive && numNeighbors == 3:
			isAlive = true

# Check current status of this cell
def isAlive():
	return isAlive

# Updates the status of this cell
def setAlive(alive):
	isALive = alive

# On each 'tick', a cell will update its status based on the rules
def tick():
	updateStatus(checkNumNeighbors())