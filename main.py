from bs4 import BeautifulSoup
import urllib.request
import urllib.parse

#choose which pdfs to download (ex: 1-6, 10, 12)
#parse links to downloader function

def downloader(pdf_links):
    dl_path = 'C:/Users/Y530/Downloads/python test'
    for pdf_link in pdf_links:
        dl_link=urllib.parse.urljoin(url,pdf_link) #turns links into true urls
        pdf_name=pdf_link.split('/')
        output_file=open(dl_path + '/' + pdf_name[len(pdf_name)-1], 'wb')
        output_file.write((urllib.request.urlopen(dl_link).read()))

#url='http://www.os-book.com/OSE2/practice-exer-dir/index.html'
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
        pdf_links.append(link_url) #pdf names


downloader(pdf_links)
