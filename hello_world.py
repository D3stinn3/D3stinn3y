import re
import time

def solution(N):
    binary_value = bin(N)
    for value in binary_value:
        print(value)
    
    while True:
        if value != '1':
            print('1 is there')
        elif value != '0':
            print('0 is there')
        break
    
    correct_binary = binary_value[2:]
    print(correct_binary)

    while True:
        if correct_binary != '0':
            zero_gaps = correct_binary.split('0')
            print(len(zero_gaps))
        if correct_binary != '1':
            one_gaps = correct_binary.split('1')
            one_gaps_transformed = str(one_gaps)
            one_gaps_transformed.strip('')
            print(len(one_gaps), len(one_gaps_transformed))
        break

solution(147)

def solution(A):
    A = [1, 2, 3]
    for value in A:
        if value in range(A) < 0:
            print('not a valid number!')
        else:
            print('valid number!')


"""yeild functions"""

def list_comprehension(R):
    mylist = [x*x for x in range(R)] # list comprehension does the work of a generator
    # because of the [x*x for x in range(R)] it alsready knows what to do
    for iterable in mylist:
        print(iterable)

    mylist1 = range(R) # the generator that yeilds the iterations

    for iter in mylist1:
        yield iter*iter # calling a func at this point does not run the program!


object = list_comprehension(3) # list_comprehension becomes an object
# the object must be called in order to yield results
for i in object:
    print(i)

class Child_id:

    def __init__(self, distance, min_dist, max_dist):
        self.distance = distance
        self.min_dist = min_dist
        self.max_dist = max_dist


    def get_child_names(self, average_dist):
        if self.distance >= 1:
            yield self.max_dist
        elif self.distance <= 1:
            yield self.min_dist
        while True:
            if average_dist > 0:
                yield self.distance % average_dist
            elif average_dist < 0:
                yield self.distance * average_dist

child = Child_id(1, 0, 1)
child_instance = child.get_child_names(-2)
print(child_instance.__next__())


class Bank(): # Bank and Atm creation and state of country!
    crisis = False
    
    def atm(self):
        while not self.crisis: # crisis/exhaustion control on generators in banking application
            yield '1000ksh'
    
kenya_commercial_bank = Bank()
uhuru_highway_atm = kenya_commercial_bank.atm()

print(uhuru_highway_atm.__next__())
print(uhuru_highway_atm.__next__()) # the atm will serve gracefully when there is no crisis!
print([uhuru_highway_atm.__next__() for cash in range(3)]) # list comprehension
juja_atm = kenya_commercial_bank.atm()
print([juja_atm.__next__() for cash in range(3)])
# this leads us to when crisis is on the way...

try:
    kenya_commercial_bank.crisis = True 
    # the crisis is on, this translates to the atm

    print(uhuru_highway_atm.__next__())
     # the bank atm gives out no money!

    juja_atm = kenya_commercial_bank.atm()
    print([juja_atm.__next__() for cash in range(3)])


except StopIteration as si:
    
    print(f'{si} signal error! cant process any more cash!')


"""object oriented programming"""


class Student:
    
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def get_grade(self): # this is amethod to the class student
        return self.grade


class Course:

    def __init__(self, name, max_students):
        self.active = False
        self.name = name
        self.max_students = max_students
        self.students = [] # list of students

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True # return true if the student was added succesfully!
        return False

    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()

        return value / len(self.students)


s1 = Student('Maria', 24, 95)
s2 = Student('Destinne', 26, 98)
s3 = Student('Bill', 19, 65)

course = Course('Science', 2)
course.add_student(s1)
course.add_student(s2)

print(course.students[0].name) # fetches the students list iterable 0 defined in Course!
print(course.get_average_grade())


"""object inheritance"""


class Pet: # this is the parent class that all the otehr classes inherit from!

    def __init__(self, name, age, appearance, weight):
        self.name = name
        self.age = age
        self.appearance = appearance
        self.weight = weight
    
    def reveal(self):
        print(f'jina langu ni {self.name} na nina miaka {self.age}')


    def speak(self):
        print(f'{self.name} hajui cha kusema!') # overriding the method spaek in child classes 

