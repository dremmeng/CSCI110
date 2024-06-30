
f = open(r'C:\Users\Drewr\Documents\School\CSCI110\Alice.txt', 'r',encoding="utf8")


count = {}

for line in f:
    for word in line.split():

        word = word.replace('_', '').replace('"', '').replace(',', '').replace('.', '')
        word = word.replace('-', '').replace('?', '').replace('!', '').replace("'", "")
        word = word.replace('(', '').replace(')', '').replace(':', '').replace('[', '')
        word = word.replace(']', '').replace(';', '')

        word = word.lower()

        if word.isalpha():
            if word in count:
                count[word] = count[word] + 1
            else:
                count[word] = 1
keys = count.keys()
myKeys = list(count.keys())
myKeys.sort()
sorted_dict = {i: count[i] for i in myKeys}
out = open(r'C:\Users\Drewr\Documents\School\CSCI110\alice_words.txt', 'w')

for word in sorted_dict:
    out.write(word + " " + str(count[word]))
    out.write('\n')

print("The word 'alice' appears " + str(count['alice']) + " times in the book.")