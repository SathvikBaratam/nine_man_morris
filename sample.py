import os
print(os.getcwd())
os.chdir(r'C:\Users\barat\OneDrive\Desktop')
os.mkdir('testing')
print(os.getcwd())
print(os.listdir())
#favorities(argument of the function) is a python list.If the file doesnot exist it
#creates a new file.f the file already exists → it erases old content and writes new content
#This is why favorites update every time.FAV_FILE is equal to "favorite_cities.json"
#with->closes the file ,f->(temp variable)represents the open file,w->means write mode.
#json.dump() converts Python objects → JSON format #json.dump() will write the JSON data directly into this file f.


"r" means read mode

"favorite_cities.json" is opened

f becomes the file object you read from
What does json.load(f) do?

Reads the JSON file

Converts JSON text → Python list
This is the default empty result.

Meaning:

User has no favorites saved yet

File not created yet

So return an empty list

This avoids a crash