class Dog(Pet): # object inheritance

    def speak(self):
        print('na mimi hua na ---> bark!')

    def illness(self):
        if self.age >= 20 or self.appearance == 'pale':
            print(f'{self.name} is so sick and needs to see a doctor!')
            print('%s is really sick because of his/her %s appearance' % (self.name, self.appearance)) 
            return self.name

class Cat(Pet): # Dog and Cat classes are child classes inheriting from parent class Pet!

    def speak(self):
        print('na mimi hua na ---> meow!')

    def illness(self):
        if self.age >= 10 or self.appearance == 'pale':
            print(f'{self.name} is so sick and needs medical attention')
            print('this is because %s is of age: %d' % (self.name, self.age))
            return self.name

class Fish(Pet): # the child class that has been overridden!
    
    def speak(self):
        print(f'{self.name} labda atoe ---> mabubbles!')

    def illness(self):
        if self.weight <= 1 or self.appearance == 'pale':
            print(f'dear {self.name} is in so much pain and needs to see a doctor immediately')
            print('%s is in serious danger becuase of the weight level: %d' % (self.name, self.weight))
            return self.name

p = Pet('Destinne', 10, 'pale', 0)
p.reveal()
c = Cat('fury', 2, 'pale', 0)
c.reveal()
c.speak()
c.illness()
d = Dog('Loki', 4, 'pale', 0)
d.reveal()
d.speak()
d.illness()
f = Fish('Lubbles', 10, 'pale', 0)
f.reveal()
f.speak()
f.illness()


def Respect():
    x = {}
    x[1] = 'natumia key value ya kwanza --->  1' # this is a hash value!
    x[1.0] = 'natumia key value ya pili ---> 1.0' # this is not a hash value!
    print(x)

    # to actually check
    if x[1] is hash(1):
        print('this is a hash value!')
    elif x[1] is not hash(1):
        print('this is a not a hash value!')
    else:
        print('this is not any value! between none hash and hash!')

Respect()

def the_main():
    pass

class Searching_Dir():

    def __init__(self, phone_number, user, text, message):
        self.stealth_search = False
        self.phone_number = phone_number
        self.user = user
        self.text = text
        self.message = message

class Slow_Search(Searching_Dir):

    def user_verification(self):
        if self.user is type(str):
            print('huyu ni mtu real na anaitwa %s!' % (self.user))
        elif self.user is type(int):
            print('huyu ameingia na code na code yake ni %d' % (self.user))
        elif self.user is type(float):
            print('huyu ni robot na identification yake ni %d' % (self.user))

        else:
            print('can not be described!')

    def number_verification(self):
        if len(self.text) != 12:
            return False
        for i in range(4):
            if not self.text[i].isdecimal():
                return False
        if not self.text[0] == '+':
            return False
        if not self.text[4] == '-':
            return False
        for x in range(5, 7):
            if not self.text[x].isdecimal():
                return False
        while True:
            if not self.text:
                print('we have not experienced any text yet!')
            if not self.user:
                print('we have not experienced any user')

class number_from_text(Searching_Dir):


    def vetting(self):            
        for i in range(len(self.message)):
            chunk = self.message[i : i+12]
            if self.text in chunk:
                print('Phone number found: ' + self.text)


search = Searching_Dir('+25470852', 'Destinne', '+25470852', 'sasa hii ni number yako? +25470852')
search1 = Slow_Search('+25470852', 'Maria', '+25470852', 'excuse me, is this your number? +25470852 ')
print(search1.user_verification())
print(search1.number_verification())

search2 = number_from_text('+25470852', 'Destinne', '+25470852', 'sasa hii ni number yako? +25470852')
print(search2.vetting())


"""Regex Functions"""


def Regex():
    Regex_Phone = re.compile(r'\d\d\d - \d\d\d - \d\d\d\d') # the raw string is the standard string used in regex applications
    num = input('Please input phone number to verify: ')
    message = 'my name is Destinne and {0}'.format(num)
    mo = Regex_Phone.findall(message)
    mo1 = Regex_Phone.search(num)
    print('phone number found and verified as ' + ' value!')


Regex()

def Regex1():
    Regex_Phone = re.compile(r'\nd\nd\nd - \nd\nd\nd') # the regex representation
    num = input('please input phone number to verify: ')
    message = 'my name is Destine and {0}'.format(num)
    mo  = Regex_Phone.search(num)
    mo1 = Regex_Phone.search(message)
    print(str(mo), str(mo1))

