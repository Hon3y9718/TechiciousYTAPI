from flask import Flask, jsonify
from FetchData import SearchFunc, fetchRequiredData, getChannelVideos

app = Flask(__name__)

channel_id = 'UC5SMqP_8QsmPDWhNmjgInlg'
uploads_playlist = 'UU5SMqP_8QsmPDWhNmjgInlg'
rftString = ['Reflections for Today', 'Reflection for Today']
QnAString = ['Question and Answer', 'Questions and Answers']

@app.route('/')
def Home():
    inforMation = 'In Order to get videos Related to \nQuestion and Answer - /qna\nReflection for Today - /rft \nFor All Videos - /Everything'
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

if __name__ == "__main__":
    app.run()