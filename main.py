from zipfile import ZipFile

with ZipFile('Archive.zip', 'r') as zip_object:
    
    zip_object.extractall()

print(zip_object.namelist())