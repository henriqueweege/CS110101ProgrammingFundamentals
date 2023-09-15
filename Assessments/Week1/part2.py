class AssessmentPart2:
    def __init__(self, age, city, country, continent, startDateExam, endDateExam, temperature):
        self._age = age
        self._city = city
        self._country = country
        self._continent = continent
        self._startDateExam = startDateExam
        self._endDateExam = endDateExam
        self._temperature = temperature
        self._multiplier = 2
    
    def GetMultipliedAge(self):
        return f"Age multiplyed by {self._multiplier} is {self._age *2}"
    
    def GetLocalization(self):
        return f"City is {self._city}. Country is {self._country}. Continent is {self._continent}."
    
    def GetExaminationSchedule(self):
        return f"The final exam period: {self._startDateExam} - {self._endDateExam}"
    
    def GetTemperature(self):
        return f"The temperature is {self._temperature}°C"



part2Class = AssessmentPart2(26, "Jaraguá do Sul", "Brazil", "South America", "02/11", "05/11", "21")
print(part2Class.GetMultipliedAge())
print(part2Class.GetLocalization())
print(part2Class.GetExaminationSchedule())
print(part2Class.GetTemperature())

#