from googleapiclient.discovery import build
import os
# Arguments that need to passed to the build function
DEVELOPER_KEY = 'key'
#print(DEVELOPER_KEY)
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

# creating Youtube Resource Object
youtube_object = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                       developerKey=DEVELOPER_KEY)


def youtube_search_keyword(query, video, max_results):
    # calling the search.list method to
    # retrieve youtube search results
    try:
        search_keyword = youtube_object.search().list(q=query, part="id, snippet",
                                                      maxResults=max_results).execute()

        # extracting the results from search response
        results = search_keyword.get("items", [])
        print(results)
        # empty list to store video,
        # channel, playlist metadata
        videos = []
        playlists = []
        channels = []
        print(results)
        # extracting required info from each result object
        for result in results:

            # video result object
            if result['id']['kind'] == "youtube#video":
                videos.append("\n*Video title* : ▶ *{}*   \n\nvideo URL : https://www.youtube.com/watch?v={}\n".format(result["snippet"]["title"],
    result['id']['videoId']))

            # playlist result object
            elif result['id']['kind'] == "youtube#playlist":
                playlists.append("\n*PlayList title* : ▶ *{}*   \n\nPlaylist URL : https://www.youtube.com/playlist?list={}\n".format(result["snippet"]["title"],
    result['id']['playlistId']))

            # channel result object
            elif result['id']['kind'] == "youtube#channel":
                channels.append("\n*Channel Name* : ▶ *{}*     \n\nChannel URL : https://www.youtube.com/channel/{}\n\nChannel description : {}\n\n\n".format(result["snippet"]["title"],
                                                           result['id']['channelId'] , result['snippet']['description']))

        ideos ="Videos : \n {} \n".format("".join(videos))
        hannels=" \n {} \n".format("".join(channels))
        laylists="Playlists : \n {} \n".format("".join(playlists))
        print('before video , channel and playlist')
        if video.get('data_type')=='video':
            return ideos

        elif video.get('data_type')=='playlist':
            return laylists
        elif video.get('data_type')=='channel':
            if len(hannels)<10:
                return hannels
            else:
                chan = "\n"+hannels.split("\n\n\n")[0]
                #res = chan[1]
                return chan
        else:
            if len(hannels.split('\n'))>3:
                s = "Result for the following is : \n{} \n{} \n\n".format(ideos , hannels )
            else:
                s=ideos
            return s

    except Exception:
        print('error \n'+Exception)

#youtube_search_keyword('shutterclosed', max_results=7)

