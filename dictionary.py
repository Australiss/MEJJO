def dictionarypage():
    dictionaryMenu = 1
    while dictionaryMenu == 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf', 75)
        TextSurf, TextRect = text_objects("MEJJO SCRABBLE", largeText)
        TextRect.center = ((display_width / 2), (display_height / 3))
        gameDisplay.blit(TextSurf, TextRect)
        button("ADDAWORD", 350, 380, 160, 40, green, bright_green, "addaword")
        button("SEARCH WORD", 350, 480, 160, 40, green, bright_green,"searchword")
        button("MAIN MENU", 350, 530, 160, 40, red, bright_red, "mainMenu")
        pygame.display.update()
        clock.tick(60)


def dictionarysearch():
    wordLookup = tkinter.simpledialog.askstring('Search word', 'Enter the word you want to search')
    if dict_en.check(wordLookup):
        tkinter.messagebox.showinfo('Dictionary', 'Word already in dictionary')
    else:
        if wordLookup in userDictionary.keys():
            tkinter.messagebox.showinfo('Dictionary', 'Word already in user added dictionary')
        else:
            tkinter.messagebox.showinfo('Dictionary', 'Word not found in dictionary')

def dictionaryadd():
    wordadd = tkinter.simpledialog.askstring('Add word', 'Enter the word you want to Add')
    userDictionary[wordadd] = wordadd
    tkinter.messagebox.showinfo('Dictionary', 'Word added to user dictionary')
