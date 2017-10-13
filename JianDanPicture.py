#煎蛋网的图片爬取
import urllib.request
from bs4 import BeautifulSoup
headers = {'User-Agent':
           'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.89 Safari/537.36'}

def jiandan(url):
    request = urllib.request.Request(url,None,headers)
    response = urllib.request.urlopen(request)
    content = response.read()
    soup = BeautifulSoup(content,'lxml')
    #print(soup.prettify())
    items = soup.find_all('img')
    x=1
    li = []
    for i in items:
        #print(i.get('src'))
        #若果url中有http：直接添加到li这个链表中去
        if 'http:'in i.get('src'):
            li.append(i.get('src'))
        #如果url中有https：也同样的添加到li这个链表中
        if 'https:' in i.get('src'):
            li.append(i.get('src'))
        #如果url中没有http：或者https：，则添加到http：到url中
        else:
            li.append('http:'+i.get('src'))
     #利用for循环个每一个照片去命名，每次命名递加1
    for j in li:
        print(j)
        localpath = 'F:\\picture\\{}.jpg'.format(x)
        urllib.request.urlretrieve(j,filename = localpath)
        x= x+1
#启动这个程序
if __name__ == '__main__':
    num = int(input('请问你需要爬取多少页？'))
    #通过一个for循环去遍历url，然后在调用jiandan()这个方法
    for i in range(1,num):
        url = "http://jandan.net/ooxx/page-"+str(i)+"#comments"
        jiandan(url)
    
