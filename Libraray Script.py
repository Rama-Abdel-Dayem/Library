import sqlite3 as sql
import itertools
import numpy as np
import pandas as pd

conn=sql.Connection('library.db')

curr=conn.cursor()


class Books:
    book_number_iter = itertools.count()
    def __init__(self,title,lang=None,year=None,num_copies=None,publisher=None,authors=None):
        self.book_number=next(self.book_number_iter)

        self.title =title 
        self.lang=lang
        self.year_published=year
        self.num_copies=num_copies
        self.publisher=publisher

        if authors:
            self.authors=[]
            if(type(authors)==list):
                self.authors=authors
                for author in authors:
                    conn.execute("INSERT INTO Written_By (Author_ID, Book_Number) VALUES (?, ?);",
                        (self.id,author))
            else:
                self.authors.append(authors)
                conn.execute("INSERT INTO Written_By (Author_ID, Book_Number) VALUES (?, ?);",
                        (self.id,authors))
        else:
            self.authors=[]



        conn.execute("INSERT INTO Books (Book_Number, Publisher, Genre, Title, Lang, Num_Copies, Year_Published) VALUES(?, ?, ?, ?, ?, ?, ?)",
                     (self.title,self.lang,self.year_published,self.num_copies,self.publisher))
        



#Setters 
    def setTitle(self,x):
        self.title=x
        conn.execute('UPDATE Books Set Title = ? where book_number = ?',(self.title,self.book_number))

    def setLang(self,x):
        self.lang=x
        conn.execute('UPDATE Books Set Lang = ? where book_number = ?',(self.lang,self.book_number))

    def setYearPublished(self,x):
        self.year_published=x
        conn.execute('UPDATE Books Set Year_Published = ? where book_number = ?',(self.year_published,self.book_number))

    def setNumCopies(self,x):
        self.num_copies=x
        conn.execute('UPDATE Books Set Num_Copies = ? where book_number = ?',(self.num_copies,self.book_number))

    def setPublisher(self,x):
        self.publisher=x
        conn.execute('UPDATE Books Set Publisher = ? where book_number = ?',(self.publisher,self.book_number))


#Getters
    def getTitle(self):
        return self.title
    
    def getLang(self):
        return self.lang
    
    def getYearPublished(self):
        return self.year_published
    
    def getNumCopies(self):
        return self.num_copies
    
    def getPublisher(self):
        return self.publisher


class Authors:
    id_iter = itertools.count()
    def __init__(self,f='ANON',m='ANON',l='ANON',lang=[]):
        self.id=next(self.id_iter)

        self.first_name=f
        self.middle_name = m
        self.last_name=l

        self.lang=[]
        if(type(lang)==list):
            for i in lang:
                self.lang.append(i)
        else:
            self.lang.append(lang)

        conn.execute("INSERT INTO Authors (ID, First_Name, Middle_Name, Last_Name) VALUES(?, ?, ?, ?);",
                     (self.id,self.first_name,self.middle_name,self.last_name))
        
        for language in self.lang:
            conn.execute("INSERT INTO languages (author_id, lang) VALUES(?, ?);",
                        (self.id,language))

#Setters 
    def setFirstName(self,x):
        self.first_name=x
        conn.execute('UPDATE Authors Set first_name = ? where id = ?',(self.first_name,self.id))

    def setMiddleName(self,x):
        self.first_name=x
        conn.execute('UPDATE Authors Set middle_name = ? where id = ?',(self.middle_name,self.id))

    def setLastName(self,x):
        self.first_name=x
        conn.execute('UPDATE Authors Set last_name = ? where id = ?',(self.last_name,self.id))


    def setLang(self,x):

        if type(x)==list:
            for i in x:
                self.lang.append(i)
                conn.execute("INSERT INTO languages (author_id, lang) VALUES(?, ?);",
                        (self.id,i))
                
        else:
            self.lang.append(x)
            conn.execute("INSERT INTO languages (author_id, lang) VALUES(?, ?);",
                        (self.id,x))


    


#Getters
    def getFirstName(self):
        return self.first_name
    
    def getMiddleName(self):
        return self.middle_name
    
    def getLastName(self):
        return self.last_name
    
    def getLang(self):
        return self.lang
    
    
