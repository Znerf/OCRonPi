from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import json
import requests

app = Flask(__name__)
CORS(app)


@app.route('/h', methods=['GET'])
def get_node_ui():
    print('hg')
    return send_from_directory('ui', 'cam.html')

@app.route('/check', methods=['POST'])
def getImage():
    values = request.get_json()
    #print(values)

    if not values:
        response = {'message': 'No data found.'}
        return jsonify(response), 400
    # a=open('1.jpeg',mode='a')
    # for b in values['image']:
    #     a.write(b)
    # print (values['image'])
    url = "http://localhost:5000/getData"
    data = {'image': values['image'], 'imageText': 'Bob'}
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    r = requests.post(url, data=json.dumps(data), headers=headers)

    response = {'message': 'No data found.'}
    return jsonify(response), 200


'''
@app.route('/network', methods=['GET'])
def get_network_ui():
    return send_from_directory('ui', 'network.html')


@app.route('/desk', methods=['POST'])
def create_keys():
    desk.create_keys()
    if desk.save_keys():
        global blockchain
        blockchain = Blockchain(desk.public_key, port)
        response = {
            'public_key': desk.public_key,
            'private_key': desk.private_key
        }
        return jsonify(response), 201
    else:
        response = {
            'message': 'Saving the keys failed.'
        }
        return jsonify(response), 500


@app.route('/desk', methods=['GET'])
def load_keys():
    if desk.load_keys():
        global blockchain
        blockchain = Blockchain(desk.public_key, port)
        response = {
            'public_key': desk.public_key,
            'private_key': desk.private_key,
        }
        return jsonify(response), 201
    else:
        response = {
            'message': 'Loading the keys failed.'
        }
        return jsonify(response), 500



@app.route('/broadcast-transaction', methods=['POST'])
def broadcast_transaction():
    values = request.get_json()
    #print(values)
    if not values:
        response = {'message': 'No data found.'}
        return jsonify(response), 400
    required = ['official', 'image', 'imageText', 'signature']
    if not all(key in values for key in required):
        response = {'message': 'Some data is missing.'}
        return jsonify(response), 400
    success = blockchain.add_transaction(
        values['official'], values['image'], values['imageText'], values['signature'], is_receiving=True)
    if success:
        response = {
            'message': 'Successfully added transaction.',
            'transaction': {
                'official': values['official'],
                'image': values['image'],
                'imageText': values['imageText'],
                'signature': values['signature']
            }
        }
        return jsonify(response), 201
    else:
        response = {
            'message': 'Creating a transaction failed.'
        }
        return jsonify(response), 500


@app.route('/broadcast-block', methods=['POST'])
def broadcast_block():
    values = request.get_json()
    if not values:
        response = {'message': 'No data found.'}
        return jsonify(response), 400
    if 'block' not in values:
        response = {'message': 'Some data is missing.'}
        return jsonify(response), 400
    block = values['block']
    if 'index' not in block:
        response = {'message': 'Some data is missing.'}
        return jsonify(response), 400

    print (block)

    if block['index'] == blockchain.chain[-1].index + 1:
        if blockchain.add_block(block):
            response = {'message': 'Block added'}
            return jsonify(response), 201
        else:
            response = {'message': 'Block seems invalid.'}
            print('block seems invalid')
            return jsonify(response), 409
    elif block['index'] > blockchain.chain[-1].index:
        response = {'message': 'Blockchain seems to differ from local blockchain.'}
        blockchain.resolve_conflicts = True
        return jsonify(response), 200
    else:
        response = {'message': 'Blockchain seems to be shorter, block not added'}
        return jsonify(response), 409


@app.route('/transaction', methods=['POST'])
def add_transaction():
    if desk.public_key == None:
        response = {
            'message': 'No wallet set up.'
        }
        return jsonify(response), 400
    values = request.get_json()
    if not values:
        response = {
            'message': 'No data found.'
        }
        return jsonify(response), 400
    required_fields = ['imageText', 'image']
    if not all(field in values for field in required_fields):
        response = {
            'message': 'Required data is missing.'
        }
        return jsonify(response), 400
    image = values['image']
    imageText = values['imageText']
    signature = desk.sign_transaction(desk.public_key, image, imageText)
    success = blockchain.add_transaction(
        desk.public_key,image, imageText, signature)
    if success:
        response = {
            'message': 'Successfully added transaction.',
            'transaction': {
                'official': desk.public_key,
                'image': image,
                'imageText':imageText,
                'signature': signature
            }
        }
        return jsonify(response), 201
    else:
        response = {
            'message': 'Creating a transaction failed.'
        }
        return jsonify(response), 500


@app.route('/mine', methods=['POST'])
def mine():
    if blockchain.resolve_conflicts:
        response = {'message': 'Resolve conflicts first, block not added!'}
        return jsonify(response), 409
    block = blockchain.mine_block()
    if block != None:
        #dict_block = block.__dict__.copy()
        #dict_block['transactions'] = [
        #    tx.__dict__ for tx in dict_block['transactions']]
        response = {
            'message': 'Block added successfully.',
            # 'block': block,
        }
        return jsonify(response), 201
    else:
        response = {
            'message': 'Adding a block failed.',
            'desk_set_up': desk.public_key != None
        }
        return jsonify(response), 500


@app.route('/resolve-conflicts', methods=['POST'])
def resolve_conflicts():
    replaced = blockchain.resolve()
    if replaced:
        response = {'message': 'Chain was replaced!'}
    else:
        response = {'message': 'Local chain kept!'}
    return jsonify(response), 200


@app.route('/transactions', methods=['GET'])
def get_open_transaction():
    transactions = blockchain.get_open_transactions()
    dict_transactions = [tx.__dict__ for tx in transactions]
    return jsonify(dict_transactions), 200


@app.route('/chain', methods=['GET'])
def get_chain():
    chain_snapshot = blockchain.chain
    dict_chain = [block.__dict__.copy() for block in chain_snapshot]
    for dict_block in dict_chain:
        dict_block['transactions'] = [
            tx.__dict__ for tx in dict_block['transactions']]
    return jsonify(dict_chain), 200


@app.route('/node', methods=['POST'])
def add_node():
    values = request.get_json()
    if not values:
        response = {
            'message': 'No data attached.'
        }
        return jsonify(response), 400
    if 'node' not in values:
        response = {
            'message': 'No node data found.'
        }
        return jsonify(response), 400
    node = values['node']
    blockchain.add_peer_node(node)
    response = {
        'message': 'Node added successfully.',
        'all_nodes': blockchain.get_peer_nodes()
    }
    return jsonify(response), 201


@app.route('/node/<node_url>', methods=['DELETE'])
def remove_node(node_url):
    if node_url == '' or node_url == None:
        response = {
            'message': 'No node found.'
        }
        return jsonify(response), 400
    blockchain.remove_peer_node(node_url)
    response = {
        'message': 'Node removed',
        'all_nodes': blockchain.get_peer_nodes()
    }
    return jsonify(response), 200


@app.route('/nodes', methods=['GET'])
def get_nodes():
    nodes = blockchain.get_peer_nodes()
    response = {
        'all_nodes': nodes
    }
    return jsonify(response), 200
'''


if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument('-p', '--port', type=int, default=5005)
    args = parser.parse_args()
    port = args.port
    app.run(host='0.0.0.0', port=port)
