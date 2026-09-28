class student: #class 
    def __init__(self,name,skillInput): #intialize
        self.name=name #your name
        self.skills=[] #empty list of skills
        self.skillInput=skillInput # for getting real time input
    def addSkill (self):
        is_running = True # for while condition
        while is_running:
                self.skillInput = input("Enter a skill (Press q to exit) = ") # enter a skill
                if self.skillInput == "q": # if user enters q
                    is_running = False # exit the loop

                elif self.skillInput not in self.skills: # else if entered skill is not in the list 
                     self.skills.append(self.skillInput) # append it

                else:
                     print("Skill already exists")
                
                if self.skillInput.isdigit(): # if input is a digit or a special character
                     print("Invalid Input") 

    def getinfo (self): #function to display name and list 
        print("Name= ",self.name) 
        print("List Of Your Skills :", self.skills)


