// const registrationForm = document.getElementById('registrationForm');
// const passwordInput = document.getElementById('password');
// const confirmPasswordInput = document.getElementById('confirm-password');
// const passwordError = document.getElementById('passwordError');

// registrationForm.addEventListener('submit', function(event) {
//   if (passwordInput.value == confirmPasswordInput.value) {
//     event.preventDefault();
//     passwordError.style.display = 'block';
//   } else {
//     passwordError.style.display = 'none';
//   }
// });





document.getElementById("registrationForm").addEventListener("submit", function(event) {
  event.preventDefault();


 const email = document.getElementById("email").value.trim();
 const password = document.getElementById("password").value;
 const confirmPassword = document.getElementById("confirmPassword").value;
 const nickname = document.getElementById("nickname").value.trim();


  if (!email || !password || !confirmPassword || !nickname) {
    alert("Please fill in all fields");
    return;
  }

  if (password !== confirmPassword) {
    alert("Passwords do not match");
    return;
  }


  alert("Registration successful! Redirecting to homepage...");

  window.location.href = "about.html";
});
