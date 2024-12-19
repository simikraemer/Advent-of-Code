from collections import Counter

def parse_input(lines):
    lines = [line.strip() for line in lines]    
    handtücher = lines[0].split(", ")    
    muster = [line for line in lines[2:] if line]    
    return handtücher, muster

def handtücher_zuordnen(handtücher, muster):
    def can_build_design(muster, handtuch_counts):        
        if muster == "":
            return True # Muster gebaut
        
        for handtuch in handtuch_counts:
            if muster.startswith(handtuch):
                if can_build_design(muster[len(handtuch):], handtuch_counts):
                    return True

        return False
    counter1 = 0
    handtuch_counts = Counter(handtücher)

    for design in muster:
        result = can_build_design(design, handtuch_counts.copy())
        if result:
            counter1 += 1

    return counter1

def zähle_alle_möglichkeiten(handtücher, muster):
    def zähle_möglichkeiten(muster):
        dp = [0] * (len(muster) + 1)
        dp[0] = 1

        for i in range(len(muster) + 1):
            for handtuch in handtücher:
                if muster[i - len(handtuch):i] == handtuch and i >= len(handtuch):
                    dp[i] += dp[i - len(handtuch)]

        return dp[len(muster)]

    alle_möglichkeiten = 0

    for design in muster:
        möglichkeiten = zähle_möglichkeiten(design)
        alle_möglichkeiten += möglichkeiten

    return alle_möglichkeiten


with open("AdventofCode2024/input/19.txt", "r") as file:
    lines = file.readlines()
    
handtücher, muster = parse_input(lines)

counter1 = handtücher_zuordnen(handtücher, muster)
print("Aufgabe 1:", counter1)

counter2 = zähle_alle_möglichkeiten(handtücher, muster)
print("Aufgabe 2:", counter2)