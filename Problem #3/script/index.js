const form = document.querySelector("#register-form");
form.addEventListener("submit", (event) => {
  event.preventDefault();
  const formData = new FormData(form);
  const data = {};
  for (const [key, value] of formData.entries()) {
    /* USER CODE Begin: Validate data */
    if (value === "") {
      alert("Input cannot be empty");
      return false;
    }
    if (key === "email") {
      let atPosition = value.indexOf("@");
      let dotPosition = value.lastIndexOf(".");
      if (
        atPosition < 1 ||
        dotPosition < atPosition + 2 ||
        dotPosition + 2 >= value.length
      ) {
        alert("Please enter a valid email address");
        return false;
      }
    }

    if (key === "confirmpassword") {
      if (data["password"] !== value) {
        alert("Confirm password does not match!");
        return false;
      }
    }
    data[key] = value;

    /* USER CODE Begin: Validate data */
  }
  console.log(data);
  /* USER CODE Begin: What happened next after recieve form data (Optional) */

  /* USER CODE END: What happened next after recieve form data (Optional) */
});
