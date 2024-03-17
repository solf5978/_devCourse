import fs from "fs";

const todosPath = "todos.json";

type Todo = {
  id: number;
  task: string;
};

function getTodos(): Todo[] {
  if (!fs.existsSync(todosPath)) {
    return [];
  }
  const data = fs.readFileSync(todosPath, "utf8");
  return JSON.parse(data.toString()) as Todo[];
}
function listTodos(): void {
  const todos = getTodos();
  console.log(todos.forEach((todo) => `${todo.id}. ${todo.task}`));
}
function saveTodos(todos: Todo[]): void {
  fs.writeFileSync(todosPath, JSON.stringify(todos));
}
function removeTodo(id: number): void {
  const todos = getTodos();
  const index = todos.findIndex((todo) => todo.id === id);
  if (index === -1) {
    console.log("Todo not found");
    return;
  } else {
    const removedTodo = todos.splice(index, 1)[0];
    console.log(`Todo ${removedTodo.id} : ${removedTodo.task} removed`);
    saveTodos(todos);
  }
}
function addTodo(task: string): void {
  const todos = getTodos();
  const id = todos.length > 0 ? todos[todos.length - 1].id + 1 : 1;
  todos.push({ id, task });
  saveTodos(todos);
  console.log(`Added todo ${task} with id ${id}`);
}
function cli(): void {
  const subCommand = process.argv[2];
  const options = process.argv.slice(3);

  switch (subCommand) {
    case "list":
      if (options.length === 0) {
        listTodos();
      } else {
        console.log("Invalid options");
      }
      break;
    case "add":
      if (options.length === 1) {
        addTodo(options[0]);
      } else {
        console.log("Invalid number of arguments");
      }
      break;
    case "remove":
      if (options.length === 1) {
        const id = parseInt(options[0], 10);
        if (isNaN(id)) {
          console.log("Invalid id");
        } else {
          removeTodo(id);
        }
      } else {
        console.log("Invalid number of arguments");
      }
      break;

    default:
      console.log("Invalid command");
  }
}
