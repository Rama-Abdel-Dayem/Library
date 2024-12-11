import sqlite3 as sql
import itertools
import numpy as np
import pandas as pd
#import streamlit as sl

conn=sql.Connection('library.db')

curr=conn.cursor()

# curr.execute("create table Books(Book_Number int Primary Key,Publisher Varchar(50) ,Genre Varchar(15),Title Varchar(50) not null,Lang char(3) not null, Num_Copies int not null,Year_Published date);")


# curr.execute("create table Authors(ID int Primary Key,First_Name Varchar(50),Middle_Name Varchar(50),Last_Name Varchar(50));")

# curr.execute("create table Written_By(Author_ID int,Book_Number int,constraint written_by_pk Primary Key (Author_ID,Book_Number),constraint written_by_authorFK Foreign Key (Author_ID) References Authors,constraint written_by_BookFK Foreign Key (Book_Number) References Books);")

# curr.execute("create table Members(ID int Primary Key,Phone_Number varchar(15),First_Name Varchar(50) not null, Middle_Name Varchar(50), Last_Name Varchar(50) not null,Area_Name varchar(50),Street_Name varchar(50) not null,BuildingNo varchar(5),Email Varchar(50));")

# curr.execute("create table Staff(ID int primary key,First_Name Varchar(50) not null, Middle_Name Varchar(50), Last_Name Varchar(50)  not null,Position Varchar(50) not null,Phone_Number varchar(15),Email Varchar(50));")

# curr.execute("create table Issue_History(ID int primary key,Issuing_Date Date,Return_Due Date,Return_Date Date,Book_Number int,Member_ID int,Staff_ID int,constraint Issue_History_Book_fk Foreign Key (Book_Number) References Books,constraint Issue_History_member_fk Foreign Key (Member_ID) References Members,constraint Issue_History_Staff_fk Foreign Key (Staff_ID) References Staff );")


# curr.execute("create table languages(author_id int,lang char(3),constraint lang_author_if foreign key (author_id) references authors(id),constraint pk_lanuages primary key (author_id,lang));")


class Books:
    book_number_iter = itertools.count()
    def __init__(self,title,lang=None,year=None,num_copies=None,publisher=None,authors=None,genre=None):
        self.book_number=next(self.book_number_iter)

        self.genre=genre
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
                        (author,self.book_number))
            else:
                self.authors.append(authors)
                conn.execute("INSERT INTO Written_By (Author_ID, Book_Number) VALUES (?, ?);",
                        (author,self.book_number))
        else:
            self.authors=[]



        conn.execute("INSERT INTO Books (Book_Number, Publisher, Genre, Title, Lang, Num_Copies, Year_Published) VALUES(?, ?, ?, ?, ?, ?, ?)",
                     (self.book_number,self.publisher,self.genre,self.title,self.lang,self.year_published,self.num_copies))
        



