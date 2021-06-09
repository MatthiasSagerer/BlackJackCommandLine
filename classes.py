from functions import intInput, randCard, sumOfList, newDeck
from functions import deck

points = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
          "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10, "A": 11}


class GameParticipant:
    def __init__(self):
        print('A new game participant has been created.')
        self.cards = []
        self.points = 0

    def takeCards(self, num=1):
        for i in range(num):
            self.cards.append(randCard())


class Player(GameParticipant):
    def __init__(self):
        super().__init__()
        print('New Player has been created.')
        self.money = 0
        self.starting_money = 0
        self.current_bet = 0

    def selectStartingAmount(self):
        self.money = intInput(
            'Enter the amount of dollars that you would like to start with: $')
        print(f'You will start with ${self.money}.')
        self.starting_money = self.money

    def makeABet(self):
        self.current_bet = intInput('Your bet in this round: $')
        while self.current_bet < 1:
            print('You have to bet at least 1$.')
            self.current_bet = intInput('Your bet in this round: $')
        while self.current_bet > self.money:
            print(f'You only have ${self.money}!')
            self.current_bet = intInput('Your bet in this round: $')

    def showCards(self):
        print(f'\nYour cards: {self.cards[:]}')

    def countPoints(self):
        global points
        player_points = []
        ace_count = 0
        for item in self.cards:
            if item == 'A':
                ace_count += 1
            player_points.append(points[item])
        p_points = sumOfList(player_points)
        while p_points > 21 and ace_count > 0:
            p_points -= 10
            ace_count -= 1
        alt_points = p_points
        alt = False
        while ace_count > 0:
            alt_points -= 10
            ace_count -= 1
            alt = True
        all_points = [p_points, alt_points, alt]
        return all_points


class Dealer(GameParticipant):
    def __init__(self):
        super().__init__()
        print('New Dealer has been created.')
        self.cards = []


# for debugging/testing
# TODO: DELETE BEFORE FINISHING THE CODE !!
if True:
    mario = Player()
    realDeal = Dealer()

    newDeck()

    mario.takeCards(3)
    realDeal.takeCards()

    print(mario.cards)
    print(realDeal.cards)

    print(len(deck))

# TODO Player class:
#   - countPoints -> define and use POINTS ATTRIBUTE
#                    in parent Class!!

# TODO: dealer class:
#   - countPoints -> define and use POINTS ATTRIBUTE
#                    in parent Class!!