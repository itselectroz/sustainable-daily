# Sustainable Daily


## About the project
Sustainable Daily is designed to integrate sustinable activities into everyday life.

We aim to gamify the process of building sustainable habits through daily goals which give you points and levels. These can be used to unlock fun characters and accessories to enhance your profile.

<br>

### Home Page
On the home page the user is shown all of their daily tasks. These include randomised global tasks that everyone can complete to earn points and xp, aswell as personal tasks that don't earn the user anything.

Some examples of global tasks are minigames, quizes, surveys, and finding certain things such as water fountains and recycle bins.

<br>

### Profile Page
The proile page displays the user's name, level and points. There are different tabs for customising parts of a profile such as, username color, background color, character and accessories.

<br>

### Leaderboard Page
The leaderboard page displays mutliple leaderboards of users. A global leaderboard will show all users, along with their current level and points. User's may join private leaderboards via code sharing, to have the options of seeing only users that they choose. The list of users can be sorted by name, level and points by clicking the respective buttons.

<br>

### Login Page
The login page allows registered users to login to their accounts.

<br>

### Registration Page
The registration page allows users to create a new account.

<br>

---

<br>

## Running the project
To run the project:
- Open a terminal
- Navigate to the project directory: ```cd ecm2434-gsep```
- Run the server: ```python manage.py runserver```
- Open a browser
- Navigate to ```127.0.0.1:8000```

<br>

---

<br>

## Testing the project
To test the project:
- Open a terminal
- Navigate to the project directory: ```cd ecm2434-gsep```
- Run the tests: ```python manage.py test```

We also have automated test suites setup using Github actions. The configuration files for this can be found in `.github/workflows`. This includes testing and linting.

We test the project using django's built in tests.

<br>

---

<br>

## Contributing to the project

This section outlines the guidelines we follow when contributing code to the repository.

We have the project setup so that you are unable to commit directly to master, and instead must go through a pull request.

All features should be implemented in a feature branch, such as `profile-tests` or `settings-page`. The branch should then be merged into the `master` branch using a pull-request.

In order for a pull request to be merged it must have been reviewed by another group member, and all github action workflows must be passing - linting and tests.

We lint the project using flake8, which tests against the PEP8 python format.

To lint the project locally, ensure `flake8` is installed and simply run `flake8` from the command line whilst in the root directory.

<br>

---

<br>

## Main Contributions

These do not state precisely what was done by who, as everyone had more contributions than listed here. This is just a rough guideline of who wrote what code.

The login page and logic was done by Joshua Cox and Harry Whittle.
The registration page and logic was done by Joshua Hammond and Harry Whittle.
The home page was made by Luke Buncle.
The leaderboard page was made by Oscar Moores.
The profile page was made by Dora Napier.

The navbar was made by Luke Buncle.

The sorting minigame was created by Joshua Hammond.
The catching minigame was created by Joshua Cox.

Everyone made significant contributions to all portions of the project, majority of which are not listed here. To see all contributions and code changes please view the [github](https://github.com/itselectroz/ecm2434-gsep).

Matt Collinson has been added as a member of the repository.
