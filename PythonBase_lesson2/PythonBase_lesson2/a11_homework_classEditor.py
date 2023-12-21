

class Editor:
    def __init__(self):
        self.password = None

    def view_document(self):        
        print("View documents")


    def edit_document(self): 
       
        if self.password == '12355':
            print("Access is open!!!")
        else:        
            print("Enter password for edit documents.")



class Proeditor(Editor):
    def edit_document(self):
        self.password = str(input("Enter password: "))
        super().edit_document()        




if __name__ == '__main__':
    #object = Editor()
    #object.view_document()
    #object.edit_document()

    object2 = Proeditor()
    object2.edit_document()