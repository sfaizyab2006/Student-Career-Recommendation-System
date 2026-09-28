from career import career
from careerMatch import careerMatch
from student import student

student1 = student("Faizyab", "NA")

career1 = career("AI Engineer", ["Python", "C++", "Java", "SQL"])
career2 = career("Data Scientist", ["Python", "SQL", "Machine Learning"])
career3 = career("Web Developer", ["HTML", "CSS", "JavaScript"])
career4 = career("Teacher", ["Communication", "Subject Knowledge", "Patience"])
career5 = career("Software Developer", ["Python", "Java", "C++"])
career6 = career("Data Analyst", ["Python", "SQL", "Data Visualization"])
career7 = career("Graphic Designer", ["Adobe Photoshop", "Creativity", "Attention to Detail"])
career8 = career("Marketing Manager", ["Communication", "Strategic Thinking", "Digital Marketing"])
career9 = career("Financial Analyst", ["Excel", "Financial Modeling", "Analytical Skills"])
career10 = career("Project Manager", ["Leadership", "Communication", "Organizational Skills"])
career11 = career("Content Writer", ["Writing Skills", "Research", "SEO"])
career12 = career("HR Manager", ["Communication", "Recruitment", "Employee Relations"])
career13 = career("Sales Manager", ["Communication", "Negotiation", "Sales Strategy"])
career14 = career("Mechanical Engineer", ["AutoCAD", "SolidWorks", "Problem Solving"])
career15 = career("Civil Engineer", ["AutoCAD", "Structural Analysis", "Project Management"])
career16 = career("Electrical Engineer", ["Circuit Design", "MATLAB", "Problem Solving"])
career17 = career("Data Engineer", ["Python", "SQL", "Big Data Technologies"])
career18 = career("UX Designer", ["User Research", "Wireframing", "Prototyping"])
career19 = career("Mobile App Developer", ["Java", "Kotlin", "Swift"])
career20 = career("Cybersecurity Analyst", ["Network Security", "Threat Analysis", "Incident Response"])

careers = [
    career1,
    career2,
    career3,
    career4,
    career5,
    career6,
    career7,
    career8,
    career9,
    career10,
    career11,
    career12,
    career13,
    career14,
    career15,
    career16,
    career17,
    career18,
    career19,
    career20,
]


def main():
    student1.addSkill()
    student1.getinfo()

    for options in careers:
        matchingCareers = careerMatch(options, student1)
        percent = matchingCareers.calculateMatch(options)
        if percent >= 50:
            options.showCareer()
            print("Match Percentage:", percent, "%")


if __name__ == "__main__":
    main()