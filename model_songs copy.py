import random

song_data = []
sadsong_list = [
    "I Bet On Losing Dogs by Mitski"
    "Matilda by Harry Styles",
    "Music For a Sushi Restaurant by Harry Styles",
    "Mirrorball by Taylor Swift",
    "About You by The 1975",
    "Kyoto by Phoebe Bridgers",
    "Les by Childish Gambino",
    "Freakin' Out On the Interstate by Briston Maroney"
    "Lonely Bones by dodie",
    "Scott Street by Phoebe Bridgers",
    "dumb dumb by mazie",
    "Dark Red by Steve Lacy",
    "Infrunami by Steve Lacy",
    "She Plays Bass by beabadoobee",
    "Japanese Denim by Daniel Caesar",
    "I THINK by Tyler, The Creator",
    "Long Way Down by Dr. Dog",
    "Baby I'm Yours by Artic Monkeys",
    "White Ferrari by Frank Ocean",
    'Iceblink Luck by Cocteau Twins'

    "First Love/Late Spring by Mitski",
    "YKWIM? by Yot Club",
    "Last Words of a Shooting Star by Mitski",
    "Liquid Smooth by Mitski",
    "While My Guitar Gently Weeps by The Beatles",
- ["Francis Forever by Mitski",
- ["Thank You by Dido",
- ["I Bet on Losing Dogs by Mitski",
- ["Twilight by bôa",
- ["People by Agust D",
- ["It just is by eaj ft. Seori]",
- ["Who by Lauv ft. BTS",
- ["eclipse by ASH ISLAND",
- ["Pity Party by Melanie Martinez",
- ["See You Again by Wiz Khalifa ft. Charlie Puth",
- ["Let You Down by NF",
- ["Better Now by Post Malone",
- ["One Last Time by Ariana Grande",
- ["Dive with you by Seori ft. eaj",
- ["The One That Got Away by Katy Perry",
- ["Breakeven by The Script",
- ["Let Her Go by Passenger",
- ["Talking to the Moon by Bruno Mars",
- ["The Scientist by Coldplay",
- ["I took a pill in Ibiza by Mike Posner",
- ["Jealous by Labrinth"
]

# Initialize jokes
def initSongs():
    # setup jokes into a dictionary with id, joke, haha, boohoo
    item_id = 0
    for item in song_list:
        song_data.append({"id": item_id, "song": item, "sad": 0, "happy": 0})
        item_id += 1
    # prime some haha responses
    for i in range(10):
        id = getRandomSong()['id']
        addSongSad(id)
    # prime some haha responses
    for i in range(5):
        id = getRandomSong()['id']
        addSongHappy(id)
        
# Return all jokes from jokes_data
def getSongs():
    return(song_data)

# Joke getter
def getSong(id):
    return(song_data[id])

# Return random joke from jokes_data
def getRandomSong():
    return(random.choice(song_data))

# Liked joke
def favoriteSong():
    best = 0
    bestID = -1
    for song in getSongs():
        if song['sad'] > best:
            best = song['sad']
            bestID = song['id']
    return song_data[bestID]
    
# Jeered joke
def sadSong():
    worst = 0
    worstID = -1
    for song in getSong():
        if song['happy'] > worst:
            worst = song['happy']
            worstID = song['id']
    return song_data[worstID]

# Add to haha for requested id
def addSongSad(id):
    song_data[id]['sad'] = song_data[id]['sad'] + 1
    return song_data[id]['sad']

# Add to boohoo for requested id
def addSongHappy(id):
    song_data[id]['happy'] = song_data[id]['happy'] + 1
    return song_data[id]['happy']

# Pretty Print joke
def printSong(song):
    print(song['id'], song['Song'], "\n", "Sad:", song['sad'], "\n", "Happy:", song['happy'], "\n")

# Number of jokes
def countSongs():
    return len(song_data)

# Test Joke Model
if __name__ == "__main__": 
    initSongs()  # initialize jokes
    
    # Most likes and most jeered
    best = favoriteSong()
    print("Most sad", best['sad'])
    printSong(best)
    worst = sadSong()
    print("Most happy", worst['happy'])
    printSong(worst)
    
    # Random joke
    print("Random song")
    printSong(getRandomSong())
    
    # Count of Jokes
    print("Song Count: " + str(countSongs()))