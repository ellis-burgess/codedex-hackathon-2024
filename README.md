# codedex-hackathon-2024
Team SunSpark's Codedex Summer Hackathon 2024 Submission

## How to set up to run on your local server
1. Using command line interface, set up a virtual environment (how to do this will depend on your operating system).
2. Activate your virtual environment, then install all requirements listed in 'requirements.txt'.
3. Run the command `set flask_app=wsgi`
 - Note: if you're on a Unix machine, you will need to run `export flask_app=wsgi` instead
4. run `flask run` and control (or command) + click on the link posted to the terminal.

If you want to run in debug mode (for better error handling), run `set flask_debug=TRUE` (or `export flask_debug=True` if you're on a Unix machine)