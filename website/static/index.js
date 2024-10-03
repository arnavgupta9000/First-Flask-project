function deleteNote(noteId) {
    fetch('/delete-note', {
    method: 'POST',
    body: JSON.stringify({noteId: noteId}) // basically this will delete the note
    }).then((_res) => {
        window.location.href= "/";  // reload window
    });
}
