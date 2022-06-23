# Write a program that keeps the information about companies and their employees. 
# You will be receiving company names and an employees' id until you receive the command "End" command.
# Add each employee to the given company. Keep in mind that a company cannot have two employees with the same id.
# Print the company name and each employee's id in the following format:
# "{company_name}
# -- {id1}
# -- {id2}
# …
# -- {idN}"

company_data = dict()


cmd = input()
while not cmd == "End":
    cmd = cmd.split(" -> ")
    company = cmd[0]
    id_num = cmd[1]
    if company not in company_data:
        company_data[company] = []
    if id_num not in company_data[company]:
        company_data[company].append(id_num)
    cmd = input()

for comp in company_data:
    print(f"{comp}")
    for el in company_data[comp]:
        print(f"-- {el}")
