'''This software is to take inventory of books that are taken in and out of a university 
libray.

'''

from collections import deque
stack = deque()


class MyStack:
    def __init__(self,firstName,secondName, idCard):
        self.firstName = firstName
        self.secondName = secondName
        self.idCard = idCard
    


    def fullName(self):
        return f'{self.firstName} {self.secondName}'
    

    def add_book(self):        
        book_name = input("What is the name of the book: ")
        stack.append(book_name)

    
    def remove_book(self):
        stack.pop()


#Initialize
User = MyStack("John","Doe", "")



#if __name__ == "__main__":
