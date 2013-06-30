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
    res = {}
    for line in sent_file:
  	term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
  	scores[term] = int(score)  # Convert the score to an integer.
    
    tweets=[]
    for line in tweet_file:
	tweets.append(json.loads(line))
	
    strn=[]
    m=0	
    for i in tweets:
	if i.get("place"):
		if i["place"]["country_code"]=="US":
			if i["place"]["full_name"][-2:] in res:
				res[i["place"]["full_name"][-2:]]+=1
			else:
				res[i["place"]["full_name"][-2:]]=1
			
    
    sort_list=sorted(res, key=res.get, reverse=True)
    if sort_list:
	print sort_list[0]
if __name__ == '__main__':
    main()
    
