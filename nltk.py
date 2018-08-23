###NLTK-TweetTokenizer####
# Import the necessary modules
from nltk.tokenize import regexp_tokenize
from nltk.tokenize import TweetTokenizer

#tweets=['This is the best #nlp exercise ive found online! #python', '#NLP is super fun! <3 #learning', 'Thanks @datacamp :) #nlp #python']

print (tweets)
# Define a regex pattern to find hashtags: pattern1
pattern1 = r"#\w+"

# Use the pattern on the first tweet in the tweets list
print(regexp_tokenize(tweets[0],pattern1))

# Write a pattern that matches both mentions and hashtags
pattern2 = r"([@#]\w+)"

# Use the pattern on the last tweet in the tweets list
print(regexp_tokenize(tweets[-1],pattern2))

# Use the TweetTokenizer to tokenize all tweets into one list
tknzr = TweetTokenizer()
#all_tokens=[]
#for t in tweets:
#    print ("\n")
#    print(all_tokens)
#    print(t)
#    all_tokens = all_tokens + [tknzr.tokenize(t)]
#print(all_tokens)

all_tokens=[]
all_tokens=[tknzr.tokenize(t) for t in tweets]
print(all_tokens)

########NLTK - ASCII###########
from nltk.tokenize import word_tokenize
from nltk.tokenize import regexp_tokenize
#german_text="Wann gehen wir Pizza essen? 🍕 Und fährst du mit Über? 🚕"
# Tokenize and print all words in german_text
print (german_text)
all_words = word_tokenize(german_text)
print(all_words)

# Tokenize and print only capital words
capital_words = r"[A-ZÜ]\w+"
print(regexp_tokenize(german_text, capital_words))

# Tokenize and print only emoji
emoji = "['\U0001F300-\U0001F5FF'|'\U0001F600-\U0001F64F'|'\U0001F680-\U0001F6FF'|'\u2600-\u26FF\u2700-\u27BF']"

print(regexp_tokenize(german_text, emoji))

########MatPlotLib - Charting the word lengths ###########
from matplotlib import pyplot as plt
# Split the script into lines: lines
#print (holy_grail)
#lines = re.split('\n',holy_grail)
lines = holy_grail.split('\n')
print(lines)
# Replace all script lines for speaker
pattern = "[A-Z]{2,}(\s)?(#\d)?([A-Z]{2,})?:"
lines = [re.sub(pattern, '', l) for l in lines]
print(lines)
# Tokenize each line: tokenized_lines
tokenized_lines = [regexp_tokenize(s,"\w+") for s in lines]
print(tokenized_lines)
# Make a frequency list of lengths: line_num_words
line_num_words = [len(t_line) for t_line in tokenized_lines]

# Plot a histogram of the line lengths
plt.hist(line_num_words)

# Show the plot
plt.show()
