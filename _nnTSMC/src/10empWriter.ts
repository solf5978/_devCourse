import { CSVWriter } from "./08CSVWriter";

interface Employee {
    id: number
    name: string
    role: string
    salary: number
}

const employeeWriter = new CSVWriter<Employee>(['id', 'name', 'role', 'salary'])

employeeWriter.addRows([
    { id: 1, name: 'john', salary: 50000, role: 'manager'},
    { id: 2, name: 'john', salary: 50000, role: 'manager'},
    { id: 3, name: 'john', salary: 50000, role: 'manager'},
    { id: 4, name: 'john', salary: 50000, role: 'manager'},
])

employeeWriter.save('data/employees.csv')