# I Made Claude Code Think Before It Codes. Here's the Prompt.

**Type:** article
**URL:** https://dev.to/_vjk/i-made-claude-code-think-before-it-codes-heres-the-prompt-bf
**Topic:** Prompting Strategies
**Published:** unknown

## Content

# I Made Claude Code Think Before It Codes. Here's the Prompt. - DEV Community
[Skip to content](https://dev.to/_vjk/i-made-claude-code-think-before-it-codes-heres-the-prompt-bf#main-content)

[![Image 1: DEV Community](https://media2.dev.to/dynamic/image/quality=100/https://dev-to-uploads.s3.amazonaws.com/uploads/logos/resized_logo_UQww2soKuUsjaOGNB38o.png)](https://dev.to/)

[Powered by Algolia](https://www.algolia.com/developers/?utm_source=devto&utm_medium=referral)

[Log in](https://dev.to/enter?signup_subforem=1)[Create account](https://dev.to/enter?signup_subforem=1&state=new-user)

## DEV Community

![Image 2](https://assets.dev.to/assets/heart-plus-active-9ea3b22f2bc311281db911d416166c5f430636e76b15cd5df6b3b841d830eefa.svg)82 Add reaction 

![Image 3](https://assets.dev.to/assets/sparkle-heart-5f9bee3767e18deb1bb725290cb151c25234768a0e9a2bd39370c382d02920cf.svg)59 Like ![Image 4](https://assets.dev.to/assets/multi-unicorn-b44d6f8c23cdd00964192bedc38af3e82463978aa611b4365bd33a0f1f4f3e97.svg)5 Unicorn ![Image 5](https://assets.dev.to/assets/exploding-head-daceb38d627e6ae9b730f36a1e390fca556a4289d5a41abb2c35068ad3e2c4b5.svg)3 Exploding Head ![Image 6](https://assets.dev.to/assets/raised-hands-74b2099fd66a39f2d7eed9305ee0f4553df0eb7b4f11b01b6b1b499973048fe5.svg)10 Raised Hands ![Image 7](https://assets.dev.to/assets/fire-f60e7a582391810302117f987b22a8ef04a2fe0df7e3258a5f49332df1cec71e.svg)5 Fire 

14 Jump to Comments 21 Save  Boost 

Copy link

Copied to Clipboard

[Share to X](https://twitter.com/intent/tweet?text=%22I%20Made%20Claude%20Code%20Think%20Before%20It%20Codes.%20Here%27s%20the%20Prompt.%22%20by%20%40_vlad_ko%20%23DEVCommunity%20https%3A%2F%2Fdev.to%2F_vjk%2Fi-made-claude-code-think-before-it-codes-heres-the-prompt-bf)[Share to LinkedIn](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fdev.to%2F_vjk%2Fi-made-claude-code-think-before-it-codes-heres-the-prompt-bf&title=I%20Made%20Claude%20Code%20Think%20Before%20It%20Codes.%20Here%27s%20the%20Prompt.&summary=Claude%20Code%20is%20the%20fastest%20coder%20I%27ve%20ever%20worked%20with.%20It%20can%20scaffold%20a%20feature%2C%20write%20tests%2C%20and...&source=DEV%20Community)[Share to Facebook](https://www.facebook.com/sharer.php?u=https%3A%2F%2Fdev.to%2F_vjk%2Fi-made-claude-code-think-before-it-codes-heres-the-prompt-bf)[Share to Mastodon](https://s2f.kytta.dev/?text=https%3A%2F%2Fdev.to%2F_vjk%2Fi-made-claude-code-think-before-it-codes-heres-the-prompt-bf)

[Share Post via...](https://dev.to/_vjk/i-made-claude-code-think-before-it-codes-heres-the-prompt-bf#)[Report Abuse](https://dev.to/report-abuse)

[![Image 8: Cover image for I Made Claude Code Think Before It Codes. Here's the Prompt.](https://media2.dev.to/dynamic/image/width=1000,height=420,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fg7yz9ml71u14a3red18y.png)](https://media2.dev.to/dynamic/image/width=1000,height=420,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fg7yz9ml71u14a3red18y.png)

[![Image 9: _vjk profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F100128%2F6fbe85b3-c5e2-494b-a165-ea5eb819aecd.png)](https://dev.to/_vjk)

[v.j.k.](https://dev.to/_vjk)
Posted on Mar 10

![Image 10](https://assets.dev.to/assets/sparkle-heart-5f9bee3767e18deb1bb725290cb151c25234768a0e9a2bd39370c382d02920cf.svg)59![Image 11](https://assets.dev.to/assets/multi-unicorn-b44d6f8c23cdd00964192bedc38af3e82463978aa611b4365bd33a0f1f4f3e97.svg)5![Image 12](https://assets.dev.to/assets/exploding-head-daceb38d627e6ae9b730f36a1e390fca556a4289d5a41abb2c35068ad3e2c4b5.svg)3![Image 13](https://assets.dev.to/assets/raised-hands-74b2099fd66a39f2d7eed9305ee0f4553df0eb7b4f11b01b6b1b499973048fe5.svg)10![Image 14](https://assets.dev.to/assets/fire-f60e7a582391810302117f987b22a8ef04a2fe0df7e3258a5f49332df1cec71e.svg)5

# I Made Claude Code Think Before It Codes. Here's the Prompt.

[#claudecode](https://dev.to/t/claudecode)[#ai](https://dev.to/t/ai)[#tdd](https://dev.to/t/tdd)[#productivity](https://dev.to/t/productivity)

Claude Code is the fastest coder I've ever worked with. It can scaffold a feature, write tests, and open a PR in minutes. But I kept running into the same problem: the code _worked_, and then it _didn't_.

A race condition in a status transition. A hard-coded string that should have been a constant. A transaction that rolled back an audit record it was supposed to keep. Tests that asserted `true` instead of asserting the _right_ value.

The fixes were always fast too. But each fix came with a side quest: the incident, the regression, the "why didn't we catch this?" retro. The velocity was high. The _net_ velocity, after accounting for the bugs, wasn't.

And even with a decent `CLAUDE.md`, I was still babysitting every session. Please don't forget TDD this time. Hey, you forgot to check Bug Bot. Can you actually run the tests before opening the PR? Each prompt felt like a conversation with someone extremely talented who also had the short-term memory of a goldfish. The problem wasn't Claude's ability. It was that good habits written down somewhere in a markdown file don't automatically become _practiced_ habits. I was the process. Which meant the process was inconsistent, forgetful, and increasingly annoyed at itself.

So I tried something different. Instead of fixing Claude's output, I changed how Claude _thinks_.

## [](https://dev.to/_vjk/i-made-claude-code-think-before-it-codes-heres-the-prompt-bf#the-problem-isnt-intelligence-its-process) The problem isn't intelligence. It's process.

Watch a junior developer work: they read the ticket, open the file, start typing. They're fast. They're also the ones who forget to check if the method they're calling actually exists, or whether the database column they're referencing was renamed three weeks ago. (It was renamed three weeks ago. It's always three weeks ago.)

Now watch a senior developer: they read the ticket, read the code around it, read the tests, check the git history, _then_ start typing. They're slower to start but faster to finish, because they don't have to go back and fix what they broke.

Claude Code defaults to junior mode. Not because it lacks knowledge, but because it lacks _process_. It has no internal checklist telling it to verify assumptions, write tests first, or think about what happens when two requests hit the same endpoint at the same time. It's enthusiastic. It ships. And enthusiasm, it turns out, does not catch nullable datetime crashes.

I built that checklist.

## [](https://dev.to/_vjk/i-made-claude-code-think-before-it-codes-heres-the-prompt-bf#introducing-raw-wizard-endraw-) Introducing `/wizard`

`/wizard` is a Claude Code skill, a markdown file that lives in your project and activates when you type `/wizard` in the CLI. It transforms Claude from a fast coder into a methodical software architect. Think of it as the senior engineer looking over Claude's shoulder, except this one never asks if you've tried turning it off and on again.

It's an 8-phase methodology, and it works best with a few things already in place: a `CLAUDE.md` defining your project conventions, a GitHub issue created before work begins (`/wizard` can help you write one), a real commitment to TDD, and a clean feature branch per task. For CI, I use GitHub Actions, but the skill doesn't care. It just needs something to respond to in Phase 8. More on that shortly.

Here's how the 8 phases work.

### [](https://dev.to/_vjk/i-made-claude-code-think-before-it-codes-heres-the-prompt-bf#phase-1-plan-before-you-touch-anything) Phase 1: Plan before you touch anything

Claude reads your `CLAUDE.md`, finds the linked GitHub issue, and builds a structured todo list before a single line of code is written. It assesses complexity: how many files are likely affected, whether there's architectural impact, how much could go wrong. Then it sizes the work accordingly.

This sounds obvious. It is obvious. It's also the step that gets skipped most often when you're in a hurry, which is exactly when you need it most. Funny how that works.

### [](https://dev.to/_vjk/i-made-claude-code-think-before-it-codes-heres-the-prompt-bf#phase-2-explore-before-you-assume) Phase 2: Explore before you assume

With a plan in place, Claude explores the actual codebase. It greps for every model, method, relationship, and constant it intends to use and verifies they exist before referencing them in code.

Without this phase, Claude might confidently call `user.clientProfile.accounts`, a relationship chain it hallucinated with complete conviction. Phase 2 exists specifically to prevent that. This one change alone eliminated an entire class of bugs in my project. Turns out "does this actually exist" is a pretty good question to ask before you build on top of it.

### [](https://dev.to/_vjk/i-made-claude-code-think-before-it-codes-heres-the-prompt-bf#phase-3-write-the-tests-first) Phase 3: Write the tests first

Phase 3 enforces TDD. Claude writes failing tests, runs them (they must fail), implements the minimum code to make them pass, then verifies. In that order, every time, no shortcuts.

But here's the key part: it uses a **mutation testing mindset**. Instead of `assert($result)`, it writes `assertEquals('completed', $result->status)`. Instead of checking that a function runs without errors, it checks that _every_ side effect actually happened: the timestamp was set, the notification was sent, the counter was incremented.

The difference matters. `assert(true)` passes if the code does nothing. Mutation-resistant assertions catch real bugs. Your test suite should be a skeptic, not the friend who tells you your PR looks great without reading it.

### [](https://dev.to/_vjk/i-made-claude-code-think-before-it-codes-heres-the-prompt-bf#phase-4-implement-the-minimum) Phase 4: Implement the minimum

With failing tests in place, Claude writes the implementation. Not the full vision, not the clever abstraction it already has in mind, just the minimum code required to make the tests pass. Scope creep is a bug too, and it's the most expensive kind because it looks like progress.

### [](https://dev.to/_vjk/i-made-claude-code-think-before-it-codes-heres-the-prompt-bf#phase-5-verify-nothing-regressed) Phase 5: Verify nothing regressed

Phase 5 runs the broader test suite, not just the new tests. The goal is zero regressions. If something unrelated broke, better to find out now than in a PR review comment that says "uh, why is the billing module failing?"

### [](https://dev.to/_vjk/i-made-claude-code-think-before-it-codes-heres-the-prompt-bf#phase-6-document-while-the-context-is-fresh) Phase 6: Document while the context is fresh

Inline comments, changelog entries, anything that needs updating. Small step, easy to skip, always worth doing before the context evaporates. The next person reading this code might be you in three months, staring at it with absolutely no memory of why you made that decision.

### [](https://dev.to/_vjk/i-made-claude-code-think-before-it-codes-heres-the-prompt-bf#phase-7-the-adversarial-review) Phase 7: The adversarial review

This is where `/wizard` earns its keep. Before every commit, Claude reviews its own work not as the author, but as an attacker. The checklist:

*   What happens if this runs twice concurrently?
*   What if the input is null? Empty? Negative?
*   What assumptions am I making that could be wrong?
*   Would I be embarrassed if this broke in production?

This isn't theoretical. In my codebase, this phase caught:

*   A status transition service that lacked database locking. Two concurrent API calls could apply conflicting transitions. A race condition, just sitting there quietly, waiting for a bad day.
*   A Blade template calling `->format()` on a nullable datetime. A crash on any page load where the field was null. Completely silent until it wasn't.
*   Notification payloads using hard-coded category strings instead of the enum that was _literally created in the same PR_. Breathtaking, really.

None of these would have been caught by tests alone. They required thinking about the code in a different mode: as an attacker, not an author.

### [](https://dev.to/_vjk/i-made-claude-code-think-before-it-codes-heres-the-prompt-bf#phase-8-the-quality-gate-cycle) Phase 8: The quality gate cycle

Phase 8 handles the PR lifecycle. `/wizard` doesn't just open the PR and consider its job done. It monitors the automated review bot status (Bug Bot, CodeRabbit, whatever you have), reads every finding, fixes valid issues, replies to false positives, and repeats until the status is clean.

This is the phase I used to do manually and frequently forgot, leaving PRs sitting with unresolved bot findings for days. Now it's part of the process, which is exactly where it should have been all along.

## [](https://dev.to/_vjk/i-made-claude-code-think-before-it-codes-heres-the-prompt-bf#a-real-example) A real example

Here's what all 8 phases look like on a real task: implementing ACAT transfer status tracking with notifications.

**Phase 1**: Claude reads `CLAUDE.md`, finds the GitHub issue, assesses the task as "Complex" (7+ files, architectural impact), and builds a todo list.

**Phase 2**: Claude greps for the `AcatTransfer` model, verifies the `VALID_TRANSITIONS` constant exists, checks that `ClientProfile` has the right relationships, and confirms the `NotificationCategory` enum. No hallucinated method chains. No surprises.

**Phase 3**: Claude writes 23 failing tests covering status transitions, notifications, command behavior, and dashboard rendering. Runs them. All fail. Good. That's the point.

**Phase 4**: Claude implements the service, command, 5 notification classes, controller changes, and Blade template. Runs tests. All pass.

**Phase 5**: Runs the full related test suite (49 tests). Zero regressions.

**Phase 6**: Updates the changelog and adds inline comments to the transition service.

**Phase 7**: Adversarial review catches that `initiated_at->format()` could NPE if the field is null. Fixes it before it becomes a 2am incident.

**Phase 8**: Opens PR. Bug Bot finds 4 issues:

1.   Hard-coded category strings (should use enum): fixed
2.   Missing database locking on status transitions: fixed with `lockForUpdate()`
3.   Nullable `initiated_at` in Blade template: fixed with null-safe operator
4.   Wrong notification tone for completion events: fixed

After 3 fix cycles, Bug Bot returns `success`. PR ready.

**Total**: 49 tests, 108 assertions, 4 bugs caught before they shipped. Not bad for a checklist.

## [](https://dev.to/_vjk/i-made-claude-code-think-before-it-codes-heres-the-prompt-bf#how-to-install-it) How to install it

One command:

```
curl -sL https://raw.githubusercontent.com/vlad-ko/claude-wizard/main/install.sh | bash
```

This drops three files into `.claude/skills/wizard/`:

*   `SKILL.md`: The core 8-phase methodology
*   `CHECKLISTS.md`: Quick-reference checklists
*   `PATTERNS.md`: Common patterns and anti-patterns

Then type `/wizard` in Claude Code to activate it.

## [](https://dev.to/_vjk/i-made-claude-code-think-before-it-codes-heres-the-prompt-bf#making-it-yours) Making it yours

The skill is framework-agnostic by design. It doesn't know if you're writing Laravel, Rails, Next.js, or Rust. The methodology, plan, explore, test, implement, verify, document, review, ship, works everywhere.

But it gets _more_ powerful when you customize it. In my project, I added:

*   Laravel-specific test commands (`./vendor/bin/sail test`)
*   Our logging service patterns (`LoggingService::logPortfolioEvent()`)
*   Database locking conventions for our ORM
*   Bug Bot thread resolution commands (GraphQL mutations)
*   Alpine.js requirements for UI components

The more project-specific context you add, the less Claude has to guess. And the less Claude guesses, the fewer bugs slip through. Turns out those two things are related.

## [](https://dev.to/_vjk/i-made-claude-code-think-before-it-codes-heres-the-prompt-bf#what-its-not) What it's not

`/wizard` is not a replacement for code review. It's not a testing framework. It's not a CI pipeline.

It's a **process prompt**: a way to encode senior engineering habits into Claude's workflow so those habits happen consistently, on every task, even at 2am when you're tired and just want the feature to ship.

The prompt is roughly 500 lines of markdown. There's no magic. It's the same checklist a good tech lead would run through, made explicit and repeatable. The only surprising thing is that nobody bothered writing it down sooner.

## [](https://dev.to/_vjk/i-made-claude-code-think-before-it-codes-heres-the-prompt-bf#the-source) The source

The full skill is open-source at [github.com/vlad-ko/claude-wizard](https://github.com/vlad-ko/claude-wizard). MIT licensed. Fork it, customize it, make it better.

It came out of building [wealthbot.io](https://wealthbot.io/), a fintech platform where "it mostly works" is genuinely not a product strategy. The patterns were refined over hundreds of PRs and real production incidents. The framework-specific parts have been stripped, but the methodology is battle-tested.

If you try it, I'd love to hear what it catches for you.

[![Image 15: profile](https://media2.dev.to/dynamic/image/width=64,height=64,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Forganization%2Fprofile_image%2F6839%2F3d85988f-d18e-4522-b261-f86613cd9b50.png) Sonar](https://dev.to/sonar)Promoted

*   [What's a billboard?](https://dev.to/billboards)
*   [Manage preferences](https://dev.to/settings/customization#sponsors)

* * *

*   [Report billboard](https://dev.to/report-abuse?billboard=259979)

[![Image 16: State of Code Developer Survey report](https://media2.dev.to/dynamic/image/width=775%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fucarecdn.com%2F2f2ce9b0-68e0-48a1-bf3e-46c08831a9be%2F)](https://www.sonarsource.com/sem/the-state-of-code/developer-survey-report/?utm_medium=paid&utm_source=dev&utm_campaign=ss-state-of-code-developer-survey26&utm_content=report-devsurvey-banner-x-2&utm_term=ww-all-x&s_category=Paid&s_source=Paid+Social&s_origin=dev&bb=259979)

## [](https://dev.to/_vjk/i-made-claude-code-think-before-it-codes-heres-the-prompt-bf#state-of-code-developer-survey-report)[State of Code Developer Survey report](https://www.sonarsource.com/sem/the-state-of-code/developer-survey-report/?utm_medium=paid&utm_source=dev&utm_campaign=ss-state-of-code-developer-survey26&utm_content=report-devsurvey-banner-x-2&utm_term=ww-all-x&s_category=Paid&s_source=Paid+Social&s_origin=dev&bb=259979)

Did you know 96% of developers don't fully trust that AI-generated code is functionally correct, yet only 48% always check it before committing? Check out Sonar's new report on the real-world impact of AI on development teams.

[Read the results](https://www.sonarsource.com/sem/the-state-of-code/developer-survey-report/?utm_medium=paid&utm_source=dev&utm_campaign=ss-state-of-code-developer-survey26&utm_content=report-devsurvey-banner-x-2&utm_term=ww-all-x&s_category=Paid&s_source=Paid+Social&s_origin=dev&bb=259979)

 Read More 

## Top comments (14)

Subscribe

![Image 17: pic](https://media2.dev.to/dynamic/image/width=256,height=,fit=scale-down,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F8j7kvp660rqzt99zui8e.png)

Personal Trusted User[Create template](https://dev.to/settings/response-templates)
Templates let you quickly answer FAQs or store snippets for re-use.

Submit Preview[Dismiss](https://dev.to/404.html)

[](https://dev.to/_vjk/i-made-claude-code-think-before-it-codes-heres-the-prompt-bf)

[![Image 18: crapkit profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F111099%2Fd1ca5317-eb52-4abe-a801-02bfbf1a72b8.jpeg)](https://dev.to/crapkit)

[Patrick Nemenz](https://dev.to/crapkit)

 Patrick Nemenz 

[![Image 19](https://media2.dev.to/dynamic/image/width=90,height=90,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F111099%2Fd1ca5317-eb52-4abe-a801-02bfbf1a72b8.jpeg) Patrick Nemenz](https://dev.to/crapkit)

Follow

*    Location   Vienna, Austria  
*    Joined  Oct 30, 2018 

•[Mar 12](https://dev.to/_vjk/i-made-claude-code-think-before-it-codes-heres-the-prompt-bf#comment-35f26)

*   [Copy link](https://dev.to/_vjk/i-made-claude-code-think-before-it-codes-heres-the-prompt-bf#comment-35f26)

*    Hide 

*   [Report abuse](https://dev.to/report-abuse?url=https://dev.to/crapkit/comment/35f26)

I think that plan is solid in itself and tries to enforce some very important software engineering and QA practices.

That said, the assumption that you can _make Claude think something in particular_ or assume a software architect role -- hell, that any LLM can think _at all_ -- is misguided. Instead you're just trying to offset statistics in your favour. Statistics-based output will still bullshit you now and then, and you still won't know whether it does, or not. (I see you trying _very hard_ to, with all that reference output for human oversight, but still: LLM slop remains, no matter how hard you push.)

I will still try (and perhaps keep) using this as part of my ever-growing push for quality.

 My point is that caution should go up, not down, with increasingly sophisticated and convincing output.

2 likes Like Reply

[](https://dev.to/_vjk/i-made-claude-code-think-before-it-codes-heres-the-prompt-bf)

[![Image 20: _vjk profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F100128%2F6fbe85b3-c5e2-494b-a165-ea5eb819aecd.png)](https://dev.to/_vjk)

[v.j.k.](https://dev.to/_vjk)

 v.j.k. 

[![Image 21](https://media2.dev.to/dynamic/image/width=90,height=90,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F100128%2F6fbe85b3-c5e2-494b-a165-ea5eb819aecd.png) v.j.k.](https://dev.to/_vjk)

Follow

*    Location   Miami, FL  
*    Joined  Sep 10, 2018 

•[Mar 13](https://dev.to/_vjk/i-made-claude-code-think-before-it-codes-heres-the-prompt-bf#comment-35ggo)

*   [Copy link](https://dev.to/_vjk/i-made-claude-code-think-before-it-codes-heres-the-prompt-bf#comment-35ggo)

*    Hide 

*   [Report abuse](https://dev.to/report-abuse?url=https://dev.to/_vjk/comment/35ggo)

It’s not a bulletproof solution to let AI build things for you. These are simply guardrails, grounded in old school, battle tested software architecture and development principles that guide the AI in the right direction.

Sure, I dress it up with a bit of marketing flair, otherwise where’s the fun. But details aside, it works far better than raw prompt slinging. The goal is simple, make your life easier while still respecting the fundamentals of good software engineering.

 Like Reply

[](https://dev.to/_vjk/i-made-claude-code-think-before-it-codes-heres-the-prompt-bf)

[![Image 22: alpha_compadre profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F3823338%2F20d6f8b5-b069-4f61-9194-e6b4d8195a6c.png)](https://dev.to/alpha_compadre)

[Alpha Compadre](https://dev.to/alpha_compadre)

 Alpha Compadre 

[![Image 23](https://media2.dev.to/dynamic/image/width=90,height=90,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F3823338%2F20d6f8b5-b069-4f61-9194-e6b4d8195a6c.png) Alpha Compadre](https://dev.to/alpha_compadre)

Follow

 Building Drafted — AI email drafts that sound like you. Privacy-first, runs locally, never auto-sends. One-time purchase, not a subscription. 

*    Joined  Mar 14, 2026 

•[Mar 14](https://dev.to/_vjk/i-made-claude-code-think-before-it-codes-heres-the-prompt-bf#comment-35i1o)

*   [Copy link](https://dev.to/_vjk/i-made-claude-code-think-before-it-codes-heres-the-prompt-bf#comment-35i1o)

*    Hide 

*   [Report abuse](https://dev.to/report-abuse?url=https://dev.to/alpha_compadre/comment/35i1o)

The "process over intelligence" framing is exactly right. I've been applying the same thinking to AI outside of coding — specifically to email communication.

Most AI email tools operate in what you'd call "junior mode": they see an email, they generate a reply, they fire. Fast, enthusiastic, and occasionally catastrophic (wrong tone to a client, missing context on a sensitive thread, confidently replying to something that needed a human pause).

Your 8-phase approach maps surprisingly well to non-coding AI workflows. For email, the equivalent looks something like:

1.   READ — Understand the full thread context, not just the latest message
2.   EXPLORE — Check who's on the thread, what the relationship history is
3.   ASSESS — Rate confidence (is this a routine reply or a landmine?)
4.   DRAFT — Generate a response based on all that context
5.   VERIFY — Human reviews before anything gets sent

I'm building a Mac app (Drafted) that follows this exact philosophy. It reads your Gmail inbox, assesses confidence on each email (High/Medium/Low), and pre-drafts replies — but crucially, it never sends anything. You always review, edit, and hit send yourself.

The parallel to your CLAUDE.md approach: just like you encode process into the prompt so Claude doesn't skip steps, we encode process into the tool so the AI doesn't skip the "should a human look at this first?" step. The answer is always yes.

Curious if you've thought about applying the /wizard methodology beyond code — documentation, communication, operational workflows? The "think before you act" principle feels universally applicable.

2 likes Like Reply

[](https://dev.to/_vjk/i-made-claude-code-think-before-it-codes-heres-the-prompt-bf)

[![Image 24: _vjk profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F100128%2F6fbe85b3-c5e2-494b-a165-ea5eb819aecd.png)](https://dev.to/_vjk)

[v.j.k.](https://dev.to/_vjk)

 v.j.k. 

[![Image 25](https://media2.dev.to/dynamic/image/width=90,height=90,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F100128%2F6fbe85b3-c5e2-494b-a165-ea5eb819aecd.png) v.j.k.](https://dev.to/_vjk)

Follow

*    Location   Miami, FL  
*    Joined  Sep 10, 2018 

•[Mar 30](https://dev.to/_vjk/i-made-claude-code-think-before-it-codes-heres-the-prompt-bf#comment-3679k)

*   [Copy link](https://dev.to/_vjk/i-made-claude-code-think-before-it-codes-heres-the-prompt-bf#comment-3679k)

*    Hide 

*   [Report abuse](https://dev.to/report-abuse?url=https://dev.to/_vjk/comment/3679k)

Thanks for the kind words, and Drafted sounds like a genuinely thoughtful take on AI-assisted communication. The confidence-scoring layer is smart -- a lot of tools skip straight to drafting without asking whether this is even the kind of email that should be auto-drafted at all.

Funny you asked about applying the methodology beyond code -- I shipped something yesterday that does exactly that. Battle Mage is a Slack agent powered by Claude that answers questions about a GitHub codebase when you @mention it. It reads your repo in real time, follows up in threads, and even lets you correct it so it builds a shared knowledge base over time. For me it started as a way to help new users onboard to a product without drowning a small team in repetitive questions -- same "think before you act" principle, different domain.

Repo is here if you want to take a look: [github.com/vlad-ko/battle-mage](https://github.com/vlad-ko/battle-mage)

Still needs some polishing, but I plan on announcing it to the world shortly.

p. s. I've got a whole magical AI army all of a sudden 😆 it's lore I can enjoy.

1 like Like Reply

[](https://dev.to/_vjk/i-made-claude-code-think-before-it-codes-heres-the-prompt-bf)

[![Image 26: mattbuscher profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F3858526%2F1305ceba-22fc-43f0-b8f4-813eeda077ee.png)](https://dev.to/mattbuscher)

[Matt Buscher](https://dev.to/mattbuscher)

 Matt Buscher 

[![Image 27](https://media2.dev.to/dynamic/image/width=90,height=90,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F3858526%2F1305ceba-22fc-43f0-b8f4-813eeda077ee.png) Matt Buscher](https://dev.to/mattbuscher)

Follow

 40+ years in engineering & executive management. Now teaching AI how to be managed. Creator of PromptPack. Writing about AI workflows and project structure. 

*    Email  [matt@aipromptpacks.io](mailto:matt@aipromptpacks.io) 
*    Location   United States  
*    Joined  Apr 3, 2026 

•[Apr 4](https://dev.to/_vjk/i-made-claude-code-think-before-it-codes-heres-the-prompt-bf#comment-36cd2)

*   [Copy link](https://dev.to/_vjk/i-made-claude-code-think-before-it-codes-heres-the-prompt-bf#comment-36cd2)

*    Hide 

*   [Report abuse](https://dev.to/report-abuse?url=https://dev.to/mattbuscher/comment/36cd2)

This is the right instinct — getting Claude to plan before executing is huge.

I'd push it one step further: externalize the plan into a file, not just the prompt. When the plan lives in chat, it dies with the session. When it lives in a markdown file (like execution/tasks.md), any future session can pick it up and continue.

Same goes for decisions and constraints. The golden rule I follow: if it matters, move it from chat into markdown. Chat is for thinking. Files are for preserving.

Solves the "I have to re-explain everything every session" problem completely.

2 likes Like Reply

[](https://dev.to/_vjk/i-made-claude-code-think-before-it-codes-heres-the-prompt-bf)

[![Image 28: _vjk profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F100128%2F6fbe85b3-c5e2-494b-a165-ea5eb819aecd.png)](https://dev.to/_vjk)

[v.j.k.](https://dev.to/_vjk)

 v.j.k. 

[![Image 29](https://media2.dev.to/dynamic/image/width=90,height=90,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F100128%2F6fbe85b3-c5e2-494b-a165-ea5eb819aecd.png) v.j.k.](https://dev.to/_vjk)

Follow

*    Location   Miami, FL  
*    Joined  Sep 10, 2018 

•[Apr 8](https://dev.to/_vjk/i-made-claude-code-think-before-it-codes-heres-the-prompt-bf#comment-36hmj)

*   [Copy link](https://dev.to/_vjk/i-made-claude-code-think-before-it-codes-heres-the-prompt-bf#comment-36hmj)

*    Hide 

*   [Report abuse](https://dev.to/report-abuse?url=https://dev.to/_vjk/comment/36hmj)

Indeed. My prompts went from long winded essays begging it not to forget TDD or this or that. To "work on 1234, follow our dev cycle until the PR is ready to merge" ...

1 like Like Reply

[](https://dev.to/_vjk/i-made-claude-code-think-before-it-codes-heres-the-prompt-bf)

[![Image 30: dale21certs profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F3825908%2F00436e10-ac95-4be0-ba25-59ed22fa2bb6.png)](https://dev.to/dale21certs)

[Larry Barrow](https://dev.to/dale21certs)

 Larry Barrow 

[!

[Content truncated]