#Setters 
    def setTitle(self,x):
        self.title=x
        conn.execute('UPDATE Books Set Title = ? where book_number = ?',(self.title,self.book_number))

    def setGenre(self,x):
        self.title=x
        conn.execute('UPDATE Books Set genre = ? where book_number = ?',(self.genre,self.book_number))

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
    
    def getGenre(self):
        return self.genre
    
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
        return pd.DataFrame(curr.fetchall(),columns=['Book_Number', 'Publisher', 'Genre', 'Title', 'Lang', 'Num_Copies', 'Year_Published'])
    
    def getBooksOnTitle(self,x):
        curr.execute('select * from books where title = ?',(x))
        return pd.DataFrame(curr.fetchall(),columns=['Book_Number', 'Publisher', 'Genre', 'Title', 'Lang', 'Num_Copies', 'Year_Published'])
        
    def getBooksOnNumber(self,x):
        curr.execute('select * from books where book_number = ?',(x))
        return pd.DataFrame(curr.fetchall(),columns=['Book_Number', 'Publisher', 'Genre', 'Title', 'Lang', 'Num_Copies', 'Year_Published'])
        
    def getBooksOnLang(self,x):
        curr.execute('select * from books where lang = ?',(x))
        return pd.DataFrame(curr.fetchall(),columns=['Book_Number', 'Publisher', 'Genre', 'Title', 'Lang', 'Num_Copies', 'Year_Published'])
        
    def getBooksOnGenre(self,x):
        curr.execute('select * from books where Genre = ?',(x))
        return pd.DataFrame(curr.fetchall(),columns=['Book_Number', 'Publisher', 'Genre', 'Title', 'Lang', 'Num_Copies', 'Year_Published'])
        
    def getBooksOnYearPublished(self,x):
        curr.execute('select * from books where year_published = ?',(x))
        return pd.DataFrame(curr.fetchall(),columns=['Book_Number', 'Publisher', 'Genre', 'Title', 'Lang', 'Num_Copies', 'Year_Published'])
        
    def getBooksOnPublisher(self,x):
        curr.execute('select * from books where publisher = ?',(x))
        return pd.DataFrame(curr.fetchall(),columns=['Book_Number', 'Publisher', 'Genre', 'Title', 'Lang', 'Num_Copies', 'Year_Published'])
        
    def getAvailableBooks(self):
        curr.execute('SELECT b.* FROM books b LEFT JOIN (SELECT book_number, COUNT(*) AS unava FROM issue_history WHERE return_date IS NULL GROUP BY book_number) taken ON b.book_number = taken.book_number WHERE b.num_copies - COALESCE(taken.unava, 0) != 0;')
        return pd.DataFrame(curr.fetchall(),columns=['Book_Number', 'Publisher', 'Genre', 'Title', 'Lang', 'Num_Copies', 'Year_Published'])
        

    def getAllAuthors(self):
        curr.execute('select * from authors')
        return pd.DataFrame(curr.fetchall(),columns=['ID', 'First_Name', 'Middle_Name', 'Last_Name'])
        
    def getAuthorsOnFirstName(self,x):
        curr.execute('select * from authors where first_name = ?', (x))
        return pd.DataFrame(curr.fetchall(),columns=['ID', 'First_Name', 'Middle_Name', 'Last_Name'])

    def getAuthorsOnMiddleName(self,x):
        curr.execute('select * from authors where middle_name = ?', (x))
        return pd.DataFrame(curr.fetchall(),columns=['ID', 'First_Name', 'Middle_Name', 'Last_Name'])

    def getAuthorsOnLastName(self,x):
        curr.execute('select * from authors where last_name = ?', (x))
        return pd.DataFrame(curr.fetchall(),columns=['ID', 'First_Name', 'Middle_Name', 'Last_Name'])

    def getAuthorsOnID(self,x):
        curr.execute('select * from authors where id = ?', (x))
        return pd.DataFrame(curr.fetchall(),columns=['ID', 'First_Name', 'Middle_Name', 'Last_Name'])


    def getAllMembers(self):
        curr.execute('select * from members')
        return pd.DataFrame(curr.fetchall(),columns=['ID', 'First_Name', 'Middle_Name', 'Last_Name','street_name','area_name','buildingno','phone_number','email'])
    
    def getMembersOnFirstName(self,x):
        curr.execute('select * from members where first_name = ?', (x))
        return pd.DataFrame(curr.fetchall(),columns=['ID', 'First_Name', 'Middle_Name', 'Last_Name','street_name','area_name','buildingno','phone_number','email'])

    def getMembersOnMiddleName(self,x):
        curr.execute('select * from members where middle_name = ?', (x))
        return pd.DataFrame(curr.fetchall(),columns=['ID', 'First_Name', 'Middle_Name', 'Last_Name','street_name','area_name','buildingno','phone_number','email'])

    def getMembersOnLastName(self,x):
        curr.execute('select * from members where last_name = ?', (x))
        return pd.DataFrame(curr.fetchall(),columns=['ID', 'First_Name', 'Middle_Name', 'Last_Name','street_name','area_name','buildingno','phone_number','email'])

    def getMembersOnID(self,x):
        curr.execute('select * from members where id = ?', (x))
        return pd.DataFrame(curr.fetchall(),columns=['ID', 'First_Name', 'Middle_Name', 'Last_Name','street_name','area_name','buildingno','phone_number','email'])
    

    def getMembersOnAreaName(self,x):
        curr.execute('select * from members where area_name = ?', (x))
        return pd.DataFrame(curr.fetchall(),columns=['ID', 'First_Name', 'Middle_Name', 'Last_Name','street_name','area_name','buildingno','phone_number','email'])
    
    def getMembersOnStreetName(self,x):
        curr.execute('select * from members where street_name = ?', (x))
        return pd.DataFrame(curr.fetchall(),columns=['ID', 'First_Name', 'Middle_Name', 'Last_Name','street_name','area_name','buildingno','phone_number','email'])
    
    def getMembersOnBuildingNo(self,x):
        curr.execute('select * from members where buildingno = ?', (x))
        return pd.DataFrame(curr.fetchall(),columns=['ID', 'First_Name', 'Middle_Name', 'Last_Name','street_name','area_name','buildingno','phone_number','email'])
    
    def getMembersOnPhoneNumber(self,x):
        curr.execute('select * from members where phone_number = ?', (x))
        return pd.DataFrame(curr.fetchall(),columns=['ID', 'First_Name', 'Middle_Name', 'Last_Name','street_name','area_name','buildingno','phone_number','email'])
    
    def getMembersOnEmail(self,x):
        curr.execute('select * from members where email = ?', (x))
        return pd.DataFrame(curr.fetchall(),columns=['ID', 'First_Name', 'Middle_Name', 'Last_Name','street_name','area_name','buildingno','phone_number','email'])

    def getAllStaff(self):
        curr.execute('select * from staff')
        return pd.DataFrame(curr.fetchall(),columns=['ID', 'First_Name', 'Middle_Name', 'Last_Name','Position','Phone_Number','Email'])
    
    def getStaffOnFirstName(self,x):
        curr.execute('select * from staff where first_name = ?', (x))
        return pd.DataFrame(curr.fetchall(),columns=['ID', 'First_Name', 'Middle_Name', 'Last_Name','Position','Phone_Number','Email'])

    def getStaffOnMiddleName(self,x):
        curr.execute('select * from staff where middle_name = ?', (x))
        return pd.DataFrame(curr.fetchall(),columns=['ID', 'First_Name', 'Middle_Name', 'Last_Name','Position','Phone_Number','Email'])

    def getStaffOnLastName(self,x):
        curr.execute('select * from staff where last_name = ?', (x))
        return pd.DataFrame(curr.fetchall(),columns=['ID', 'First_Name', 'Middle_Name', 'Last_Name','Position','Phone_Number','Email'])

    def getStaffOnID(self,x):
        curr.execute('select * from staff where id = ?', (x))
        return pd.DataFrame(curr.fetchall(),columns=['ID', 'First_Name', 'Middle_Name', 'Last_Name','Position','Phone_Number','Email'])
    
    def getStaffOnPosition(self,x):
        curr.execute('select * from staff where position = ?', (x))
        return pd.DataFrame(curr.fetchall(),columns=['ID', 'First_Name', 'Middle_Name', 'Last_Name','Position','Phone_Number','Email'])

    def getStaffOnPhone(self,x):
        curr.execute('select * from staff where phone_number = ?', (x))
        return pd.DataFrame(curr.fetchall(),columns=['ID', 'First_Name', 'Middle_Name', 'Last_Name','Position','Phone_Number','Email'])
    
    def getStaffOnEmail(self,x):
        curr.execute('select * from staff where email = ?', (x))
        return pd.DataFrame(curr.fetchall(),columns=['ID', 'First_Name', 'Middle_Name', 'Last_Name','Position','Phone_Number','Email'])

    def getIssue_History(self):
        curr.execute('select * from Issue_History')
        return pd.DataFrame(curr.fetchall(),columns=['ID', 'Issuing_Date', 'Return_Due', 'Return_Date', 'Book_Number', 'Member_ID', 'Staff_ID'])
    
    def getIssue_HistoryOnReturnDue(self,x):
        curr.execute('select * from Issue_History where Return_Due = ?', (x))
        return pd.DataFrame(curr.fetchall(),columns=['ID', 'Issuing_Date', 'Return_Due', 'Return_Date', 'Book_Number', 'Member_ID', 'Staff_ID'])

    def getIssue_HistoryOnReturnDate(self,x):
        curr.execute('select * from Issue_History where Return_Date = ?', (x))
        return pd.DataFrame(curr.fetchall(),columns=['ID', 'Issuing_Date', 'Return_Due', 'Return_Date', 'Book_Number', 'Member_ID', 'Staff_ID'])

    def getIssue_HistoryOnIssueDate(self,x):
        curr.execute('select * from Issue_History where Issue_Date = ?', (x))
        return pd.DataFrame(curr.fetchall(),columns=['ID', 'Issuing_Date', 'Return_Due', 'Return_Date', 'Book_Number', 'Member_ID', 'Staff_ID'])

    def getIssue_HistoryOnID(self,x):
        curr.execute('select * from Issue_History where id = ?', (x))
        return pd.DataFrame(curr.fetchall(),columns=['ID', 'Issuing_Date', 'Return_Due', 'Return_Date', 'Book_Number', 'Member_ID', 'Staff_ID'])
    
    def getIssue_HistoryBookNumber(self,x):
        curr.execute('select * from Issue_History where book_number = ?', (x))
        return pd.DataFrame(curr.fetchall(),columns=['ID', 'Issuing_Date', 'Return_Due', 'Return_Date', 'Book_Number', 'Member_ID', 'Staff_ID'])
    
    def getIssue_HistoryOnStaffID(self,x):
        curr.execute('select * from Issue_History where staff_id = ?', (x))
        return pd.DataFrame(curr.fetchall(),columns=['ID', 'Issuing_Date', 'Return_Due', 'Return_Date', 'Book_Number', 'Member_ID', 'Staff_ID'])
    
    def getIssue_HistoryOnMemberID(self,x):
        curr.execute('select * from Issue_History where member_id = ?', (x))
        return pd.DataFrame(curr.fetchall(),columns=['ID', 'Issuing_Date', 'Return_Due', 'Return_Date', 'Book_Number', 'Member_ID', 'Staff_ID'])
    
    def getOverdueIssues(self,x):
        curr.execute('select * from issue_history where (return_due<SYSDATE and return_date is null) or return_due<return_date;')
        return pd.DataFrame(curr.fetchall(),columns=['ID', 'Issuing_Date', 'Return_Due', 'Return_Date', 'Book_Number', 'Member_ID', 'Staff_ID'])
    
    def getBooksByAuthor(self,x):
        curr.execute("select b.* from books b, authors a, written_by w where w.author_id =a.id and w.book_number = b.book_number and a.id=?", 
                     (x))
        return pd.DataFrame(curr.fetchall(),columns=['Book_Number', 'Publisher', 'Genre', 'Title', 'Lang', 'Num_Copies', 'Year_Published'])

    def getAuthorOfBook(self,x):
        curr.execute("select b.* from books b, authors a, written_by w where w.author_id =a.id and w.book_number = b.book_number and b.book_number=?", 
                     (x))
        return pd.DataFrame(curr.fetchall(),columns=['ID', 'First_Name', 'Middle_Name', 'Last_Name'])        

    def addBook(self,x:Books):
        for book in self.books:
            if book.getID()==x.getID():
                book.setNumCopies(book.getNumCopies()+1)
                return 
            
        self.books.append(x)


    def addAuthor(self,x:Authors):            
        self.authors.append(x)
        
    def addStaff(self,x:Staff):            
        self.staff.append(x)

    def addMember(self,x:Members):            
        self.members.append(x)

    def addIssueRecord(self,x:Issue_History):            
        self.issue_history.append(x)
    