class Members:
    id_iter = itertools.count()
    def __init__(self,f,l,street,m=None,area=None,build=None,email=None,phone_number=None):
        self.id=next(self.id_iter)

        self.first_name=f
        self.middle_name =m
        self.last_name=l

        self.__street_name=street
        self.__area_name=area
        self.__buildingNo=build
        self.__phone_number=phone_number
        self.__email=email

        conn.execute("INSERT INTO Members (ID, First_Name, Middle_Name, Last_Name,street_name,area_name,buildingno,phone_number,email) VALUES(?, ?, ?, ?,?,?,?,?,?);",
                     (self.id,self.first_name,self.middle_name,self.last_name,self.__street_name,self.__area_name,self.__buildingNo,self.__phone_number,self.__email))


#Setters 
    def setFirstName(self,x):
        self.first_name=x
        conn.execute('UPDATE members Set first_name = ? where id = ?',(self.first_name,self.id))

    def setMiddleName(self,x):
        self.first_name=x
        conn.execute('UPDATE members Set middle_name = ? where id = ?',(self.middle_name,self.id))

    def setLastName(self,x):
        self.first_name=x
        conn.execute('UPDATE members Set last_name = ? where id = ?',(self.last_name,self.id))

    def setEmail(self,x):
        self.email=x
        conn.execute('UPDATE members Set email = ? where id = ?',(self.__email,self.id))

    def setPhoneNumber(self,x):
        self.first_name=x
        conn.execute('UPDATE members Set phone_number = ? where id = ?',(self.__phone_number,self.id))

    def setArea(self,x):
        self.first_name=x
        conn.execute('UPDATE members Set area_name = ? where id = ?',(self.__area_name,self.id))

    def setStreetName(self,x):
        self.first_name=x
        conn.execute('UPDATE members Set street_name = ? where id = ?',(self.__street_name,self.id))

    def setBuildingNo(self,x):
        self.first_name=x
        conn.execute('UPDATE members Set buildingno = ? where id = ?',(self.__buildingNo,self.id))


    


#Getters
    def getFirstName(self):
        return self.first_name
    
    def getMiddleName(self):
        return self.middle_name
    
    def getLastName(self):
        return self.last_name
    
    def getEmail(self):
        return self.__email
    
    def getPhoneNumber(self):
        return self.__phone_number
    
    def getAreaName(self):
        return self.__area_name
    
    def getStreetName(self):
        return self.__street_name
    
    def getBuildingNo(self):
        return self.__buildingNo
    

class Staff:
    id_iter = itertools.count()
    def __init__(self,f,l,street,p,phone=None,email=None,m=None):
        self.id=next(self.id_iter)

        self.first_name=f
        self.middle_name =m
        self.last_name=l

        self.position=p
        self.__phone_number=phone
        self.__email=email

        conn.execute("INSERT INTO Staff (ID, First_Name, Middle_Name, Last_Name,Position,Phone_Number,Email) VALUES(?,?,?,?,?,?,?);",
                     (self.id,self.first_name,self.middle_name,self.last_name,self.position,self.__phone_number,self.__email))



#Setters 
    def setFirstName(self,x):
        self.first_name=x
        conn.execute('UPDATE Staff Set first_name = ? where id = ?',(self.first_name,self.id))

    def setMiddleName(self,x):
        self.middle_name=x
        conn.execute('UPDATE Staff Set middle_name = ? where id = ?',(self.middle_name,self.id))

    def setLastName(self,x):
        self.last_name=x
        conn.execute('UPDATE Staff Set last_name = ? where id = ?',(self.last_name,self.id))

    def setEmail(self,x):
        self.__email=x
        conn.execute('UPDATE Staff Set email = ? where id = ?',(self.__email,self.id))

    def setPhoneNumber(self,x):
        self.__phone_number=x
        conn.execute('UPDATE Staff Set phone_number = ? where id = ?',(self.__phone_number,self.id))

    def setPosition(self,x):
        self.position=x
        conn.execute('UPDATE staff Set position = ? where id = ?',(self.position,self.id))


    


#Getters
    def getFirstName(self):
        return self.first_name
    
    def getMiddleName(self):
        return self.middle_name
    
    def getLastName(self):
        return self.last_name
    
    def getEmail(self):
        return self.__email
    
    def getPhoneNumber(self):
        return self.__phone_number
    
    def getPosition(self):
        return self.position
    

