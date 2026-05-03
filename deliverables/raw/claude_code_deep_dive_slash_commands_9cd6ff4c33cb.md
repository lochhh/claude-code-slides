# This is the second article in the CCDD (Claude Code Deep Dive) series.

**Type:** article
**URL:** https://medium.com/@the.gigi/claude-code-deep-dive-slash-commands-9cd6ff4c33cb
**Topic:** Slash Commands & Skills
**Published:** unknown

## Content

# Claude Code Deep Dive - Slash Commands | by Gigi Sayfan | Medium

[Sitemap](https://medium.com/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fmedium.com%2F%40the.gigi%2Fclaude-code-deep-dive-slash-commands-9cd6ff4c33cb&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

Get app

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fmedium.com%2F%40the.gigi%2Fclaude-code-deep-dive-slash-commands-9cd6ff4c33cb&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![Image 1](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

Member-only story

[![Image 2: Gigi Sayfan](https://miro.medium.com/v2/resize:fill:64:64/0*3m2lzp7-O-yNYycQ.)](https://medium.com/@the.gigi?source=post_page---byline--9cd6ff4c33cb---------------------------------------)

[Gigi Sayfan](https://medium.com/@the.gigi?source=post_page---byline--9cd6ff4c33cb---------------------------------------)

Follow

6 min read

·

Jan 12, 2026

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fp%2F9cd6ff4c33cb&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40the.gigi%2Fclaude-code-deep-dive-slash-commands-9cd6ff4c33cb&user=Gigi+Sayfan&userId=beb8ed7bf2e5&source=---header_actions--9cd6ff4c33cb---------------------clap_footer------------------)

5

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F9cd6ff4c33cb&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40the.gigi%2Fclaude-code-deep-dive-slash-commands-9cd6ff4c33cb&source=---header_actions--9cd6ff4c33cb---------------------bookmark_footer------------------)

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3D9cd6ff4c33cb&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40the.gigi%2Fclaude-code-deep-dive-slash-commands-9cd6ff4c33cb&source=---header_actions--9cd6ff4c33cb---------------------post_audio_button------------------)

Share

This is the second article in the _CCDD_ (Claude Code Deep Dive) series. If you haven’t read the first one, check out [Claude Code Deep Dive - Basics](https://medium.com/@the.gigi/claude-code-deep-dive-basics-ca4a48003b02) where I covered getting started, permissions, sessions and running Claude Code in the terminal and IDE.

Today we’re diving into slash commands. We’ll cover both the built-in ones and how to create your own custom commands.

**“Automation is not about replacing humans, it’s about amplifying them.” ~ Satya Nadella**

_If you’re not a member read this story for free on_[_The Gigi Zone_](https://the-gigi.github.io/gigi-zone/posts/2026/01/cc-deep-dive-02-slash-commands/)_._

Press enter or click to view image in full size

![Image 3](https://miro.medium.com/v2/resize:fit:700/0*3-E1Bu4Y7yzHPXHF.png)

### ⌨️ Built-in Slash Commands ⌨️

Claude Code has a ton of useful slash commands. Just type `/` and start scrolling.

Press enter or click to view image in full size

![Image 4](https://miro.medium.com/v2/resize:fit:700/0*vNBEfS19A48w-sk4.png)

I’ll cover the ones I’ve actually used, but explore on your own — there’s more than what I’m showing here.

### /clear (aka /reset)

When you’re done with a conversation and want to start fresh, `/clear` is your friend. It's faster than exiting and starting Claude Code again.

### /compact

The `/compact` command summarizes the conversation and replaces the current context with the summary. Claude Code does this automatically…

## Create an account to read the full story.

The author made this story available to Medium members only.

If you’re new to Medium, create a new account to read this story on us.

[Continue in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3Dregwall&source=-----9cd6ff4c33cb---------------------post_regwall------------------)

Or, continue in mobile web

[Sign up with Google](https://medium.com/m/connect/google?state=google-%7Chttps%3A%2F%2Fmedium.com%2F%40the.gigi%2Fclaude-code-deep-dive-slash-commands-9cd6ff4c33cb%3Fsource%3D-----9cd6ff4c33cb---------------------post_regwall------------------%26skipOnboarding%3D1%7Cregister%7Cremember_me&source=-----9cd6ff4c33cb---------------------post_regwall------------------)

[Sign up with Facebook](https://medium.com/m/connect/facebook?state=facebook-%7Chttps%3A%2F%2Fmedium.com%2F%40the.gigi%2Fclaude-code-deep-dive-slash-commands-9cd6ff4c33cb%3Fsource%3D-----9cd6ff4c33cb---------------------post_regwall------------------%26skipOnboarding%3D1%7Cregister%7Cremember_me&source=-----9cd6ff4c33cb---------------------post_regwall------------------)

Sign up with email

Already have an account? [Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fmedium.com%2F%40the.gigi%2Fclaude-code-deep-dive-slash-commands-9cd6ff4c33cb&source=-----9cd6ff4c33cb---------------------post_regwall------------------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fp%2F9cd6ff4c33cb&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40the.gigi%2Fclaude-code-deep-dive-slash-commands-9cd6ff4c33cb&user=Gigi+Sayfan&userId=beb8ed7bf2e5&source=---footer_actions--9cd6ff4c33cb---------------------clap_footer------------------)

5

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fp%2F9cd6ff4c33cb&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40the.gigi%2Fclaude-code-deep-dive-slash-commands-9cd6ff4c33cb&user=Gigi+Sayfan&userId=beb8ed7bf2e5&source=---footer_actions--9cd6ff4c33cb---------------------clap_footer------------------)

5

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F9cd6ff4c33cb&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40the.gigi%2Fclaude-code-deep-dive-slash-commands-9cd6ff4c33cb&source=---footer_actions--9cd6ff4c33cb---------------------bookmark_footer------------------)

[![Image 5: Gigi Sayfan](https://miro.medium.com/v2/resize:fill:96:96/0*3m2lzp7-O-yNYycQ.)](https://medium.com/@the.gigi?source=post_page---post_author_info--9cd6ff4c33cb---------------------------------------)

[![Image 6: Gigi Sayfan](https://miro.medium.com/v2/resize:fill:128:128/0*3m2lzp7-O-yNYycQ.)](https://medium.com/@the.gigi?source=post_page---post_author_info--9cd6ff4c33cb---------------------------------------)

Follow

## [Written by Gigi Sayfan](https://medium.com/@the.gigi?source=post_page---post_author_info--9cd6ff4c33cb---------------------------------------)

[205 followers](https://medium.com/@the.gigi/followers?source=post_page---post_author_info--9cd6ff4c33cb---------------------------------------)

·[34 following](https://medium.com/@the.gigi/following?source=post_page---post_author_info--9cd6ff4c33cb---------------------------------------)

Follow

## No responses yet

[](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page---post_responses--9cd6ff4c33cb---------------------------------------)

![Image 7](https://miro.medium.com/v2/resize:fill:32:32/1*dmbNkD5D-u45r44go_cf0g.png)

Write a response

[What are your thoughts?](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40the.gigi%2Fclaude-code-deep-dive-slash-commands-9cd6ff4c33cb&source=---post_responses--9cd6ff4c33cb---------------------respond_sidebar------------------)

Cancel

Respond

[Help](https://help.medium.com/hc/en-us?source=post_page-----9cd6ff4c33cb---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----9cd6ff4c33cb---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----9cd6ff4c33cb---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----9cd6ff4c33cb---------------------------------------)

[Press](mailto:pressinquiries@medium.com)

[Blog](https://blog.medium.com/?source=post_page-----9cd6ff4c33cb---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----9cd6ff4c33cb---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----9cd6ff4c33cb---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----9cd6ff4c33cb---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----9cd6ff4c33cb---------------------------------------)
