<!--
.. title: From birds to Mastodons
.. slug: from-birds-to-mastodons
.. date: 2018-08-18 19:26:39+02:00
.. tags: Twitter, Mastodon, accessibility
.. category: 
.. link: 
.. description: 
.. type: text
-->

Two days ago, Twitter deprecated its streaming API. This means that third-party apps can no longer receive tweets and direct messages in real time, and have to wait 2 minutes to receive updates. As this is suboptimal for some people (and thus the #BreakingMyTwitter hashtag was born), people have started to search for alternatives. The most (if not the only) acclaimed candidate, at least in my circle of Twitter, has been [Mastodon.][mastodon]
[mastodon]: https://joinmastodon.org/

## So what's Mastodon?

Mastodon is a decentraliced and federated social network. This means that there are multiple interconnected servers (called instances), and there's no central one (no instance is "above" any other, no instance has more authority than any other). You can follow and view the statuses of people in other instances by knowing their username and instance. Think of e-mail as an analogy:  you can send an email from gmail to outlook, and there is no central email server.

## Comparing Twitter and Mastodon

Mastodon is similar to Twitter, without the noise of ads or sorting algorythms. You get the statuses (or "toots", as they're called) in reverse chronological order. You can boost (same as retweeting in Twitter) and like toots, and of course, you can follow people. You have several third-party clients.

One key difference is that each instance has its own rules, and in some cases an instance can be more of a niche for a community in particular. You can, of course, self-host an instance for yourself or for more people, if you like. In [joinmastodon.org,][mastodon] you can find a list of instances with their rules, though I guess there may be even more scattered through Internet, without counting the personal ones.

Another difference is that there are three home timelines: one where toots by people you follow appear; another one where all toots by the instance's users appear; and another one where all the toots from instances your instance knows about appear.

Lastly, Mastodon is open-source. This means that anybody can view its code and edit it.

## Concerns

First, my user experience with the Mastodon official web client hasn't been as good as I'd like. Accessibility is lacking in some respects (mostly related to navigation and some unlabeled controls here and there). However, workarounds do exist, and I hope developers will listen to their users.

Also, I can see that [IFTTT] doesn't support it right now, so I cannot automatically post my updates and statuses from other services to Mastodon or vice-versa as easily as I'd like to. However, it can be done by using their API, with the Maker service (a fancy name for webhooks), which fires every time a certain trigger is used. 
[IFTTT]: https://ifttt.com

---

Thanks for reading! If you have any questions or comments, post them below or drop me a line. By the way, you can [Follow me on Mastodon,][followme] if you like.
[followme]: https://mastodon.social/@sukiletxe
