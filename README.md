# AgileJeera6 🚀

## About the application 📱
- This application is driven by a graphical user interface (GUI), providing users with an intuitive way to interact with its features and functionalities.

- Aumeter is a free, user-friendly meditation application aimed at improving mental health.

- It offers concise, scientifically-backed audio and visual meditation sessions.

- Key features include login functionality, meditation sessions, study music,  sleep sounds, favorites management and progress tracking."

- Aumeter integrates seamlessly with Firebase's real-time database for user authentication and storing session progress, ensuring that users can access their data across multiple devices and receive updates instantly.

## Python Installation 🛠️
Check that you have the latest version of Python 3 installed

## MAKE AND MAKEFILE

We recommend working with the MakeFile so make sure you have 'make' installed in your machine
If not installed see video on how to install:

https://www.youtube.com/watch?v=5TavcolACQY&list=PLEtyhUSKTK3hOCnMrPKGOu3_VjUAkhsgG&index=3

by Mikael Roos

The Makefile contains a target to execute or run several commands.

## Cloning App

With the terminal navigate to the location you want the game and execute this command:

    git clone https://github.com/bhavikbhagwani/AgileJeera6.git



Go into the src directory:

    cd src 

## SETTING VENV

Once having 'make' installed, first of all you need to set the virtual environment and activate it. 
(Make sure you are in the AgileJeera6/ directory)
You can set a virtual environment using 

            make venv

Then, you should activate the virtual environment using

            . .venv/Scripts/activate

You should see a (.venv) in your terminal
This will allow all features to be found and run
You can later deactivate the virtual environment by using

            deactivate

For Windows start the venv with:

    . .venv/Scripts/activate

For Unix and Macs start it with:

    .venv/bin/activate

Install the needed dependencies using: 

    make install

## before running
It is important to download two other dependancies that are required in order
for this application to function: pygame and pyrebase. These can be done in the terminal:
    pip install pygame

    pip install pyrebase4


## To run the application ▶️
The MakeFile provides a command for running the application, by typing:

The application can be initialized in two ways:
One way is by executing the 'app.py' file in the src directory:

    python app.py

Another way is by using the MakeFile. The MakeFile provides a
command for running the application, by typing:

    make start

## Cleanup 🧹

To clean up generated and installed files, use the following commands:

    make clean

To clean up documentation files:

    make clean-doc

To clean up source files:

    make clean-src

To clean up everything:

    make clean-all

## Testing ✅

For running unit tests you can type:

    make test

You can run linters using

        make lint

or separetaly using

        make flake8         make pylint

## Documentation 📄
Documentation is a helpful feature to help understand the code for other developers
First of all install the 'dot' command  to help generate the UML diagrams from the source code
For windows, you can do it through chocolatey in Powershell as administrator:

        choco install graphviz

For mac OS, through the 'brew' package manager.

        brew install graphviz

Debian (and other Linux), through your package manager.

        apt install graphviz

After the installation is done you can check what version you got.

        $ dot -V

To generate HTML documentation for all classes just type

        make pdoc

This will generate HTML documentation inside doc/pdoc

To generate UML diagrams you can just type

        make pyreverse

This will generate UML diagrams inside doc/pyreverse

Now, you should have a doc/ directory inside pig with pyreverse/ and pdoc/

You can also just run the two targets directly (pyreverse and pdoc) using

                make doc

The pdoc folder will have HTML documentation for all classes found and
the pyreverse folder will have UML diagrams for all classes found
