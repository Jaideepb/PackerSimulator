from merchant1Constants import ASIN_POSITION_MAP, STORE_LAYOUT_WIDTH, STORE_LAYOUT_HEIGHT, INIT_WEIGHT, UNIT_TRAVEL_WEIGHT

asinGrid_temp = []

def print_grid():
    for h in range(STORE_LAYOUT_WIDTH):
        print asinGrid_temp[h]

def asin_matrix(asin, loc, layout):
    x1 = loc['x']
    y1 = loc['y']
    global asinGrid_temp
    asinGrid_temp = [[INIT_WEIGHT for x in range(STORE_LAYOUT_WIDTH)] for y in range(STORE_LAYOUT_HEIGHT)]
    find_distance(x1, y1, STORE_LAYOUT_WIDTH - 1, STORE_LAYOUT_HEIGHT - 1, layout, 0)
    return asinGrid_temp

def find_distance(x, y, maxX, maxY, layout, weight):
    if(x<0 or y<0 or x>maxX or y>maxY):
        return
    if(layout[x][y]=='XXX'):
        return
    if(asinGrid_temp[x][y]<weight):
        return
    else :
        if (asinGrid_temp[x][y]>weight):
            asinGrid_temp[x][y] = weight
        find_distance(x-1, y, maxX, maxY, layout, weight + UNIT_TRAVEL_WEIGHT)
        find_distance(x+1, y, maxX, maxY, layout, weight + UNIT_TRAVEL_WEIGHT)
        find_distance(x, y-1, maxX, maxY, layout, weight + UNIT_TRAVEL_WEIGHT)
        find_distance(x, y+1, maxX, maxY, layout, weight + UNIT_TRAVEL_WEIGHT)

def build_matrix(asinGrid, asinDict):
    matrix = [[0 for x in range(len(asinGrid.keys()))] for y in range(len(asinGrid.keys()))]
    asinsList = asinGrid.keys()

    for k in asinsList:
        for j in asinsList:
            matrix[ASIN_POSITION_MAP[k]][ASIN_POSITION_MAP[j]] = asinGrid[k][asinDict[j]['x']][asinDict[j]['y']]

    return matrix