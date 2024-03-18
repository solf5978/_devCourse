import type { LocationInfo } from "./location";
import { fetchLocationData } from "./location";
const GEOCODE_API_URL = "https://maps.googleapis.com/maps/api/geocode/json";
const WEATHER_API_URL = "https://api.openweathermap.org/data/2.5?";
async function main(): Promise<number> {
  if (process.argv.length < 3) {
    console.error("Usage: weather LOCATION");
    return 1;
  }
  const location = process.argv[2];
  let locInfo: LocationInfo;
  try {
    locInfo = await fetchLocationData(GEOCODE_API_URL, location);
  } catch (err) {
    console.error(err);
    return 1;
  }
  console.log(locInfo);
  return await Promise.resolve(0);
}

main().catch((err) => console.error(err));
