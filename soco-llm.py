print("hello")

corpus = """
            soco
            going
            fell
            fall
            paper
            push
            git
            it is a water
            etc.
            anything
            llm model

        """

new_corpus = corpus.split()
print(new_corpus)

# Create tokens ONCE, with a boundary marker after each word
abc = []
for word in new_corpus:
    for letter in word:
        abc.append(letter)
    abc.append(" ")  # boundary marker so words don't merge into each other

while True:

    print("\nCurrent tokens:")
    print(abc)

    pairs = []

    for i in range(len(abc) - 1):
        pair = (abc[i], abc[i + 1])
        pairs.append(pair)

    from collections import Counter

    pair_count = Counter(pairs)

    if not pair_count:
        print("No more pairs to merge.")
        break

    print("\nPair counts:")
    for pair, count in pair_count.items():
        print(f"{pair} : {count}")

    most_frequent = pair_count.most_common(1)

    merge_target_pair, freq = most_frequent[0]

    if freq == 1:
        print("\nNo pairs occur more than once. Stopping.")
        break

    print("\nMerging:", merge_target_pair)

    new_tokens = []

    i = 0
    while i < len(abc):
        if (
            i < len(abc) - 1
            and (abc[i], abc[i + 1]) == merge_target_pair
        ):
            new_tokens.append(abc[i] + abc[i + 1])
            i += 2
        else:
            new_tokens.append(abc[i])
            i += 1

    # IMPORTANT: keep the merged tokens
    abc = new_tokens

print("\nFinal tokens:")
print(abc)
print("\nReconstructed:", "".join(abc))