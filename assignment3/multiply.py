import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    
    value = record
#    words = value.split()
#    for w in words:
    if record[0]=="a":
        mr.emit_intermediate((record[1],0), (record[2],record[3]))
 	mr.emit_intermediate((record[1],1), (record[2],record[3]))
	mr.emit_intermediate((record[1],2), (record[2],record[3]))
	mr.emit_intermediate((record[1],3), (record[2],record[3]))
	mr.emit_intermediate((record[1],4), (record[2],record[3]))
    else:
	mr.emit_intermediate((0,record[2]), (record[1],record[3]))
 	mr.emit_intermediate((1,record[2]), (record[1],record[3]))
	mr.emit_intermediate((2,record[2]), (record[1],record[3]))
	mr.emit_intermediate((3,record[2]), (record[1],record[3]))
	mr.emit_intermediate((4,record[2]), (record[1],record[3]))

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    	print key, list_of_values
    	a={}
    	b={}
	val =0
    	for rec in list_of_values:
		if a.has_key(rec[0]):
			val = val+ a[rec[0]]*rec[1]
    		else:
			a[rec[0]]=rec[1]
    	
	
    	mr.emit((key[0],key[1],val))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
