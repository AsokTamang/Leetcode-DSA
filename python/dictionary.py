movie = {
    "title": "Life of Brian",
    "year": 1979,
    "cast": ["John", "Eric", "Michael", "George", "Terry"],
}


movie["title"] = "Spiderman unlimited"
print(movie["title"])
print(movie)
movie.update({"title": "batman the dark king"})

print(movie)


for key, value in movie.items():
    print(f"{key} has a value {value}")


python = {'John':35,'Eric':36,'Michael':35,'Terry':38,'Graham':37,'TerryG':34}
holy_grail = {'Arthur':40,'Galahad':35,'Lancelot':'39','Knight of NI':40, 'Zoot':17}
life_of_brian = {'Brian':33,'Reg':35,'Stan/Loretta':32,'Biccus Diccus':45}    
total={}
for values in (python,holy_grail,life_of_brian):
    total.update(values)
print(total)    


for key,value in total.items():
    if type(value)==str:
           total[key]=int(value)
print(sum(total.values()))  #here first of all im using int to convert the string into integer then using sum to find the total sum of valeus in this dict.