Regex1()

def Regex2():
    Bat_Regex = re.compile(r'Batwo(man)*') # regex funcs are written in raw strings!
    Bat_Search = Bat_Regex.search('Batman was here!')
    Bat_Search1 = Bat_Regex.search('Batwoman is here')
    print(Bat_Search, Bat_Search1)

Regex2()


def Regex3():
    Joker_Regex = re.compile(r'(Ha){3}')
    Joker_Regex1 = re.compile(r'(Ha){2,6}')
    # the greedy regex will always have the 
    Joker_Regex2 = re.compile(r'(Ha){0,3}?') # non-greedy rejex is defined by the question marks!
    Joker_Search = Joker_Regex.search('HaHaHa')
    Joker_Search1 = Joker_Regex1.search('HaHaHaHaHaHa')
    Joker_Search2 = Joker_Regex2.search('HaHaHa')

    if Joker_Regex is Joker_Regex2:
        print('the regex is possible by position')
    
    else:
        print('the regex is not possible by position')

    if Joker_Search == None:
        print(Joker_Search)

    else:
        print(Joker_Search.group())

    if Joker_Search.group() == Joker_Search2.group():
        print('the question mark does not define greedy and non greedy!')
    
    else:
        print('the question mark defines greedy and non greedy!')
        print(Joker_Search.group(), Joker_Search2.group())

    

Regex3()

def Regex4():
    print('this is the forth regex involving types of regex formation!')
    first_regex = re.compile(r'\w+\s\d+')
    find_module = first_regex.findall('sabuni 5, kamusi 4, makali 3')
    print(str(find_module) + ' is a character class regex values!')
    print(str(find_module.append('lovey 6')))
    second_regex = re.compile(r'[AEIOUaeiou]')
    print('the second regex creates the first instance of word groupings made by vowels!')
    find_module1 = second_regex.findall('arCH, Your baCk From thE sTART')
    print(str(find_module1) + ' is considered a positive character class regex value!')
    third_regex = re.compile(r'[^AEIOUaeiou]')
    find_module2 = third_regex.findall('promiSE mE FOrever')

    #the findall module may become a substitute to search module in regex functions
    print(str(find_module2) + 'is a negative character class!')

Regex4()

def Regex5():
    Kuanza_na = re.compile(r'^Hello') # means must start with the string hello!
    Kumaliza_na = re.compile(r'\d+$') # means must end with a numeral

    message = 'Hello, 42'
    
    reg1 = Kuanza_na.search(message)
    reg2 = Kumaliza_na.search(message)

    if message.startswith('Hello') is str(reg1.group()):
        print(reg1.group())
    else:
        print(reg2.group())
    
    if message.endswith('42') is str(reg2.group()):
        print(reg2.group())
    else:
        print(reg1.group())


    for x in message:
        print(message.split(','))


Regex5()

def Regex_Matching():
    print('there are different types of matching in regex values')

Regex_Matching()

class General:

    def _init__(self, regexnum, matcher, message, searchmode, grouping):
        self.regexnum = regexnum
        self.matcher = matcher
        self.message = message
        self.searchmode = searchmode
        self.grouping = grouping
    
class Matching1(General):

    def Parantheses(self):
        print('termed as grouping with parantheses')

        regex1 = re.compile(r'self.matcher')
        searching = regex1.search(str(self.message))

        if str(self.regexnum) == str(regex1):
            print('starting searching mode!')
            time.sleep(2)
            outcome = searching.group()
            print(outcome)
        else:
            print('starting searching mode!')
            time.sleep(2)
            return outcome

class Matching2(General):

    def Piping(self):
        print('termed as grouping with the pipe!')

        regex2 = re.compile(r'Destinne|Maria')
        searching2 = regex2.search(str(self.message))

        if str(self.regexnum) == str(regex2):
            print('starting searching mode!')
            time.sleep(2)
            outcome1 = searching2.group()
            print(outcome1)
        else:
            print('starting searching mode!')
            time.sleep(2)
            return outcome1



def Excercise():

    myNumber = 42

    if myNumber == 42:
        print('correct')
    
    else:
        print('incorrect')


Excercise()


    

