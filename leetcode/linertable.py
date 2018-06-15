#coding:utf-8
class List(object):
    def __init__(self,_maxlen=10):
        pass

    def is_empty(self):     #判定线性表是否为空
        pass

    def is_full(self):      #判定线性表是否全满
        pass

    #获取线性表种某一位置的元素
    def __getitem__(self, i):
        pass

    #修改线性表种某一位置的元素
    def __setitem__(self, key, value):
        pass

    #按值查找元素的位置
    def getLoc(self,value):
        pass

    #统计线性表中元素的个数
    def Count(self):
        pass

    #表末尾插入操作
    def appendLast(self,value):
        pass

    #表任意位置插入操作：
    def insert(self,i,value):
       pass


    #删除某一位置的操作
    def remove(self,i):
        pass

    #输出操作
    def printList(self):
        pass

    #销毁操作
    def destroy(self):
        pass

class SequList(List):
    """docstring for SequList"""
    def __init__(self, maxlen=10):
        super(SequList, self).__init__()
        self._maxlen = maxlen
        self._data = []
        self._curlen = 0

    def is_empty(self):     #判定线性表是否为空
        return self._curlen==0

    def is_full(self):      #判定线性表是否全满
        return self._curlen==_maxlen

    #获取线性表种某一位置的元素
    def __getitem__(self, i):
        if 0<=i and i<self._curlen:
            return self._data[i]
        else:
            raise ValueError("index %d out of range"%(i))

    #修改线性表种某一位置的元素
    def __setitem__(self, key, value):
        if 0<=key and key<self._curlen:
            self._data[key] = value
        else:
            raise ValueError("index %d out of range"%(i))

    #按值查找元素的位置
    def getLoc(self,value):
        return self._data.index(value)

    #统计线性表中元素的个数
    def Count(self):
        return self._curlen

    #表末尾插入操作
    def appendLast(self,value):
        if self._curlen < self._maxlen:
            self._data.append(value)
            self._curlen+=1
        else:
            raise ValueError("index %d out of range"%(i))

    #表任意位置插入操作：
    def insert(self,i,value):
        if self._curlen < self._maxlen:
            self._data.insert(i,value)
            self._curlen+=1
        else:
            raise ValueError("list is_full")

    #删除某一位置的操作
    def remove(self,i):
        if self._curlen > 0:
            self._data.pop(i)
            self._curlen-=1
        else:
            raise ValueError("index %d out of range"%(i))

    #输出操作
    def printList(self):
        for v in self._data:
            print(v)

    #销毁操作
    def destroy(self):
        del self._data
        self._curlen=0




class listNode(object):
    """docstring for listNode"""
    def __init__(self, data = None):
        super(listNode, self).__init__()
        self._data = data
        self._next = None

    def getdata(self):
        return self._data

    def setdata(self,data):
        self._data = data

    def getnext(self):
        return self._next

    def setnext(self,next):
        self._next = next

class LinkedList(List):
    """docstring for ClassName"""
    def __init__(self):
        super(List, self).__init__()
        self._linkedlist = None
        self._curlen = 0

    def is_empty(self):     #判定线性表是否为空
        return self._curlen == 0

    #获取线性表种某一位置的元素
    def __getitem__(self, i):
        if i <= self._curlen:
            tmp = self._linkedlist
            j = 1
            while j<i:
                tmp = tmp._next
                j+=1
            return tmp.getdata()
        else:
            raise ValueError("index %d out of range"%(i))

    #修改线性表种某一位置的元素
    def __setitem__(self, key, value):
        if key <= self._curlen:
            tmp = self._linkedlist
            j = 1
            while j<i:
                tmp = tmp._next
                j+=1
            tmp.setdata(value)
        else:
            raise ValueError("index %d out of range"%(i))

    #按值查找元素的位置
    def getLoc(self,value):
        tmp = self._linkedlist
        i = 0
        while tmp:
            if tmp.getdata()==value:
                return i
            tmp = tmp.getnext()
            i=i+1
        return -1

    #统计线性表中元素的个数
    def Count(self):
        return self._curlen

    #表末尾插入操作
    def appendLast(self,value):
        if self._linkedlist ==None:
            self._linkedlist = listNode(value)
        else:
            tmp = self._linkedlist
            while tmp.getnext():
                tmp = tmp.getnext()
            tmp.setnext(listNode(value))
        self._curlen+=1

    #表任意位置插入操作：
    def insert(self,i,value):
        if self._curlen >=i:
            j = -1
            tmp = self._linkedlist
            while j<i-1:
                tmp = tmp.getnext()
                j+=1
            node = listNode(value)
            node.setnext(tmp.getnext())
            tmp.setnext(node)
            self._curlen+=1
        else:
            raise ValueError("index %d out of range"%(i))



    #删除某一位置的操作
    def remove(self,i):
        if self._curlen >=i:
            j = -1
            tmp = self._linkedlist
            while j<i-1:
                tmp = tmp.getnext()
                j+=1
            removenode = tmp.getnext()
            tmp.setnext(removenode.getnext())
            del removenode
            self._curlen-=1
        else:
            raise ValueError("index %d out of range"%(i))


    #输出操作
    def printList(self):
        tmp = self._linkedlist
        while tmp:
            print(tmp.getdata())
            tmp = tmp.getnext()


    #销毁操作
    def destroy(self):
        tmp = self._linkedlist
        while tmp:
            tmpnext = tmp.getnext()
            del tmp
            tmp = tmpnext


linkedList = LinkedList()
for i in range(10):
    linkedList.appendLast(i)

linkedList.printList()

print(linkedList.getLoc(5))
print(linkedList.Count())
linkedList.remove(5)
print(linkedList.Count())
linkedList.insert(5,6)
linkedList.printList()
linkedList.destroy()
