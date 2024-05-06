function uploadFiles() {
    const input = document.getElementById('fileInput');
    const files = input.files;
    const formData = new FormData();

    // Filter files by extension
    for (let i = 0; i < files.length; i++) {
        const file = files[i];
        const fileNameParts = file.name.split('.');
        const fileExtension = fileNameParts[fileNameParts.length - 1].toLowerCase();
        
        if (fileExtension === 'py' || fileExtension === 'php') {
            formData.append('files', file);
        }
    }

    // Send files to Django view
    fetch('/uploads/', {
        method: 'POST',
        body: formData
    })
    .then(response => {
        if (response.ok) {
            return response.json();
        }
        throw new Error('Network response was not ok.');
    })
    .then(data => {
        // Handle response from Django view
        console.log(data);
    })
    .catch(error => {
        console.error('There was a problem with the fetch operation:', error);
    });
}