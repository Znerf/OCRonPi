from flask import Flask, jsonify, request, send_from_directory,render_template
from flask_cors import CORS
import json
import requests,base64
# from PyTransmit import FTPClient

# ftp_obj = FTPClient()
#import cv2

app = Flask(__name__,static_url_path='/static')
CORS(app)




@app.route('/h', methods=['GET'])
def get_node_ui():
    print('hg')
    return send_from_directory('ui', 'cam.html')

@app.route('/get', methods=['GET'])
def getim():
    print('gettng image')
    a=open('mage.png','rb')
    return '*'+str(base64.b64encode(a.read()))+'$'
    # return send_from_directory('', 'mage.png')

@app.route('/reques', methods=['POST'])
def getImage():
    values = request.data
    #print(values)
    #print(values)
    if not values:
        response = {'message': 'No data found.'}
        return jsonify(response), 400

    aa=base64.b64decode(values)
    f = open('mage.png', 'wb')
    f.write(aa)
    f.close()
    #z= base64.b64decode(values)
    #cv2.imshow('df',z)
    # a=open('1.jpeg',mode='a')
    # for b in values['image']:
    #     a.write(b)
    # print (values['image'])

    f=open('mage.png','rb')
    # # FTP Details
    # FTP_HOST = "http://localhost"
    # FTP_USER = ""
    # FTP_PASS = ""
    # FTP_PORT = 5000

    # Connect to the server
    # ftp_obj.connect(FTP_HOST, FTP_USER, FTP_PASS, FTP_PORT)
    # print(ftp_obj.get_message())
    import requests

    url = "http://localhost:5000/getData"
    # files = {'image': open('mage.png', 'rb')}
    # headers = {
    #     'authorization': "Bearer {token}"
    # }
    # response = requests.post( url, data={'imasfd':'adadf'})
    # url = "http://localhost:5000/getData"
    # files = {'imageText':'Anythng' }
    # requests.post(url, files=files)
    z=f.read()
    # print(z)
    ze=base64.b64encode(z)
    # ze=base64.b64encode(ze)
    # data = {'imageText': ze,'image':'asdfdf'}
    # headers = {'Content-type': 'application/png', 'Accept': 'text/plain'}
    # r = requests.post(url, files= f.read(),headers=headers)
    # files = {'upload_file': open('mage.png','rb')}
    # values = {'DB': 'photcat', 'OUT': 'csv', 'SHORT': 'short'}
    #
    # r = requests.post(url, files=files, data=json.dumps(values))
    print(ze)
    ef=True
    # while(ef== True):
    z=f.read(1)
    if not z:
        ef=False
    data = {'imageText': 'str(values)','image':'asdfdf'}
    # with open('data.json', 'w') as outfile:
    #     json.dump(data, outfile)

    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    r = requests.post(url, json.dumps(data),headers=headers)#, headers=headers


    response = {'message': 'No data found.'}
    return jsonify(response), 200



if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument('-p', '--port', type=int, default=5005)
    args = parser.parse_args()
    port = args.port
    app.run(host='0.0.0.0', port=port)
