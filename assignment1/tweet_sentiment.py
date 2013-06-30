import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    #afinnfile = open("AFINN-111.txt")
    scores = {} # initialize an empty dictionary
    for line in sent_file:
  	term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
  	scores[term] = int(score)  # Convert the score to an integer.
    tweets=[]
    for line in tweet_file:
	tweets.append(json.loads(line))
	
    strn=[]	
    for i in tweets:
	ans = 0.0
	m=0
	if i.has_key("text"):
		strn.append(i["text"])
		#print strn[i]
	else:
		strn.append(" ")
		#print strn[i]
		
	sentiment=strn[m].split()
	m=m+1;
	
    	for word in sentiment:
		if scores.has_key(word):
			ans = ans+scores[word]
			
		else:
			ans=ans+0
	print float(ans)		
	

    
    #hw()
    #lines(sent_file)
    #lines(tweet_file)
    
if __name__ == '__main__':
    main()
    
