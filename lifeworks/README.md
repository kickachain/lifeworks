# created a virtual environment with python3

To create a virtual environment from the root folder (Lifeworks) run [ python3 -m venv lifeworks-venv ]

To activate the virtual environment from the root folder (Lifeworks) run the 
following command [ source lifeworks-venv/bin/activate ]

To deactivate just run [ deactivate ] from the terminal in any directory

after initialising the virtual envronment

# install dependancy packages for environment

in the backend-assessment directory is a requirements.txt file with all the packages required
to install them run from the root folder (Lifeworks) run [ pip3 install -r /backend-assessment/requirements.txt ]

# config variables that can be changed (optional)

in backend-assessment/main.py main function there is some config variables these are:
    * relative path for output file (has to be an existing path)
    * age limit (no negative numbers, working with int types)

# run the script/module

run from the root folder (Lifeworks)
[ python3 /backend-assessment/main.py ]


