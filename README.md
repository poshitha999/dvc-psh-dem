create env

'''bash
conda create -n wineq python=3.11 -y

activate env
'''bash
conda activate wineq
'''

create a req fil
'''bash
pip install -r tequirements.txt


download the data

git init

dvc init

dvc add data_given/winequality.csv

Add everything in the directory to the staging area
'''bash
git add . 
git commit -m "first commit"