#sl.write('Hello World')    



# fake  data

# Initialize Authors
author1 = Authors(f="John", m="A", l="Doe", lang=["ENG"])
author2 = Authors(f="Jane", m="B", l="Smith", lang=["ENG"])
author3 = Authors(f="James", m="C", l="Johnson", lang=["ENG"])
author4 = Authors(f="Emily", m="D", l="Williams", lang=["ENG"])
author5 = Authors(f="Michael", m="E", l="Brown", lang=["ENG"])

authors_in_library=[author1,author2,author3,author4,author5]

# Initialize Books
book1 = Books(title="The Great Adventure", lang="ENG", year="2020-05-12", num_copies=10, publisher="Penguin", authors=[1],genre='Fanasty')
book2 = Books(title="Science Explained", lang="ENG", year="2018-03-25", num_copies=5, publisher="HarperCollins", authors=[2],genre='Non Fiction')
book3 = Books(title="Magic World", lang="ENG", year="2015-08-19", num_copies=8, publisher="Macmillan", authors=[3, 1],genre='Fanasty')  # John Doe also wrote this
book4 = Books(title="Life of a Legend", lang="ENG", year="2019-07-30", num_copies=12, publisher="Random House", authors=[4],genre='Biography')
book5 = Books(title="Physics for Beginners", lang="ENG", year="2017-09-18", num_copies=7, publisher="Oxford", authors=[5],genre='Non Fiction')

