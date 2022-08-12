const container = document.querySelector(".container"),
	pwdShowHide = document.querySelectorAll(".showHidePwd"),
	pwdFields = document.querySelectorAll(".pwd"),
	signup = document.querySelector(".signup-switch"),
	login = document.querySelector(".login-switch");
	button = document.querySelector(".btn-primary")

pwdShowHide.forEach(icon => {
	icon.addEventListener("click", () => {
		pwdFields.forEach(pwdField => {
			if (pwdField.type === "password") {
				pwdField.type = "text";

				pwdShowHide.forEach(icon => {
					icon.classList.replace("uil-eye-slash", "uil-eye");
				})
			} else {
				pwdField.type = "password";

				pwdShowHide.forEach(icon => {
					icon.classList.replace("uil-eye", "uil-eye-slash");
				})
			}
		})
	})
})

signup.addEventListener("click", () => {
	container.classList.add("switch");
})

login.addEventListener("click", () => {
	container.classList.remove("switch");
})

function redirect() {
	location.href = "login.html";
}

