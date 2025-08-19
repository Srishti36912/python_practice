from html.parser import HTMLParser

N = int(input())

class myHtmlParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if not attrs:
            print(tag)
        if attrs:
            print(tag)
            for attr in attrs:
                print("->",attr[0], ">", attr[1])

html = ""

for i in range(N):
    html += input()
parser = myHtmlParser()
parser.feed(html)