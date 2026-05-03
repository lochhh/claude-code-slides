# Claude Code Hooks: Automation and Customization of Development Workflows : AntonioCortes.com

**Type:** article
**URL:** https://antoniocortes.com/en/post/2025/claude_code_hooks_automatizacion_01_julio_2025/
**Topic:** Hooks
**Published:** unknown

## Content

[DrZippie](/drzippie/) [Blog](/post/) [Portfolio](/portfolio/) [Etiquetas](/tags/) [Categorías](/categories/)

ES [EN](/en/)

### Últimas Entradas

[![Auto Memory y Auto Dream: como Claude Code aprende y consolida su memoria](/uploads/claude-code-auto-dream_hu_24c92ba809be202.jpg)

#### Auto Memory y Auto Dream: como Claude Code aprende y consolida su memoria

• Inteligencia Artificial](/2026/03/30/auto-memory-y-auto-dream-como-claude-code-aprende-y-consolida-su-memoria/)

[![Claude Code con LSP: de buscar texto a entender codigo](/uploads/claude-code-lsp_hu_12ebc12b0a07f5ee.jpg)

#### Claude Code con LSP: de buscar texto a entender codigo

• Inteligencia Artificial](/2026/03/10/claude-code-con-lsp-de-buscar-texto-a-entender-codigo/)

[![Ghost Jobs: la economía construida sobre empleos que no existen](/uploads/ghost-jobs_hu_3a11f9a6254eaac6.jpg)

#### Ghost Jobs: la economía construida sobre empleos que no existen

• Reflexiones](/2026/03/10/ghost-jobs-la-econom%C3%ADa-construida-sobre-empleos-que-no-existen/)

[![DuckDB y httpfs detrás de un proxy: el secreto que nadie te cuenta](/uploads/duckdb-httpfs-proxy_hu_a6f216bec02f2893.jpg)

#### DuckDB y httpfs detrás de un proxy: el secreto que nadie te cuenta

• Bases de Datos](/2026/03/02/duckdb-y-httpfs-detr%C3%A1s-de-un-proxy-el-secreto-que-nadie-te-cuenta/)

[![Cómo PostgreSQL estima tus consultas (y por qué a veces se equivoca)](/uploads/postgresql-statistics_hu_f137102e88bfe995.jpg)

#### Cómo PostgreSQL estima tus consultas (y por qué a veces se equivoca)

• Bases de Datos](/postgresql-statistics/)

[![Analizando el aislamiento de filesystems en contenedores para cargas multi-tenant](/uploads/container-filesystem-isolation-security_hu_ec6c32714c5f2aec.jpg)

#### Analizando el aislamiento de filesystems en contenedores para cargas multi-tenant

• DevOps](/aislamiento-filesystem-contenedores-multitenencia/)

[Ver todos los artículos](/post/)

# Claude Code Hooks: Automation and Customization of Development Workflows

With the constant evolution of AI-powered development tools, **Claude Code** has introduced a revolutionary feature: **Hooks**. This feature allows developers to customize and automate specific behaviors in the Claude Code lifecycle, transforming suggestions into executable code that works deterministically.

Hooks represent a qualitative leap in the customization of AI development tools, allowing each team and developer to adapt Claude Code to their specific needs and project standards.

## What are Claude Code Hooks?

**Claude Code Hooks** are user-defined shell commands that execute automatically at various specific points in the Claude Code lifecycle. Unlike prompting instructions, hooks guarantee that certain actions **always** occur, providing deterministic control over the tool’s behavior.

### The Problem They Solve

Traditionally, customizing AI tool behavior required:

* **Repetitive instructions** in every conversation
* **Dependence on the LLM** to remember and execute specific actions
* **Inconsistencies** in code standard application
* **Manual processes** for formatting, validation, and logging

Hooks eliminate these limitations by **encoding rules as applications** that execute automatically.

## Transformative Use Cases

### 1. **Automatic Code Formatting**

```
# Hook that automatically formats TypeScript files # Hook that automatically formats TypeScript files # Hook that automatically formats TypeScript fileshook_command="if [[ \$file_path =~ \.ts$ ]]; then prettier --write \$file_path; fi" hook_command="if [[ \$file_path =~ \.ts$ ]]; then prettier --write \$file_path; fi" hook_command ="if [[ \$file_path =~ \.ts ]]; then prettier --write \$file_path; fi"
```

