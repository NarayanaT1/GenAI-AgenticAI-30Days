# Toy Byte Pair Encoding (BPE) demo
# Safe, educational code — no external dependencies
from collections import Counter

corpus = ["low", "lower", "lowest", "newer", "wider"]
# Represent words as characters + end-of-word marker </w>
tokens = [list(word) + ["</w>"] for word in corpus]

def get_stats(tokens):
    pairs = Counter()
    for word in tokens:
        for i in range(len(word)-1):
            pairs[(word[i], word[i+1])] += 1
    return pairs

def merge(tokens, pair):
    new_tokens = []
    bigram = "".join(pair)
    for word in tokens:
        i = 0
        merged = []
        while i < len(word):
            if i < len(word)-1 and (word[i], word[i+1]) == pair:
                merged.append(bigram)
                i += 2
            else:
                merged.append(word[i])
                i += 1
        new_tokens.append(merged)
    return new_tokens

if __name__ == "__main__":
    print("Initial tokens:", tokens)
    for _ in range(5):
        pairs = get_stats(tokens)
        if not pairs:
            break
        best = max(pairs, key=pairs.get)
        print("Merging:", best)
        tokens = merge(tokens, best)
        print(tokens)