books_in_library=[book1,book2,book3,book4,book5]


# Initialize Members
member1 = Members(f="Alice", l="Green", street="Main St.", m="M", area="Downtown", build="101", email="alice.green@email.com", phone_number="123-456-7890")
member2 = Members(f="Bob", l="Blue", street="Elm St.", m="N", area="Uptown", build="202", email="bob.blue@email.com", phone_number="234-567-8901")
member3 = Members(f="Charlie", l="White", street="Oak St.", m="O", area="Suburbs", build="303", email="charlie.white@email.com", phone_number="345-678-9012")
member4 = Members(f="David", l="Black", street="Pine St.", m="P", area="City Center", build="404", email="david.black@email.com", phone_number="456-789-0123")
member5 = Members(f="Eve", l="Red", street="Coastal Rd.", m="Q", area="Beachside", build="505", email="eve.red@email.com", phone_number="567-890-1234")

members_in_library=[member1,member2,member3,member4,member5]


# Initialize Staff
staff1 = Staff(f="Sarah", l="Davis", street="Main St.", p="Manager", phone="678-901-2345", email="sarah.davis@email.com")
staff2 = Staff(f="Tom", l="White", street="Elm St.", p="Assistant", phone="789-012-3456", email="tom.white@email.com")
staff3 = Staff(f="Linda", l="Miller", street="Oak St.", p="Librarian", phone="890-123-4567", email="linda.miller@email.com")
staff4 = Staff(f="James", l="Taylor", street="Pine St.", p="Security", phone="901-234-5678", email="james.taylor@email.com")
staff5 = Staff(f="Sophia", l="Wilson", street="Coastal Rd.", p="Technician", phone="012-345-6789", email="sophia.wilson@email.com")

