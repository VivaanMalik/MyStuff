import pyperclip as pc
import requests
from bs4 import BeautifulSoup
import sys
import os
#os.remove("output.txt")
finaltext=""
pagetext=""
output="Books/"
output+=input("File name: ")
copytext=bool(input("Copy Text: "))
output+=".txt"
emptypage_count=0

with open(output, "w+") as f:
    f.writelines(["Courtesy of VivaanDaGr8\n"]);
    
def request(url, ch, no):
    global emptypage_count
    global pagetext
    global finaltext
    pagetext=""
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'} 
    resp=requests.get(url, headers=headers)
    
      
    #http_respone 200 means OK status
    #print(resp.status_code)
    if resp.status_code==200 or resp.status_code==301:
        #print("Successfully opened the web page")
        #print("The text are as follow :-\n")
      
        # we need a parser,Python built-in HTML parser is enough .
        soup=BeautifulSoup(resp.text,'html.parser')    
        #print(soup)
        # l is the list which contains all the text i.e news 
        l=soup.find("div",{"class":"container", "id":"sticky-end"})
      
        #now we want to print only the text part of the anchor.
        #find all the elements of a, i.e anchor
        for i in l.findAll("p"):
            if ch==True:
                 print("\n")
                 print("\n")
                 print("Part " +str(no))
                 print("\n")
                 print("\n")
            print(i.text)                
            pagetext+=i.text+"\n"
            finaltext+=i.text+"\n"
            with open(output, "a") as f:
                if ch==True:
                     f.write("\n")
                     f.write("\n")
                     f.write("Part " +str(no))
                     f.write("\n")
                     f.write("\n")
                     ch=False
                f.write(i.text+ "\n")
        #print(pagetext)
    else:
        print("Error")
        
def text():
    global pagetext
    global finaltext
    
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
    booklink=input("Book Link: " )
    answr=requests.get(booklink, headers=headers, allow_redirects=False)
    if answr.status_code==200:
        newsoup=BeautifulSoup(answr.text,'html.parser')    
        x=newsoup.find("div",{"class":"story-parts"})
        #l=soup.find("ul")
        urls = []
        for link in x.find_all('a'):
            #print(link.get("href",{"class":"story-parts__part"}))
            url_add="https://wattpad.com"+link.get("href",{"class":"story-parts__part"})
            urls.append(url_add)
        #print (urls)
        
        y=1
        for chlink in urls:
           
            emptypage=0
            page_no=2
            #print("b4lol")
            #print (chlink)
            request(chlink, True, y)
            #print("lol")
            while emptypage<=1: 
                new_url=chlink
                new_url+="/page/"
                new_url+=str(page_no)
                back_pagetext=pagetext
                request(new_url, False, 1)
                if back_pagetext==pagetext:
                    emptypage+=1
                    
                        
                        #sys.exit()
                page_no+=1
            y+=1
    
          

##input("Url: ")
##resp=requests.get(url)
##text1 = "GeeksforGeeks"
##
##
### copying text to clipboards
##
##  
### pasting the text from clipboard
##text2 = pc.paste()

text()
if copytext:
    pc.copy(finaltext)
