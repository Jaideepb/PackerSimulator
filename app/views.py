from app import app
from flask import jsonify, request
from app.Stores.packlistGenerator import packOrder

packlistModel = {
    'orderId' : 'ORDER-ID',
    'packlistStartTime' : 'EPOCH_TIME',
    'packlistEndTime' : 'EPOCH_TIME',
    'asinList' :
    [
        {

            'asin' : 'ASIN1',
            'category' : 'Fruits',
            'pickTime' : 'EPOCH_TIME'
        },
        {
            'asin' : 'ASIN2',
            'category' : 'Diary',
            'pickTime' : 'EPOCH_TIME'
        }
    ]
}

@app.route('/packerSimulator/getPacklistModel',methods=['GET'])
def get_packlist_model():
    return jsonify({'packlist' : packlistModel})

@app.route('/packerSimulator/packOrder', methods=['POST'])
def get_packlist():
    # if not request.json or 'orderId' in request.json:
    if not request.json or not 'orderId' in request.json:
        # abort(400)
        return jsonify({'Response': 400})

    order_data = request.json

    packlist = packOrder(order_data)

    return jsonify({'Response' : packlist}), 201