### 2. **Custom Notifications**

```
# Slack notification when Claude requests permissions # Slack notification when Claude requests permissions # Slack notification when Claude requests permissionshook_command="curl -X POST \$SLACK_WEBHOOK -d '{\"text\":\"Claude Code needs your attention\"}'" hook_command="curl -X POST \$SLACK_WEBHOOK -d '{\"text\":\"Claude Code needs your attention\"}'" hook_command ="curl -X POST \$SLACK_WEBHOOK -d '{\"text\":\"Claude Code needs your attention\"}'"
```

### 3. **Logging and Compliance**

```
# Log all executed commands for auditing # Log all executed commands for auditing # Log all executed commands for auditinghook_command="echo \$(date): \$command >> ~/.claude/audit.log" hook_command="echo \$(date): \$command >> ~/.claude/audit.log" hook_command ="echo \$(date): \$command >> ~/.claude/audit.log"
```

### 4. **Convention Validation**

```
# Verify commits follow team standards # Verify commits follow team standards # Verify commits follow team standardshook_command="./scripts/validate-commit-message.sh \$commit_message" hook_command="./scripts/validate-commit-message.sh \$commit_message" hook_command ="./scripts/validate-commit-message.sh \$commit_message"
```

### 5. **Custom Permissions**

```
# Block modifications to production files # Block modifications to production files # Block modifications to production fileshook_command="if [[ \$file_path =~ ^production/ ]]; then exit 2; fi" hook_command="if [[ \$file_path =~ ^production/ ]]; then exit 2; fi" hook_command ="if [[ \$file_path =~ ^production/ ]]; then exit 2; fi"
```

## Step-by-Step Configuration

### Basic Configuration: Logging Hook

Let’s create our first hook that logs all bash commands executed by Claude Code.

#### Step 1: Open Hooks Configuration

```
# In Claude Code, run the slash command # In Claude Code, run the slash command # In Claude Code, run the slash command/hooks /hooks 
```

Select the `PreToolUse` event to intercept commands before execution.

#### Step 2: Add Matcher

```
Matcher: Bash 
```

This makes the hook only execute for shell commands.

#### Step 3: Configure the Hook

```
# Command that logs execution # Command that logs execution # Command that logs executionecho "$(date): Command executed by Claude Code" >> ~/.claude/command_log.txt echo "$(date): Command executed by Claude Code" >> ~/.claude/command_log.txt echo "$(): Command executed by Claude Code"
```

#### Step 4: Save Configuration

Select `User settings` to apply the hook to all projects.

### Advanced Configuration: Automatic Formatting

```
{ { { "hooks": {  "hooks": { "hooks":{ "PostToolUse": [  "PostToolUse": [ "PostToolUse":[ {  { { "matcher": "Edit|Write",  "matcher": "Edit|Write", "matcher": "Edit|Write", "hooks": [  "hooks": [ "hooks":[ {  { { "type": "command",  "type": "command", "type": "command", "command": "if [[ \"$file_path\" =~ \\.(js|ts|jsx|tsx)$ ]]; then prettier --write \"$file_path\"; fi"  "command": "if [[ \"$file_path\" =~ \\.(js|ts|jsx|tsx)$ ]]; then prettier --write \"$file_path\"; fi" "command":"if [[ \"$file_path\" =~ \\.(js|ts|jsx|tsx)$ ]]; then prettier --write \"$file_path\"; fi" },  }, }, {  { { "type": "command",  "type": "command", "type": "command", "command": "if [[ \"$file_path\" =~ \\.go$ ]]; then gofmt -w \"$file_path\"; fi"  "command": "if [[ \"$file_path\" =~ \\.go$ ]]; then gofmt -w \"$file_path\"; fi" "command":"if [[ \"$file_path\" =~ \\.go$ ]]; then gofmt -w \"$file_path\"; fi" },  }, }, {  { { "type": "command",  "type": "command", "type": "command", "command": "if [[ \"$file_path\" =~ \\.py$ ]]; then black \"$file_path\"; fi"  "command": "if [[ \"$file_path\" =~ \\.py$ ]]; then black \"$file_path\"; fi" "command":"if [[ \"$file_path\" =~ \\.py$ ]]; then black \"$file_path\"; fi" }  } } ]  ] ] }  } } ]  ] ] }  } }} } }
```

