# CBA API TEST 


The test have been written in python and are run using pytest unit test framework.
The tests are defined in the tests folder. Some of the tests are parametrised and 
can be run on multiple inputs, controlled from the test data files in the test_data folder.

NOTE:
Set the delete-key in the test data file or as an environment variable.
$ set DELETE_KEY=xxxx


    RUNNING THE TESTS
    ======================
    - Install python 3.x
        https://www.python.org/downloads/
    
    - Navigate to the test repository 

    - Install requirements
        $ pip install -r requirements.txt   
    
    - Set PYTHONPATH to .
        windows:
        > set PYTHONPATH=.

        linux:
        $ export PYTHONPATH=.
        
    - Run tests using pytest command from the project folder (cba-api-tests)
      $ pytest --html=report.html --self-contained-html tests
                OR
      $ pytest --html=report.html --self-contained-html <path-to-tests-folder>

    - HTML report is generated as report.html in the folder the tests are run from 
      or in the path specified in --html option of the pytest command.




    