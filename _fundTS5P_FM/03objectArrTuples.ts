const myCar = {
  make: "Toyota",
  model: "Corolla",
  year: 2002,
};

let vehicle: {
  make: string;
  model: string;
  year: number;
} = myCar;

function printCar(vehicle: { make: string; model: string; year: number }) {
  console.log(`${vehicle.make} ${vehicle.model} ${vehicle.year}`);
}