## Types of Hook Events

### 1. **PreToolUse**

Executes **before** Claude processes a tool.

**Use cases:**

* Permission validation
* Pre-condition verification
* Blocking dangerous operations

```
# Example: Block edits to critical files # Example: Block edits to critical files # Example: Block edits to critical filesif [[ "$file_path" =~ (package\.json|\.env) ]]; then if [[ "$file_path" =~ (package\.json|\.env) ]]; then if[[" $file_path " =(\. |\.)]]; then echo "Error: Critical file protected" >&2  echo "Error: Critical file protected" >&2 echo"Error: Critical file protected" & 2  exit 2 # Block the operation  exit 2 # Block the operation exit 2 # Block the operation fi fi fi
```

### 2. **PostToolUse**

Executes **after** a tool completes successfully.

**Use cases:**

* Automatic formatting
* Post-processing validation
* Change notifications

```
# Example: Run tests after code changes # Example: Run tests after code changes # Example: Run tests after code changesif [[ "$file_path" =~ \.test\.(js|ts)$ ]]; then if [[ "$file_path" =~ \.test\.(js|ts)$ ]]; then if[[" $file_path " =\.\.(|)]]; then  npm test "$file_path"  npm test "$file_path" test " $file_path " fi fi fi
```

### 3. **Notification**

Executes when Claude Code sends notifications.

**Use cases:**

* Custom notifications
* Integration with external systems
* Multi-channel alerts

```
# Example: Discord notification # Example: Discord notification # Example: Discord notificationcurl -H "Content-Type: application/json" \ curl -H "Content-Type: application/json" \ "Content-Type: application/json" \  -d '{"content":"Claude Code requires attention"}' \  -d '{"content":"Claude Code requires attention"}' \ '{"content":"Claude Code requires attention"}' \  "$DISCORD_WEBHOOK"  "$DISCORD_WEBHOOK" " $DISCORD_WEBHOOK "
```

### 4. **Stop**

Executes when Claude Code finishes responding.

**Use cases:**

* Execute post-processing scripts
* Generate session reports
* Clean temporary files

```
# Example: Generate changes report # Example: Generate changes report # Example: Generate changes reportgit diff --stat > session_changes.txt git diff --stat > session_changes.txt 
```

## Input Data Structure

Hooks receive contextual information via JSON in stdin:

### PreToolUse Input

```
{ { { "event": "PreToolUse",  "event": "PreToolUse", "event": "PreToolUse", "session_id": "session_123",  "session_id": "session_123", "session_id": "session_123", "tool_name": "Edit",  "tool_name": "Edit", "tool_name": "Edit", "tool_input": {  "tool_input": { "tool_input":{ "file_path": "src/component.tsx",  "file_path": "src/component.tsx", "file_path":"src/component.tsx", "content": "// New content...",  "content": "// New content...", "content":"// New content...", "start_line": 1,  "start_line": 1, "start_line": 1, "end_line": 10  "end_line": 10 "end_line": 10 }  } }} } }
```

### PostToolUse Input

```
{ { { "event": "PostToolUse",  "event": "PostToolUse", "event": "PostToolUse", "session_id": "session_123",  "session_id": "session_123", "session_id": "session_123", "tool_name": "Bash",  "tool_name": "Bash", "tool_name": "Bash", "tool_input": {  "tool_input": { "tool_input":{ "command": "npm test"  "command": "npm test" "command": "npm test" },  }, }, "tool_response": {  "tool_response": { "tool_response":{ "exit_code": 0,  "exit_code": 0, "exit_code": 0, "stdout": "Tests passed",  "stdout": "Tests passed", "stdout": "Tests passed", "stderr": ""  "stderr": "" "stderr": "" }  } }} } }
```

## Advanced Hook Examples

### Code Validation System

