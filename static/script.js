function togglePassword() {
    const passwordInput = document.getElementById("password");

    if (passwordInput.type === "password") {
        passwordInput.type = "text";
    } else {
        passwordInput.type = "password";
    }
}

function generatePassword() {
    const chars =
        "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*";
    let password = "";

    for (let i = 0; i < 16; i++) {
        password += chars.charAt(Math.floor(Math.random() * chars.length));
    }

    document.getElementById("generatedPassword").value = password;
}

function copyPassword() {
    const generatedPassword = document.getElementById("generatedPassword");

    if (generatedPassword.value === "") {
        alert("Generate a password first!");
        return;
    }

    navigator.clipboard.writeText(generatedPassword.value)
        .then(() => {
            alert("Password copied successfully!");
        })
        .catch(() => {
            alert("Unable to copy password.");
        });
}