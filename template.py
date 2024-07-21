import os

dirs = [
    os.path.join("data","raw"),
    os.path.join("data","processed"),
    "notebooks",
    "saved_models",
    "src"
]

# loop over the directory list to create directory, exist_ok = True to make sure you can run multiple times
# create a .gitkeep file as well inn all the folders
for dir_ in dirs:
    os.makedirs(dir_,exist_ok = True)
    with open(os.path.join(dir_,".gitkeep"),"w") as f:
        pass

# .gitignore says what shouldn't be pushed
# init.py to mae sure it reads the src as a python package
files = [
    "dvc.yaml",
    "params.yaml",
    ".gitignore",
    os.path.join("src","__init__.py"),    
]
# 
for file_ in files:
    with open(file_, "w") as f:
        pass