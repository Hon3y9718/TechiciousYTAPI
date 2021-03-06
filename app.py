from flask import Flask, json, jsonify
from flask_cors import CORS
from FetchData import SearchFunc, fetchRequiredData, getChannelVideos, SearchotherFunc

app = Flask(__name__)
CORS(app)

channel_id = 'UC5SMqP_8QsmPDWhNmjgInlg'
uploads_playlist = 'UU5SMqP_8QsmPDWhNmjgInlg'
rftString = ['Reflections for Today', 'Reflection for Today']
QnAString = ['Question and Answer', 'Questions and Answers']

@app.errorhandler(404) 
def ErrorHandler(e):
    return f'You found nothing its a 404 Error'

@app.route('/')
def Home():
    inforMation = 'In Order to get videos Related to \nQuestion and Answer - /qna\nReflection for Today - /rft \n All Except for QnA and RFT - /others'
    return inforMation

@app.route('/qna')
def FetchQnA():
    SearchFunc(channel_id, QnAString)
    Data = fetchRequiredData('fileChannel.json')
    return jsonify(Data)

@app.route('/rft')
def FetchRFT():
    SearchFunc(channel_id, rftString)
    Data = fetchRequiredData('fileChannel.json')
    return jsonify(Data)

@app.route('/everything')
def FetchEverything():
    getChannelVideos(channel_id)
    Data = fetchRequiredData('AllVids.json')
    return jsonify(Data)

@app.route('/others')
def Other():
    SearchotherFunc(channel_id)
    Data = fetchRequiredData('fileChannel.json')
    return jsonify(Data)

if __name__ == "__main__":
    app.run()
