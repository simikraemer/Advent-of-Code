from collections import defaultdict

def mix(secret, value):
    return secret ^ value

def prune(secret):
    return secret % 16777216

def process(secret):
    # 1
    secret = mix(secret, secret * 64)
    secret = prune(secret)

    # 2
    secret = mix(secret, secret // 32)
    secret = prune(secret)

    # 3
    secret = mix(secret, secret * 2048)
    secret = prune(secret)

    return secret


def aufgabe1(lines, wdh):
    counter = 0
    for secret in lines:
        for _ in range(wdh):
            secret = process(secret)
        counter += secret
    return counter


def aufgabe2(lines, wdh):
    sequence_occurrences = defaultdict(list)

    for secret_index, secret in enumerate(lines):
        prices = []
        prev_price = None
        for _ in range(wdh):
            secret = process(secret)
            price = secret % 10
            if prev_price is not None:
                diff = price - prev_price
                prices.append((price, diff))
            prev_price = price

        seen = set()
        for i in range(len(prices) - 3):
            seq = tuple(diff for _, diff in prices[i:i+4])
            if seq not in seen:
                sequence_occurrences[seq].append((prices[i + 3][0], secret_index + 1, i + 4))
                seen.add(seq)

    max_bananas = 0

    for seq, occurrences in sequence_occurrences.items():
        used_buyers = set()
        total_bananas = 0
        for price, buyer_index, position in occurrences:
            if buyer_index not in used_buyers:
                total_bananas += price
                used_buyers.add(buyer_index)
        if total_bananas > max_bananas:
            max_bananas = total_bananas
    
    return max_bananas


with open("2024/input/22.txt", "r") as file:
    lines = [int(line.strip()) for line in file.readlines()]

wdh = 2000

print("Aufgabe 1:", aufgabe1(lines, wdh))
print("Aufgabe 2:", aufgabe2(lines, wdh))