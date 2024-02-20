
"""
stmt = 'statement'; Vilken kod man ska testa.
number = 'number of iterations'; Testar 'number' antal gånger och tar snabbaste.
"""


class Song:
    def __init__(self, rad):
        self.trackid = rad[0]
        self.låttid = rad[1]
        self.artist = rad[2]
        self.låttitel = rad[3]

    def __lt__(self, other):
        return self.låttitel < other.låttitel


song_list = []
artist_list = []
track_list = []
with open('unique_tracks.txt', 'r', encoding='utf-8') as f:
    for row in f.readlines():
        row = row.rstrip('\n').split('<SEP>')
        song_list.append(Song(row))
        artist_list.append(row[2])
        track_list.append(row[3])




