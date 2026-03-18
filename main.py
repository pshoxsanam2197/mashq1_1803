# 1. Dictionary (lug‘at) tushunchasi
1-s
students = {"Ali": 85,
            "Vali": 90,
            "Hasan": 78,
            "Husan": 92
}
print(students)
max_ball = max(students.values())
print(max_ball)

for v, k in enumerate(students):
    if max_ball == students[k]:
        print(k)
        break

# 2-s
sales = {"apples": 50,
         "oranges": 75,
         "bananas": 30,
         "pears": 45
}
print(sales)
s = sum(sales.values())
print(s)

# 3-s
grades = {"Math": 80,
          "Physics": 75,
          "Chemistry": 85,
          "Biology": 90
}
print(grades)
for fan, ball in grades.items():
    if ball > 75:
        print(fan)

# 4-s
inventory = {"pen": 10,
             "pencil": 20,
             "notebook": 15,
             "eraser": 5
}
min_miqdor = min(inventory.values())
print(min_miqdor)

for v, k in enumerate(inventory):
    if min_miqdor == inventory[k]:
        print(k)
        break

# 5-s
products = {"A": 100, "B": 200, "C": 150, "D": 250}
print(products)
f = products.values()
print(f)
ortacha = sum(f) / len(f)
print(ortacha)

# 2. Dictionary yaratish usullari
# 1-s
d = dict()
d['x'] = 10
d['y'] = 20
d['z'] = 30

print(d)

# 2-s
d = {"a": 5, "b": 10}
d['c'] = 15
d['d'] = 20
print(d)

# 3-s
d = dict(name="Ali", age=20)
print(d)
d["age"] = 25
print(d)

# 4-s
d = {}

# 5-s
d1 = {"x":1, "y":2}
d2 = {"y":3, "z":4}
d3 = {**d1, **d2}
print(d3)

# 3. Dictionary metodlari
# 1-s
grades = {"Math": 80,
          "Physics": 90,
          "Chemistry": 85
}
print(grades)
d = grades.keys()
print(d)

# 2-s
grades = {"Math": 80,
          "Physics": 90,
          "Chemistry": 85
}
print(grades)
g = grades.values()
print(g)

# 3-s
grades = {"Math": 80, "Physics": 90, "Chemistry": 85}

for fan, ball in grades.items():
    if ball > 85:
        print(f"{fan}: {ball} - Excellent")
    else:
        print(f"{fan}: {ball}")

# 4-s
inventory = {"pen": 10,
             "pencil": 20,
             "notebook": 15
}
qiymat = inventory.get("eraser", 0)
print(qiymat)

# 5-s
scores = {"Ali": 85,
          "Vali": 90,
          "Hasan": 78
}
for name, score in scores.items():
    print(f"{name} scored {score} points")

# 4. Dictionary + List aralash amaliyot
# 1-s
students = {"Ali": [85, 90],
            "Vali": [78, 88],
            "Hasan": [92, 95]
}
print(students)
f = students.values()
print(f)
ortacha = sum(f) / len(f)
print(ortacha)

# 2-s
inventory = {"pens": [10, 15],
             "pencils": [5, 10],
             "notebooks": [20, 25]
}

for product, amounts in inventory.items():
    total = sum(amounts)
    print(f"{product}: {total}")

# 3-s
grades = {"Math": [80, 85, 90],
          "Physics": [70, 75, 80]
}

for subject, scores in grades.items():
    print(f"{subject}: {max(scores)}")

# 4-s
students = {"Ali": [85, 90, 95], "Vali": [70, 75, 80]}

for name, scores in students.items():
    total = sum(scores)
    if total > 250:
        print(f"{name}: Passed")
    else:
        print(f"{name}: Failed")

# 5-s
scores = {"Ali": [10, 20], "Vali": [5, 15], "Hasan": [20, 25]}

for name, marks in scores.items():
    average = sum(marks) / len(marks)
    if average > 15:
        print(f"{name}: A")
    else:
        print(f"{name}: B")
