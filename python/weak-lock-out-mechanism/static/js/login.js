const form = document.getElementById("login-form");
const error = document.getElementById("error");

form.addEventListener("submit", async (e) => {
  e.preventDefault();
  const username = document.getElementById("username").value;
  const password = document.getElementById("password").value;
  const captcha = document.getElementById("captcha").value;

  const response = await fetch("/login/", {
    method: "POST",
    body: JSON.stringify({ username, password, captcha }),
    headers: {
      "Content-Type": "application/json",
    },
  });

  if (response.status === 200) {
    window.location.href = "/";
  } else {
    const data = await response.json();
    error.innerText = data.error;
  }
});
