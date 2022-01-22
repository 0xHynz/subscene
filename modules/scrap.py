import re
import os
import sys
import requests
import concurrent.futures as future


class Subscene:

    baseURL = "https://subscene.my.id/"

    def createFolder(self,title):
        self.path = "output/{}".format(title)
        try:
           os.makedirs(self.path,exist_ok=False)
        except FileExistsError:
           return self.path+'/'
        return self.path+'/'

    def getLink(self,src):
        self.src = src #source code of html page
        self.data = []
        for value in re.findall(r'<a href="(.*?)" title="(.*?)">',src):
            value = (re.sub(r'Subtitle Indonesia','',value[1]),value[0])
            None if re.findall(r'https:\/\/(.*?)\/',self.baseURL)[0] in value[0] else self.data.append(value)

        return self.data

    def start_download(self,path,pool=4):
        self.path = [x for x in path]
        self.path.pop(len(self.path)-len(self.path));self.path = "".join(self.path)

        self.reqs = requests.get(self.baseURL+self.path).text
        self.links = re.findall(r' <a href="(.*?)" title="(.*?)">',self.reqs)
        self.title = self.links[int(len(self.links)-1)][1];self.links.pop(int(len(self.links)-1))
        print()

        def process(urlf): #urlf: url & filename

            reqs = requests.get(urlf[0]).text
            url = re.findall(r'<a rel="nofollow" href="(.*?)"',reqs)[0]
            folderPath = self.createFolder(self.title)
            r = requests.get(url).content

            if urlf[1].endswith('zip'):
               filename = urlf[1]
            else:
               filename = urlf[1]+'.zip'

            with open(folderPath+filename,'wb') as File:
                 File.write(r)
                 File.close()

            return """[+] success downloaded
    - filename: {}
    - output: {}
""".format(filename,folderPath)

        self.relinks = []
        for link in self.links:
             self.relinks.append((self.baseURL.replace('id/','id')+link[0],link[1]))

        with future.ThreadPoolExecutor(max_workers=pool) as pool:
             resp = [pool.submit(process,url) for url in self.relinks]
             for read in resp:
                 print(read.result())



class Functions(Subscene):

    def __init__(self):
         Subscene.__init__(self)

    @classmethod
    def search(self,query):
        self.url = Subscene.baseURL+"pencarian?s={}".format(query)
        self.res = self.getLink(self,requests.get(self.url).text)

        if not self.res:
           sys.exit('\n[!] sorry dude, result not found try with another query')

        return self.res

    """
	coming soon feature, if you want to contribution
	with this you can pull request in my github
    """

    def genre(self):
        pass

    def tahun(self):
        pass

    def bahasa(self):
        pass



