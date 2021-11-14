h = input('username:')
if h == (''):
    print(' ')
elif h == h:
    print('Hello,' + (' ')  + h)
input('')

def game():

    import random
    
    #list of artists, and list of songs with song and artist in same position in each list
    artists = ['Mark Ronson, Bruno Mars', 'Luis Fonsi', 'Ed Sheeran', 'Cardi B', 'Lil Nas X', 'AC/DC']
    songs = ['Uptown Funk', 'Despacito', 'Shape Of You', 'WAP', 'Old Town Road', 'Back In Black']

    #get a random integer between zero and total size of artists list
    random_integer = random.randrange(1, len(artists),1)

    #use the random integer to pick an artist for the quiz question
    artist_selected = artists[random_integer]

    #get the correct answer using the random artist selected
    song_answer = songs[random_integer]

    #convert the song answer to lowercase to match it against lowercase user entered answer
    # to make it work no matter user types in upper case, lower case or mixed
    song_answer_lower = song_answer.lower()

    #get each word of the correct song title
    words = song_answer.split()

    #extract just first letter of each word in the correct song title
    letters = [word[0] for word in words]

    #create variable to store the first letter of each word in the song title to show as hint to user
    song_hint = " ".join(letters)
    #start displaying content to the user
    print('**')
    print('Guess the song!')
    print('**')

    #show the artist selected for this quiz question
    print("Guess this artist's song: " + artist_selected)

    #show the hint for the song selected for this quiz question
    print('Hint for the song: ' + song_hint)

    #get user's input answer, they can type in lowercase or uppercase or mixed
    guess = input('Enter your answer here: ')

    #convert user input guess into lowercase just like done for correct song title
    guess_lower = guess.lower()

    #check user input against correct answer/song


    ##if guess_lower in songs_lower: #old code line - this only checks if song is in list of songs
    if guess_lower == song_answer_lower: #this checks if the user input is correct song for that artist
        print('Correct')
        print('The answer was: ' + song_answer)
    elif guess_lower == '': #this checks if the user typed no answer before pressing enter
        print('Wrong, You have not entered an answer.')
        print('The right answer was: ' + song_answer)
    elif guess_lower != song_answer_lower: #this checks if the user input is correct song for that artist
        print('Wrong')
        print('The right answer was: ' + song_answer)  
    
    play()

def play():    
    replay = input('If you want to play this game again press y for yes or n for no:')
    if replay.lower() == ('y'):
        game()
    elif replay.lower() == ('n'):
        print('bye')

game()
