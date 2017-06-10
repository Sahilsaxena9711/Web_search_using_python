import webbrowser

def pyGoogleSearch():
    address = 'http://google.com/#q='
    word = input('Enter you search : \n>>>')
    newWord = address + word
    webbrowser.open(newWord)

pyGoogleSearch()
