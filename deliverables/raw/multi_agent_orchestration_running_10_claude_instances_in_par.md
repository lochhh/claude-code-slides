# Multi-Agent Orchestration: Running 10+ Claude Instances in Parallel ...

**Type:** article
**URL:** https://dev.to/bredmond1019/multi-agent-orchestration-running-10-claude-instances-in-parallel-part-3-29da
**Topic:** Subagents & Parallel Execution
**Published:** unknown

## Content

![DEV Community](https://media2.dev.to/dynamic/image/quality=100/https://dev-to-uploads.s3.amazonaws.com/uploads/logos/resized_logo_UQww2soKuUsjaOGNB38o.png)

## DEV Community

![](https://assets.dev.to/assets/heart-plus-active-9ea3b22f2bc311281db911d416166c5f430636e76b15cd5df6b3b841d830eefa.svg)
![](https://assets.dev.to/assets/sparkle-heart-5f9bee3767e18deb1bb725290cb151c25234768a0e9a2bd39370c382d02920cf.svg)
![](https://assets.dev.to/assets/multi-unicorn-b44d6f8c23cdd00964192bedc38af3e82463978aa611b4365bd33a0f1f4f3e97.svg)
![](https://assets.dev.to/assets/exploding-head-daceb38d627e6ae9b730f36a1e390fca556a4289d5a41abb2c35068ad3e2c4b5.svg)
![](https://assets.dev.to/assets/raised-hands-74b2099fd66a39f2d7eed9305ee0f4553df0eb7b4f11b01b6b1b499973048fe5.svg)
![](https://assets.dev.to/assets/fire-f60e7a582391810302117f987b22a8ef04a2fe0df7e3258a5f49332df1cec71e.svg)
![bredmond1019](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F278401%2F4023ed91-84e3-406e-9c9a-e63a0f049d42.jpg)

Posted on Aug 2, 2025

![](https://assets.dev.to/assets/sparkle-heart-5f9bee3767e18deb1bb725290cb151c25234768a0e9a2bd39370c382d02920cf.svg)
![](https://assets.dev.to/assets/multi-unicorn-b44d6f8c23cdd00964192bedc38af3e82463978aa611b4365bd33a0f1f4f3e97.svg)
![](https://assets.dev.to/assets/exploding-head-daceb38d627e6ae9b730f36a1e390fca556a4289d5a41abb2c35068ad3e2c4b5.svg)
![](https://assets.dev.to/assets/raised-hands-74b2099fd66a39f2d7eed9305ee0f4553df0eb7b4f11b01b6b1b499973048fe5.svg)
![](https://assets.dev.to/assets/fire-f60e7a582391810302117f987b22a8ef04a2fe0df7e3258a5f49332df1cec71e.svg)

# Multi-Agent Orchestration: Running 10+ Claude Instances in Parallel (Part 3)

## [Mastering Claude Code (3 Part Series)](/bredmond1019/series/32756)

Last Tuesday at 3 AM, I watched 12 Claude agents rebuild my entire frontend while I slept. One agent refactored components, another wrote tests, a third updated documentation, and a fourth optimized performance.

By morning, I had a pull request with 10,000+ lines of perfectly coordinated changes.

This isn't science fiction. This is multi-agent orchestration with Claude Code, and it's changing how we build software at scale.

## The Multi-Agent Revolution

In Parts 1 and 2, we explored Claude's capabilities and hook system. Now, let's tackle the ultimate productivity multiplier: running multiple Claude instances in parallel.

But first, a warning: **This is where things get complex**. Multiple agents mean:

Get it wrong, and you'll have chaos. Get it right, and you'll achieve superhuman productivity.

## The Architecture That Makes It Possible

Here's the system architecture I use for multi-agent orchestration:

`┌─────────────────────────────────────────────┐
│ Orchestrator (Meta-Agent) │
│ Decides what needs to be done │
└──────────────────┬──────────────────────────┘
│ Creates tasks
▼
┌─────────────────────────────────────────────┐
│ Task Queue (Redis) │
│ Stores and distributes work │
└─────┬───────┬───────┬───────┬──────────────┘
│ │ │ │
▼ ▼ ▼ ▼
┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐
│ Agent 1 │ │ Agent 2 │ │ Agent 3 │ │ Agent N │
│Frontend │ │ Backend │ │ Tests │ │ Docs │
└─────────┘ └─────────┘ └─────────┘ └─────────┘
│ │ │ │
└───────┴───────┴───────┘
│
▼
┌──────────────────┐
│ Observability │
│ Dashboard │
└──────────────────┘`

## Step 1: The Meta-Agent Orchestrator

The meta-agent is Claude running in a special mode where it doesn't write code - it manages other agents:

`# orchestrator.py
import json
import redis
import subprocess
from typing import List, Dict
class MetaAgent:
def __init__(self):
self.redis = redis.Redis(host='localhost', port=6379, db=0)
self.task_queue = 'claude_tasks'
def analyze_project(self, requirements: str) -> List[Dict]:
"""Use Claude to break down requirements into parallel tasks"""
prompt = f"""
Analyze these requirements and break them into independent tasks
that can be executed in parallel by specialized agents:
{requirements}
Return a JSON array of tasks with:
- id: unique identifier
- type: frontend|backend|testing|docs|refactor
- description: what needs to be done
- dependencies: array of task IDs that must complete first
- files: array of files this task will modify
"""
# Call Claude API
 response = self.call_claude(prompt)
return json.loads(response)
def distribute_tasks(self, tasks: List[Dict]):
"""Queue tasks for worker agents"""
# Sort by dependencies
 sorted_tasks = self.topological_sort(tasks)
for task in sorted_tasks:
# Check dependencies
 if self.dependencies_complete(task):
self.redis.lpush(self.task_queue, json.dumps(task))
else:
# Queue for later
 self.redis.lpush(f"{self.task_queue}:pending", json.dumps(task))
def spawn_worker_agents(self, count: int):
"""Launch Claude worker agents"""
for i in range(count):
subprocess.Popen([
'claude-code',
'--mode', 'worker',
'--id', f'agent-{i}',
'--config', 'worker-config.json'
])`

## Step 2: Specialized Worker Agents

Each worker agent has a specific role and configuration:

`# worker_agent.py
import os
import json
import redis
import time
class WorkerAgent:
def __init__(self, agent_id: str, specialization: str):
self.id = agent_id
self.specialization = specialization
self.redis = redis.Redis(host='localhost', port=6379, db=0)
def run(self):
"""Main worker loop"""
while True:
# Get task from queue
 task_data = self.redis.brpop('claude_tasks', timeout=5)
if task_data:
task = json.loads(task_data[1])
# Check if this agent can handle the task
 if self.can_handle(task):
self.execute_task(task)
else:
# Put it back for another agent
 self.redis.lpush('claude_tasks', task_data[1])
time.sleep(1)
def execute_task(self, task: Dict):
"""Execute a task with Claude"""
# Acquire file locks
 locked_files = self.acquire_locks(task['files'])
try:
# Set up Claude context
 prompt = self.build_prompt(task)
# Execute with Claude
 os.environ['CLAUDE_SESSION_ID'] = f"{self.id}-{task['id']}"
result = self.run_claude(prompt)
# Report completion
 self.redis.hset(f"task:{task['id']}", 'status', 'complete')
self.redis.hset(f"task:{task['id']}", 'result', result)
# Trigger dependent tasks
 self.trigger_dependencies(task['id'])
finally:
# Release locks
 self.release_locks(locked_files)
def acquire_locks(self, files: List[str]) -> List[str]:
"""Acquire exclusive locks on files"""
locked = []
for file_path in files:
lock_key = f"lock:{file_path}"
# Try to acquire lock with timeout
 if self.redis.set(lock_key, self.id, nx=True, ex=300):
locked.append(file_path)
else:
# Couldn't get lock, release all and retry
 self.release_locks(locked)
time.sleep(2)
return self.acquire_locks(files)
return locked`

## Step 3: Real-Time Observability

With multiple agents running, observability becomes critical. Here's my monitoring dashboard:

`<!DOCTYPE html>
<html>
<head>
<title>Claude Multi-Agent Command Center</title>
<script src="https://cdn.jsdelivr.net/npm/vue@3"></script>
<style>
.agent-grid {
display: grid;
grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
gap: 20px;
padding: 20px;
}
.agent-card {
border: 2px solid #3498db;
border-radius: 8px;
padding: 15px;
position: relative;
}
.agent-card.active {
border-color: #2ecc71;
box-shadow: 0 0 10px rgba(46, 204, 113, 0.3);
}
.agent-status {
position: absolute;
top: 10px;
right: 10px;
width: 12px;
height: 12px;
border-radius: 50%;
background: #95a5a6;
}
.agent-status.active { background: #2ecc71; }
.agent-status.busy { background: #f39c12; }
.agent-status.error { background: #e74c3c; }
.task-progress {
margin-top: 10px;
height: 20px;
background: #ecf0f1;
border-radius: 10px;
overflow: hidden;
}
.task-progress-bar {
height: 100%;
background: linear-gradient(90deg, #3498db, #2ecc71);
transition: width 0.3s;
}
.conflict-alert {
background: #e74c3c;
color: white;
padding: 10px;
border-radius: 5px;
margin: 10px;
}
</style>
</head>
<body>
<div id="app">
<h1>Claude Multi-Agent Command Center</h1>
<!-- Overall Stats -->
<div class="stats">
<h2>Mission Status</h2>
<p>Active Agents: {{ activeAgents.length }}</p>
<p>Tasks Completed: {{ completedTasks }} / {{ totalTasks }}</p>
<p>Files Modified: {{ modifiedFiles.size }}</p>
<p>Conflicts Detected: {{ conflicts.length }}</p>
</div>
<!-- Conflict Alerts -->
<div v-if="conflicts.length > 0" class="conflict-alert">
⚠️ File Conflicts Detected:
<ul>
<li v-for="conflict in conflicts" :key="conflict.file">
{{ conflict.file }} - {{ conflict.agents.join(' vs ') }}
</li>
</ul>
</div>
<!-- Agent Grid -->
<div class="agent-grid">
<div v-for="agent in agents"
:key="agent.id"
:class="['agent-card', { active: agent.status === 'active' }]">
<div :class="['agent-status', agent.status]"></div>
<h3>{{ agent.id }}</h3>
<p>Type: {{ agent.specialization }}</p>
<p>Current Task: {{ agent.currentTask || 'Idle' }}</p>
<div v-if="agent.currentTask" class="task-progress">
<div class="task-progress-bar"
:style="{ width: agent.progress + '%' }"></div>
</div>
<p>Files: {{ agent.workingFiles.join(', ') || 'None' }}</p>
<p>Tasks Completed: {{ agent.completedCount }}</p>
</div>
</div>
<!-- Activity Stream -->
<div class="activity-stream">
<h2>Live Activity</h2>
<div v-for="event in recentEvents" :key="event.id" class="event">
<span class="timestamp">{{ formatTime(event.timestamp) }}</span>
<span class="agent">{{ event.agentId }}:</span>
<span class="action">{{ event.action }}</span>
</div>
</div>
</div>
<script>
const { createApp } = Vue;
createApp({
data() {
return {
agents: [],
conflicts: [],
recentEvents: [],
totalTasks: 0,
completedTasks: 0,
modifiedFiles: new Set(),
ws: null
};
},
computed: {
activeAgents() {
return this.agents.filter(a => a.status === 'active');
}
},
methods: {
connect() {
this.ws = new WebSocket('ws://localhost:3001/agents');
this.ws.onmessage = (event) => {
const data = JSON.parse(event.data);
switch(data.type) {
case 'agent_update':
this.updateAgent(data.agent);
break;
case 'conflict':
this.conflicts.push(data.conflict);
break;
case 'task_complete':
this.completedTasks++;
break;
case 'event':
this.recentEvents.unshift(data.event);
this.recentEvents = this.recentEvents.slice(0, 50);
break;
}
};
},
updateAgent(agentData) {
const index = this.agents.findIndex(a => a.id === agentData.id);
if (index >= 0) {
this.agents[index] = agentData;
} else {
this.agents.push(agentData);
}
// Track modified files
if (agentData.workingFiles) {
agentData.workingFiles.forEach(f => this.modifiedFiles.add(f));
}
},
formatTime(timestamp) {
return new Date(timestamp).toLocaleTimeString();
}
},
mounted() {
this.connect();
}
}).mount('#app');
</script>
</body>
</html>`

## Real-World Example: The Frontend Refactor

Last week, I needed to refactor my entire component library from class components to functional components with hooks. Here's how multi-agent orchestration handled it:

### The Meta-Agent's Plan:

`[
{
"id": "analyze-1",
"type": "analysis",
"description": "Scan all components and create refactoring plan",
"dependencies": [],
"files": []
},
{
"id": "refactor-buttons",
"type": "frontend",
"description": "Convert all Button components to functional",
"dependencies": ["analyze-1"],
"files": ["components/Button/*.tsx"]
},
{
"id": "refactor-forms",
"type": "frontend",
"description": "Convert all Form components to functional",
"dependencies": ["analyze-1"],
"files": ["components/Form/*.tsx"]
},
{
"id": "update-tests-buttons",
"type": "testing",
"description": "Update Button component tests",
"dependencies": ["refactor-buttons"],
"files": ["__tests__/Button/*.test.tsx"]
},
{
"id": "update-tests-forms",
"type": "testing",
"description": "Update Form component tests",
"dependencies": ["refactor-forms"],
"files": ["__tests__/Form/*.test.tsx"]
},
{
"id": "update-docs",
"type": "docs",
"description": "Update component documentation",
"dependencies": ["refactor-buttons", "refactor-forms"],
"files": ["docs/components/*.md"]
}
]`

### The Execution:

**Total time**: 2 hours (vs estimated 2 days manual work)  
**Lines changed**: 12,000+  
**Tests passing**: 100%  
**Conflicts**: 0

## Handling the Complexity

### Challenge 1: Resource Management

Running 10+ Claude instances will max out your system. Here's my resource manager:

`# resource_manager.py
import psutil
import docker
class ResourceManager:
def __init__(self, max_agents=10):
self.max_agents = max_agents
self.docker = docker.from_env()
def can_spawn_agent(self) -> bool:
# Check CPU usage
 if psutil.cpu_percent(interval=1) > 80:
return False
# Check memory
 if psutil.virtual_memory().percent > 85:
return False
# Check active containers
 active = len([c for c in self.docker.containers.list()
if 'claude-agent' in c.name])
return active < self.max_agents
def spawn_agent_container(self, agent_config):
"""Spawn agent in Docker container for isolation"""
container = self.docker.containers.run(
'claude-agent:latest',
environment=agent_config,
detach=True,
name=f"claude-agent-{agent_config['id']}",
volumes={
'/project': {'bind': '/workspace', 'mode': 'rw'}
},
cpu_quota=50000, # Limit CPU usage
 mem_limit='2g' # Limit memory
 )
return container`

### Challenge 2: Coordination Without Conflicts

The key is smart task distribution and file locking:

`# conflict_prevention.py
class ConflictPrevention:
def __init__(self):
self.file_graph = self.build_dependency_graph()
def build_dependency_graph(self):
"""Map file dependencies to prevent conflicts"""
# Analyze imports and exports
 graph = {}
for file in glob.glob('**/*.ts', recursive=True):
imports = self.extract_imports(file)
graph[file] = imports
return graph
def can_modify_simultaneously(self, file1: str, file2: str) -> bool:
"""Check if two files can be modified in parallel"""
# Check if files import each other
 if file2 in self.file_graph.get(file1, []):
return False
if file1 in self.file_graph.get(file2, []):
return False
# Check if they share common dependencies
 deps1 = set(self.file_graph.get(file1, []))
deps2 = set(self.file_graph.get(file2, []))
shared = deps1.intersection(deps2)
# Allow if no shared critical dependencies
 return len(shared) == 0 or all(
not self.is_critical(dep) for dep in shared
)`

### Challenge 3: Quality Control

With multiple agents, quality control becomes critical:

`# quality_gate.py
class QualityGate:
def __init__(self):
self.checks = [
self.check_tests_pass,
self.check_type_safety,
self.check_no_conflicts,
self.check_performance,
self.check_security
]
def validate_agent_work(self, agent_id: str, changes: Dict):
"""Validate agent's changes before merging"""
results = []
for check in self.checks:
result = check(changes)
results.append(result)
if not result['passed']:
# Revert changes and reassign task
 self.revert_changes(changes)
self.reassign_task(agent_id, result['reason'])
return False
return True
def check_tests_pass(self, changes):
"""Run tests on changed files"""
affected_tests = self.find_affected_tests(changes['files'])
result = subprocess.run(
['npm', 'test'] + affected_tests,
capture_output=True
)
return {
'passed': result.returncode == 0,
'reason': result.stderr.decode() if result.returncode != 0 else None
}`

## The Economics of Multi-Agent Development

Let's talk ROI. Running 10 Claude agents costs approximately:

But the productivity gains:

For a team of 5 developers, this replaces roughly $50,000/month in engineering time for $2,000/month in compute costs.

## Getting Started with Multi-Agent

Start small:

## The Future is Distributed

We're entering an era where a single developer can orchestrate an entire team of AI agents. The bottleneck isn't coding speed anymore - it's our ability to coordinate and direct these agents effectively.

Next week, I'm experimenting with 50+ agents working on a complete application rewrite. The meta-agent will manage sub-orchestrators, each controlling their own team of specialized agents.

It's turtles all the way down, and it's beautiful.

## 🚀 Take Your AI Engineering to the Next Level

### **🌐 Visit [learn-agentic-ai.com](https://learn-agentic-ai.com) - Your Hub for Advanced AI Development**

### **🎓 Complete Learning Paths:**

### **📚 Essential Reading for Multi-Agent Systems:**

### **💡 Business & ROI Resources:**

### **🛠️ Tools & Templates:**

**About the Author:**  
I'm Brandon J. Redmond, AI Engineer & Agentic Systems Architect. I've built and deployed multi-agent systems processing millions of requests. Let's connect on [LinkedIn](https://www.linkedin.com/in/bredmond1019/) or explore more at [learn-agentic-ai.com](https://learn-agentic-ai.com).

Have you experimented with multiple AI agents? What challenges did you face? Let's discuss in the comments!

**Previous Articles in This Series:**

**Ready to build your own agent swarm?** Start with the [Claude Code Mastery learning path](https://learn-agentic-ai.com/en/learn/paths/claude-code-mastery) - from zero to orchestrating multiple agents in 7 comprehensive modules.

## [Mastering Claude Code (3 Part Series)](/bredmond1019/series/32756)

## Top comments (3)

![pic](https://media2.dev.to/dynamic/image/width=256,height=,fit=scale-down,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F8j7kvp660rqzt99zui8e.png)

Templates let you quickly answer FAQs or store snippets for re-use.

![adrian_pedrozeladatorre profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F2045166%2F56c2c881-8e03-4606-bbc1-6f59559a6733.jpg)
![](https://media2.dev.to/dynamic/image/width=90,height=90,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F2045166%2F56c2c881-8e03-4606-bbc1-6f59559a6733.jpg)

Dear Brandon, I am very grateful for this series of articles in which you shared your experience. Thank you so much for sharing your knowledge. I tried to access your website but I get an error message: "This deployment is temporarily paused." I am very interested in accessing your articles; how can I do so?

![max_quimby profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F3823178%2F0a97facc-1e95-494c-9db9-084aa3b35e47.png)
![](https://media2.dev.to/dynamic/image/width=90,height=90,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F3823178%2F0a97facc-1e95-494c-9db9-084aa3b35e47.png)

The conflict prevention angle here is really the crux of it — most multi-agent writeups spend all their time on the happy path and then wave at "just use file locking" like it's obvious. The detail on how you structured the Redis task queue to avoid agent contention is the part I'd love to see expanded.

One thing we've run into at scale: context window drift becomes a real failure mode when you have 10+ agents running long jobs. Agent 7 might be operating on a stale view of the codebase that agents 1–3 already modified. Do you have a mechanism for broadcasting completed-work summaries back to the orchestrator so other agents can update their working context mid-run? Or do you do a full sync-and-re-queue between phases?

The "2 days → 2 hours" framing is compelling, but the interesting follow-up question is always: what percentage of runs complete cleanly vs. require human intervention to untangle? That ratio is where the real productivity story lives.

Some comments may only be visible to logged-in visitors. [Sign in](/enter) to view all comments.

Are you sure you want to hide this comment? It will become hidden in your post, but will still be visible via the comment's [permalink](#).

Hide child comments as well

Confirm

For further actions, you may consider blocking this person and/or [reporting abuse](/report-abuse)

![](https://media2.dev.to/dynamic/image/width=90,height=90,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F278401%2F4023ed91-84e3-406e-9c9a-e63a0f049d42.jpg)

### More from [bredmond1019](/bredmond1019)

💎 DEV Diamond Sponsors

Thank you to our Diamond Sponsors for supporting the DEV Community

![Google AI - Official AI Model and Platform Partner](https://media2.dev.to/dynamic/image/width=880%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fxjlyhbdqehj3akhz166w.png)

Google AI is the official AI Model and Platform Partner of DEV

![Neon - Official Database Partner](https://media2.dev.to/dynamic/image/width=880%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fbnl88cil6afxzmgwrgtt.png)

Neon is the official database partner of DEV

![Algolia - Official Search Partner](https://media2.dev.to/dynamic/image/width=880%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fv30ephnolfvnlwgwm0yz.png)

Algolia is the official search partner of DEV

[DEV Community](/) — A space to discuss and keep up software development and manage your software career

Built on [Forem](https://www.forem.com) — the [open source](https://dev.to/t/opensource) software that powers [DEV](https://dev.to) and other inclusive communities.

Made with love and [Ruby on Rails](https://dev.to/t/rails). DEV Community © 2016 - 2026.

![DEV Community](https://media2.dev.to/dynamic/image/width=190,height=,fit=scale-down,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F8j7kvp660rqzt99zui8e.png)

We're a place where coders share, stay up-to-date and grow their careers.

![](https://assets.dev.to/assets/sparkle-heart-5f9bee3767e18deb1bb725290cb151c25234768a0e9a2bd39370c382d02920cf.svg)
![](https://assets.dev.to/assets/multi-unicorn-b44d6f8c23cdd00964192bedc38af3e82463978aa611b4365bd33a0f1f4f3e97.svg)
![](https://assets.dev.to/assets/exploding-head-daceb38d627e6ae9b730f36a1e390fca556a4289d5a41abb2c35068ad3e2c4b5.svg)
![](https://assets.dev.to/assets/multi-unicorn-b44d6f8c23cdd00964192bedc38af3e82463978aa611b4365bd33a0f1f4f3e97.svg)
![](https://assets.dev.to/assets/exploding-head-daceb38d627e6ae9b730f36a1e390fca556a4289d5a41abb2c35068ad3e2c4b5.svg)
![](https://assets.dev.to/assets/exploding-head-daceb38d627e6ae9b730f36a1e390fca556a4289d5a41abb2c35068ad3e2c4b5.svg)
![](https://assets.dev.to/assets/raised-hands-74b2099fd66a39f2d7eed9305ee0f4553df0eb7b4f11b01b6b1b499973048fe5.svg)
![](https://assets.dev.to/assets/fire-f60e7a582391810302117f987b22a8ef04a2fe0df7e3258a5f49332df1cec71e.svg)
