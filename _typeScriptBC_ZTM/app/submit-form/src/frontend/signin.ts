import { checkUsername } from "../shared/username-rules";
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
  const usernameFailures = checkUsername(emailField.value);
  if (usernameFailures.length > 0) {
    const formattedErrors = usernameFailures.join("<br />");
    errors.set("invalid-email", emailField, emailInvalidLabel, formattedErrors);
  } else {
    errors.remove("invalid-email", emailField, emailInvalidLabel);
  }

  updateSubmitButton();
});
passwordField.addEventListener("input", (_) => {
  const usernameFailures = checkUsername(passwordField.value);
  if (usernameFailures.length > 0) {
    const formattedErrors = usernameFailures.join("<br />");
    errors.set(
      "invalid-password",
      passwordField,
      passwordInvalidLabel,
      formattedErrors
    );
  } else {
    errors.remove("invalid-password", passwordField, passwordInvalidLabel);
  }
  updateSubmitButton();
});
