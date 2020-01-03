from modules.child import Recruiter, Programer
from modules.more import Vacancy, Candidate

#empl = Employee('Vasya', 'blabla', 1234, 300, '11-00')
#print(empl.work())
#emp2 = Recruiter('Petya', 'vksk', 1234, 50, '11-00')
#print(emp2.work())
#print(emp2)
#emp3 = Programer('Dima', 'vksk', 1234, 100, '11-00')
#print(emp3.work())
#print(emp3)
#print(empl == emp2)
#print(empl >= emp2)
def main():

    recr = Recruiter('Masha', 'blabla',1234, 50, '9-00')
    progr1 = Programer('Dima', 'vksk', 1234, 100, '11-00')
    progr2 = Programer('Anton', 'vksk', 1234, 100, '11-00')
    cand1 = Candidate('Petya', 'blblb', 'sdd', 'Python', 3)
    cand2 = Candidate('Petya', 'blblb', 'sff', 'Recruting', 5)
    cand3 = Candidate('Petya', 'blblb', 'sss', 'Python', 5)
    vac1 = Vacancy('Python_dev', 'Python', 5)
    vac2 = Vacancy('Recruter', 'Recruting', 5)

    

