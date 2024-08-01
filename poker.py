def read_cards():
    cards = []
    for i in range(5):
        line = input()
        suit, rank = line.split()
        suit = int(suit)
        rank = int(rank)
        cards.append((suit, rank))
    return cards

def convert_cards(cards):
    suit_dict = {0: 'S', 1: 'C', 2: 'D', 3: 'H'}
    rank_dict = {1: 'A', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: '10', 11: 'J', 12: 'Q', 13: 'K'}
    converted_cards = []
    for card in cards:
        suit = suit_dict[card[0]]
        rank = rank_dict[card[1]]
        converted_cards.append(suit + rank)
    return " ".join(converted_cards)

def is_royal_flush(cards):
    suits = []
    ranks = []
    for card in cards:
        suits.append(card[0])
        ranks.append(card[1])
    ranks.sort()
    if len(set(suits)) == 1 and ranks == [1, 10, 11, 12, 13]:
        return True
    return False

def is_straight_flush(cards):
    suits = []
    ranks = []
    for card in cards:
        suits.append(card[0])
        ranks.append(card[1])
    ranks.sort()
    if len(set(suits)) == 1:
        if ranks == list(range(ranks[0], ranks[0] + 5)) or ranks == [1, 10, 11, 12, 13]:
            return True
    return False

def is_four_of_a_kind(cards):
    ranks = []
    for card in cards:
        ranks.append(card[1])
    rank_counts = Counter(ranks)
    if 4 in rank_counts.values():
        return True
    return False

def is_full_house(cards):
    ranks = []
    for card in cards:
        ranks.append(card[1])
    rank_counts = Counter(ranks).values()
    if 3 in rank_counts and 2 in rank_counts:
        return True
    return False

def is_flush(cards):
    suits = []
    for card in cards:
        suits.append(card[0])
    if len(set(suits)) == 1:
        return True
    return False

def is_straight(cards):
    ranks = []
    for card in cards:
        ranks.append(card[1])
    ranks.sort()
    if ranks == list(range(ranks[0], ranks[0] + 5)) or ranks == [1, 10, 11, 12, 13]:
        return True
    return False

def is_three_of_a_kind(cards):
    ranks = []
    for card in cards:
        ranks.append(card[1])
    rank_counts = Counter(ranks).values()
    if 3 in rank_counts:
        return True
    return False

def is_two_pair(cards):
    ranks = []
    for card in cards:
        ranks.append(card[1])
    rank_counts = Counter(ranks).values()
    if list(rank_counts).count(2) == 2:
        return True
    return False

def is_one_pair(cards):
    ranks = []
    for card in cards:
        ranks.append(card[1])
    rank_counts = Counter(ranks).values()
    if 2 in rank_counts:
        return True
    return False

def judge_hand(cards):
    if is_royal_flush(cards):
        return "ロイヤルフラッシュ"
    elif is_straight_flush(cards):
        return "ストレートフラッシュ"
    elif is_four_of_a_kind(cards):
        return "フォーカード"
    elif is_full_house(cards):
        return "フルハウス"
    elif is_flush(cards):
        return "フラッシュ"
    elif is_straight(cards):
        return "ストレート"
    elif is_three_of_a_kind(cards):
        return "スリーカード"
    elif is_two_pair(cards):
        return "ツーペア"
    elif is_one_pair(cards):
        return "ワンペア"
    else:
        return "ハイカード"

def main():
    cards = read_cards()
    converted_cards = convert_cards(cards)
    hand = judge_hand(cards)
    print(converted_cards)
    print(hand)

if __name__ == "__main__":
    main()