```
#!/bin/bash #!/bin/bash #!/bin/bash # validate_code.sh - Comprehensive validation hook # validate_code.sh - Comprehensive validation hook # validate_code.sh - Comprehensive validation hook   # Read input JSON # Read input JSON # Read input JSONinput=$(cat) input=$(cat) input =$()file_path=$(echo "$input" | jq -r '.tool_input.file_path // empty') file_path=$(echo "$input" | jq -r '.tool_input.file_path // empty') file_path =$(echo " $input " |'.tool_input.file_path // empty')tool_name=$(echo "$input" | jq -r '.tool_name') tool_name=$(echo "$input" | jq -r '.tool_name') tool_name =$(echo " $input " |'.tool_name')   # Only process file operations # Only process file operations # Only process file operationsif [[ "$tool_name" != "Edit" && "$tool_name" != "Write" ]]; then if [[ "$tool_name" != "Edit" && "$tool_name" != "Write" ]]; then if[[" $tool_name " = "Edit" && " $tool_name " = "Write"]]; then  exit 0  exit 0 exit 0 fi fi fi   # Specific validations by file type # Specific validations by file type # Specific validations by file type case "$file_path" in case "$file_path" in case " $file_path " *.js|*.ts|*.jsx|*.tsx)  *.js|*.ts|*.jsx|*.tsx) | | |) # Validate JavaScript/TypeScript syntax  # Validate JavaScript/TypeScript syntax # Validate JavaScript/TypeScript syntax if ! npx tsc --noEmit "$file_path" 2>/dev/null; then  if ! npx tsc --noEmit "$file_path" 2>/dev/null; then if " $file_path "; then echo "Error: Invalid TypeScript code" >&2  echo "Error: Invalid TypeScript code" >&2 echo"Error: Invalid TypeScript code" & 2  exit 2  exit 2 exit 2  fi  fi fi    # Run ESLint  # Run ESLint # Run ESLint if ! npx eslint "$file_path" --fix; then  if ! npx eslint "$file_path" --fix; then if " $file_path "; then echo "Warning: Linting problems detected" >&2  echo "Warning: Linting problems detected" >&2 echo"Warning: Linting problems detected" & 2  fi  fi fi ;;  ;; ;;    *.py)  *.py) )  # Validate Python syntax  # Validate Python syntax # Validate Python syntax if ! python -m py_compile "$file_path"; then  if ! python -m py_compile "$file_path"; then if " $file_path "; then echo "Error: Invalid Python syntax" >&2  echo "Error: Invalid Python syntax" >&2 echo"Error: Invalid Python syntax" & 2  exit 2  exit 2 exit 2  fi  fi fi    # Format with black  # Format with black # Format with black  black "$file_path"  black "$file_path" " $file_path " ;;  ;; ;;    *.go)  *.go) )  # Validate Go syntax  # Validate Go syntax # Validate Go syntax if ! go fmt -e "$file_path"; then  if ! go fmt -e "$file_path"; then if " $file_path "; then echo "Error: Invalid Go syntax" >&2  echo "Error: Invalid Go syntax" >&2 echo"Error: Invalid Go syntax" & 2  exit 2  exit 2 exit 2  fi  fi fi    # Run go vet  # Run go vet # Run go vet  go vet "$file_path"  go vet "$file_path" " $file_path " ;;  ;; ;; esac esac esac   echo "Validation completed for $file_path" echo "Validation completed for $file_path" echo "Validation completed for $file_path "
```

## Security Best Practices

### ⚠️ Critical Considerations

Hooks execute commands with **full user permissions** without confirmation. This requires strict precautions:

#### 1. **Input Validation and Sanitization**

