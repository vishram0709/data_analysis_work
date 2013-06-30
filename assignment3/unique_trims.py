import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()
l1=[]
# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[0]
    value = record[1]
    value = value[:-10]
    
    mr.emit_intermediate("abc", value)
       
    

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    
    l1=set(list_of_values)
    for v in l1:
      total = ""
      total=total+v
      mr.emit(total)
      
# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
