def sing_Go_team_go():
    print('Go, team, go! \nDefeat your foe.')


def sing_Go_Pause():
    sing_Go_team_go()
    print()


def sing_Simply_the_best():
    print('Simply the best, \nBetter than the rest.')
    sing_Go_Pause()
    sing_Go_team_go()


def sing_fight_song():
    sing_Go_Pause()
    sing_Go_team_go()
    for _ in range(2):
        sing_Simply_the_best()


sing_fight_song()
