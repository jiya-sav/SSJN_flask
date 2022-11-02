import random

song_data = []
song_list = [
    # from sad fastpages:
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
    "It just is by eaj ft. Seori",
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
    "Jealous by Labrinth",
    "In the End by Linkin Park",

    # from joy fastpages:
    "Bumblebee by Dora Jar",
    "Jackie and Wilson by Hozier",
    "Pumpkin by Regrettes",
    "Solar Power by Lorde",
    "Marvelous by Wallows",
    "Island In The Sun by Weezer",
    "Olivia by One Direction",
    "Mr. Blue Sky by Electric Light Orchestra",

    # Indian genre additions
    "Chammak Challo by Akon",
    "Badtameez Dil by Pritam",
    "Gallan Goodiyaan by Yashita Sharma",
    "Kajra Re by Shankar",
    "Dard-E-Disco by Sukhwinder Singh",
    "Chaiyya Chaiyya by Sukhwinder Singh",
    "Laila Main Laila by Pawni Pandey",
    "3 Peg by Sharri Man",
    "Taal se Taal by Alka Yagnik",
    "Ticket to Hollywood by Shankar-Ehsaan-Loy",
    "Laung Laachi by Mannat Noor",
    "Dil Chahta Hai by Shankar Mahadevan",
    "Dil Dhadakne Do by Joi Barua",
    "Ajab Si by KK",
    "Wakhra Swag by Navv Inder",
    "Ghoomar by Shreya Ghoshal",
    "Proper Patola by Diljit Dosanjh",
    "Tamma Tamma Loge by Bappi Lahiri",
    "Balam Pichkari by Pritam",
    "The Disco Song by Vishal-Shekar",
    "Punjabi Wedding Song by Vishal-Shekar",
    "Senorita by Farhan Akhtar",
    "Locha-E-Ulfat by Benny Dayal",
    "Bhool Bhulaiyaa by Pritam",
    "Twist by Neeraj Shridhar",
    "Dola Re by Kavita Krishnamurthy",
    "Mauja Hi Mauja by Pritam",
    "Dhoom Machale by Pritam",
    "Teri Meri by Rahat Fateh Ali Khan",
    "Patake by Sunanda",
    "Choomantar by Sohail Sen",
    "Dilbara by Pritam",
    "Jai Ho by A.R. Rahman",
    "The Last Ride by Sidhu Moose Wala",
    "Race Is On My Mind by Sunidhi Chauhan",
    "Give Me Some Sunshine by Suraj Jagan",
    "Tanhayee by Sonu Nigam",
    "Tum Hi Ho by Arjit Singh",
    "Kal Ho Naa Ho by Shankar-Eshaan Loy"
    "Jalebi Baby by Tesher"
    "Skechers by Carbine and DripReport"

    # rage songs
    "Numb by Linkin Park",
    "Testify by Rage Against The Machine",
    "Bat Country by Avenged Sevenfold",
    "T.N.T. by AC/DC",
    "King Nothing by Metallica",
    "Highway to Hell by AC/DC",
    "Devil’s Dance by Metallica",
    "I Hate Everything About You by Three Days Grace",
    "Motorbreath by Metallica",
    "How You Remind Me by Nickelback",
    "Last Resort by Papa Roach",
    "We're Not Gonna Take It by Twisted Sisters",
    "Crawling by Linkin Park",
    "Toxicity by System of the Down",
    "Tum Hi Ho by Arjit Singh",
    "Kal Ho Naa Ho by Shankar-Eshaan-Loy",


]

# Initialize jokes
def initSongs():
    # setup jokes into a dictionary with id, song, sad, happy, Indian, rage
    item_id = 0
    for item in song_list:
        song_data.append({"id": item_id, "song": item, "sad": 0, "happy": 0, "Indian": 0, "rage": 0})
        item_id += 1
    # prime some sad responses
    for i in range(10):
        id = getRandomSong()['id']
        addSongSad(id)
    # prime some happy responses
    for i in range(5):
        id = getRandomSong()['id']
        addSongHappy(id)
    # added emotion Indian
    for i in range(15):
        id = getRandomSong()['id']
        addSongIndian(id)
    # added emotion rage
    for i in range(15):
        id = getRandomSong()['id']
        addSongRage(id)
        
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

# adding Indian
def addSongIndian(id):
    song_data[id]['Indian'] = song_data[id]['Indian'] + 1
    return song_data[id]['Indian']

# adding rage
def addSongRage(id):
    song_data[id]['rage'] = song_data[id]['rage'] + 1
    return song_data[id]['rage']

# Pretty Print joke
# added indian
def printSong(song):
    print(song['id'], song['Song'], "\n", "Sad:", song['sad'], "\n", "Happy:", song['happy'], "\n", "Indian:", song['Indian'], "\n", "Rage:", song['rage'], "\n")

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