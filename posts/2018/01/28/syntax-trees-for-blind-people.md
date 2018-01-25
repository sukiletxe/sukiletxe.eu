<!--
.. title: Syntax trees for blind people
.. slug: syntax-trees-for-blind-people
.. date: 2018-01-28 12:00:00+01:00
.. tags: linguistics,accessibility,office,excel
.. category: 
.. link: 
.. description: 
.. type: text
-->

## Introduction

As I study English Philology, I have to take a course called English Grammar. In this course, I need, among other things, to analise sentences, and make syntax trees of them. Yes, those trees where you disect a sentence into phrases. But how do I, a completely blind person, do it? Images and arrows are inaccessible for me, and [the Arboreal and ArborWin fonts][arborwin], although I haven't tested them, seem to be inaccessible too. Here, I'll show the method I use.

[Arborwin]: http://www.cascadilla.com/arboreal.html

## How I do it

To draw a tree, I use Excel spreadsheets. To draw a node (an item of a tree) which has two branches, I use a merged cell, which splits into two cells below it. Then, if one of the cells has further branches, I do the same thing. 

With this procedure, I can draw a tree with  an arbitrary depth, and an arbitrary number of branches by node (although normally I work with two branches per node for this kind of tree). I think that with this system trees are easy to draw, or at least, easier than other systems I have tried. Visually, it works too, which is a plus.

## Why I don't use brackets

I don't use them because trees can get really complex. I don't know if linguists use them for large trees, but I think that, in trees with brackets, fixing mistakes is harder than in my system. But, if you don't know how to use spreadsheets, or simply you want a more conventional system, this one may work for you.

## Other systems

Of course, the possibilities are endless. If these systems don't convince you, and if you reach an agreement with your instructor (or your student), you may invent a system of your own. Also, if you are a better programmer than me, you may use something like [nested dictionaries in YAML][YAML][^1] or the [Natural Language ToolKit][NLTK].

[YAML]: http://www.yaml.org/spec/1.2/spec.html
[NLTK]: http://nltk.org
[^1]: I used YAML (although without any programming involved), and although it worked, I found it too space-consumming.

## Conclusion

I hope you have found this post helpful and informative. If you have any comments, send my an email or contact me through Twitter. At the time of writing, I haven't added the possibility to post comments yet, but if it's available when you read this, and if you prefer a more public comunication, post a comment. Also, contact me if you have any doubts, and I'll try to answer your questions. Thanks for reading!
