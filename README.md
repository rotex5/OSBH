# Open-Source Book Hub(OSHB)
![image](https://user-images.githubusercontent.com/26916048/230252396-f3cc345e-d983-4bc7-9be6-6a2366810456.png)


## Installation

To get this project up and running locally on your computer:
1. Set up the [Python development environment](https://docs.python.org/3.4/library/venv.html#creating-virtual-environments).
   We recommend using a Python virtual environment.
1. Assuming you have Python setup, run the following commands (if you're on Windows you may use `py` or `py -3` instead of `python3` to start Python):
   ```
   pip3 install -r requirements.txt
   cd src
   python3 manage.py makemigrations blog forum file_library
   python3 manage.py migrate
   python3 manage.py collectstatic
   python3 manage.py test # Run the standard tests. These should all pass.
   python3 manage.py createsuperuser # Create a superuser
   python3 manage.py runserver
   ```
1. Open a browser to `http://127.0.0.1:8000/admin/` to open the admin site
1. Create a few test objects of each type.
1. Open tab to `http://127.0.0.1:8000` to see the main site, with your new objects.
