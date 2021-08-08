

from User import Member, Librarian


lib = Librarian("Admin", "Chennai", 30, "Cheapuk", "STK University")
print(lib)
lib.addBook(" A Time to Kill", "John Grisham", "2001")
lib.addBookItem("A Time to Kill", "001aa", "B1")
lib.addBookItem("A Time to Kill", "002bb", "B2")
lib.addBook("The House of Mirth", "Edith Wharton", "2010")
lib.addBookItem("The House of Mirth", "001ab", "C1")
lib.addBookItem("The House of Mirth", "002ab", "C2")
lib.addBook("East of Eden", "John Steinbeck", "2012")
lib.addBookItem("East of Eden", "001ac", "D1")
lib.addBookItem("East of Eden", "002ac", "D2")
lib.addBookItem("East of Eden", "003ac", "D3")
lib.addBook("The Sun Also Rises", "Ernest Hemingway", "2014")
lib.addBookItem("The Sun Also Rises", "001ad", "E1")
lib.addBookItem("The Sun Also Rises", "002ad", "E2")
lib.addBook(" A Scanner Darkly", "Philip K", "2010")
lib.addBookItem(" A Scanner Darkly", "001ae", "E1")
lib.addBookItem(" A Scanner Darkly", "002ae", "E2")
lib.viewBooks()
lib.removeBookItem("001C")
lib.viewBooks()
lib.removeBook("The House of Mirth")
lib.viewBooks()


member1 = Member("Prathamesh K", "Pune", 23, "PK4321", "NESS4321")
member2 = Member("Jeff Bezoz", "America", 30, "JB1234", "USSR2121")

print(member1)
print(member2)

member1.viewBooks()
member1.search_by_book_name("A Time to Kill")
member1.search_by_book_name("The House of Mirth")
member1.search_by_author_name("Ernest Hemingway")
member1.search_by_author_name("Philip K")
member1.issue_book("The House of Mirth", 8)
member2.issue_book("The House of Mirth-2", 10)
member1.viewBooks()

lib.view_issued_books()

member1.return_book("001ac")
member1.viewBooks()

member2.issue_book("The House of Mirth-2")

lib.viewMembers()

lib.removeMember("Elon Musk")
member1.issue_book("The House of Mirth-2")
lib.viewMembers()
lib.view_issued_books()




