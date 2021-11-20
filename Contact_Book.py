
class Contact_Book:         #* Class Contact Book

    def __init__(self, name, contact_no):   #* Initialise the variables
        self.name = name    
        self.contact_no = contact_no
        self.contact_book={}        #* Dictionary for contact book
        

    def display_contact(self):      #* Display contacts method
        for key, value in self.contact_book.items():   #* Display Name, contact_no for dictionary
            print(f"Name: {key},\tContact No.: {value}")    
    
    def add_contact(self, Name, Contact_no):    #* Add contacts method
        self.contact_book[Name]=Contact_no      #* Update dictionary with name:Contact_no
        print(f"Contact for {Name} added succesfully.")

    def remove_contact(self, name):     #* Remove contacts method
        self.contact_book.pop(name)     #* Pop the contact
        print(f"Contact for {name} removed successfully.")


    def get_contact_by_name(self, name):    #* Find contact method
        if name not in self.contact_book.keys():    #* If name is not found
            print("No such contact found.(Make sure the letters case is same as the contact name)")
        elif name in self.contact_book.keys():      #* If name is found
            print("Contact no for",name,"is",self.contact_book.get(name)) 


if __name__ == '__main__':

    
    Contact_book = Contact_Book(None, None)     #* Initiate the contact book
    
    while True:     #* Forever
        print()
        print("Welcome to Contact-Book.")
        print("Choose an option to continue")
        print("1. Display Contacts")
        print("2. Add Contact")
        print("3. Remove Contact")
        print("4. Find a Contact")
        print("5. Exit")
        print()
        
        choice = int(input(">>> "))     #* Ask choice
        print()
        
        if choice == 1:         #* Call display contact method
            Contact_book.display_contact()            
           
            
        elif choice==2:         #* Call add cotact method
            
            Name = input("Enter the Name: ")
            Contact_no = int(input("Enter the contact number: "))
            
            if Name not in Contact_book.contact_book.keys():
                Contact_book.add_contact(Name, Contact_no)  
            
            elif Name in Contact_book.contact_book.keys():
                print(f"Contact for {Name} already exists.")


        elif choice==3:         #* Call the remove contact method
            
            choice3_name = input("Enter the contact name to remove: ")
            
            if choice3_name in Contact_book.contact_book.keys():    #* remove contact if exists
                Contact_book.remove_contact(choice3_name)
            
            else:
                print("Contact Name not found.")
        


        elif choice==4:     #* Find the contact by name
            
            choice4_name = input("Enter the name of the contact you want to find: ")
            Contact_book.get_contact_by_name(choice4_name)

        elif choice==5:
            print("Exiting....")
            exit()
        
        else:
            print("Invalid choice.")
            continue
