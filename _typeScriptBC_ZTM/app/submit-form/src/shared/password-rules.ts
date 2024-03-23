export function checkComplexity(plainPassword: string): string[] {
  const errors: string[] = [];
  if (plainPassword.length < 8) errors.push("password-too-short");
  return errors;
}
