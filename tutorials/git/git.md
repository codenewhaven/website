[TOC]

Git
===

What is Git?
---
Git is a tool that coders use to share code and keep track of changes they've made. Ever rewritten a paragraph of an essay, not liked how it turned it out, and wished you could go back to your previous of that paragraph? Well, that's what Git and other types of _version control_ software do for code. They allow you to go to previous points of your work where you've saved, or _committed_ your changes.

Ok, great. What can it do for me?
---
We are going to use Git to periodically save the state of our website as we make changes. After we have our code saved with Git, we can then _push_ it to _remote repositories_. What the heck is a repository? Essentially, you can think of a repository as a folder. Whenever you use Git on your machine, you are working in a _local_ repository. "Local" means the computer directly in front of you, that you're working on. A _remote_ repository is a repository that is on a different computer that's connected to yours over a _network_. You've probably heard of the network that we're going to use today: **The Internet**.

So...?
------
Sweet! Now we can move our code to other computers. Why should I care? Well, by _pushing_ our code to a special kind of computer called a _webhost_, we can make it available for other people to find on the web. If you just have your .html file sitting on your computer, you can view it _locally_ (meaning you open the file in your web browser), but nobody else can see it (would you want people to be able to see random files on your computer?). So, we need to _push_ the webpage to a public computer, whose job it is to _serve_ your webpage to whoever wants to see it. Thankfully, Github makes this super simple.

Before we learn more about Git and all of its magical code management powers, we need to learn about the application that will allow us to use to use Git (bear with me). We use git through a special program called the **terminal**. 

Exercises
---------

### 1 - Clone a Repository

    :::bash
    $ cd ~
    $ git clone git@github.com:codenewhaven/mba-website.git .i
    $ cd ~/codenewhaven/mba-website

### 2 - Make a Commit
First, make a change to your code. After that, you're ready to make your first commit!

    :::bash
    $ git commit -am "<whatever you want to say>"


### 3 - Check Where Git Will Send Code
    :::bash
    $ git remote -v
    origin  git@github.com:codenewhaven/mba-website.git (fetch)
    origin  git@github.com:codenewhaven/mba-website.git (push)


### 4 - Send your code!
    :::bash
    $ git push