class Issue_History:
    id_iter = itertools.count()
    def __init__(self,issue_date,due_date,book_num,member_id,staff_id,return_date=None):
        self.id=next(self.id_iter)

        self.issuing_date=issue_date
        self.return_date=return_date
        self.return_due=due_date
        self._book_number=book_num
        self._member_id=member_id
        self._staff_id=staff_id
        conn.execute("INSERT INTO Issue_History (ID, Issuing_Date, Return_Due, Return_Date, Book_Number, Member_ID, Staff_ID) VALUES(?, ?, ?, ?, ?, ?, ?);",
                     (self.issuing_date,self.return_due,self.return_date,self._book_number,self._member_id,self._staff_id))



#Setters 
    def setIssuingDate(self,x):
        self.issuing_date=x
        conn.execute('UPDATE Issue_History Set issuing_date = ? where id = ?',(self.issuing_date,self.id))

    def setReturnDue(self,x):
        self.return_due=x
        conn.execute('UPDATE Issue_History Set Return_Due = ? where id = ?',(self.return_due,self.id))

    def setReturnDate(self,x):
        self.return_date=x
        conn.execute('UPDATE Issue_History Set return_date = ? where id = ?',(self.return_date,self.id))

    



    


#Getters
    def getIssuingDate(self):
        return self.issuing_date

    def getReturnDue(self):
        return self.return_due
    
    def getReturnDate(self):
        return self.return_date
    
    def getMemberID(self):
        return self._member_id

    def getStaffID(self):
        return self._staff_id
    
    def getBookNumber(self):
        return self._book_number
    
    def getIssueID(self):
        return self.id
    
    
