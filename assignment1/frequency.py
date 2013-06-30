import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    
    tweet_file = open(sys.argv[1])
    
    scores = {} # initialize an empty dictionary which is our result
    
    tweets=[]
    for line in tweet_file:
	tweets.append(json.loads(line))
	
    strn=[]
    m=0	
    for i in tweets:
	
	
	if i.has_key("text"):
		strn.append(i["text"])
	
	else:
		strn.append(" ")
	
	
	sentiment=strn[m].split()
	m=m+1;
	
    	for word in sentiment:
	
		if scores.has_key(word):
			scores[word] = scores[word]+1
		else:
			scores[word]=int(0)
    
    su =sum(scores.values())	
    for (key,val) in scores.items():
	print key,float(val)/su
	
    #hw()
    #lines(sent_file)
    #lines(tweet_file)
    
if __name__ == '__main__':
    main()
    
