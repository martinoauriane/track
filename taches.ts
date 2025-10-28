// GOAL : try to assign tasks with the shortest time length to machines

interface Machine {
  name: string;
  makespan: number;
}

interface Task {
  name: string;
  length: number;
  compatible_machines: string[];
}

interface Rec {
  machine: string;
  task: string;
  start: number;
  end: number;
}

// Tâches
const taches: Record<string, Task> = {
  T1: { name: "T1", length: 5, compatible_machines: ["M1"] },
  T2: { name: "T2", length: 3, compatible_machines: ["M1", "M2"] },
  T3: { name: "T3", length: 2, compatible_machines: ["M2"] },
  T4: { name: "T4", length: 4, compatible_machines: ["M1", "M2"] },
};

// Machines
const machines: Machine[] = [
  { name: "M1", makespan: 0 },
  { name: "M2", makespan: 0 },
];

// Record
let record: Rec[] = [];

function execute(
  taches: Record<string, Task>,
  machines: Machine[],
  record: Rec[]
) {
  // Transforme l'objet en tableau pour itérer
  const remainingTasks = Object.values(taches);

  // while remaining Tasks.length > 0 permet d'arrêter la logique quand toutes les tâches ont été assignées à des machines.
  while (remainingTasks.length > 0) {
    // on assigne à l'avance à chacune des machines des tâches, en fonction de la plus courte durée d'exécution pour chacune des tâches.

    for (const machine of machines) {
      // Cherche la tâche la plus courte compatible
      let shortestTaskIndex = -1;
      let shortestLength = Infinity;

      // on parcrout toutes les tâches pour extraire:
      // - la tache compatible avec la machine
      // - la tache avec la durée de temps la plus courte

      for (let i = 0; i < remainingTasks.length; i++) {
        const task = remainingTasks[i];
        if (
          task.compatible_machines.includes(machine.name) &&
          task.length < shortestLength
        ) {
          shortestLength = task.length; // au terme de toutes les itérations on aura donc isolé la tâche avec le temps d'exécution le plus court qui soit également
          // compatible avec la machine
          shortestTaskIndex = i;
        }
      }

      if (shortestTaskIndex !== -1) {
        const task = remainingTasks[shortestTaskIndex];
        const start = machine.makespan;
        const end = start + task.length;

        record.push({ machine: machine.name, task: task.name, start, end });

        machine.makespan = end;

        remainingTasks.splice(shortestTaskIndex, 1); // supprime la tâche exécutée
      }
    }
  }
}

execute(taches, machines, record);
console.log(record);
console.log("Makespan total:", Math.max(...machines.map((m) => m.makespan)));
