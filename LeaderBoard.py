def leaderboardpage():
    leaderboardmenu = True
    while leaderboardmenu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf', 75)
        TextSurf, TextRect = text_objects("LEADERBOARD", largeText)
        TextRect.center = ((display_width / 2), (display_height / 3))
        gameDisplay.blit(TextSurf, TextRect)
        button("MAIN MENU", 350, 530, 160, 40, red, bright_red, 'mainMenu')
        pygame.display.update()
        clock.tick(60)
