# ProjectHOPE
Hackathon'25 Team HEMA ED#011, EPS#03

Project HOPE is an online platform designed to help students in crisis areas connect and access educational resources easily. Since many people in such areas might rely on older devices, the project focuses on being accessible through just a web browser and an internet connection.
The website is built using Python and Flask for its core functionality.HTML, CSS, and Bootstrap are used in making the interface and data, including user accounts, notes, chat histories, and coursework, is managed through SQL libraries.The werkzeug.security ensures the safety of personal information using secure encryption.

#Setup: 
Install the lastest version of python. Clone the project repository using git clone <repo-url>, then install flask, flask-login, flask-sql-alchemy.

#Running the website:  
To launch the platform, run python main.py, and open your browser to http://127.0.0.1:5000.
To access the chatrooms, coursework page, and notebook, you must log in
The navagation bar on the top of every page will only show you the routes you currently have access to.
You may test the notebook feature by: 
                                  Creating a blank note, for which it should prompt an error.
                                  Creating a note and then pressing the "x" in the end of it, which should cause the page to reload with the note deleted
                                  Creating a note, logging out, and then logging back in to check if the notes are being stored correctly.

#Credits: 
This project was guided by several resources, Mainly the YouTube video "Learn Flask for Web Development" by TechwithTim and the GitHub repository also from Tech With Tim's Flask Web App Tutorial. Reference to the repository is located within the proposal document.

#License: 
None.
