import json, os
from random import randint

packers = {}

def get_PackersInfo():
    global packers
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(__location__,'packerInfo.json')) as packer_info:
        packers = json.load(packer_info)

def fetch_picker():
    pkrIdx = str(randint(0, 4))
    if pkrIdx in packers:
        return packers[pkrIdx]
    else:
        return None

def timefor_packer(distance, packer, quantity):
    packerWalkingSpeed = packer['walkingSpeed']
    packerPickingSpeed = packer['pickingSpeed']

    walkingTime = distance/packerWalkingSpeed
    pickingTime = quantity/packerPickingSpeed
    return walkingTime + pickingTime