# -*- coding:utf-8 -*-
# drict = {'qw':1,'qa':-1,'asd':0,'asdf':2}
# def cmp(obj):
#     return obj.val;
# #升序
# a = sorted(drict.items(),key = lambda x:x[1])
# print(a)
#[{'softname': '1'}, {'softname': '2'}, {'softname': '3'}, {'softname': '5'}, {'softname': '7'}, {'softname': '9'}]
#降序
# data_list.sort(key=lambda obj:obj.get('softname'), reverse=True)
# print(data_list)
#[{'softname': '9'}, {'softname': '7'}, {'softname': '5'}, {'softname': '3'}, {'softname': '2'}, {'softname': '1’}]

a = [{'name':'jk', 'score':4, 'first':1, 'second':2, 'third':2}, 
     {'name':'zz', 'score':1, 'first':0, 'second':0, 'third': 1}, 
     {'name': 'ns', 'score':4, 'first':1, 'second':0, 'third':4}]

# def cmp(obj):
#     return [obj.get('score'),obj.get('first'),obj.get('second'),obj.get('third')];

# sorteda = sorted(a,key = cmp)
# print(sorteda)

# [{'second': 0, 'score': 1, 'name': 'zz', 'third': 1, 'first': 0}, 
#  {'second': 0, 'score': 4, 'name': 'ns', 'third': 4, 'first': 1}, 
#  {'second': 2, 'score': 4, 'name': 'jk', 'third': 2, 'first': 1}]

# [{'name': 'zz', 'score': 1, 'third': 1, 'first': 0, 'second': 0},
#  {'name': 'ns', 'score': 4, 'third': 4, 'first': 1, 'second': 0},
#  {'name': 'jk', 'score': 4, 'third': 2, 'first': 1, 'second': 2}+]


class pm():
    def __init_(self,name,first,second,third):
        self.name = name
        self.score = score
        self.first = first
        self.second =second
        self.third = third

    def __lt__(self,other):
        return [self.score,self.first,self.second,self.third]<[other.score,other.first,other.second,other.third]


from queue import PriorityQueue
pq = PriorityQueue()

for obj in a:
    p = pm(obj.get('name'),obj.get('score'),obj.get('first'),obj.get('second'),obj.get('third'))
    pq.put(p)


print(pq.get())
print(pq.get())
print(pq.get())