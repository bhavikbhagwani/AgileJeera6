# AgileJeera6

## About the application
- This application is driven by a graphical user interface (GUI), providing users with an intuitive way to interact with its features and functionalities.

- Aumeter is a free, user-friendly meditation application aimed at improving mental health.

- It offers concise, scientifically-backed audio and visual meditation sessions.

- Key features include login functionality, meditation sessions, study music,  sleep sounds, favorites management, progress tracking, and customer feedback."

- Aumeter integrates seamlessly with Firebase's real-time database for user authentication and storing session progress, ensuring that users can access their data across multiple devices and receive updates instantly.

## Installation
Make sure you have make installed.
With the terminal navigate to the location you want the game and execute this command:


git clone https://github.com/bhavikbhagwani/AgileJeera6.git


Go into the src directory:

cd src 

create the venv:

make venv

For Windows start the venv with:

. .venv/Scripts/activate

For Unix and Macs start it with:

.venv/bin/activate


Install the dependencies:

make install

## To run the application
The application can either be runed by executing the 'Whole_app_in_classes.py' file in the src directory or by executing this command:

make start

## Cleanup

To clean up generated and installed files, use the following commands:

make clean

To clean up documentation files:

make clean-doc

To clean up source files:

make clean-src

To clean up everything:

make clean-all

## Testing

To test all the code at once, you can use:

make pylint or make flake8


For linting:

make lint

For running tests:

make test

## Documentation
To regenerate the documentation from the code, including the UML diagrams, go to the root directory of the project and execute this command:

make doc
