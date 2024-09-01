Movie Organizer

A simple Python-based GUI application to help you organize movies you plan to watch. The application allows you to add, edit, remove, and reorder movies in a list, along with tracking the last date you plan to watch each movie. The list is saved automatically in a CSV file, so your data persists across sessions.

Features
Add Movies: Add a movie title and the last date to watch it.
Edit Movies: Edit the movie title and last date via a pop-up window.
Remove Movies: Remove selected movies from the list.
Reorder Movies: Move movies up or down in the list.
Persistent Storage: The movie list is saved in a CSV file (movies_list.csv), ensuring that all changes are preserved between sessions.

Installation
1- Clone the repository:
git clone https://github.com/your-username/movie-organizer.git
cd movie-organizer

2- Install the required dependencies:
The application uses Python's built-in tkinter library, which is included by default with Python. No additional dependencies are required.

3-Run the application:
python watch_list_organizer.py

Usage
1-Adding a Movie:
Enter the movie title and last date to watch in the respective entry fields.
Click the "Add" button to add the movie to the list.

2-Editing a Movie:
Select a movie from the list.
Click the "Edit" button to open a pop-up window.
Modify the movie title and/or last date and click "OK" to save changes or "Cancel" to discard them.

3-Removing a Movie:
Select a movie from the list.
Click the "Remove" button to delete the selected movie.

4-Reordering Movies:
Select a movie from the list.
Use the "Up" and "Down" buttons to move the movie within the list.

Files
watch_list_organizer.py: The main Python script containing the application code.
movies_list.csv: The CSV file where the movie list is saved.

Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request with improvements or bug fixes.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
This project was developed as a personal tool to keep track of movies to watch, inspired by the need for simple yet effective organization.
