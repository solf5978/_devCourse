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
function cli(): void {}