class Library:
    def __init__(self,authors=None,staff=None,members=None,issue_history=None,books=None):
        self.authors = authors if authors is not None else []
        self.staff = staff if staff is not None else []
        self.members = members if members is not None else []
        self.issue_history = issue_history if issue_history is not None else []
        self.books = books if books is not None else []

    def getAllBooks(self):
        curr.execute('select * from books')
        return curr.fetchall()
    
    def getBooksOnTitle(self,x):
        curr.execute('select * from books where title = ?',(x))
        return curr.fetchall()
        
    def getBooksOnNumber(self,x):
        curr.execute('select * from books where book_number = ?',(x))
        return curr.fetchall()
        
    def getBooksOnLang(self,x):
        curr.execute('select * from books where lang = ?',(x))
        return curr.fetchall()
        
    def getBooksOnGenre(self,x):
        curr.execute('select * from books where Genre = ?',(x))
        return curr.fetchall()
        
    def getBooksOnYearPublished(self,x):
        curr.execute('select * from books where year_published = ?',(x))
        return curr.fetchall()
        
    def getBooksOnPublisher(self,x):
        curr.execute('select * from books where publisher = ?',(x))
        return curr.fetchall()
        
    def getAvailableBooks(self):
        curr.execute('SELECT b.* FROM books b LEFT JOIN (SELECT book_number, COUNT(*) AS unava FROM issue_history WHERE return_date IS NULL GROUP BY book_number) taken ON b.book_number = taken.book_number WHERE b.num_copies - COALESCE(taken.unava, 0) != 0;')
        return curr.fetchall()
        

    def getAllAuthors(self):
        curr.execute('select * from authors')
        return curr.fetchall()
        
    def getAuthorsOnFirstName(self,x):
        curr.execute('select * from authors where first_name = ?', (x))
        return curr.fetchall()

    def getAuthorsOnMiddleName(self,x):
        curr.execute('select * from authors where middle_name = ?', (x))
        return curr.fetchall()

    def getAuthorsOnLastName(self,x):
        curr.execute('select * from authors where last_name = ?', (x))
        return curr.fetchall()

    def getAuthorsOnID(self,x):
        curr.execute('select * from authors where id = ?', (x))
        return curr.fetchall()


    def getAllMembers(self):
        curr.execute('select * from members')
        return curr.fetchall()
    
    def getMembersOnFirstName(self,x):
        curr.execute('select * from members where first_name = ?', (x))
        return curr.fetchall()

    def getMembersOnMiddleName(self,x):
        curr.execute('select * from members where middle_name = ?', (x))
        return curr.fetchall()

    def getMembersOnLastName(self,x):
        curr.execute('select * from members where last_name = ?', (x))
        return curr.fetchall()

    def getMembersOnID(self,x):
        curr.execute('select * from members where id = ?', (x))
        return curr.fetchall()
    

    def getMembersOnAreaName(self,x):
        curr.execute('select * from members where area_name = ?', (x))
        return curr.fetchall()
    
    def getMembersOnStreetName(self,x):
        curr.execute('select * from members where street_name = ?', (x))
        return curr.fetchall()
    
    def getMembersOnBuildingNo(self,x):
        curr.execute('select * from members where buildingno = ?', (x))
        return curr.fetchall()
    
    def getMembersOnPhoneNumber(self,x):
        curr.execute('select * from members where phone_number = ?', (x))
        return curr.fetchall()
    
    def getMembersOnEmail(self,x):
        curr.execute('select * from members where email = ?', (x))
        return curr.fetchall()

    def getAllStaff(self):
        curr.execute('select * from staff')
        return curr.fetchall()
    
    def getStaffOnFirstName(self,x):
        curr.execute('select * from staff where first_name = ?', (x))
        return curr.fetchall()

    def getStaffOnMiddleName(self,x):
        curr.execute('select * from staff where middle_name = ?', (x))
        return curr.fetchall()

    def getStaffOnLastName(self,x):
        curr.execute('select * from staff where last_name = ?', (x))
        return curr.fetchall()

    def getStaffOnID(self,x):
        curr.execute('select * from staff where id = ?', (x))
        return curr.fetchall()
    
    def getStaffOnPosition(self,x):
        curr.execute('select * from staff where position = ?', (x))
        return curr.fetchall()

    def getStaffOnPhone(self,x):
        curr.execute('select * from staff where phone_number = ?', (x))
        return curr.fetchall()
    
    def getStaffOnEmail(self,x):
        curr.execute('select * from staff where email = ?', (x))
        return curr.fetchall()

    def getIssue_History(self):
        curr.execute('select * from Issue_History')
        return curr.fetchall()
    
    def getIssue_HistoryOnReturnDue(self,x):
        curr.execute('select * from Issue_History where Return_Due = ?', (x))
        return curr.fetchall()

    def getIssue_HistoryOnReturnDate(self,x):
        curr.execute('select * from Issue_History where Return_Date = ?', (x))
        return curr.fetchall()

    def getIssue_HistoryOnIssueDate(self,x):
        curr.execute('select * from Issue_History where Issue_Date = ?', (x))
        return curr.fetchall()

    def getIssue_HistoryOnID(self,x):
        curr.execute('select * from Issue_History where id = ?', (x))
        return curr.fetchall()
    
    def getIssue_HistoryBookNumber(self,x):
        curr.execute('select * from Issue_History where book_number = ?', (x))
        return curr.fetchall()
    
    def getIssue_HistoryOnStaffID(self,x):
        curr.execute('select * from Issue_History where staff_id = ?', (x))
        return curr.fetchall()
    
    def getIssue_HistoryOnMemberID(self,x):
        curr.execute('select * from Issue_History where member_id = ?', (x))
        return curr.fetchall()
    
    def getOverdueIssues(self,x):
        curr.execute('select * from issue_history where (return_due<SYSDATE and return_date is null) or return_due<return_date;')
        return curr.fetchall()
    
    def getBooksByAuthor(self,x):
        curr.execute("select b.* from books b, authors a, written_by w where w.author_id =a.id and w.book_number = b.book_number and a.id=?", 
                     (x))
        return curr.fetchall()

    def getAuthorOfBook(self,x):
        curr.execute("select b.* from books b, authors a, written_by w where w.author_id =a.id and w.book_number = b.book_number and b.book_number=?", 
                     (x))
        return curr.fetchall()        

    def addBook(self,x):
        for book in self.books:
            if book.getID()==x.getID():
                book.setNumCopies(book.getNumCopies()+1)
                return 
            
        self.books.append(x)


    def addAuthor(self,x):            
        self.authors.append(x)
        
    def addStaff(self,x):            
        self.staff.append(x)

    def addMember(self,x):            
        self.members.append(x)

    def addIssueRecord(self,x):            
        self.issue_history.append(x)
    


    
    
    
    


    
    

    
    
    
    


     
    
    
    


      
    


    



    