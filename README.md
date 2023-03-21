# Sustainable Daily

## About the project

Sustainable Daily is designed to integrate sustainable activities into everyday life.

We aim to gamify the process of building sustainable habits through daily goals which give you points and levels. These can be used to unlock fun characters and accessories to enhance your profile.

The project is publicly hosted at <https://www.sustainable-daily.live/>

## Table of Contents

- [Pages](#pages)
- [Running the project](#running-the-project)
- [Testing the project](#testing-the-project)
- [Contributing to the project](#contributing-to-the-project)
- [Useful Information](#useful-information)
- [Main Contributions](#main-contributions)
- [End Notes](#end-notes)

## Pages

### Home Page

On the home page the user is shown all of their daily tasks. These include randomised global tasks that everyone can complete to earn points and xp, as well as personal tasks that don't earn the user anything.

Some examples of global tasks are minigames, quizzes, surveys, and finding certain things such as water fountains and recycle bins.

<br>

### Profile Page

The profile page displays the user's name, level and points. There are different tabs for customising parts of a profile such as, username color, background color, character and accessories.

<br>

### Leaderboard Page

The leaderboard page displays multiple leaderboards of users. A global leaderboard will show all users, along with their current level and points. User's may join private leaderboards via code sharing, to have the options of seeing only users that they choose. The list of users can be sorted by name, level and points by clicking the respective buttons.

<br>

### Login Page

The login page allows registered users to log in to their accounts.

<br>

### Registration Page

The registration page allows users to create a new account.

<br>

### Gamekeeper Pages

The game-keeper pages allow game-keepers to manage the system, this includes:

- managing admin/game-keeper accounts
- adding/removing location goals
- adding/removing surveys and survey questions
- adding/removing quiz questions

It is only accessible through a game-keeper account, for setup instructions with this page please refer [here](#default-game-keeper-account).

<br>

### Deployment

This project is currently deployed on a singular Google Cloud compute instance. It is containerised using Docker and runs on Google's container-optimised operating system.

Deployment is achieved automatically through GitHub actions.

For more details please refer to [Hosting](#hosting), [Docker](#docker), and [GitHub Actions](#github-actions)

---

<br>

## Running the project

To run the project:

- Open a terminal
- Navigate to the project directory: `cd ecm2434-gsep`
- Migrate the database: `python manage.py migrate`
- Run the server: `python manage.py runserver`
- Open a browser
- Navigate to `127.0.0.1:8000`

<br>

---

<br>

## Testing the project

To test the project:

- Open a terminal
- Navigate to the project directory: `cd ecm2434-gsep`
- Migrate the database: `python manage.py migrate`
- Run the tests: `python manage.py test`

We also have automated test suites setup using GitHub actions. The configuration files for this can be found in `.github/workflows`. This includes testing and linting.

We test the project using Django's built-in tests.

<br>

---

<br>

## Contributing to the project

This section outlines the guidelines we follow when contributing code to the repository.

We have the project setup so that you are unable to commit directly to master, and instead must go through a pull request.

All features should be implemented in a feature branch, such as `profile-tests` or `settings-page`. The branch should then be merged into the `master` branch using a pull-request.

In order for a pull request to be merged it must have been reviewed by another group member, and all GitHub action workflows must be passing - linting and tests.

The project is linted using flake8, which tests against the PEP8 python format.

To lint the project locally, ensure `flake8` is installed and simply run `flake8` from the command line whilst in the root directory.

<br>

---

<br>

## Useful Information

This section contains information that is not categorised but can be considered useful during project setup and development.

### Default game-keeper account

There is a migration script setup to automatically create a game-keeper account for the client. The default username for this account is `root` and the password is `admin`.

Please **delete this account as soon as possible**, the email, username and password configurations are **not secure**.

### Default item migrations

As items are stored in a database there are migration scripts setup to create default items needed in a new project.

This migration script is located in `sustainable_app/migrations/0003_create_items.py` should you want to add more items.

If you modify this file, please remigrate your database (see [custom commands](#custom-commands) section)

### Custom Commands

There are a variety of custom commands setup in this project to help with development.

The most useful one is `remigrate`.

```bash
python manage.py remigrate
```

This command rolls back all migrations, and reruns them. This is incredibly useful when modifying the item migration.

> Please note this **deletes and recreates** the default game-keeper account and all items.

We also have the `dailytasks` command.

```bash
python manage.py dailytasks
```

This command is what is used internally to run daily tasks, which are scheduled to run automatically at midnight (00:00) each day.

There is also the `dummydata` command.

```bash
python manage.py dummydata
```

This command is used for quickly setting up a test environment. Its purpose is to populate the database with mock data for the development environment to mimic the production environment as closely as possible.

Having the script available to automatically populate the database removes any hassle from the database being wiped, and when a wipe does happen it allows for a swift recovery.

The recommended user to use after population is `JohnS2` with the password `john`

### Docker

This project has a Dockerfile setup, allowing the application to be containerised and run extremely easily.

These next steps assume you have the docker CLI installed and have the docker daemon/service running, and that you are currently in the root directory of the project. (The directory containing the Dockerfile)

#### Building the container

```bash
docker build --platform linux/amd64 .
```

> Please note the --platform argument is not required; the amd64 platform provides support for the majority of cloud vm configurations, and will usually be used the most.

This container can then be either run locally using `docker run -p 8000:8000 container_name`, or deployed to your favourite cloud provider via their steps.

To see how we have set up the project please refer to [Hosting](#hosting).

### Hosting

> This section outlines all aspects of hosting the project except automated processes, if you would like to see how we manage CI/CD please refer to [GitHub actions](#github-actions).

The project is hosted using Google Cloud. At the time of submission, we host the project using a single e2-micro compute instance running Google's Container-Optimized OS. The project is run in a container within this instance. Due to its containerised nature it can easily be scaled up should demand for the project increase.

#### Compute Instance

The compute instance we use is an e2-micro instance running the Container-Optimized OS.

The instance is set up to automatically fetch our container from the [artifact registry](#container-hosting) upon start, and deployment to the instance simply involves restarting the instance.

The instance has the HTTP and HTTPS ports open, 80 and 443, on the firewall to allow for incoming web traffic, all other ports (with a few exceptions such as SSH) are closed. The instance has been set up with a public static IP address (see [network hosting](#network) for more info).

The e2-micro instance runs with 0.25 VCPUs and 1 GB memory, which for any large project would not be anywhere near enough, however due to the small size of the project it suits our needs nicely. As mentioned before, due to the project being containerised we can easily upscale if needed.

#### Container Hosting

We need to host the Docker container on an accessible registry for the VM to be able to pull it. We use Google's artifact registry for this, sticking with Google products allows for easy integration, meaning we do not need to set up authentication on the compute instance, we just had to give it the relevant permissions within the cloud project.

The container is hosted privately, preventing public access to our backend server application.

#### Network

The network configuration for the project is currently incredibly simple due to only having one cloud compute instance;

The instance has a static public IP address with the ports 80 and 443 exposed. We then have our DNS records setup with an A record pointing to the compute instance's IP address.

The domain (sustainable-daily) is registered through [Namecheap](http://www.namecheap.com).

### GitHub Actions

We have two GitHub actions setup:

- Test
- Deploy

#### Test

The purpose of this action is to lint the project code and run the test suites available.

This action is required to complete successfully before a pull request can be merged. It is run every time a commit is made to the project.

#### Deploy

The purpose of this action is to automatically build, push and deploy the project.

It is set up to run when a commit is tagged, such as a release tag being added.

The first step is authentication; we do this using google's auth action along with a JSON credentials object stored within GitHub secrets. The credentials object should avoid being placed in the repository at all costs as it would give direct access to the compute engine and artifact registry.

Afterwards the GCloud CLI is set up using Google's `setup-gcloud` action, and docker is set up to use gcloud authentication for specific domains.

From here the container is built using the correct tags and pushed to the artifact registry.

The compute instance is then restarted using the `gcloud compute instances update-container` command.

### Cron scheduling and daily tasks

The project requires certain tasks to run every day, such as randomising the goals for the day and tallying up minigame scores.

There were many ways to do this, such as scheduling through python or creating a Redis queue with a scheduling library, however we opted to go simple and use Linux's `cron`.

The `cron` is set up through the docker container, we simply setup a crontab task to run a script within the `scripts` directory called `dailytasks.sh`.
This script calls the `dailytasks` command through manage.py: `python manage.py dailytasks`.

This command can be run manually to trigger a "daily reset".

The daily reset command is set up to run a set of tasks

- calculate points for minigame scores
- randomise daily goals
- reset user streaks

The cron task is currently set to run at 11:55pm, there are a couple of reasons for this;

- the task needs to be run before the day rolls over
- avoid peak compute time to ensure smooth execution

<br>

---

<br>

## Main Contributions

These do not state precisely what was done by whom, as everyone had more contributions than listed here. This is simply an indication of which person is responsible for certain parts of the project.

### Main Pages

The home page was primarily developed by Luke, Oscar, Josh C and Dora. Luke created the initial file, before Oscar, Josh C and Dora padded it out with functionality such as daily and personal goals.

The leaderboard was created by Oscar, who created the design and implemented functionality. Luke later made some design changes to the page such as adding the user's profile picture.

The profile page is a key part of the gamification of this project, and can be attributed to Dora and Josh C.
Dora designed the page and added the majority of the functionality, with assistance in the later part from Josh C.

The login page was created by Josh C and Harry, with the design primarily being Josh and the functionality being Harry.

The registration page was designed by Josh H, with most of the functionality being implemented by Harry. It was later refactored by Oscar.

The navigation bar seen throughout the project was orchestrated by Luke, who carried out the design, implementation and the refactor later on.

The game-keeper pages, consisting of the main, survey, quiz and location pages, were all mostly made by Josh C. Some parts of the location functionality, such as generating QR codes, was assisted by Harry.

### Minigames and Goals

The goals were generally developed by one person per goal, rather than having many people working on them.

The catching minigame was created by Josh C, whilst the sorting minigame was created by Josh H. The minigames had some overlap, such as the start and end screens.

The quiz goal was entirely implemented by Josh H. This includes the design, functionality and database models.

Similarly, surveys were solely implemented by Oscar. This includes client and server logic, as well as design.

It is worth noting for both the quiz and survey goals, Josh C implemented the game-keeper logic for creating new surveys/quizzes.

The location goal was primarily implemented by Josh C, with assistance from Harry. This includes the game-keeper and user parts of the system.

### Miscellaneous

The streaks system, which tracks how many days in a row a user has completed goals, was developed by Oscar.

The statistics system, which keeps an estimation of the real world impact of the system, was developed by Josh H.

Daily randomisation and tracking completion of daily goals was implemented by Oscar and Harry.

Anything to do with DevOps can be attributed to Harry. This includes setting up Docker, Cloud Hosting, GitHub actions and a domain.

## End Notes

Ultimately it is incredibly difficult to solely attribute a part of the project to a single person. Everyone made incredibly significant contributions to all portions of the project, the majority of which are not listed here. To see all contributions and code changes please view the [GitHub repository](https://github.com/itselectroz/ecm2434-gsep).

We can confirm that Matt Collinson has been added as a member of the GitHub repository, and that Matt, Liam, and Nick have all been invited to the Trello board we use.
