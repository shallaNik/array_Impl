class my_array():
  def __init__(self):
    self.arr={}
    self.len=0
  
  def __str__(self):
    return str(self.__dict__)
  
  def get(self):
    return self.arr

  def push(self,item):
    self.len+=1
    print(self.len)
    self.arr[self.len-1]=item

  def pop(self):
    item=self.arr[self.len-1]
    del self.arr[self.len-1]
    self.len-=1
    return item

  def insIndex(self,index,item):
    self.len+=1
    for i in range(self.len-1,index,-1):
      self.arr[i]=self.arr[i-1]

    self.arr[index]=item

  def delIndex(self,index):
    item=self.arr[index]
    for i in range(index,self.len-1):
      self.arr[i]=self.arr[i+1]
    del self.arr[self.len-1]
    self.len-=1
    return item

array=my_array()
print(array.get())
array.push("shalaka")
array.push("hii")
array.push("welcome")
print(array.get())
array.insIndex(1,"nikam")
print(array.get())
array.delIndex(2)
print(array.get())
print(array.pop())
print(array.get())
