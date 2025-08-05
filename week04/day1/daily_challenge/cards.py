import random

# --- Card Class ---
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{self.value} of {self.suit}"


# --- Deck Class ---
class Deck:
    def __init__(self):
        self.cards = []
        self._build_deck()

    def _build_deck(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.cards = [Card(suit, value) for suit in suits for value in values]

    def shuffle(self):
        self._build_deck()  # Reset the deck
        random.shuffle(self.cards)

    def deal(self):
        if len(self.cards) == 0:
            return "No more cards to deal!"
        return self.cards.pop()


# --- Example Usage ---
if __name__ == "__main__":
    deck = Deck()
    deck.shuffle()

    print("Dealing 5 cards:")
    for _ in range(5):
        print(deck.deal())
