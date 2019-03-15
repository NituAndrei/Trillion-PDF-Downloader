from bs4 import BeautifulSoup
import urllib.request
import urllib.parse


# choose which pdfs to download (ex: 1-6, 10, 12)
# parse links to downloader function

def downloader(pdf_links):
    dl_path = 'C:/Users/Y530/Downloads/python test'
    for pdf_link in pdf_links:
        dl_link = urllib.parse.urljoin(url, pdf_link)  # turns links into true urls
        pdf_name = pdf_link.split('/')
        output_file = open(dl_path + '/' + pdf_name[len(pdf_name) - 1], 'wb')
        output_file.write((urllib.request.urlopen(dl_link).read()))


def selector(pdf_links):
    chosen_pdfs = [0] * len(pdf_links)
    numbers = '0123456789'
    print('Select pdf indexes (format: 1-6,10,20,25-40)')
    selection = input()
    if (len(selection) == 0):
        return -1
    i = 0
    while i < len(selection):
        if selection[i] in numbers:
            a = 0
            while i < len(selection) and selection[i] in numbers:
                a = a * 10 + int(selection[i])
                i = i + 1

            if a >= len(pdf_links):
                print('invalid input')
                return -1  # add message

            if i == len(selection):
                if a < len(pdf_links):
                    chosen_pdfs[a] = 1
                else:
                    print('invalid input')

            if selection[i] == ',':
                if a < len(pdf_links):
                    chosen_pdfs[a] = 1
                else:
                    print('invalid input')
                    return -1

            elif selection[i] == '-':
                b = 0
                i = i + 1
                while i < len(selection) and selection[i] in numbers:
                    b = b * 10 + int(selection[i])
                    i = i + 1
                if b >= len(pdf_links):
                    print('invalid input')
                    return -1  # add message
                while a <= b:
                    chosen_pdfs[a] = 1
                    a = a + 1

            else:
                print('format error')
                return -1
        else:
            print('format error')
            return -1
        i = i + 1

    final = []
    for i in range(len(chosen_pdfs)):
        if chosen_pdfs[i] == 1:
            final.append(pdf_links[i])

    return final


# url='http://www.os-book.com/OSE2/practice-exer-dir/index.html'
url = 'http://www.os-book.com/OSE2/practice-exer-dir/index.html'
webpage = urllib.request.urlopen(url)
webpage_src = webpage.read()
soup = BeautifulSoup(webpage_src)
pdf_links = []
for link in soup.findAll("a"):
    link_url = link.attrs['href']
    if link_url[len(link_url) - 4: len(link_url)] == '.pdf':
        pdf_links.append(link_url)  # pdf names

for i in range(len(pdf_links)):
    print('index:', i, pdf_links[i])

pdf_links = selector(pdf_links)
print(pdf_links)
# downloader(pdf_links)
