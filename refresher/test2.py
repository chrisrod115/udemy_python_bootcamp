import random


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return f"{self.rank} of {self.suit}"


class Deck:
    def __init__(self):
        self.cards = []
        suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop()


class Player:
    def __init__(self):
        self.hand = []

    def draw(self, deck):
        self.hand.append(deck.draw())
        return self.hand

    def show_hand(self):
        for card in self.hand:
            print(card)

    def get_value(self):
        value = 0
        ace = False
        for card in self.hand:
            if card.rank in ["Jack", "Queen", "King"]:
                value += 10
            elif card.rank == "Ace":
                ace = True
                value += 11
            else:
                value += int(card.rank)
        if value > 21 and ace:
            value -= 10
        return value


def main():
    deck = Deck()
    deck.shuffle()
    player = Player()
    dealer = Player()
    player.draw(deck)
    player.draw(deck)
    dealer.draw(deck)
    print("Player's hand:")
    player.show_hand()
    print("Player's value:", player.get_value())
    print("Dealer's hand:")
    dealer.show_hand()
    print("Dealer's value:", dealer.get_value())


if __name__ == "__main__":
    main()
