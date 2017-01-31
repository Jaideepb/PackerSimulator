from merchant1Layout import get_matrix
from merchant1Constants import ASIN_POSITION_MAP, QUANTITY
from pprint import pprint
import time
import numpy as np
import packerHelper

def get_packlist(order, packer):
    packlist = {}
    asinList = order['asinList']
    startingPoint = 'A0'
    last_asin = startingPoint
    packlist_asinlist = []
    time_after_packing = time.time()
    startTimeInEpoch = time_after_packing
    startTime = time.asctime(time.localtime(startTimeInEpoch))
    for l in asinList:
        packlist_asin = {}
        pkT = packerHelper.timefor_packer(get_distance_from_asin_to_asin(last_asin, l['asin']), packer, QUANTITY)
        packlist_asin['asin'] = l['asin']
        packlist_asin['category'] = l['category']
        time_after_packing = time_after_packing + pkT + get_jitter()
        time_after_packing_localtime = time.asctime(time.localtime(time_after_packing))
        packlist_asin['pickTimeEpoch'] = time_after_packing
        packlist_asin['pickTime'] = time_after_packing_localtime
        last_asin = l['asin']
        packlist_asinlist.append(packlist_asin)

    orderClosingTime = get_distance_from_asin_to_asin(last_asin, startingPoint)
    endTimeInEpoch = time_after_packing+orderClosingTime
    endTime = time.asctime(time.localtime(endTimeInEpoch))

    packlist['orderId'] = order['orderId']
    packlist['packlistStartTime'] = startTime
    packlist['packlistStartTimeEpoch'] = startTimeInEpoch
    packlist['packlistEndTimeEpoch'] = endTimeInEpoch
    packlist['packlistEndTime'] = endTime
    packlist['TimeToPack'] = endTimeInEpoch - startTimeInEpoch
    packlist['asinList'] = packlist_asinlist
    packlist['packer'] = packer['id']
    pprint(packlist)
    return packlist

def get_distance_from_asin_to_asin(fromAsin, toAsin):
    asinDistMtx = get_matrix()
    return asinDistMtx[ASIN_POSITION_MAP[fromAsin]][ASIN_POSITION_MAP[toAsin]]

def get_jitter():
    return np.random.normal(0,4,5)[0]

def packOrder(order_json):
    packer = packerHelper.fetch_picker()
    if packer is not None:
        return get_packlist(order_json, packer)
    else:
        return {"ErrorMsg": "Unable to find packer"}