a = [{'name':'jk', 'score':4, 'first':1, 'second':2, 'third':2},
     {'name':'zz', 'score':1, 'first':0, 'second':0, 'third': 1},
     {'name': 'ns', 'score':4, 'first':1, 'second':0, 'third':4}]

class pm(object):
    def __init__(self,name,score,first,second,third):
        self.name = name
        self.score = score
        self.first = first
        self.second =second
        self.third = third

    def __lt__(self,other):
        return [self.score,self.first,self.second,self.third]<[other.score,other.first,other.second,other.third]

    def show(self):
        print(self.name,self.score,self.first,self.second,self.third)

from queue import PriorityQueue
pq = PriorityQueue()

for obj in a:
    p = pm(obj.get('name'),obj.get('score'),obj.get('first'),obj.get('second'),obj.get('third'))
    pq.put(p)


pq.get().show()
pq.get().show()
pq.get().show()