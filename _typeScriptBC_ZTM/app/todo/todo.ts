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

function cliInvalidOption(command: string): void {
  console.error(`Invalid option: ${command}`);
}
function cli(): void {
  const subCommand = process.argv[2];
  const options = process.argv.slice(3);

  switch (subCommand) {
    case "--help":
      console.log("Commands:");
      console.log("add <task>");
      console.log("list");
      console.log("remove <id>");
      break;
    case "list":
      if (options.length === 0) {
        listTodos();
      } else {
        cliInvalidOption(subCommand);
      }
      break;
    case "add":
      if (options.length === 1) {
        addTodo(options[0]);
      } else {
        cliInvalidOption(subCommand);
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
        cliInvalidOption(subCommand);
      }
      break;

    default:
      cliInvalidOption(subCommand);
  }
}
