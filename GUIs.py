__author__ = 'Charlie'
'''
This will build a basic GUI with two frames one
on thet top to accept user input and one below
to dynamically display some generated information.
'''

from tkinter import * # Dont forget this!


class GUI:
    '''
    This will build a basic GUI with two frames one
    on the top to accept user input and one below
    to dynamically display some generated information.
    '''

    def __init__(self, root):
        self.root = root
        self.root.title('TK') # Add in the title for your window here
        self.topFrame = Frame(self.root)
        self.topFrame.pack()
            # This is the top frame,
            # put in the buttons and stuff for user input here
        labelExample = Label(self.topFrame, text = "This is a label:",
                             font=("Arial", 20))
        labelExample.pack()
        runIt = Button(self.topFrame,
                       text = "This Button makes it go!",
                       command = self.clicked)
        runIt.pack()

    def clicked(self):
        '''This will create the bottom frame and then
        you can populate it with data'''
        newData = self.createData()
            # stores the data returned in the createData method as newData

        self.bottomFrame = Frame(self.root)
        self.bottomFrame.pack()


        # Put code to populate your bottomFrame with newData here.

        '''Example Population of bottomFrame:'''
        i = StringVar() # this is the variable to use in the radioButton

        for item in newData:

            exampleRb = Radiobutton(self.bottomFrame, text = item,
                                    variable = i, value = item)
            exampleRb.pack()



    def createData(self):
        '''This is a method to create the data you want to
        put into your GUI'''

        # Put code that creates data here.
        # Don't forget to return it at the end.


        exampleSet = ['a','list','of','data','you','collected','somehow']
        return exampleSet



win = Tk()
    # initializes a Tk session
app = GUI(win)
    # Creates a GUI class with the Tk session
win.mainloop()
    # Keeps the window open