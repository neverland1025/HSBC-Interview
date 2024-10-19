# Review 1


# def add_to_list(value, my_list=[]): # the default value is mutable. The same list will be re-used if no list is passed in.
#
#     my_list.append(value)
#
#     return my_list


def add_to_list(value:int, my_list:list=None):
   if my_list is None:
        my_list=[]

   my_list.append(value)
   return my_list


# Review 2

# def format_greeting(name, age): #The parameters are not passed because the {name} and {age} are not properly formatted.
#     return "Hello, my name is {name} and I am {age} years old."
def format_greeting(name, age):
     return "Hello, my name is {} and I am {} years old.".format(name,age)


# Review 3

# class Counter:   #Attribute error, since self.count hasn't been defined with in __init___
#     count = 0
#
#     def __init__(self):
#         self.count += 1
#
#     def get_count(self):
#         return self.count

# First version, if you want to return a result as count+=1
class Counter:

    def __init__(self):
        self.count =0

    def get_count(self):
        return self.count
    def get_count_increment(self):
        self.count+=1

count=Counter()
print(count.get_count()) #output:0
count.get_count_increment()
count.get_count_increment()
print(count.get_count()) #output:2

#Second version, add parameter in the function, set initial value for count
class Counter1:

    def __init__(self,count=1):
        self.count =count


    def get_count(self):
        return self.count


# Review 4

import threading


class SafeCounter:  #multiple threads are trying to modify the same source, the value of count may not be incremented properly

    def __init__(self):
        self.count = 0
        self.lock = threading.Lock()  # add lock here

    def increment(self):
        with self.lock: #Ensure that only one thread can increment at a time
            self.count += 1


def worker(counter):
    for _ in range(1000):
        counter.increment()


counter = SafeCounter()

threads = []

for _ in range(10):
    t = threading.Thread(target=worker, args=(counter,))

    t.start()

    threads.append(t)

for t in threads:
    t.join()





# Review 5

def count_occurrences(lst):
    counts = {}

    for item in lst:

        if item in counts:

            counts[item]+=1 #counts[item] = + 1

        else:

            counts[item] = 1

    return counts




