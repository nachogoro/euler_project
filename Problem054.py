#!/usr/bin/python3
#coding:utf8

# http://projecteuler.net/problem=54
#
# PROBLEM CONTENT:
# In the card game poker, a hand consists of five cards and are ranked, from
# lowest to highest, in the following way:
# * High Card: Highest value card.
# * One Pair: Two cards of the same value.
# * Two Pairs: Two different pairs.
# * Three of a Kind: Three cards of the same value.
# * Straight: All cards are consecutive values.
# * Flush: All cards of the same suit.
# * Full House: Three of a kind and a pair.
# * Four of a Kind: Four cards of the same value.
# * Straight Flush: All cards are consecutive values of same suit.
# * Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
#
# The cards are valued in the order:
#
# 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.
#
# If two players have the same ranked hands then the rank made up of the
# highest value wins; for example, a pair of eights beats a pair of fives (see
# example 1 below). But if two ranks tie, for example, both players have a
# pair of queens, then highest cards in each hand are compared (see example 4
# below); if the highest cards tie then the next highest cards are compared,
# and so on.
#
# Consider the following five hands dealt to two players:
#
# Hand          Player 1            Player 2                Winner
# 1             5H 5C 6S 7S KD      2C 3S 8S 8D TD          Player 2
#               Pair of Fives       Pair of Eights
#
# 2             5D 8C 9S JS AC      2C 5C 7D 8S QH          Player 1
#               Highest card Ace    Highest card Queen
#
# 3             2D 9C AS AH AC      3D 6D 7D TD QD          Player 2
#               Three Aces          Flush with diamonds
#
# 4             4D 6S 9H QH QC      3D 6D 7H QD QS          Player 1
#               Pair of Queens      Pair of Queens
#               Highest card nine   Highest card seven
#
# 5             2H 2D 4C 4D 4S      3C 3D 3S 9S 9D          Player 1
#               Full House          Full House
#               With Three Fours    With Three Threes

# The file Problem054.data, contains one-thousand random hands dealt to two
# players. Each line of the file contains ten cards: the first five are Player
# 1's cards and the last five are Player 2's cards. You can assume that all
# hands are valid (no invalid characters or repeated cards), each player's hand
# is in no specific order, and in each hand there is a clear winner.
#
# How many hands does Player 1 win?
#

# EXPLANATION:
# For each hand analyse which is the best play that can be done with it, and
# return it as a tuple: type of play and its value. If both players have the
# same play, the value is compared. If the values match, compare the highest
# cards not used for the hand

import time
from collections import Counter, namedtuple

Card = namedtuple('Card', ['number', 'suit'])
Result = namedtuple('Result', ['index', 'value', 'remaining'])
Hands = ['high_card', 'one_pair', 'two_pairs', 'three_of_a_kind', 'straight', 'flush', 'full_house', 'four_of_a_kind', 'straight_flush', 'royal_flush']

values = {k:v for v,k in enumerate('23456789TJQKA', start=2)}

def is_royal_flush(cards):
    r = is_flush(cards)
    if r.index == None:
        return r

    v = sorted([card.number for card in cards])
    if list(range(10, 15)) == v:
        return Result(Hands.index('royal_flush'), list(reversed(v)), [])
    else:
        return Result(None, [0], v)

def is_straight_flush(cards):
    r = is_flush(cards)
    if r.index == None:
        return r

    v = sorted([card.number for card in cards])
    if list(range(v[0], v[0]+5)) == v:
        return Result(Hands.index('straight_flush'), list(reversed(v)), [])
    else:
        return Result(None, [0], v)

def is_n_of_a_kind(cards, n):
    v = [card.number for card in cards]
    occurrences = dict(Counter(v))
    for k in occurrences:
        if occurrences[k] == n:
            index = Hands.index('three_of_a_kind') if n==3 else Hands.index('four_of_a_kind')
            return Result(index, [k], sorted([i for i in v if occurrences[i] < n]))

    return Result(None, [0], v)

