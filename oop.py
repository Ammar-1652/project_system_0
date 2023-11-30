from abc import ABC, abstractmethod
from datetime import datetime
class Person():
    def __init__(self):
        pass
        
    def assign_values(self):
        self.first_name=self.get_first_name()
        self.middle_name=self.get_middle_name()
        self.last_name=self.get_last_name()
        self.personal_id=self.get_personal_id()
        self.contact_num=self.get_contact_num()
        self.email=self.get_email()
        self.profile_approved=self.get_profile_approved()
        self.date_of_birth=self.get_date_of_birth()
        self.age=self.get_age()
        self.id=self.get_id()
    
    def generate_id(self):
        pass
    
    def view_profile():
        pass
    
    #==========setters & getters=========
    
    #===========f-name===========
    def set_first_name(self,f_name):
        self.first_name=f_name
    
    def get_first_name(self):
        return self.first_name
    #=============================
    
    #=========m-name=============
    def set_middle_name(self,m_name):
        self.middle_name=m_name
    
    def get_middle_name(self):
        return self.middle_name
    #===========================
    
    #========l-name=============
    def set_last_name(self,l_name):
        self.last_name=l_name
    
    def get_last_name(self):
        return self.last_name
    #===========================
    
    #=========personal_id=========
    def set_personal_id(self,personal_id):
        self.personal_id=personal_id
    
    def get_personal_id(self):
        return self.personal_id
    #===========================
    
    #========contact_num=========
    def set_contact_num(self,contact_num):
        self.contact_num=contact_num
    
    def get_contact_num(self):
        return self.contact_num
    #==============================
    
    #==========e-mail=============
    def set_email(self,email):
        self.email=email
    
    def get_email(self):
        return self.email
    #===============================
    
    #=========profile_approved========
    def get_profile_approved(self):
        return self.profile_approved
    #==================================
    
    #===========date_of_birth==========
    def set_date_of_birth(self,date_of_birth:str):
        self.date_of_birth=date_of_birth
    
    def get_date_of_birth(self):
        return self.date_of_birth
    #======================================
    
    #===========ID====================
    def get_id(self):
        return self.id
    #============age=====================
    def calc_age(self):
        today = datetime.now()
        birthdate= datetime.strptime(str(self.get_date_of_birth()), '%d/%m/%Y')
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        return age
    
    def get_age(self):
        age=self.calc_age()
        return age

#================================End of Person class==============================================


class Student(Person):
    Student_count=0
    def __init__(self):
        Student.Student_count+=1
        
    
#==================setters & getters=======================
    def assign_values(self):
        return super().assign_values()
#======================level===================================
    def set_level(self,level):
        self.level=level
        
    def get_level(self):
        return self.level
        
#========================department======================
    def set_department(self,department):
        if self.get_level()==1 or self.get_level()==2:
            self.department="general"
        else:
            self.department=department

    def get_department(self):
        return self.department
#=======================end of Student class=====================

class Instructor(Person):
    def __init__(self):
        pass
        
#==================setters & getters=======================
    def assign_values(self):
        return super().assign_values()
#================department==============================
    def set_department(self,department):
        self.department=department

    def get_department(self):
        return self.department
    
#=======================salary======================
    def set_salary(self,salary):
        self.salary=salary
    
    def get_salary(self):
        return self.salary
#===================end of class Instructor============
class Admin(Person):
    
    def __init__(self):
        Admin.profile_approved=True
        
#=============setters & getters=================
    def assign_values(self):
        return super().assign_values()
        
        
class Professor(Instructor):
    professor_count=0
    def __init__(self):
        Professor.professor_count+=1
        
#===============setters and getters========================
    def assign_values(self):
        return super().assign_values()
#================courses teaching=======================
    def set_courses_teaching(self,courses_teaching):
        self.courses_teaching=courses_teaching
    
    def get_courses_teaching(self):
        return self.courses_teaching
        
class Professor_asst(Instructor):
    professor_asst_count=0
    def __init__(self):
        Professor_asst.professor_asst_count+=1
        
    #===============setters and getters========================
    def assign_values(self):
        return super().assign_values()
#================labs teaching=======================
    def set_courses_teaching(self,labs_teaching):
        self.labs_teaching=labs_teaching
    
    def get_courses_teaching(self):
        return self.labs_teaching
        
        
        
        
        
        
        

class Courses():
    courses_num=0
    labs_num=0
    def __init__(self,course_name,course_hours,is_with_lab=False):
        #assign values
        self.course_name=course_name
        self.course_hours=course_hours
        self.is_with_lab=is_with_lab
        Courses.courses_num+=1
        Courses.labs_num+=self.is_with_lab
