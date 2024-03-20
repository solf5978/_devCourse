export type Status = "success" | "failure";
const Department = ["Electronics", "Home & Kitchens", "Toys & Games"] as const;
export type Department = (typeof Department)[number];
export interface ApiResponseItem {
  id: number;
  name: string;
  price: number;
  qty: number;
  department: Department;
}
export interface ApiResponse {
  status: Status;
  data: {
    items: ApiResponseItem[];
  };
}

export function apiResponse(): ApiResponse | undefined;
