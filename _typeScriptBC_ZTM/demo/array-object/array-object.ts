/* eslint-disable */
import { strict as assert } from "assert";
type Links = {
  title: string;
  url: string;
};

const microsofts = {
  title: "Microsoft",
  url: "https://www.microsoft.com",
};

const typescript = {
  title: "TypeScript",
  url: "https://www.typescriptlang.org",
};

const links = [microsofts, typescript];
const tsUrl = links[1].url;
const msUrl = links[0].url;
