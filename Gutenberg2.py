from bs4 import BeautifulSoup
import urllib3
import collections

http = urllib3.PoolManager()

url = "http://www.gutenberg.org/files/56775/56775-0.txt"
response = http.request('GET', url)
cavallo = BeautifulSoup(response.data, "html.parser")
cavallo_text = cavallo.prettify().split
print(cavallo_text)

def find_most_common_words(book, top):
    """Return the most common words in 'Un Cavallo'"""
    words = collections.Counter()
    for word in book:
        words[word] += 1
    # print(words)
    return words.most_common(top)

top_ten_words = find_most_common_words(cavallo_text, 10)
print(top_ten_words)
