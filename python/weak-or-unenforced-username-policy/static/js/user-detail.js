const userInfo = document.getElementById("user-info");
const username = document.getElementById("username").dataset.username;
(async () => {
  const response = await fetch(`/users/${username}`, {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
    },
  });

  if (response.status === 200) {
    const data = await response.json();
    if (data) {
      const { name, lastname, address, phone, email } = data;
      userInfo.innerHTML = `
        <h2>Hey, ${name} ${lastname}</h2>
        <h3>Here is your information:</h3>
        <p class="address">Address: ${address}</p>
        <p class="phone">Phone: ${phone}</p>
        <p class="email">Email: ${email}</p>
      `;
    }
  } else {
    const data = await response.json();
    userInfo.innerText = data.error;
  }
})();
