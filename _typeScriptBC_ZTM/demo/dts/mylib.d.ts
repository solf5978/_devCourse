export function add(a: number, b: number, ...numbers: number[]): number;
export function max(arr: number[]): number | null;
export type CaseKinds = "upper" | "lower" | "sentence" | "camel" | "pascal";
export function setCase(message: string, kind: CaseKinds): string;
export function quote(str: string): () => string;
