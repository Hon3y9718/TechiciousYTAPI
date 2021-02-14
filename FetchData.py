from apiclient.discovery import build
import json

api_key = 'AIzaSyCdKVqEjxTV8xT25X6dk1B-xxUA7fyYrjk'
channel_id = 'UC5SMqP_8QsmPDWhNmjgInlg'
uploads_playlist = 'UU5SMqP_8QsmPDWhNmjgInlg'

youtube = build('youtube', 'v3', developerKey=api_key)

def getChannelVideos(channelId):
    res = youtube.channels().list(id=channelId, part='contentDetails', maxResults=1).execute()
    playlistId= res['items'][0]['contentDetails']['relatedPlaylists']['uploads']
    videos = []
    nextPage_token = None
    while 1:
        req = youtube.playlistItems().list(playlistId=uploads_playlist, part='snippet, id', maxResults=50, pageToken=nextPage_token).execute()

        videos += req['items']

        nextPage_token = req.get('nextPageToken')

        if nextPage_token is None:
            break

    return videos

def SearchFunc(channel_id, SearchStr):
    videos = getChannelVideos(channel_id)
    count = 0
    listOfVideos = []
    
    for video in videos:
        for Search in SearchStr:
            if Search.lower() in video['snippet']['title'].lower():
                listOfVideos.append(video)
                count = count+1

    with open('fileChannel.json', 'w') as f:
        jsonObject = json.dumps(listOfVideos)
        f.write(jsonObject)
    
def fetchRequiredData(FileName):
    file = open(FileName, 'r')
    jsonObject = json.load(file)
    DataList = []

    for i in range(len(jsonObject)):
        title = jsonObject[i]['snippet']['title']
        thumbnailUrl = jsonObject[i]['snippet']['thumbnails']['default']['url']
        thumbnailHeight = jsonObject[i]['snippet']['thumbnails']['default']['height']
        thumbnailWidth = jsonObject[i]['snippet']['thumbnails']['default']['width']
        ChannelTitle = jsonObject[i]['snippet']['channelTitle']
        VideoID = jsonObject[i]['snippet']['resourceId']['videoId']
        publishedAt = jsonObject[i]['snippet']['publishedAt']
        VideoUrl = 'https://www.youtube.com/watch?v='+VideoID
        embedURL = 'https://www.youtube.com/embed/'+VideoID

        Dict = {'Main': {
            'title':title,
            'ThumbNailDetails':{
            'thumbnailUrl':thumbnailUrl,
            'thumbnailHeight':thumbnailHeight,
            'thumbnailWidth':thumbnailWidth,
            },
            'VideoDetails':{
                'videoId':VideoID,
                'videoURL':VideoUrl,
                'embedURL':embedURL,
                'publishedAt': publishedAt,
                'channelName':ChannelTitle
            }
        },
        'APIBy': 'Techicious'
        }
        DataList.append(Dict)
    return DataList

#Fetch others
def SearchotherFunc(channel_id):
    videos = getChannelVideos(channel_id)
    count = 0
    listOfVideos = []
    listOfVideosREQ= []
    checked=True
    SearchStr1= ['Reflections for Today']
    SearchStr2= ['Reflection of Today'] 
    SearchStr3=['Reflections of Today']
    SearchStr4= ['Reflection for Today']
    SearchStr5=['Question and Answer']
    SearchStr6= ['Questions and Answers']
    #SearchStr=['The On-time Deliverance']
    
    for video in videos:
        for Search in SearchStr1:
            if Search.lower() not in video['snippet']['title'].lower():
                for Search2 in SearchStr2:
                    if Search2.lower() not in video['snippet']['title'].lower():
                        for Search3 in SearchStr3:
                            if Search3.lower() not in video['snippet']['title'].lower():
                                for Search4 in SearchStr4:
                                    if Search4.lower() not in video['snippet']['title'].lower():
                                        for Search5 in SearchStr5:
                                            if Search5.lower() not in video['snippet']['title'].lower():
                                                for Search6 in SearchStr6:
                                                    if Search6.lower() not in video['snippet']['title'].lower():
                                                        listOfVideos.append(video)

    with open('fileChannel.json', 'w') as f:
        jsonObject = json.dumps(listOfVideos)
        f.write(jsonObject)
