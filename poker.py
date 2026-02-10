import itertools
import random

def calculate_odds(community_cards, hole_cards, target_hand):
    # All possible cards (ranks and suits)
    deck = [f'{rank} {suit}' for rank in '23456789TJQKA' for suit in ['hearts', 'spades', 'clubs', 'diamonds']]
    known_cards = set(community_cards + hole_cards)  # Known cards (community + hole)
    deck = [card for card in deck if card not in known_cards]  # Remaining deck without known cards

    # Count the number of 'outs' (cards that complete the hand)
    outs = 0
    for card in deck:
        new_hand = community_cards + [card]
        if target_hand(new_hand + hole_cards):
            outs += 1

    total_draws = len(deck)  # Remaining cards in the deck

    return outs / total_draws if total_draws > 0 else 0  # Calculate odds

def is_flush(hand):
    # Check if hand is a flush (5 or more cards of the same suit)
    suits = [card.split()[-1] for card in hand]
    return any(suits.count(suit) >= 5 for suit in ['hearts', 'spades', 'clubs', 'diamonds'])

def is_straight(hand):
    # Check if hand is a straight (5 consecutive ranks)
    ranks = '23456789TJQKA'
    hand_ranks = sorted(set(ranks. index(card.split()[0]) for card in hand))  # Extract rank and convert to index
    for i in range(len(hand_ranks) - 4):
        if hand_ranks[i+4] - hand_ranks[i] == 4:
            return True
    return False

def get_user_input():
    community_input = input("Enter community cards (separated by space, e.g., '2 spades 5 spades 7 spades Jack spades'): ").split()
    hole_input = input("Enter hole cards (separated by space, e.g., 'Ace spades 9 diamonds'): ").split()

    # Combine ranks and suits into full card names
    community_cards = [f'{community_input[i]} {community_input[i+1]}' for i in range(0, len(community_input), 2)]
    hole_cards = [f'{hole_input[i]} {hole_input[i+1]}' for i in range(0, len(hole_input), 2)]

    return community_cards, hole_cards

# Main program
community_cards, hole_cards = get_user_input()

# Calculate odds for flush and straight based on user input
flush_odds = calculate_odds(community_cards, hole_cards, is_flush)
straight_odds = calculate_odds(community_cards, hole_cards, is_straight)

# Print realistic odds
print(f'Flush Draw Odds: {flush_odds:.2%}')
print(f'Straight Draw Odds: {straight_odds:.2%}')




