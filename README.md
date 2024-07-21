create env

```bash
conda create -n wineq python=3.11 -y
```
activate env
```bash
conda activate wineq
```

create a req fil
```bash
pip install -r requirements.txt
```

download the data

then follow below process
```bash
git init

dvc init

dvc add data_given/winequality.csv
```

Add everything in the directory to the staging area
```bash
git add . 

git commit -m "first commit"
```

one liner updates
```bash
git add . && git commit -m "first commit"
```
Pushing to the tremote
```bash
git remote add origin https://github.com/poshitha999/dvc-psh-dem.git
```
To change the branch name to main
```bash
git branch -M main
```
Push to the remote
```bash
git push origin main
```

## params.yaml
from [data_source][s3_source] we read the data, the we load it to [load_data][raw_dataset_csv]
