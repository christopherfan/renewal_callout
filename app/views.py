from flask import Flask, jsonify, abort, make_response, request,render_template

from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"


tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]


items = [
    {
        'id':1,
        'ActivationID': '5a43-7f71-3098-45ed-9ed1-30dc-aba1-d0a4',
        'Type': 'Subscription',
        'RemainingDays': 90,
        'Product': 'Spotlight',
        'SoldTo': 'Bravo Stage Production',
        'TotalQuantity': 13,
        'ExpirationDate': '2017-10-10',
        'Entitlement': '5a43-7f71-3098-45ed-9ed1-30dc-aba1-d0a4'
        # return self.body
    }
]





@app.route('/todo/api/v1.0/items', methods=['GET'])
def get_items():
    return jsonify({'items': items}) #replaced item



@app.route('/todo/api/v1.0/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = [item for item in items if item['id'] == item_id]
    if len(item) == 0:
        abort(404)
    return jsonify({'item': item[0]})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/todo/api/v1.0/items', methods=['POST'])
def create_item():
    if not request.json or not 'ActivationID' in request.json:
        abort(400)
    
    #Assign POST body to internal strcuture
    item= {
        'id': items[-1]['id'] + 1,
        'ActivationID': request.json['ActivationID'],
        'Type': request.json['Type'],
        'RemainingDays': request.json['RemainingDays'],
        'SoldTo': request.json['SoldTo'],
        'Product': request.json['Product'],
        'TotalQuantity': request.json['TotalQuantity'],
        'ExpirationDate': request.json['ExpirationDate'],
        'Entitlement': request.json['Entitlement'],
    }

#Old Code
    # item = {
    #     'id': items[-1]['id'] + 1,
    #     'title': request.json['title'],
    #     'description': request.json.get('description', ""),
    #     'done': False
    # }



    items.append(item)
    return jsonify({'item': item}), 201



@app.route('/renewal', methods=['GET', 'POST'])
def renewal():
    organization = request.args.get('org')
    #print("organization is ", request.args)
    something = request.args
    #for stuff in something.keys():
     #   print("Parameter=",stuff, " Value=", something[stuff])

    # x = app.models.Renewal_Item()
    # print (x[0])

    return render_template('renewal.html', param=items)