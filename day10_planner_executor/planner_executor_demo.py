# Day 10 — Planner/Executor Pattern (Toy Demo)
# Safe offline script

from dataclasses import dataclass, field

# ----- Simple plan templates -----
PLAN_TEMPLATES = {
    "Plan a weekend trip": [
        "Decide destination",
        "Set budget",
        "Book transport",
        "Reserve hotel",
        "Make a sightseeing list",
        "Pack essentials"
    ],
    "Bake a cake": [
        "Pick a recipe",
        "Gather ingredients",
        "Preheat oven",
        "Mix batter",
        "Bake and cool",
        "Decorate"
    ]
}

@dataclass
class Plan:
    task: str
    steps: list[str]

class Planner:
    def make_plan(self, task: str) -> Plan:
        steps = PLAN_TEMPLATES.get(task, [
            "Define scope",
            "List steps",
            "Execute steps",
            "Review results"
        ])
        return Plan(task=task, steps=steps)

@dataclass
class ExecutorResult:
    step: str
    status: str
    note: str = ""

class Executor:
    def run_step(self, step: str) -> ExecutorResult:
        # Simulate doing the step with a simple success message
        return ExecutorResult(step=step, status="done", note=f"Completed: {step}")

class Supervisor:
    def run(self, task: str):
        planner = Planner()
        executor = Executor()
        transcript = []

        transcript.append(f"Planner: Received task '{task}'")
        plan = planner.make_plan(task)
        transcript.append(f"Planner: Steps -> {', '.join(plan.steps)}")

        for i, step in enumerate(plan.steps, 1):
            res = executor.run_step(step)
            transcript.append(f"Executor: Step {i}/{len(plan.steps)} '{res.step}' -> {res.status}. {res.note}")

        transcript.append("Supervisor: Task completed! ✅")
        return transcript

if __name__ == "__main__":
    TASK = "Plan a weekend trip"
    s = Supervisor()
    log = s.run(TASK)
    print("=== Planner/Executor Demo ===")
    for line in log:
        print(line)