staff_in_library=[staff1,staff2,staff3,staff4,staff5]


# Initialize Issue_History
issue1 = Issue_History(issue_date="2024-11-01", due_date="2024-11-15", book_num=101, member_id=1, staff_id=3, return_date="2024-11-14")
issue2 = Issue_History(issue_date="2024-11-05", due_date="2024-11-19", book_num=102, member_id=2, staff_id=4, return_date="2024-11-18")
issue3 = Issue_History(issue_date="2024-10-20", due_date="2024-11-03", book_num=103, member_id=3, staff_id=2, return_date="2024-11-01")
issue4 = Issue_History(issue_date="2024-11-10", due_date="2024-11-24", book_num=104, member_id=4, staff_id=5, return_date="2024-11-23")
issue5 = Issue_History(issue_date="2024-11-07", due_date="2024-11-21", book_num=105, member_id=5, staff_id=1, return_date="2024-11-20")
issue6 = Issue_History(issue_date="2024-10-20", due_date="2024-11-01", book_num=102, member_id=4, staff_id=1, return_date=None)
issue7 = Issue_History(issue_date="2024-11-10", due_date="2024-11-24", book_num=102, member_id=3, staff_id=5, return_date=None)
issue8 = Issue_History(issue_date="2024-11-07", due_date="2024-11-21", book_num=105, member_id=5, staff_id=1, return_date=None)

issuing_in_library=[issue1,issue2,issue3,issue4,issue5]






    


    
    

    
    
    
    


     
    
    
    


      
    


    



    