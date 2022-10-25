import random

# dictionary with songs added in; this dictionary is specific to sad songs
song_data = []
sadsong_list = [
    "First Love/Late Spring by Mitski",
    "YKWIM? by Yot Club",
    "Last Words of a Shooting Star by Mitski",
    "Liquid Smooth by Mitski",
    "While My Guitar Gently Weeps by The Beatles",
    "Francis Forever by Mitski",
    "Thank You by Dido",
    "I Bet on Losing Dogs by Mitski",
    "Twilight by bôa",
    "People by Agust D",
    "It just is by eaj ft. Seori]",
    "Who by Lauv ft. BTS",
    "eclipse by ASH ISLAND",
    "Pity Party by Melanie Martinez",
    "See You Again by Wiz Khalifa ft. Charlie Puth",
    "Let You Down by NF",
    "Better Now by Post Malone",
    "One Last Time by Ariana Grande",
    "Dive with you by Seori ft. eaj",
    "The One That Got Away by Katy Perry",
    "Breakeven by The Script",
    "Let Her Go by Passenger",
    "Talking to the Moon by Bruno Mars",
    "The Scientist by Coldplay",
    "I took a pill in Ibiza by Mike Posner",
    "Jealous by Labrinth"
]

# function initsongs is defined
def initSongs():
    # setup songs into a dictionary with id sad or happy, randomly
    item_id = 0
    for item in song_list:
        song_data.append({"id": item_id, "song": item, "sad": 0, "happy": 0})
        item_id += 1
    # assign song as sad
    for i in range(10):
        id = getRandomSong()['id']
        addSongSad(id)
    # assign song as happy
    for i in range(5):
        id = getRandomSong()['id']
        addSongHappy(id)
        
# Return all songs from songs_data
def getSongs():
    return(song_data)

# define song getter function
def getSong(id):
    return(song_data[id])

# Return a random song from song_data
def getRandomSong():
    return(random.choice(song_data))

# sad voted song song
def favoriteSong():
    best = 0
    bestID = -1
    for song in getSongs():
        if song['sad'] > best:
            best = song['sad']
            bestID = song['id']
    return song_data[bestID]
    
# sad song
def sadSong():
    worst = 0
    worstID = -1
    for song in getSong():
        if song['happy'] > worst:
            worst = song['happy']
            worstID = song['id']
    return song_data[worstID]

# Add to sad songs for requested id
def addSongSad(id):
    song_data[id]['sad'] = song_data[id]['sad'] + 1
    return song_data[id]['sad']

# Add to happy songs for requested id
def addSongHappy(id):
    song_data[id]['happy'] = song_data[id]['happy'] + 1
    return song_data[id]['happy']

# print happy/ sad song
def printSong(song):
    print(song['id'], song['Song'], "\n", "Sad:", song['sad'], "\n", "Happy:", song['happy'], "\n")

# Number of songs
def countSongs():
    return len(song_data)

# Test song Model
if __name__ == "__main__": 
    initSongs()  # initialize jokes
    
    # Most likes and most jeered
    best = favoriteSong()
    print("Most sad", best['sad'])
    printSong(best)
    worst = sadSong()
    print("Most happy", worst['happy'])
    printSong(worst)
    
    # Random song
    print("Random song")
    printSong(getRandomSong())
    
    # Count of songs
    print("Song Count: " + str(countSongs()))