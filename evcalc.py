from itertools import combinations
import numpy as np

class CardGameInteractive:
    def __init__(self):
        self.all_cards = set(range(1, 11))
        self.deck = set(self.all_cards)
        self.revealed_cards = set()

    def start_game(self):
        player_card = int(input("Enter your card (1-10): "))
        self.player_card = player_card
        self.deck.remove(player_card)

    def reveal_card(self):
        card = int(input("Enter revealed card: "))
        if card in self.deck:
            self.deck.remove(card)
            self.revealed_cards.add(card)
        else:
            print("Card already revealed or does not exist. Try again.")

    def calculate_ev(self):
        possible_sets = list(combinations(self.deck, 3))  # 3 other cards + player's card makes 4
        evens, odds, sums, diffs, mins, maxes = [], [], [], [], [], []

        for s in possible_sets:
            cards = set(s) | {self.player_card}
            even_product = np.prod([c for c in cards if c % 2 == 0]) or 1
            odd_product = np.prod([c for c in cards if c % 2 != 0]) or 1

            total_diff = abs(even_product - odd_product)

            evens.append(even_product)
            odds.append(odd_product)
            sums.append(even_product+odd_product)
            diffs.append(total_diff)
            mins.append(min(cards))
            maxes.append(max(cards))

        # Calculate expected values
        ev = {
            'EVEN': np.mean(evens),
            'ODD': np.mean(odds),
            'SUM': np.mean(sums),
            'DIFF': np.mean(diffs),
            'MIN': np.mean(mins),
            'MAX': np.mean(maxes)
        }

        return ev

    def run(self):
        self.start_game()
        while len(self.revealed_cards) < 6:
            self.reveal_card()
            ev = self.calculate_ev()
            print(f"Current EVs: {ev}")

# This game will run in a terminal or command line environment.
game = CardGameInteractive()
game.run()
