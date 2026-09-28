class careerMatch: #class
    def __init__ (self,career,student): #initialize
        self.student=student #student 
        self.career=career #career

    def calculateMatch(self,career): #function to calculate match percent
        student_skills=self.student.skills #skills of student (object composition)        
        required_skills= career.requiredSkills #skills required for career(object composition)
        
        matched_skills=0 #total matched skills
        
        for skill in student_skills: #loop and check each skill of student
            if skill in required_skills: #match student skill with required skill
                matched_skills+=1 #add 1 to the matched skill if the students's skill matches with the required skill
        percentage=(matched_skills/len(required_skills))*100 #formula
        return percentage #return the percent
    