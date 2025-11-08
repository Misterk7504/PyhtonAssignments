# payroll_system.py
class Employee:
    def __init__(self, name, emp_id, base_salary):
        self._name = name          # protected
        self._emp_id = emp_id
        self._base_salary = base_salary
    
    # Getter methods
    def get_name(self):
        return self._name
    
    def get_emp_id(self):
        return self._emp_id
    
    def get_base_salary(self):
        return self._base_salary
    
    # Required polymorphic method
    def calculate_pay(self):
        raise NotImplementedError("Subclass must implement calculate_pay()")
    
    # Clean string representation
    def __repr__(self):
        return f"{self.__class__.__name__}(name='{self._name}', emp_id='{self._emp_id}', base_salary={self._base_salary})"


class FullTimeEmployee(Employee):
    def calculate_pay(self):
        # Full-time: base salary + 20% bonus
        return self._base_salary * 1.20


class PartTimeEmployee(Employee):
    def __init__(self, name, emp_id, base_salary, hours_worked):
        super().__init__(name, emp_id, base_salary)
        self._hours_worked = hours_worked
    
    def calculate_pay(self):
        # Part-time: hourly rate = base_salary / 160, then multiply by hours worked
        hourly_rate = self._base_salary / 160
        return hourly_rate * self._hours_worked
    
    def __repr__(self):
        return (f"PartTimeEmployee(name='{self._name}', emp_id='{self._emp_id}', "
                f"base_salary={self._base_salary}, hours_worked={self._hours_worked})")


# Demo usage
if __name__ == "__main__":
    employees = [
        FullTimeEmployee("Ajay Sharma", "FT001", 80000),
        PartTimeEmployee("Priya Verma", "PT005", 40000, 90),
        FullTimeEmployee("Rohan Patel", "FT002", 95000),
        PartTimeEmployee("Neha Singh", "PT012", 35000, 120)
    ]
    
    print("=== Payroll System Output ===\n")
    for emp in employees:
        print(f"{emp.get_name()} ({emp.get_emp_id()})")
        print(f"   Type: {emp.__class__.__name__}")
        print(f"   Net Pay: ₹{emp.calculate_pay():,.2f}")
        print("-" * 40)


#### out put ##3
=== Payroll System Output ===

Ajay Sharma (FT001)
   Type: FullTimeEmployee
   Net Pay: ₹96,000.00
----------------------------------------
Priya Verma (PT005)
   Type: PartTimeEmployee
   Net Pay: ₹22,500.00
----------------------------------------
Rohan Patel (FT002)
   Type: FullTimeEmployee
   Net Pay: ₹114,000.00
----------------------------------------
Neha Singh (PT012)
   Type: PartTimeEmployee
   Net Pay: ₹26,250.00
----------------------------------------