import axios from "axios";

export interface LocationInfo {
  displayName: string;
  lat: number;
  lon: number;
}

export async function fetchLocationData(
  apiUrl: string,
  locationName: string
): Promise<LocationInfo> {
  const options = {
    method: "GET",
    url: apiUrl,
    params: {
      q: locationName,
    },
  };
  const response = await axios.request<LocationInfo[]>(options);

  if (response.status === 200) {
    if (response.data.length > 0) {
      return response.data[0];
    } else {
      throw new Error("Location not found");
    }
  } else {
    throw new Error("Unable to fetch location data");
  }
}
