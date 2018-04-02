from bs4 import BeautifulSoup
import urllib3

http = urllib3.PoolManager()

url = "http://www.gutenberg.org/files/56775/56775-0.txt"
response = http.request('GET', url)
soup = BeautifulSoup(response.data, "html.parser")
print(soup)
