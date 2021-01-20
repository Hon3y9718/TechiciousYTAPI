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
    with open('AllVids.json', 'w') as f:
        json.dump(videos, f)

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
        VideoUrl = 'https://www.youtube.com/watch?v='+VideoID

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
                'channelName':ChannelTitle
            }
        },
        'APIBy': 'Techicious'
        }
        DataList.append(Dict)
    return DataList
