import bcrypt from "bcrypt";

const saltRounds = 10;

export class HashedPassword {
  constructor(readonly hashed: string) {}
}

export async function hasedPassword(plain: string): Promise<HashedPassword> {
  return await new Promise((resolve, reject) => {
    bcrypt.hash(plain, saltRounds, (err, hashed) => {
      if (err !== undefined) {
        reject(err);
      } else {
        resolve(new HashedPassword(hashed));
      }
    });
  });
}

export async function cmpPassword(
  plain: string,
  storedHash: HashedPassword
): Promise<boolean> {
  return await bcrypt.compare(plain, storedHash.hashed);
}
