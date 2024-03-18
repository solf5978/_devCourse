import type { LocationInfo } from "./location";
import { fetchLocationData } from "./location";
import { fetchWeatherData } from "./weatherapi";
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
  console.log(`Fetching weather data for ${locInfo.displayName}...\n`);
  try {
    const weatherData = await fetchWeatherData(
      WEATHER_API_URL,
      locInfo.lat,
      locInfo.lon
    );
    console.log(weatherData.format());
  } catch (err) {
    console.log(err);
    return 1;
  }
  console.log(locInfo);
  return await Promise.resolve(0);
}

main().catch((err) => console.error(err));
