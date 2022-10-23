import json

class employee:
    def file_handling(self):
        file = open("C:\\Users\\mange\\Documents\\Data Science\\assignment_6\\employee.json")
        data = json.load(file)
        return f"{data} \n {type(data)}"

employee_obj = employee()
print(employee_obj.file_handling())