def is_full_house(cards):
    r = is_n_of_a_kind(cards, 3)

    if not r.index:
        return r

    v = sorted([card.number for card in cards])
    if len(r.remaining) != 2 or len(set(r.remaining)) != 1:
        return Result(None, [0], v)

    return Result(Hands.index('full_house'), [r.value, r.remaining[0]], [])

def is_flush(cards):
    v = sorted([card.number for card in cards])
    suit = cards[0].suit
    # Check if all is same suit
    for card in cards:
        if card.suit != suit:
            return Result(None, 0, v)

    return Result(Hands.index('flush'), list(reversed(v)), [])

def is_straight(cards):
    v = sorted([card.number for card in cards])
    if list(range(v[0], v[0]+5)) == v:
        return Result(Hands.index('straight'), list(reversed(v)), [])
    else:
        return Result(None, [0], v)

def is_two_pairs(cards):
    v = [card.number for card in cards]
    pairs = []
    occurrences = dict(Counter(v))
    for k in occurrences:
        if occurrences[k] == 2:
            pairs.append(k)

    if len(pairs) == 2:
        return Result(Hands.index('two_pairs'), list(reversed(sorted(pairs))), [i for i in v if i not in pairs])

    return Result(None, [0], v)

def is_one_pair(cards):
    v = [card.number for card in cards]
    pair = None
    occurrences = dict(Counter(v))
    for k in occurrences:
        if occurrences[k] == 2:
            pair = k
            break

    if pair != None:
        return Result(Hands.index('one_pair'), [pair], [i for i in v if i != pair])

    return Result(None, [0], v)

def high_card(cards):
    return Result(Hands.index('high_card'), list(reversed(sorted([card.number for card in cards]))), [])

def represents_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def get_best_hand(string_rep):
    cards_str_rep = string_rep.split(' ')
    cards = []
    for c in cards_str_rep:
        cards.append(Card(values[c[0]], c[1]))

    royal_flush_result = is_royal_flush(cards)
    if royal_flush_result.index != None:
        return royal_flush_result

    straight_flush_result = is_straight_flush(cards)
    if straight_flush_result.index != None:
        return straight_flush_result

    four_of_a_kind_result = is_n_of_a_kind(cards, 4)
    if four_of_a_kind_result.index != None:
        return four_of_a_kind_result

    full_house_result = is_full_house(cards)
    if full_house_result.index != None:
        return full_house_result

    flush_result = is_flush(cards)
    if flush_result.index != None:
        return flush_result

    straight_result = is_straight(cards)
    if straight_result.index != None:
        return straight_result

    three_of_a_kind_result = is_n_of_a_kind(cards, 3)
    if three_of_a_kind_result.index != None:
        return three_of_a_kind_result

    two_pairs_result = is_two_pairs(cards)
    if two_pairs_result.index != None:
        return two_pairs_result

    one_pair_result = is_one_pair(cards)
    if one_pair_result.index != None:
        return one_pair_result

    return high_card(cards)


def player_1_wins(p1_besthand, p2_besthand):
    if p1_besthand.index > p2_besthand.index:
        return True

    if p2_besthand.index > p1_besthand.index:
        return False

    # They have the same best hand, compare values
    for i in range(0, len(p1_besthand.value)):
        if p1_besthand.value[i] > p2_besthand.value[i]:
            return True

        if p2_besthand.value[i] > p1_besthand.value[i]:
            return False

    # The values of their hand are equal, compare their remaining cards
    for i in range(0, len(p1_besthand.remaining)):
        if p1_besthand.remaining[i] > p2_besthand.remaining[i]:
            return True

        if p2_besthand.remaining[i] > p1_besthand.remaining[i]:
            return False

    # It's a tie
    return False

def main():
    with open('Problem054.data') as f:
        lines = f.read().splitlines()

    won_by_player1 = 0

    print(sum(1 for l in lines if player_1_wins(get_best_hand(l.split('|')[0]), get_best_hand(l.split('|')[1]))))

if __name__ == '__main__':
    start = time.time()
    main()
    elapsed = time.time() - start
    print('Solved in %.2f seconds' % elapsed)
