import fb #To install this package run: sudo pip install fb

from facepy import GraphAPI #To install this package run: sudo pip install facepy


import time



token="CAACEdEose0cBAF8BlO3Ia40sSkixRbIZCZCbTR7geiwXICAUVkmlUoq3F0HSbP12EJHUpSJjGrorZBlx6Hp6DGsK32jQKEebpAEJl16AGp8QprRZBkEbDu7ofjqMtv3ITVdVlW6MHETTtx6lV8VrcyqZBqwEVLiovYV479z8YYPJyPbvpTUkciLa9TrVegbELrs89VHNyXZCR0OgxZAZAQKsKI0jP210WD1hOLQJqlpzkgZDZD"#Insert access token here.  

facebook=fb.graph.api(token)

graph1 = GraphAPI(token)



vid=272908816135266 

query=str(vid)+"/posts?fields=id&limit=5000000000"

r=graph1.get(query)




idlist=[x['id'] for x in r['data']]

print("There are "+ str(len(idlist)) +" commentable posts.")


char1='y'

count=0

if char1=='y':

    nos=input("Enter number of posts to be commented on: ")

    if nos<=len(idlist):

       for indid in idlist[len(idlist)-(nos):len(idlist)-1]:

    	  count=count+1

          facebook.publish(cat="comments",id=indid,message="You the best AB! :D")

	  time.sleep(6)

          

          print("Post Number:"+str(count)+" on www.facebook.com/"+str(indid).split('_')[0]+"/posts/"+str(indid).split('_')[1])	  

    else: 

          print("Not that many commentable posts available. ")

else :

  print("No complaints made.")
