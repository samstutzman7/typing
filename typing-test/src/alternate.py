import random

def alternate_words(four_letter_words, five_letter_words):
    result = []
    i, j = 0, 0

    while i < len(four_letter_words) and j < len(five_letter_words):
        result.append(four_letter_words[i])
        result.append(five_letter_words[j])
        i += 1
        j += 1

    # If one list is longer than the other, add the remaining words from that list.
    result.extend(four_letter_words[i:])
    result.extend(five_letter_words[j:])

    return result

# Example usage:
four_letter_words = [
    "word", "test", "data", "love", "zone", "luck", "easy", "dark", "deep", "open",
    "blue", "moon", "rich", "long", "loud", "star", "cold", "warm", "high", "slow",
    "fast", "gold", "book", "film", "song", "rock", "fire", "away", "time", "safe",
    "good", "best", "hard", "kind", "soft", "pure", "full", "true", "cool", "calm",
    "wild", "rich", "well", "fine", "peak", "peak", "free", "fair", "nice", "pink",
    "tree", "lead", "gray", "hurt", "worn", "rich", "road", "left", "fall", "luck",
    "luck", "help", "hold", "pale", "dark", "pass", "rich", "beam", "ring", "park",
    "ring", "walk", "stay", "lend", "rise", "sing", "wage", "flow", "bend", "wear",
    "spin", "stay", "earn", "feed", "seal", "rule", "sink", "last", "beam", "home",
    "cook", "read", "wear", "grip", "fold", "bear", "kill", "ride", "yell", "open",
    "rule", "roof", "draw", "push", "bath", "pull", "fear", "fast", "dear", "sand",
    "word", "test", "data", "love", "time", "work", "help", "play", "well", "wish",
    "hard", "cool", "fine", "rich", "gold", "true", "kind", "deep", "dark", "free",
    "star", "moon", "blue", "pink", "loud", "soft", "fire", "open", "road", "away",
    "park", "rock", "book", "film", "song", "rock", "lead", "gray", "beam", "pale",
    "luck", "safe", "peak", "fall", "walk", "bend", "spin", "stay", "earn", "ring",
    "beam", "seal", "last", "road", "left", "cook", "read", "wear", "fold", "bear",
    "kill", "ride", "yell", "home", "rule", "roof", "draw", "push", "bath", "pull",
    "fear", "fast", "dear", "sand", "clay", "wind", "rock", "gift", "zone", "wave",
    "race", "dark", "lend", "flow", "wait", "high", "road", "hope", "seed", "jump",
    "bone", "room", "true", "mind", "belt", "gate", "lend", "lend", "silk", "hill",
    "need", "care", "king", "pink", "mild", "rice", "size", "time", "pool", "fair"
]

five_letter_words = [
    "apple", "happy", "table", "ocean", "music", "dream", "peace", "fruit", "alive", "waste",
    "smile", "light", "magic", "heart", "brave", "magic", "angel", "faith", "cloud", "scent",
    "queen", "crown", "forge", "proud", "space", "dream", "sunny", "frost", "crisp", "whale",
    "spark", "grape", "piano", "watch", "chill", "juicy", "honor", "fancy", "sweep", "lucky",
    "honey", "candy", "sleet", "daisy", "lunar", "flame", "flock", "enjoy", "heart", "rover",
    "sheep", "lakes", "sugar", "brush", "marsh", "sugar", "shine", "fleet", "joker", "young",
    "trick", "night", "blend", "hills", "coast", "forge", "light", "sunny", "dream", "frank",
    "brave", "peace", "brisk", "creek", "magic", "sweet", "alive", "peace", "angel", "heart",
    "swirl", "magic", "scent", "queen", "vivid", "forge", "candy", "music", "dream", "peace",
    "waste", "sunny", "alive", "honor", "crown", "dream", "brave", "ocean", "lunar", "queen",
    "magic", "candy", "happy", "smile", "table", "heart", "brave", "cloud", "light", "dream",
    "apple", "happy", "table", "ocean", "music", "demon", "peace", "fruit", "alive", "waste",
    "dream", "queen", "vivid", "magic", "smile", "light", "forge", "swirl", "proud", "cloud",
    "space", "cream", "brave", "blend", "dusty", "honor", "fancy", "spare", "earth", "crown",
    "spark", "crisp", "chest", "grape", "tiger", "piano", "watch", "chill", "scent", "angel",
    "frost", "faith", "whale", "daisy", "wings", "leafy", "grind", "shiny", "flock", "sunny",
    "magic", "zesty", "quest", "fleet", "enjoy", "juicy", "jolly", "candy", "zoned", "peace",
    "bliss", "heart", "honey", "brisk", "young", "creek", "lucky", "flame", "brave", "cheer",
    "sweep", "quack", "lunar", "shine", "trick", "night", "joker", "lunar", "coast", "marsh",
    "thorn", "sheep", "tooth", "sugar", "forge", "sleet", "smile", "rover", "hills", "rider",
    "queen", "music", "dream", "lakes", "grand", "waste", "dream", "brave", "alive", "sunny",
    "sweet", "peace", "frank", "witty", "swirl", "magic", "vivid", "crown", "queen", "ocean"
]

for _ in range(25):
    random.shuffle(four_letter_words)
    random.shuffle(five_letter_words)

    result = alternate_words(four_letter_words[:50], five_letter_words[:50])

    # Join the words with spaces and print them in the desired format
    formatted_result = " ".join(result)
    print(formatted_result)
