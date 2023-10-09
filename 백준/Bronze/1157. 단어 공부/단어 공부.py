word = input().upper()
word_list = list(set(word))
word_count = []

for i in word_list:
    count = word.count(i)
    word_count.append(count)

if word_count.count(max(word_count)) >= 2:
    print("?")
else:
    print(word_list[word_count.index(max(word_count))])