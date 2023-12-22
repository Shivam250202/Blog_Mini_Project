function validateForm() {
    var title = document.getElementById("title").value;
    var content = document.getElementById("content").value;

    if (title.trim() === "" || content.trim() === "") {
        alert("Title and Content cannot be empty!");
        return false; // Prevent form submission
    }

    return true; // Allow form submission
}
