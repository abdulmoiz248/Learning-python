
def even_sum():
    number=input('Enter Number= ')
    number=int(number)
    sum=0;
    while number!=0 :
        if number%2==0 :
            sum+=number
        number = input('Enter Number= ')
        number = int(number)
    print('Sum=',sum)

def reversestring() :
    str=input("String= ")
    index= len(str)-1
    while index>=0 :
        print(str[index],end='')
        index=index-1

'''
reversestring()



str=open('practice.txt')


#count=0
#for line in str :
  #  line=line.rstrip()
 #   print(line)
 #   count+=1
#print('Count=',count)

#le=str.read()
#print(le)
#print('total words=',len(le))
#print(le[:5])

#for line in str :
#    if line.startswith('Hello'):
#        print('mil gyi oyee')

#l1=[1,2,3]
#l2=[4,5]
#l3=l1+l2
#print(l3)

#print(l3[:3])

list=list()
list.append('Abdul Moiz')
list.append('Lol')
print(9 in list)
list.sort()
print(list)

def sum_file():
    str=open('practice.txt')
    for line in str:
        arr=line.split()
        sum=0
        for number in arr:
            num=int(number)
            sum+=num
        print('Sum=',sum)
    print("End of Function")

def write_To_file(sum):
    str=open('practice.txt','a')  #a for append / w for simple write
    str.write(sum)

#sum_file()
#write_To_file('sum')


fruit=dict()
fruit[1]='Banana'
fruit['Apple']=2
fruit['Mango']=3
fruit['Melon']=4

#print(fruit['Mango'])
#print(fruit)
x=fruit.get('Melon')
print(x)

def find_repeat_name():
    file=open('practice.txt')
    names=dict()
    for name in file:
        
      #  if names.__contains__(name):
       #     names[name]=names[name]+1
        #    continue
       # names[name]=1
        
        
#alterante approach
        names[name] = names.get(name, 0) + 1
    print(names)

#find_repeat_name()

def find_number_of_words():
    line =input('Enter a Statement:')
    count=dict()
    for word in line.split():
         count[word]=count.get(word,0)+1
    print(count)

#find_number_of_words()

names=dict()
names['Abdul']=1
names['Moiz']=2
names['Maryam']=3
names['Wahb']=4

for name,id in names.items():
    print(name,id)
'''

