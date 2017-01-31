import json
import os
from distanceMatrix import asin_matrix, build_matrix
from merchant1Constants import ASIN_POSITION_MAP, STORE_LAYOUT_WIDTH, STORE_LAYOUT_HEIGHT, WALL, EMPTY_BLOCK

'''
Merchant-1 Layout: A typical store with 20*20 grid with blocks in-between
'''

layout = [[EMPTY_BLOCK for x in range(STORE_LAYOUT_WIDTH)] for y in range(STORE_LAYOUT_HEIGHT)]
asinDict = {}
asinGrid = {}
asinDistMtx = []

def print_layout():
    for h in range(STORE_LAYOUT_HEIGHT):
        print layout[h]

def create_empty_layout_with_walls():
    for h in range(1, STORE_LAYOUT_HEIGHT-1):
        for block in range(2, len(layout[h]),3):
            layout[h][block] = WALL

def fill_store_in_items():
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(__location__,'merchant1Asins.json')) as asin_data:
        data = json.load(asin_data)

    for k, v in data.iteritems():
        layout[v['X']][v['Y']] = k
        asinDict[k] = {'x':v['X'], 'y':v['Y']}

    for k in asinDict.keys():
        asinGrid[k] = asin_matrix(k, asinDict[k], layout)

def build_asin_distance_matrix():
    global asinDistMtx
    asinDistMtx = build_matrix(asinGrid, asinDict)

def get_asinlist():
    return asinDict

def print_matrix():
    for h in range(len(ASIN_POSITION_MAP.keys())):
        print asinDistMtx[h]

def print_asin_grid(asin):
    grid = asinGrid[asin]
    for h in range(STORE_LAYOUT_WIDTH):
        print grid[h]

def create_store():
    create_empty_layout_with_walls()
    fill_store_in_items()
    build_asin_distance_matrix()
    return layout

def get_matrix():
    return asinDistMtx

