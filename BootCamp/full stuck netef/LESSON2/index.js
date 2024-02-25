const users = [];
function register(event) {
  event.preventDefault();
  const user = {};
  const formData = new FormData(event.target);
  formData.forEach((v, k) => (user[k] = v));
  users.push(user);
  event.target.reset();
}

function showAllUsers() {
  console.log(users);
}

function resetForm() {
  document.getElementById("myForm").reset();
}
