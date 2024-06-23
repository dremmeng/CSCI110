import string
s = """I jounreyed long in walking far beyond the place of stopping where there was no more returning to the people I had known."""


def Count_e(text):
    text = text.translate(str.maketrans('', '', string.punctuation)).lower()
    words = text.split()
    e = [word for word in words if 'e' in word]
    e_count = len(e)
    word_count = len(words)
    if word_count > 0:
        percentage = (e_count / word_count) *100
    else:
        percentage = 0
    print("Your text contains "+ str(word_count) + " words, of which "+ str(e_count) + " ("+str(percentage)+"%) contain an 'e'.")
Count_e(s)