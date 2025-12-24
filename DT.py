def decision_tree(age, income):
    if age > 40:
        return "Yes"
    else:
        if income > 60000:
            return "Yes"
        else:
            return "No"

print(decision_tree(25, 50000))
print(decision_tree(45, 80000))
