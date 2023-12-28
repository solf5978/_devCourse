// Equal Sign

const myCar = {
  make: "Toyota",
  model: "Corolla",
  year: 2002,
};

// Colon Sign For Declaration
let vehicle: {
  make: string;
  model: string;
  year: number;
} = myCar;

function printCar(vehicle: { 
  make: string; 
  model: string; 
  year: number;
  chargeVoltage?: number  // ? -> Optional Props
}) {
  let str = `${vehicle.make} ${vehicle.model} ${vehicle.year}`
  str += `// $vehicle.chargeVoltage}`
  console.log(str)
}

