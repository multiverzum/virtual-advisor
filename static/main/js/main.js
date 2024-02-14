function showAlert(text, messageType) {
    const alert = document.getElementById('dynamic-alert');
    const textElement = document.getElementById('alert-text');

    if (messageType === 'success') {
        alert.classList.add('alert-success', 'bg-success', 'text-white');
    } else if (messageType === 'danger' || messageType === 'error') {
        alert.classList.add('alert-danger', 'bg-danger', 'text-white');
    } else if (messageType === 'info') {
        alert.classList.add('alert-info', 'bg-info', 'text-white');
    } else if (messageType === 'primary') {
        alert.classList.add('alert-primary', 'bg-primary', 'text-white');
    }

    textElement.textContent = text;
    alert.style.display = 'block';
    
    $("#dynamic-alert").fadeTo(2000, 500).slideUp(500, function () {
        $("#dynamic-alert").slideUp(500);
    });
}