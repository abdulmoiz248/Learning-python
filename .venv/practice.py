
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
'''
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
write_To_file('sum')



