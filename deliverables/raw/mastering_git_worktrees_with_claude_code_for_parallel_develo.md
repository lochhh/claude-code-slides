# Mastering Git Worktrees with Claude Code for Parallel Development Workflow

**Type:** article
**URL:** https://medium.com/@dtunai/mastering-git-worktrees-with-claude-code-for-parallel-development-workflow-41dc91e645fe
**Topic:** Git Worktrees
**Published:** unknown

## Content

# Mastering Git Worktrees with Claude Code for Parallel Development Workflow | by Dogukan Uraz Tuna | Medium | Medium

[Sitemap](https://medium.com/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fmedium.com%2F%40dtunai%2Fmastering-git-worktrees-with-claude-code-for-parallel-development-workflow-41dc91e645fe&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

Get app

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fmedium.com%2F%40dtunai%2Fmastering-git-worktrees-with-claude-code-for-parallel-development-workflow-41dc91e645fe&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![Image 1](https://miro.medium.com/v2/resize:fill:32:32/1*dmbNkD5D-u45r44go_cf0g.png)

# Mastering Git Worktrees with Claude Code for Parallel Development Workflow

[![Image 2: Dogukan Tuna](https://miro.medium.com/v2/resize:fill:32:32/1*jtH-z1jhchV1GI10iy4IzA.jpeg)](https://medium.com/@dtunai?source=post_page---byline--41dc91e645fe---------------------------------------)

[Dogukan Tuna](https://medium.com/@dtunai?source=post_page---byline--41dc91e645fe---------------------------------------)

Follow

10 min read

·

Jun 23, 2025

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fp%2F41dc91e645fe&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40dtunai%2Fmastering-git-worktrees-with-claude-code-for-parallel-development-workflow-41dc91e645fe&user=Dogukan+Tuna&userId=5b0793975632&source=---header_actions--41dc91e645fe---------------------clap_footer------------------)

173

4

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F41dc91e645fe&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40dtunai%2Fmastering-git-worktrees-with-claude-code-for-parallel-development-workflow-41dc91e645fe&source=---header_actions--41dc91e645fe---------------------bookmark_footer------------------)

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3D41dc91e645fe&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40dtunai%2Fmastering-git-worktrees-with-claude-code-for-parallel-development-workflow-41dc91e645fe&source=---header_actions--41dc91e645fe---------------------post_audio_button------------------)

Share

Press enter or click to view image in full size

![Image 3](https://miro.medium.com/v2/resize:fit:700/1*S01ccRU5eHyApcr1akNvig.avif)

Most underrated feature in Claude Code could be the ability to create like many different Claude Code instances at once using Git worktrees and have them all tackle different parts of your project in parallel.

However, context switching problem is a major bottleneck but running multiple Claude Code sessions simultaneously — each working on different features in complete isolation is a development velocity accelerator. Imagine this, it’s 2 PM, you’re deep in the vibe zone with Claude Code building a complex machine learning pipeline.

In this blog post, regardless from your goal, we will examine what you need to do to set up such a workflow and how you can benefit from its different use cases.

## Table of Contents

*   Context Switching Nightmare
*   Git Worktrees: New Development Workflow with Claude
*   Setting Up Parallel Vibe Development
*   Real-World Applications
*   Advanced Techniques & Automation
*   Troubleshooting & Optimization
*   Final Thoughts

## Context Switching Problem

Claude follows your PLAN, uses MEMORY, makes analysis, and understands your codebase perfectly, you’re making incredible progress on your data preprocessing module, when suddenly — ping! — a critical bug report lands or a new high-priority task request comes in.

You know what comes next:

1.   `git stash`_your current work (goodbye, Claude's context, maybe)_
2.   `git checkout main`
3.   `git checkout -b hotfix/urgent-bug`
4.   _Start Claude Code from scratch, re-explain the entire ML pipeline architecture_
5.   _Fix the bug while Claude struggles to understand your data flow and model dependencies_
6.   _Deploy the fix_
7.   _Switch back to your feature branch_
8.   _Spend 20 minutes getting Claude back up to speed on your preprocessing work_

This is the context switching tax. Every time you force Claude to jump between branches, you’re losing its most valuable asset: the deep understanding it built up about your specific codebase.

When you force Claude Code to context-switch between branches, you’re throwing away its most valuable asset: the deep understanding it has built up about your specific codebase, your patterns, your goals.

Git worktrees solve this by letting you run multiple Claude Code sessions in parallel, each with its own isolated context. No more context switching. No more lost momentum. Just pure, uninterrupted vibe zone development flow.

## Traditional vs Worktree Workflow

Here’s the difference in parallel development capability:

 

Traditional Single-Directory Approach:

┌─────────────────────────────────────────────────────────────┐

│ Single Repository Directory │

│ ┌─────────────────────────────────────────────────────────┐ │

│ │ Current Branch: main → feature/auth → bugfix → main │ │

│ │ │ │

│ │ Context Lost ❌ Context Lost ❌ Context Lost ❌ │ │

│ │ ↓ ↓ ↓ │ │

│ │ git stash git checkout git checkout │ │

│ │ git checkout git stash git stash │ │

│ │ restart AI restart AI restart AI │ │

│ └─────────────────────────────────────────────────────────┘ │

│ Sequential Work Only - One Task at a Time │

└─────────────────────────────────────────────────────────────┘

Git Worktrees Approach:

┌─────────────────────────────────────────────────────────────┐

│ Multiple Isolated Directories │

│ ┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐ │

│ │ ml-training/ │ │ ml-inference/ │ │ ml-hotfix/ │ │

│ │ Branch: train │ │ Branch: api │ │ Branch: bugfix │ │

│ │ Claude Code ✅ │ │ Claude Code ✅ │ │ Claude Code ✅ │ │

│ │ Context: FULL │ │ Context: FULL │ │ Context: FULL │ │

│ │ Status: Active │ │ Status: Active │ │ Status: Active │ │

│ └─────────────────┘ └─────────────────┘ └─────────────────┘ │

│ Parallel Work ✅ - Multiple Tasks Simultaneously │

└─────────────────────────────────────────────────────────────┘
## Understanding Git Worktrees

Git worktrees let you check out multiple branches into separate physical directories, all linked to the same repository. Think of it as having multiple “copies” of your project, each on a different branch, without the overhead of multiple clones.

Here’s the magic: each directory maintains complete isolation while sharing the same Git history. No more `git stash`. No context switching. Just pure, uninterrupted flow.

# Your main project

~/ml-project/ # main branch

├── .git/ # The actual Git repository (shared)

├── src/

├── models/

├── data/

└── requirements.txt

# After creating worktrees - each is a complete, isolated workspace

~/ml-project-training/ # feature/model-training branch 

├── .git # → Links to main .git repository

├── src/ # Independent file states

├── models/ # Different model versions

├── data/ # Same data, different processing

├── requirements.txt # Potentially different dependencies

└── experiments/ # Training-specific experiments

~/ml-project-inference/ # feature/inference-api branch 

├── .git # → Links to main .git repository

├── src/ # Independent file states

├── models/ # Production model versions

├── api/ # API-specific code

├── requirements.txt # API-focused dependencies

└── tests/ # API integration tests

~/ml-project-bugfix/ # hotfix/data-corruption branch

├── .git # → Links to main .git repository

├── src/ # Hotfix-specific changes

├── data/ # Data validation fixes

└── requirements.txt # Minimal dependencies for debugging

```
**Key Benefits:**

*   Each directory maintains **complete isolation** — no file conflicts between tasks
*   All worktrees share the **same Git history** — commits, branches, and remotes are synchronized
*   **No more**`git stash` - your work stays exactly where you left it
*   **No context switching overhead** — Claude Code maintains full understanding in each environment
*   **Zero risk of wrong branch commits** — impossible to accidentally commit to the wrong branch

## Claude Code Context Management

Understanding how Claude Code builds and maintains context is crucial for maximizing worktree benefits:

**Claude Code Context Sources:**

*   **File System Awareness**: Open files, project structure, directory organization
*   **Git History Integration**: Recent commits, branch relationships, change patterns
*   **Dependency Understanding**: Package files, import relationships, environment configs
*   **Conversation Memory**: Your instructions, preferences, and ongoing discussions
*   **Code Pattern Recognition**: Coding style, architecture decisions, naming conventions

**Traditional Branch Switching Problems:**

_Single Directory Workflow:_

Branch Switch → Context Reset → Manual Re-explanation Required

1.   git checkout feature-branch # File system changes
2.   Claude loses project context # ❌ Forgets current work
3.   Must re-explain architecture # ⏱️ 10–15 minutes lost
4.   Claude relearns codebase # 🔄 Inefficient repetition
5.   Finally productive again # 💸 Expensive context rebuild

**Worktree Advantage:**

_Multi-Directory Workflow:_ Each Worktree → Persistent Context → Immediate Productivity

1.   _cd ../ml-project-training # Directory switch only_
2.   _Claude retains full context # ✅ Remembers everything_
3.   _Immediate task continuation # ⚡ Zero warm-up time_
4.   _Deep understanding preserved # 🧠 Accumulated knowledge_
5.   _Maximum efficiency achieved # 🚀 Peak performance_

This context preservation is what transforms worktrees from a simple Git feature into a productivity multiplier for AI-assisted development.

## Productivity Setup

# Create worktrees for parallel development

git worktree add ../ml-pipeline-training -b feature/model-training main

git worktree add ../ml-pipeline-inference -b feature/inference-api main 

git worktree add ../ml-pipeline-hotfix -b hotfix/data-corruption main

# Open each in separate editor windows

code ../ml-pipeline-training # Window 1: Model training pipeline

code ../ml-pipeline-inference # Window 2: Inference API development

code ../ml-pipeline-hotfix # Window 3: Critical data bug fix
**Now you can:**

*   Have Claude Code work on your PyTorch training loop in Window 1
*   Let another Claude session build your FastAPI inference endpoint in Window 2
*   Quickly fix data corruption bugs in Window 3 without losing context anywhere

## Powerful Use Cases

### Model Comparison

Compare different models (sonnet or opus or codex) on identical tasks using separate worktrees:

# Create separate worktrees for each AI

git worktree add ../ml-claude-implementation -b experiment/claude-automl main

git worktree add ../ml-codex-implementation -b experiment/codex-automl main

# Set up identical specifications

echo "# AutoML Pipeline Specification

Build an automated machine learning pipeline for tabular data.

Requirements:

- Data preprocessing (missing values, encoding, scaling)

- Feature selection using statistical methods

- Model selection (RandomForest, XGBoost, LightGBM)

- Automated hyperparameter tuning

- Cross-validation and performance metrics

- Model persistence and loading" > specs/automl.md
Give both AIs the same prompt: _“Implement @specs/automl.md”_

## Get Dogukan Tuna’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Subscribe

- [x] 

Remember me for faster sign in

 

Run both sessions simultaneously and compare:

*   Implementation approach and code quality
*   Time to completion
*   How well each AI follows specifications
*   Error handling and edge cases

When finished, merge the better implementation:

# Choose the better implementation

git add -A

git commit -m "Implement AutoML pipeline with preprocessing and model selection"

# Back to main project

cd ../ml-project

git merge experiment/claude-automl

# Clean up

git worktree remove ../ml-claude-implementation

git branch -d experiment/claude-automl
### Safe Framework Migrations

Test large-scale refactoring in isolated worktrees:

git worktree add ../ml-pytorch-migration -b experiment/pytorch-migration main

cd ../ml-pytorch-migration

# Let Claude Code handle the migration while your main work continues

# Convert TensorFlow models, data loaders, and training loops to PyTorch

# If it goes sideways, simply delete the folder—no git history pollution
### Enhanced Code Reviews

Prepare enhanced code reviews without touching your main branch:

git worktree add ../ml-review -b review/feature-data-pipeline feature-data-pipeline

# Use Claude Code to:

# - Add comprehensive docstrings to all functions

# - Generate documentation for data schemas and model architectures

# - Create unit tests for data validation and model inference

# - Add type hints and clean up code style

# - Generate example usage and integration tests
### Parallel Environment Testing

Run multiple Python environments and experiments simultaneously:

# In training worktree

cd ../ml-training && python -m uvicorn training_api:app --port 8000

# In inference worktree 

cd ../ml-inference && python -m uvicorn inference_api:app --port 8001

# In experimental worktree

cd ../ml-experiment && jupyter lab --port 8888

# Compare model performance across different endpoints and notebook experiments
### Safe Dependency Upgrades

Test major dependency upgrades safely:

git worktree add ../ml-pytorch-2 -b upgrade/pytorch-2.0 main

cd ../ml-pytorch-2

pip install torch==2.0.0 torchvision==0.15.0
### Simultaneous Feature Development

Work on multiple ML features simultaneously:

git worktree add ../ml-feature-engineering -b feature/advanced-features main

git worktree add ../ml-model-optimization -b feature/model-compression main

git worktree add ../ml-monitoring -b feature/model-monitoring main

# Each Claude Code session focuses on its specific ML component:

# - Feature engineering with statistical transformations

# - Model quantization and pruning techniques 

# - MLOps monitoring and drift detection
## Troubleshooting Common Issues

### Problem — 1:

“fatal: ‘branch’ is already checked out”. You’re trying to create a worktree for a branch that’s already checked out somewhere.

# List all worktrees to find conflicts

git worktree list

# Remove the conflicting worktree

git worktree remove /path/to/conflicting/worktree

# Or use --force to override

git worktree add --force ../new-location existing-branch
### Problem — 2:

Python packages and dependencies consume excessive disk space.

Solution: Use virtual environment sharing or containerization.

# Option 1: Shared conda environment (recommended)

conda create -n ml-shared python=3.10

conda activate ml-shared

pip install -r requirements.txt

# Use the same environment across worktrees

cd ../ml-project-training && conda activate ml-shared

cd ../ml-project-inference && conda activate ml-shared

# Option 2: Poetry with shared cache

poetry config cache-dir /shared/poetry-cache

poetry install # Uses shared dependency cache

# Option 3: Docker with shared volumes

docker run -v $(pwd):/workspace -v ml-packages:/opt/conda/lib/python3.10/site-packages python:3.10
### Problem — 3

Data and model conflicts between ML worktrees.

Solution: Use isolated data paths and model versioning.

# Different data paths per worktree

export DATA_PATH=/data/training-experiments

export MODEL_PATH=/models/training-v1

export DATA_PATH=/data/inference-production 

export MODEL_PATH=/models/production-v2

# Or containerized data isolation

docker run --name ml-training-env -v training-data:/data -v training-models:/models python:3.10

docker run --name ml-inference-env -v inference-data:/data -v production-models:/models python:3.10

# MLflow model registry for version management

mlflow server --backend-store-uri sqlite:///training.db --default-artifact-root ./training-artifacts

mlflow server --backend-store-uri sqlite:///production.db --default-artifact-root ./production-artifacts
### Problem — 4

Too many worktrees and can’t remember what each one does.

Solution: Use a naming convention and regular cleanup.

# Good naming

myapp-feat-auth-oauth2 # Feature: OAuth2 authentication

myapp-bug-payment-timeout # Bug: Payment timeout issue

myapp-exp-react-18 # Experiment: React 18 upgrade

# Bad naming

myapp-1, myapp-temp, myapp-test
### Problem — 5

Each worktree has different package versions, causing conflicts.

Solution: Use lockfiles and version pinning.

# Copy lockfiles to new worktrees

cp requirements.txt ../myapp-feature/

cp setup-requirements.txt ../myapp-feature/

# Or use exact versions

pip install --save-exact torch==2.0.0 torchvision==0.15.0
## Workflow Automation Scripts

### Ultimate Workflow Creation

#!/bin/bash

# save as: create-worktree.sh

if [ $# -eq 0 ]; then

 echo "Usage: $0 <branch-name> [base-branch]"

 exit 1

fi

BRANCH_NAME=$1

BASE_BRANCH=${2:-main}

REPO_NAME=$(basename $(git rev-parse --show-toplevel))

WORKTREE_PATH="../${REPO_NAME}-${BRANCH_NAME}"

# Create worktree

git worktree add -b "$BRANCH_NAME" "$WORKTREE_PATH" "$BASE_BRANCH"

# Setup environment

cd "$WORKTREE_PATH"

npm install # or your setup command

# Create task file

echo "# Task: $BRANCH_NAME

## Description:

[Add your task description here]

## Files to modify:

- 

## Success criteria:

- " > TASK.md

# Open in editor

code .

echo "Worktree created at: $WORKTREE_PATH"

echo "Task file created: TASK.md"

echo "Ready for Claude Code!"
### **Automated Cleanup**

#!/bin/bash

# save as: cleanup-worktrees.sh

echo "Cleaning up merged worktrees..."

git worktree list | grep -v "$(git rev-parse --show-toplevel)" | while read worktree branch commit; do

 branch_name=$(echo $branch | sed 's/\[//g' | sed 's/\]//g')

 

 # Check if branch is merged

 if git branch --merged main | grep -q "$branch_name"; then

 echo "Removing merged worktree: $worktree ($branch_name)"

 git worktree remove "$worktree"

 git branch -d "$branch_name"

 fi

done

echo "Cleanup complete!"
There are many other scripts that take worktree automation to the next level, for more please review _.claude/commands_ under the below repository:

## [GitHub - evmts/tevm-monorepo: An Ethereum Node built to run in Browser, Bun, Deno, and Node.js ### An Ethereum Node built to run in Browser, Bun, Deno, and Node.js - evmts/tevm-monorepo github.com](https://github.com/evmts/tevm-monorepo?source=post_page-----41dc91e645fe---------------------------------------)

Even, [we have an helper of Git worktree helper for Claude Code:](https://x.com/yongyuanxi/status/1936914281502744731)

## Disk Space Management

Worktrees use extra disk space for each checkout since they replicate certain working files from the repository. However, because they share the main `.git` directory rather than duplicating it entirely, the overall disk usage remains relatively low.

Here’s how to optimize:

```bash

# Use Git's built-in deduplication

git repack -ad

# Share node_modules between worktrees (be careful!)

# Only do this for read-only dependencies

ln -s ../../myapp-main/node_modules ./node_modules

# Use pnpm for automatic dependency sharing

pnpm install # Automatically shares packages

```
## Conclusion

Git worktrees with Claude Code isn’t just a workflow improvement — it’s an important shift in how you build things. You’re no longer a single developer switching between tasks. You’re a conductor orchestrating multiple AI-powered development streams in parallel. The future of development is parallel, AI-assisted, and context-aware. Git worktrees are starting point to that future when you augmented with AI coding agents.

_This blog post is cross-posted on my website:_

## [Mastering Git Worktrees with Claude Code for Parallel Development Workflow ### Use Git worktrees to run multiple Claude Code sessions in parallel. Learn how to eliminate context switching overhead… dogukantuna.me](https://dogukantuna.me/blog/mastering-git-worktrees-with-claude-code?source=post_page-----41dc91e645fe---------------------------------------)

[Claude Code](https://medium.com/tag/claude-code?source=post_page-----41dc91e645fe---------------------------------------)

[Agents](https://medium.com/tag/agents?source=post_page-----41dc91e645fe---------------------------------------)

[Agentic Ai](https://medium.com/tag/agentic-ai?source=post_page-----41dc91e645fe---------------------------------------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fp%2F41dc91e645fe&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40dtunai%2Fmastering-git-worktrees-with-claude-code-for-parallel-development-workflow-41dc91e645fe&user=Dogukan+Tuna&userId=5b0793975632&source=---footer_actions--41dc91e645fe---------------------clap_footer------------------)

173

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fp%2F41dc91e645fe&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40dtunai%2Fmastering-git-worktrees-with-claude-code-for-parallel-development-workflow-41dc91e645fe&user=Dogukan+Tuna&userId=5b0793975632&source=---footer_actions--41dc91e645fe---------------------clap_footer------------------)

173

4

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F41dc91e645fe&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40dtunai%2Fmastering-git-worktrees-with-claude-code-for-parallel-development-workflow-41dc91e645fe&source=---footer_actions--41dc91e645fe---------------------bookmark_footer------------------)

[![Image 4: Dogukan Tuna](https://miro.medium.com/v2/resize:fill:48:48/1*jtH-z1jhchV1GI10iy4IzA.jpeg)](https://medium.com/@dtunai?source=post_page---post_author_info--41dc91e645fe---------------------------------------)

[![Image 5: Dogukan Tuna](https://miro.medium.com/v2/resize:fill:64:64/1*jtH-z1jhchV1GI10iy4IzA.jpeg)](https://medium.com/@dtunai?source=post_page---post_author_info--41dc91e645fe---------------------------------------)

Follow

## [Written by Dogukan Tuna](https://medium.com/@dtunai?source=post_page---post_author_info--41dc91e645fe---------------------------------------)

[142 followers](https://medium.com/@dtunai/followers?source=post_page---post_author_info--41dc91e645fe---------------------------------------)

·[13 following](https://medium.com/@dtunai/following?source=post_page---post_author_info--41dc91e645fe---------------------------------------)

Website: [dtunai.blog](http://dtunai.blog/)

Follow

## Responses (4)

[](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page---post_responses--41dc91e645fe---------------------------------------)

![Image 6](https://miro.medium.com/v2/resize:fill:32:32/1*dmbNkD5D-u45r44go_cf0g.png)

Write a response

[What are your thoughts?](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40dtunai%2Fmastering-git-worktrees-with-claude-code-for-parallel-development-workflow-41dc91e645fe&source=---post_responses--41dc91e645fe---------------------respond_sidebar------------------)

Cancel

Respond

[![Image 7: Piyush Kukadiya](https://miro.medium.com/v2/resize:fill:32:32/0*RCOIQiujo5ORGDAi.jpg)](https://medium.com/@piyush.kukadiya?source=post_page---post_responses--41dc91e645fe----0-----------------------------------)

[Piyush Kukadiya](https://medium.com/@piyush.kukadiya?source=post_page---post_responses--41dc91e645fe----0-----------------------------------)

[Mar 26](https://medium.com/@piyush.kukadiya/cant-you-save-session-on-specific-branch-and-resume-it-whenever-you-switch-back-b2b6ad69539a?source=post_page---post_responses--41dc91e645fe----0-----------------------------------)

Can't you save session on specific branch and resume it whenever you switch back?

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fp%2Fb2b6ad69539a&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40piyush.kukadiya%2Fcant-you-save-session-on-specific-branch-and-resume-it-whenever-you-switch-back-b2b6ad69539a&user=Piyush+Kukadiya&userId=14d79f8a3dad&source=---post_responses--b2b6ad69539a----0-----------------respond_sidebar------------------)

Reply

[![Image 8: Tom Clark](https://miro.medium.com/v2/resize:fill:32:32/2*z4g-ykQB7dCFfmf9q_1yeQ.jpeg)](https://medium.com/@thclark?source=post_page---post_responses--41dc91e645fe----1-----------------------------------)

[Tom Clark](https://medium.com/@thclark?source=post_page---post_responses--41dc91e645fe----1-----------------------------------)

[Feb 6(edited)](https://thclark.medium.com/interesting-but-what-are-the-actual-benefits-over-just-using-multiple-clones-38dd53764ea7?source=post_page---post_responses--41dc91e645fe----1-----------------------------------)

Interesting but what are the actual benefits over just using multiple clones? Maybe if your repo is vast, or you're using git-lfs it avoids duplicate downloading of all the history, but for any normal size of repo the cost of cloning is pretty negligible. So are there any benefits other than that?

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fp%2F38dd53764ea7&operation=register&redirect=https%3A%2F%2Fthclark.medium.com%2Finteresting-but-what-are-the-actual-benefits-over-just-using-multiple-clones-38dd53764ea7&user=Tom+Clark&userId=3dabf88fa82b&source=---post_responses--38dd53764ea7----1-----------------respond_sidebar------------------)

1 reply

Reply

[![Image 9: Lars](https://miro.medium.com/v2/resize:fill:32:32/0*4iUZreGop5BZNhbG)](https://medium.com/@lars.schlensog?source=post_page---post_responses--41dc91e645fe----2-----------------------------------)

[Lars](https://medium.com/@lars.schlensog?source=post_page---post_responses--41dc91e645fe----2-----------------------------------)

[Oct 8, 2025](https://medium.com/@lars.schlensog/very-cool-will-implement-this-when-creating-websites-like-webdevradar-com-e7a6115c4e23?source=post_page---post_responses--41dc91e645fe----2-----------------------------------)

Very cool will implement this when creating websites like webdevradar.com

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fp%2Fe7a6115c4e23&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40lars.schlensog%2Fvery-cool-will-implement-this-when-creating-websites-like-webdevradar-com-e7a6115c4e23&user=Lars&userId=01321510de57&source=---post_responses--e7a6115c4e23----2-----------------respond_sidebar------------------)

Reply

See all responses

## More from Dogukan Tuna

![Image 10: Streaming deepagents and task delegation with real-time output](https://miro.medium.com/v2/resize:fit:679/format:webp/1*kq7DwsV3IiwkCSR0uXpfRw.png)

[![Image 11: Dogukan Tuna](https://miro.medium.com/v2/resize:fill:20:20/1*jtH-z1jhchV1GI10iy4IzA.jpeg)](https://medium.com/@dtunai?source=post_page---author_recirc--41dc91e645fe----0---------------------aaf590b8_a8b1_4914_9b3e_415f2ac70c4d--------------)

[Dogukan Tuna](https://medium.com/@dtunai?source=post_page---author_recirc--41dc91e645fe----0---------------------aaf590b8_a8b1_4914_9b3e_415f2ac70c4d--------------)

## [Streaming deepagents and task delegation with real-time output ### Using an LLM to call tools in a loop is the simplest form of an agent. This architecture, however, can yield agents that are “shallow” and…](https://medium.com/@dtunai/streaming-deepagents-and-task-delegation-with-real-time-output-023e9ec049ba?source=post_page---author_recirc--41dc91e645fe----0---------------------aaf590b8_a8b1_4914_9b3e_415f2ac70c4d--------------)

Oct 21, 2025

[38](https://medium.com/@dtunai/streaming-deepagents-and-task-delegation-with-real-time-output-023e9ec049ba?source=post_page---author_recirc--41dc91e645fe----0---------------------aaf590b8_a8b1_4914_9b3e_415f2ac70c4d--------------)

[](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40dtunai%2Fmastering-git-worktrees-with-claude-code-for-parallel-development-workflow-41dc91e645fe&source=---author_recirc--41dc91e645fe----0-----------------explicit_signal----aaf590b8_a8b1_4914_9b3e_415f2ac70c4d--------------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F023e9ec049ba&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40dtunai%2Fstreaming-deepagents-and-task-delegation-with-real-time-output-023e9ec049ba&source=---author_recirc--41dc91e645fe----0-----------------bookmark_preview----aaf590b8_a8b1_4914_9b3e_415f2ac70c4d--------------)

![Image 12: Writing AI Agent with Rust from Scratch, Deploying to Edge with WebAssembly — OS Week 1](https://miro.medium.com/v2/resize:fit:679/format:webp/1*1m7zk9ocKO9SEA7dMgNH3A.png)

[![Image 13: ITNEXT](https://miro.medium.com/v2/resize:fill:20:20/1*yAqDFIFA5F_NXalOJKz4TA.png)](https://medium.com/itnext?source=post_page---author_recirc--41dc91e645fe----1---------------------aaf590b8_a8b1_4914_9b3e_415f2ac70c4d--------------)

In

[ITNEXT](https://medium.com/itnext?source=post_page---author_recirc--41dc91e645fe----1---------------------aaf590b8_a8b1_4914_9b3e_415f2ac70c4d--------------)

by

[Dogukan Tuna](https://medium.com/@dtunai?source=post_page---author_recirc--41dc91e645fe----1---------------------aaf590b8_a8b1_4914_9b3e_415f2ac70c4d--------------)

## [Writing AI Agent with Rust from Scratch, Deploying to Edge with WebAssembly — OS Week 1 ### Let’s write AI agent with Rust from scratch, deploy to the client-side edge with WebAssembly…](https://medium.com/itnext/writing-ai-agent-with-rust-from-scratch-deploying-to-edge-with-webassembly-os-week-1-bc0825b6303b?source=post_page---author_recirc--41dc91e645fe----1---------------------aaf590b8_a8b1_4914_9b3e_415f2ac70c4d--------------)

Jul 29, 2024

[23 2](https://medium.com/itnext/writing-ai-agent-with-rust-from-scratch-deploying-to-edge-with-webassembly-os-week-1-bc0825b6303b?source=post_page---author_recirc--41dc91e645fe----1---------------------aaf590b8_a8b1_4914_9b3e_415f2ac70c4d--------------)

[](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40dtunai%2Fmastering-git-worktrees-with-claude-code-for-parallel-development-workflow-41dc91e645fe&source=---author_recirc--41dc91e645fe----1-----------------explicit_signal----aaf590b8_a8b1_4914_9b3e_415f2ac70c4d--------------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fbc0825b6303b&operation=register&redirect=https%3A%2F%2Fitnext.io%2Fwriting-ai-agent-with-rust-from-scratch-deploying-to-edge-with-webassembly-os-week-1-bc0825b6303b&source=---author_recirc--41dc91e645fe----1-----------------bookmark_preview----aaf590b8_a8b1_4914_9b3e_415f2ac70c4d--------------)

![Image 14: Utilizing Airflow for Planning, Scheduling, Executing and Scaling AI Agentic Workloads](https://miro.medium.com/v2/resize:fit:679/format:webp/1*3X_mquSYRZBTxZ7bHDoItQ.jpeg)

[![Image 15: Dogukan Tuna](https://miro.medium.com/v2/resize:fill:20:20/1*jtH-z1jhchV1GI10iy4IzA.jpeg)](https://medium.com/@dtunai?source=post_page---author_recirc--41dc91e645fe----2---------------------aaf590b8_a8b1_4914_9b3e_415f2ac70c4d--------------)

[Dogukan Tuna

[Content truncated]
