class Doctor():
    
    def __init__(self):
        print("This is class doctor")
        
    def BMI(weight, height):
        bmi = weight/(height*height)
        print("Your BMI is "+str(bmi))
        
    def heart_rate(heart_rates):
        if(heart_rates>60 and heart_rates<100):
            print("Great your heart rate is normal")
        else:
            print("You do not have a normal heart rate, please visit the clinic")

class patient(Doctor):
    
    def __init__(self, name, weight, height, heart_rates):
        self.patient_name = name
        self.patient_weight = weight
        self.patient_height = height
        self.patient_heart_rates = heart_rates
        
    def healthCheck(self):
        print("\n Patient Name: ", self.patient_name)
        Doctor.BMI(self.patient_weight, self.patient_height)
        Doctor.heart_rate(self.patient_heart_rates)
        


patient1 = patient("Michael", 30, 0.9144, 80)
patient1.healthCheck()

patient2 = patient("John", 40, 1, 90)
patient2.healthCheck()

patient3 = patient("Jake", 50, 0.85, 110)
patient3.healthCheck()

patient4 = patient("Bob", 45, 0.9374, 60.5)
patient4.healthCheck()

patient5 = patient("Dave", 73, 0.8643, 123)
patient5.healthCheck()

patient6 = patient("Lisa", 77, 0.9543, 83)
patient6.healthCheck()

patient7 = patient("Tina", 83, 1.3, 98)
patient7.healthCheck()

patient8 = patient("Conny", 43, 1.12, 101)
patient8.healthCheck()

patient9 = patient("Dom", 83, 1.456, 85)
patient9.healthCheck()

patient10 = patient("Chris", 63, 0.9643, 117)
patient10.healthCheck()