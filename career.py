class career: #class
    def __init__(self,name,requiredSkills): #intialzie
        self.name=name #career name
        self.requiredSkills=requiredSkills #list of required skills
    def showCareer(self): #function to show career and its skills
        print("Career Name= ",self.name) #name of career
        print("Required Skills:  ") #required skills

        for skill in self.requiredSkills: #loop to print each skill in the list
            print("-", skill) #print them
        