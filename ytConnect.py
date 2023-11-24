import requests as req
from bs4 import BeautifulSoup

class ytConnecting :
    def main(self):
        pass

    def session(self, input):
        with req.session() as Session :
            searchYT = Session.get("https://www.youtube.com/results?search_query="+input)
            ytParser = BeautifulSoup(searchYT.text, 'html.parser')
            ytFind = ytParser.find_all('script')
            ytReplace = ytFind[-6].text.split(r'{"videoId":"')
            ytList = ["https://youtube.com/watch?v="+ytReplace[1][:11],
                      "https://youtube.com/watch?v="+ytReplace[4][:11],
                      "https://youtube.com/watch?v="+ytReplace[7][:11]]
            
            return ytList

            if __name__ == "__main__":
                print(ytList)

#obj = ytConnecting()
#obj.session()