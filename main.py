from bs4 import BeautifulSoup
import urllib.request

url='http://www.os-book.com/OSE2/practice-exer-dir/index.html'
webpage = urllib.request.urlopen(url)
webpage_src = webpage.read()
soup = BeautifulSoup(webpage_src)
for link in soup.findAll("a"):
    link_url=link.attrs['href']
    if(link_url)
