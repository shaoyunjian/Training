import urllib.request as req

def getData(url, review):
  request = req.Request(url, headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
  })

  with req.urlopen(request) as response:
    data = response.read().decode("utf-8")

  import bs4
  root = bs4.BeautifulSoup(data, "html.parser")
  titles = root.find_all("div", class_="title")
  with open("movie.txt", mode="a", encoding="utf-8") as file:
    for title in titles:
      # filtering reviews
      if title.a != None and review in title.a.string[0:4]:
        file.write(title.a.string +"\n")

  # search the last page
  nextLink = root.find("a", string="‹ 上頁")
  return nextLink["href"]


# use function getData to get the link from the last page
def getReview(review):
  pageURL = "https://www.ptt.cc/bbs/movie/index.html"
  count = 0
  while count < 10:
    pageURL="https://www.ptt.cc"+getData(pageURL, review)
    count+=1

# pass an argument to the function getReview to print the data
getReview("[好雷]")
getReview("[普雷]")
getReview("[負雷]") 
