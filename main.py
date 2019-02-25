from bs4 import BeautifulSoup
import urllib.request

#choose which pdfs to download (ex: 1-6, 10, 12)
#parse links to downloader function

url='http://www.os-book.com/OSE2/practice-exer-dir/index.html'
webpage = urllib.request.urlopen(url)
webpage_src = webpage.read()
soup = BeautifulSoup(webpage_src)
pdf_links = []
for link in soup.findAll("a"):
    link_url=link.attrs['href']
    if( link_url[len(link_url)-1]=='f' and
    link_url[len(link_url)-2]=='d' and
    link_url[len(link_url)-3]=='p' and
    link_url[len(link_url)-4]=='.'): #checked if link ends in .pdf
        print(link_url)
        pdf_links.append(link_url) #watch out for relative paths

for i in pdf_links:
    print(i)