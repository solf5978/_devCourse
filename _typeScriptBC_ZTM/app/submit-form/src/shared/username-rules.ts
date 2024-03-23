export function checkUsername(username: string): string[] {
  const errors: string[] = [];
  if (username.length < 3) {
    errors.push("Username must be at least 3 characters long");
  }
  if (username.length > 20) {
    errors.push("Username must be at most 20 characters long");
  }
  if (!username.match(/^[a-zA-Z0-9]+$/)) {
    errors.push("Username must only contain letters and numbers");
  }
  return errors;
}