```
#!/bin/bash #!/bin/bash #!/bin/bash # secure_hook_template.sh # secure_hook_template.sh # secure_hook_template.sh   # Function to sanitize inputs # Function to sanitize inputs # Function to sanitize inputssanitize_input() { sanitize_input() { (){ local input="$1"  local input="$1" local input = " $1 "  # Remove dangerous characters  # Remove dangerous characters # Remove dangerous characters echo "$input" | sed 's/[;&|`$(){}[\]\\]//g'  echo "$input" | sed 's/[;&|`$(){}[\]\\]//g' echo " $input " |'s/[;&|`$(){}[\]\\]//g'} } }   # Function to validate paths # Function to validate paths # Function to validate pathsvalidate_path() { validate_path() { (){ local path="$1"  local path="$1" local path = " $1 "    # Block path traversal  # Block path traversal # Block path traversal if [[ "$path" == *".."* ]]; then  if [[ "$path" == *".."* ]]; then if[[" $path " ==".."]]; then echo "Error: Path traversal detected" >&2  echo "Error: Path traversal detected" >&2 echo"Error: Path traversal detected" & 2  exit 1  exit 1 exit 1  fi  fi fi    # Ensure path is within project  # Ensure path is within project # Ensure path is within project if [[ ! "$path" =~ ^[./] ]]; then  if [[ ! "$path" =~ ^[./] ]]; then if[[" $path " =[]]]; then echo "Error: Path outside project" >&2  echo "Error: Path outside project" >&2 echo"Error: Path outside project" & 2  exit 1  exit 1 exit 1  fi  fi fi} } }   # Read and validate input # Read and validate input # Read and validate inputinput=$(cat) input=$(cat) input =$()file_path=$(echo "$input" | jq -r '.tool_input.file_path // empty') file_path=$(echo "$input" | jq -r '.tool_input.file_path // empty') file_path =$(echo " $input " |'.tool_input.file_path // empty')   if [[ -n "$file_path" ]]; then if [[ -n "$file_path" ]]; then if[[" $file_path "]]; then  validate_path "$file_path"  validate_path "$file_path" " $file_path " file_path=$(sanitize_input "$file_path")  file_path=$(sanitize_input "$file_path") file_path =$(" $file_path ") fi fi fi
```

#### 2. **Safe Use of Variables**

```
# ❌ INCORRECT - Vulnerable to injection # ❌ INCORRECT - Vulnerable to injection # ❌ INCORRECT - Vulnerable to injectioncommand="ls $user_input" command="ls $user_input" command = "ls $user_input "   # ✅ CORRECT - Properly quoted variables # ✅ CORRECT - Properly quoted variables # ✅ CORRECT - Properly quoted variablescommand="ls \"$user_input\"" command="ls \"$user_input\"" command = "ls \" $user_input \""   # ✅ SAFER - Prior validation # ✅ SAFER - Prior validation # ✅ SAFER - Prior validationif [[ "$user_input" =~ ^[a-zA-Z0-9._/-]+$ ]]; then if [[ "$user_input" =~ ^[a-zA-Z0-9._/-]+$ ]]; then if[[" $user_input " =[]]]; then command="ls \"$user_input\""  command="ls \"$user_input\"" command = "ls \" $user_input \"" else else else echo "Invalid input" >&2  echo "Invalid input" >&2 echo "Invalid input" & 2  exit 1  exit 1 exit 1 fi fi fi
```

## Conclusion: Transforming Development with AI

Claude Code Hooks represent a fundamental paradigm in how AI tools integrate into real development workflows. By enabling **deterministic automation** and **granular customization**, they transform Claude Code from an assistance tool to an **extensible development platform**.

**Key benefits:**

* ✅ **Guaranteed consistency** in code standards
* ✅ **Automation of repetitive tasks**
* ✅ **Deep integration** with existing tools
* ✅ **Granular control** over AI behaviors
* ✅ **Enterprise scalability** with centralized policies

**To get started:**

1. Identify repetitive manual processes in your workflow
2. Implement simple hooks (logging, formatting)
3. Gradually add more sophisticated validations and controls
4. Share successful configurations with your team

Hooks not only improve individual productivity, but allow teams to encode their collective knowledge in automations that benefit the entire organization.

The future of software development lies in tools that not only assist, but adapt and evolve with the specific needs of each project and team. Claude Code Hooks marks the path toward that reality.

---

**Useful links:**

* [Official Hooks Documentation](https://docs.anthropic.com/en/docs/claude-code/hooks)
* [Claude Code Documentation](https://docs.anthropic.com/en/docs/claude-code)
* [Model Context Protocol](https://docs.anthropic.com/en/docs/claude-code/mcp)

**Tags:** #ClaudeCode #Hooks #AI #Automation #DevOps #Workflow #Development #Productivity
