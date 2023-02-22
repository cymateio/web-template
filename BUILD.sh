### ACTIVATE VIRTUAL ENV
source venv/bin/activate

### EXPORT PYTHONPATH
export PYTHONPATH=$(python3 src/main/python/company-template/utils/get_pythonpath.py)
echo $PYTHONPATH

### RUN PYTEST
current_date_time="$(date +%Y-%m-%d_%H-%M-%S)"
python3 src/main/python/company-template/tests/run_tests.py 2>&1 | tee test-output/console/console_"$current_date_time".log

### REMOVE __pycache__
find . | grep -E "(/__pycache__$|\.pyc$|\.pyo$)" | xargs rm -rf

### DEACTIVATE VIRTUAL ENV
deactivate