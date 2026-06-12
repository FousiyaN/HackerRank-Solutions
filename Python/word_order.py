n = int(input())
count = {}
new_word = []

for i in range(n):
    word = input()

    if word not in count:
        count[word] = 1
        new_word.append(word)
    else:
        count[word] += 1

print(len(new_word))

for word in new_word:
    print(count[word], end=" ")
