### Open Project Root

cd ~/twin-cessna-safety-data
ls

# you should see:

venv/
data/
analysis/
scripts/

### Reactivate Virtual Environment

Reactivate Virtual Environment

# you should see: 

(venv) user@penguin:~/twin-cessna-safety-data$

### Verify Correct Interpreter

which python

# you should see: 

.../twin-cessna-safety-data/venv/bin/python

# then confirm packages

python -m pip list

### If Dependencies Are Missing

python -m pip install -r requirements.txt

# Only required if:

venv was deleted and recreated

New machine

Packages truly missing

Reactivation alone does not require reinstalling.

### Full Clean Rebuild (Rare)

Only required if virtuam environment is corrupted

deactivate
rm -rf venv
python3 -m venv venv
source venv/bin/activate
python -m pip install -r requirements.txt