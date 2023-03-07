# Youtube Tutorial Refernce Learning : https://www.youtube.com/@buildwithpython

# Imported Library
import string
from  collections import Counter
import matplotlib.pyplot as plt

# Read The Text File
text = open("read.txt",encoding="utf-8").read()

# Make It Lower Case
lower_case = text.lower()

# Remove Punctuation With Library String
cleaned_text = lower_case.translate(str.maketrans('','',string.punctuation))

# Tokenize Proccess
tokenize_word = cleaned_text.split()

# Stop word
stop_word = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
"yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
"they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
"those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
"does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
"of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
"after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
"further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
"few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
"too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

# Pengecekan Stop word
final_word = []
for word in tokenize_word:
    if word not in stop_word:
        final_word.append(word)

# NLP Emotion Algorithm by reference emotions.txt
emotion_list = []
with open('emotions.txt','r') as file:
    for line in file:
        clear_line = line.replace("\n",'').replace(",",'').replace("'",'').strip()
        word,emotion = clear_line.split(':')
        
        if word in final_word:
            emotion_list.append(emotion)

# Using Counter Library for count emotion
print("My Emotion :",emotion_list)
w = Counter(emotion_list)
print(w)

fig,ax1 = plt.subplots()
ax1.bar(w.keys(),w.values())
fig.autofmt_xdate()
plt.savefig('graph.png')

plt.show()