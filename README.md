# NLP 
### Charting library - matplotlib
> Straightforward - bar chart,line charts, scatter plot
> This will generate histogram
`from matplotlib import pyplot as plt
plt.hist([1, 5, 5, 7, 7, 7, 9])
plt.show()`

> How to use matplotlib in word tokenization

`from matplotlib import pyplot as plt
from nltk.tokenize import word_tokenize
words = word_tokenize("This is a pretty cool tool!")
word_lengths = [len(w) for w in words]
plt.hist(word_lengths)
plt.show()`
