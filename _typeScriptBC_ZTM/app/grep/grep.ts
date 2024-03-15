import { readFileSync } from "fs";

const args = process.argv.slice(2);
const filename = args[0];
const searchString = args[1];

const contents = readFileSync(filename, "utf8");
const lines = contents.split("\n");

for (let i = 0; i < lines.length; i++) {
  const line = lines[i];
  if (line.includes(searchString)) {
    console.log(line);
  }
}

for (const line of lines) {
  if (line.includes(searchString)) {
    console.log(line);
  }
}
lines.forEach((line) => {
  if (line.includes(searchString)) {
    console.log(line);
  }
});

console.log(lines.filter((line) => line.includes(searchString)).join("\n"));
