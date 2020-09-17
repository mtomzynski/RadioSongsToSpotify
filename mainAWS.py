import requests
import datetime
import time

# url = 'http://nowyswiat.online/wp-content/plugins/wp-lunaradio/current.txt'
# currentTime = (datetime.datetime.now()).strftime('%H:%M')
# filePath = '/home/ec2-user/TheNewWorldRadio/TheNewWorldRadioSongs.txt'

"""
Simple function to get single song's title from given url of http://nowyswiat.online.
"""
def getSong(url):
    requests.encoding = 'utf-8'
    song = requests.get(url).text
    return song


"""
The function returns a collection of songs found so far.
The main reason to run it, it is because if program stops and runs again, it starts with clear set of song
and it will not check already saved songs in the file.
"""
def getSongsSetRead(filePath):
    songsSet = set(open(filePath, mode='r', encoding='utf-8').read().split('\n'))
    return songsSet


"""
The "main" function
"""
def saveSongs(whiletime, url, filePath):
    # get current set of songs from saved file
    songsSet = getSongsSetRead(filePath)
    while (datetime.datetime.now()).strftime('%H:%M') <= whiletime:
        # get currently played song
        currentSong = getSong(url)
        if currentSong not in songsSet and currentSong not in ['', ' ', 'Radio Nowy Swiat - Pion i poziom!'] and currentSong.find('Radio Nowy') == -1:
            print(currentSong)
            with open(filePath, mode='a', encoding='utf-8') as songsFile:
                songsFile.write('\n')
                songsFile.write(currentSong)
        # after saving, add currently played song to set
        songsSet.add(currentSong)
        time.sleep(30)
    return None

# def deleteDuplicatesFromFile(filePath):
#     with open(filePath, mode='a', encoding='utf-8') as songsFile:
#         for line in songsFile:
#             print(line)

saveSongs('23:59'
          ,'http://nowyswiat.online/wp-content/plugins/wp-lunaradio/current.txt'
          ,'/home/ec2-user/TheNewWorldRadio/TheNewWorldRadioSongs.txt')
