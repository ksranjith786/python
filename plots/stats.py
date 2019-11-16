
class Stats:
    def __init__(self):
        pass


class City:
    # name

class Venue:
    # name

class Team:
    # name

class Match:
    # id
    # innings
    # teams{X:Y}
    # winner
    # player[]
    # city
    # venue
    # heldDate

class Player:
    # name

class Batsman(Player):
    # runs
    # singles
    # doubles
    # triples
    # fours
    # sixes
    # thirtyPlus
    # fiftyPlus
    # hundredPlus
    # hunderdAndFiftyPlus
    # retiredHurt

class Bowler(Player):
    # lbws
    # bowled
    # hitWicket

class Fielder(Player):
    # catches
    # runouts

class WicketKeeper(Player):
    # stumpings