# Open-Source Book Hub(OS|HB)
![image](https://user-images.githubusercontent.com/26916048/230252396-f3cc345e-d983-4bc7-9be6-6a2366810456.png)

## Introduction
[OS|BH](https://osbh-gfjw3.ondigitalocean.app/) Provides free access to diverse genres of resources including hobby-related ones and aims to reduce the challenging barriers to sharing and accessing knowledge or niche readings by empowering learning, literary leisure and exploration through community-driven open access.

### Blog Posts

For a more in-depth description of OSBH as well as an overview of its tech stack and development process, do visit the links below:

- [The Adventure of Building OSBH: Triumphs, Trials, and Thrills](https://medium.com/@David-Inkheart/the-adventure-of-building-osbh-triumphs-trials-and-thrills-dc8fceb173f)
- [Building a Community](https://github.com/rotex5/Personal-blog/blob/master/OSHBblog/README.md)


### Authors
**Philip**: [Twitter](https://twitter.com/_Ukanwoke) | [LinkedIn](https://www.linkedin.com/in/philip-ukanwoke-81a611209) | [GitHub](https://github.com/Kaditcuy)

**David**: [Twitter](https://twitter.com/ROTEXXXX) | [LinkedIn](https://www.linkedin.com/in/davidson-ogaraku-a9547aa7) | [GitHub](https://github.com/rotex5)

**Davidson**: [Twitter](https://twitter.com/David_Inkheart) | [LinkedIn](https://www.linkedin.com/in/david-okolie) | [GitHub](https://github.com/David-Inkheart)

## Installation
### Getting started Locally
To get this project up and running locally on your computer:
1. Set up the [Python development environment](https://docs.python.org/3.4/library/venv.html#creating-virtual-environments).
   We recommend using a Python virtual environment.
1. Assuming you have Python setup, run the following commands (if you're on Windows you may use `py` or `py -3` instead of `python3` to start Python):
   ```
   pip3 install -r requirements.txt   # To install all project dependecies
   cd src
   python3 manage.py makemigrations blog forum file_library
   python3 manage.py migrate
   python3 manage.py collectstatic
   python3 manage.py test # Run the standard tests. These should all pass.
   python3 manage.py createsuperuser  # Create a superuser
   python3 manage.py runserver
   ```
1. Open a browser to `http://127.0.0.1:8000/admin/` to open the admin site
1. Create a few test objects of each type.
1. Open tab to `http://127.0.0.1:8000` to see the main site, with your new objects.

### How to deploy this code
* This project was deployed using Digital Ocean free tier plan. You can click [here](https://docs.digitalocean.com/tutorials/app-deploy-django-app/) for a detailed documention on how to deploy this code.

## Usage
Direactions on how to use this site with detailed screenshot

## License
This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.
