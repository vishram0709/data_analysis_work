import sys
import json
import operator
#x = {1: 2, 3: 4, 4:3, 2:1, 0:0}

def main():
    
    tweet_file = open(sys.argv[1])
    
    scores = {} # initialize an empty dictionary
    
    tweets=[]
    for line in tweet_file:
      tweets.append(json.loads(line))
    

    for ent in tweets:
      if ent.has_key("entities"):
	 if ent["entities"].has_key("hashtags"):
	    if ent["entities"]["hashtags"]:
	       for taglist in ent["entities"]["hashtags"]:
		   if scores.has_key(taglist["text"]):
	 	      scores[taglist["text"]]+=1.0
		   else:
		      scores[taglist["text"]]=1.0
    sorted_x = sorted(scores.iteritems(), key=operator.itemgetter(1))
    
    for i in range(10):
	print sorted_x[i][0],sorted_x[i][1]
if __name__ == '__main__':
    main()
    
