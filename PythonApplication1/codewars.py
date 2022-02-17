#CODEWARS KATA'S

def string_to_array(s):
    mylist = list(str(s).rsplit(' '))
    return mylist


def descending_order(num):
    #1234 -> 4321 
    return  int("".join(sorted(str(num) , reverse= True)))

def solution(num):
   if num < 0 : return 0 
   sum = 0
   for i in range(num):
       if i%3 == 0 or i%5 ==0 : sum+=i
   return sum 




word = ''
word += 'c'
word += 'b'
word += 'x'
print(word)
