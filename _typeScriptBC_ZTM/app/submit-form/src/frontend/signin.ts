import { FieldError } from "./field-error";
const passwordField = document.getElementById("password") as HTMLInputElement;
const passwordInvalidLabel = document.getElementById(
  "invalid-password"
) as HTMLElement;
const emailField = document.getElementById("email") as HTMLInputElement;
const emailInvalidLabel = document.getElementById(
  "invalid-email"
) as HTMLElement;
const submitBtn = document.getElementById("form-submit") as HTMLButtonElement;
const errors = new FieldError();

function updateSubmitButton(): void {
  if (errors.isEmpty()) {
    submitBtn.classList.remove("btn-disabled");
  } else {
    submitBtn.classList.add("btn-disabled");
  }
}

emailField.addEventListener("input", (_) => {
  updateSubmitButton();
});
passwordField.addEventListener("input", (_) => {
  updateSubmitButton();
});
