text = """
    How I want a drink, alcoholic of course, after the heavy chapters involving
    quantum mechanics. All of thy geometry, Herr Planck, is fairly hard.
"""

# TODO
# 文字数取得
word_lengths = [len(word.strip(",.")) for word in text.split()]

# つなげる
result = "".join(map(str, word_lengths))

print(result)   