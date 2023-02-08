### ACTIVATE VIRTUAL ENV
source venv/bin/activate

### EXPORT PYTHONPATH
export PYTHONPATH=$(python3 src/main/python/company-template/utils/get_pythonpath.py)
echo $PYTHONPATH

### RUN PYTEST
python3 src/main/python/company-template/tests/run_tests.py

### REMOVE __pycache__
find . | grep -E "(/__pycache__$|\.pyc$|\.pyo$)" | xargs rm -rf

### DEACTIVATE
deactivate