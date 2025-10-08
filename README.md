[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Live Demo](https://img.shields.io/website?label=Live%20Demo&url=http://hackyeah.site)](http://hackyeah.site)

# 🎮 HackYeah 2025

The MVP project for the 2025 edition of HackYeah stationary hackathon.

**Live Demo: [Open](http://hackyeah.site)**

![App Demo Slider](static/app-demo.gif)

## ℹ️ Organizers info

Main Hackathon site: [hackyeah.pl](https://hackyeah.pl/)

Archive Hachathon site (2025 edition): [2025.hackyeah.pl](https://2025.hackyeah.pl)

Event organizer: [proidea.pl](https://proidea.pl/)

## 👥 Team - GiveMeASecond

This table outlines the core members of the team, their primary role or focus area, and their respective GitHub handles.

| Name | Role / Focus | GitHub Handle |
| :--- | :--- | :--- |
| **Arkadiusz Pabian** | Team Leader | [@ArkadiuszPabian](https://github.com/ArkadiuszPabian) |
| **Paulina Rutkowska** | UX / Graphic Designer | [@PaulinaRutkowska3](https://github.com/PaulinaRutkowska3) |
| **Pola Palonek** | Creative person | [@Polaxxd](https://github.com/Polaxxd) |
| **Szymon Główka** | Backend Developer | [@szymonglowka](https://github.com/szymonglowka) |
| **Julen Zulaika** | Frontend Developer | [@JulenZZZ](https://github.com/JulenZZZ) |
| **Mateusz Łagocki** | Tester | [@Mateuszl28](https://github.com/Mateuszl28) |

## 📝 Hackathon task description

> Selected task: **LifeRun** by [ZUS](https://www.zus.pl/)
>
> Time to finish the challenge: **24 hours**.

Life is a constant sequence of decisions that shape the future – from education and career choices, through lifestyle and relationships, to financial security in old age. In the rush of everyday life, we rarely reflect on the long-term impact of our actions. How do overwork, lack of savings, or neglecting health affect quality of life later on? And on the other hand – how can investing in education, nurturing passions, or maintaining balance between work and family contribute to greater stability and fulfillment in the future? The simulation game Life Run poses a fundamental question: what does a well-planned life really mean? It is not only about finances, but also about health, relationships, and a sense of satisfaction. As part of this challenge, participants will explore these complexities and look for ways to present the consequences of everyday choices in an engaging and accessible way.

## 💡 MVP description

> Product name: **Virtual Tomorrow** (**Wirtualne Jutro**).

Virtual Tomorrow is an educational life simulator that teaches strategic financial and career planning. The application visualizes the long-term consequences of decisions, letting players guide a character from youth through to retirement. In a safe, virtual environment, users learn how their choices impact their future well-being and financial security.

## 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- [Docker](https://www.docker.com/get-started) and [Docker Compose](https://docs.docker.com/compose/install/)
- [Git](https://git-scm.com/)

### Installation & Running

1.  **Clone the repository:**
    ```sh
    git clone [https://github.com/arkadiuszpabian/hackyeah2025.git](https://github.com/arkadiuszpabian/hackyeah2025.git)
    cd hackyeah2025/hackyeahAPI
    ```

2.  **Create your environment file:**
    Duplicate the `.env.example` file and rename it to `.env`. Then, fill in the required environment variables.
    ```sh
    cp .env.example .env
    ```

3.  **Build and run the Docker containers:**
    The project uses Docker to manage the development environment. Use `docker-compose` to build and run the services.
    ```sh
    docker-compose up --build
    ```

4.  **Access the application:**
    Once the containers are running, you can access the application in your browser at:
    [http://localhost:8000](http://localhost:8000)

### Environment Variables

The application requires the following environment variables to be set in the `.env` file:

| Variable             | Description                                                                    | Example Value                                  |
| :------------------- | :----------------------------------------------------------------------------- | :--------------------------------------------- |
| `DJANGO_SECRET_KEY`  | A secret key for a particular Django installation.                             | `"your-super-secret-key"`                      |
| `DEBUG`              | Toggles Django's debug mode. Set to `1` for development.                       | `1`                                            |
| `DJANGO_ALLOWED_HOSTS` | A list of strings representing the host/domain names that this Django site can serve. | `"localhost,127.0.0.1"`                        |
| `DATABASE_URL`       | The connection string for the PostgreSQL database.                             | `"postgres://user:pass@host:port/db"`          |

## 🛠️ Tech Stack

- **Frontend**: HTML / CSS / JS
- **Backend**: Python / Django
- **Deployments**: Docker

## 🧰 Tools used

- **IDE**: Visual Studio Code
- **Design Tools**: Figma / Canva
- **Version Control**: Git

## 🔌 API Documentation

The application exposes a RESTful API to provide the game's structure and rules.

| Method | Endpoint           | Description                                                                              |
| :----- | :----------------- | :--------------------------------------------------------------------------------------- |
| `GET`  | `/api/game-rules/` | Retrieves all life stages, including their associated questions, answers, conditions, and impacts. |

## 👨‍💻 Developer guidelines

Commit message format: [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)

Branching: [Feature Branch Workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/feature-branch-workflow)

### 📋 Conventional Commits and Branch Prefixes

| Type           | Branch Prefix | Purpose                                                                        | Example Branch             |
| :------------- | :------------ | :----------------------------------------------------------------------------- | :------------------------- |
| **`feat`**     | `feat/`       | **New feature** for the application (e.g., user login, data visualization).    | `feat/user-onboarding`     |
| **`fix`**      | `fix/`        | **Bug fix** for existing incorrect behavior.                                   | `fix/api-auth-header`      |
| **`chore`**    | `chore/`      | Maintenance, build config, tooling (ESLint, Prettier, dependencies setup).     | `chore/setup-husky`        |
| **`test`**     | `test/`       | Adding new tests or correcting existing tests.                                 | `test/user-service-logic`  |
| **`docs`**     | `docs/`       | Changes to documentation (README, guides).                                     | `docs/update-readme-team`  |
| **`refactor`** | `refactor/`   | Code change that doesn't fix a bug or add a feature (e.g., reorganizing code). | `refactor/move-auth-files` |
