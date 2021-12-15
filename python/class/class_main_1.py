import work

employee1 = work.employee('윤정호',145)
employee2 = work.employee('드와이트',123)
employee3 = work.employee('마이클',110)

employee1.wage()
employee2.wage()
employee3.wage()

print("-------임금 인상-------")
work.employee.hourlywage = 9000

employee1.set_hourlywage(10000)

employee1.wage()
employee2.wage()
employee3.wage()