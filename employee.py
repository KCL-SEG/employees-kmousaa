"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, salary, hours = 0, com_type = None, commission = 0, contract = 0):
        self.name = name
        self.salary = salary
        self.hours = hours
        self.commission = commission
        self.contract = contract
        self.com_type = com_type

    @property
    def add_commission(self):
      if self.com_type == None:
        return self.commission

      elif  self.com_type == "contract":
        return self.commission * self.contract

      elif  self.com_type == "fixed":
        return self.commission

    def get_pay(self):
      if self.hours == 0:
        return self.salary + self.add_commission
      else:
        return (self.salary * self.hours) + self.add_commission


    def __str__(self):
        return f"{self.name} works on a monthly salary of {self.salary} and receives a commission for {self.contract} contract(s) at {self.commission}/contract.  Their total pay is {self.get_pay()}."


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', salary = 4000, com_type = None)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', salary = 25, hours = 100)
# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', salary = 3000, commission = 200, contract = 4, com_type = "contract")
# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', salary = 25, hours = 150, commission = 220, contract = 3, com_type = "contract")
# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', salary = 2000, commission = 1500, com_type = "fixed")
# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', salary = 30, hours = 120, commission = 600, com_type = "fixed")
