emoji_converter = {
    ":)" : "🙂",
    ":(" : "☹️",
    "-_-" : "😑"
}
sentence = input("How are you feeling?: ")
for ch in sentence.split():
    new_sentence = sentence.replace(ch,emoji_converter.get(ch,ch))

print(new_sentence)