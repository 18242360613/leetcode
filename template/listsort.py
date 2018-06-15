a = [{'name':'jk', 'score':4, 'first':1, 'second':2, 'third':2},
     {'name':'zz', 'score':1, 'first':0, 'second':0, 'third': 1},
     {'name': 'ns', 'score':4, 'first':1, 'second':0, 'third':4}]

def cmp(obj):
    return [obj.get('score'),obj.get('first'),obj.get('second'),obj.get('third')];

sorteda = sorted(a,key = cmp)
print(sorteda)