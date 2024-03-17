const GEOCODE_API_URL = "https://maps.googleapis.com/maps/api/geocode/json";
async function main(): Promise<number> {
  if (process.argv.length < 3) {
    console.error("Usage: weather LOCATION");
    return 1;
  }
  const location = process.argv[2];
  return await Promise.resolve(0);
}

main().catch((err) => console.error(err));
