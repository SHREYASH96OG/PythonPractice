class books:
  
  def education(self):
    print("Generally all books are Educational")
  
  def novel(self):
    print("Books which tells story")
    
    
class classics(books):
  
  
  def Antiquarian(self):
    print("(Antiquarian)This are books which tells about all history ")
    
    
book1 = books()
book1.education()
book1.antiquarian()
