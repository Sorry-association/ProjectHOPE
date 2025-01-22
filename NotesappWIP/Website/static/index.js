function deleteNote(noteId) {
    fetch('/delete-note', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ noteId: noteId }),
    }).then((response) => {
        if (response.ok) {
            // Redirect to the notebook page after successful deletion of the note to see the updated list of notes
            window.location.href = '/notebook';
        } else {
            console.error('Failed to delete note:', response.statusText);
            // Displaying an error message to the user if the note could not be deleted
        }
    }).catch((error) => {
        console.error('Error:', error);
    });
}