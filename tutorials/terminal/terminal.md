[TOC]

The Terminal
============

The terminal allows us to interact with the computer in a different way than we normally do. While I'm sure you're used to clicking around to open files and folders (in computer-speak, we refer to folders as _directories_), in the terminal we do everything from the keyboard. When we _execute_ commands, we're really just running little programs. It's a lot like clicking on an application's icon, but in a way that's easier for the computer to understand.

The terminal also allows us to navigate the _file system_, which is just a fancy way of saying all of the files and folders on our computer. We can think of the file system as a structure called a _tree_, like this:

    Figure 1.1
                   "/"
                 /     \
                /       \
               /         \
              /           \
             /             \
            /               \
       "Applications"      "Users"  
           |                  |
    "Sublime\ Text\ 2.app"  "bob"   
                            /   \
                           /     \
                  --> "code"     "essays" 
                      /   \         |
                     |     |    "boring.doc"
                   "js"   "html"
                     |     |
                     |    "index.html"
                  "fun.js"
    CONTENTS
    --------
    /: Applications, Users
    Applications: "Sublime\ Text\ 2.app"
    Users: bob
    bob: code, essays
    code: js, html
    js: fun.js
    html: index.html
    essays: boring.doc

    PATH EXAMPLES
    -------------
    /
    /Applications
    /Applications/Sublime\ Text\ 2.app
    /Users
    /Users/bob
    /Users/bob/code
    /Users/bob/code/js
    /Users/bob/code/js/fun.js
    /Users/bob/code/html/index.html
    /Users/bob/essays
    /Users/bob/essays/boring.doc

    (current directory denoted by "-->")

Whenever we use the terminal, just like with Finder, we are "in" a specific folder. For instance, if we click on Finder and then Pictures, we are "in" the Pictures folder. We call this directory that we are "in" at any given point in time our current _working directory_. We can find our current working directory with the command `pwd`, which we'll talk about later.

Usually, we can tell the difference between files and directories by the presence/absence of a _file appendage_. Files have them, directories (for our purposes) don't. For example, we can tell that `fun.js` is a _javascript_ file by the `.js` file appendage. Similarly, we can tell that `code` is a folder because it has no file appendage.

We locate files or directories in the file system using something called a _path_. A path is like an address: it tells us where to find something on our computer. A path is a string of folders separated by forward-slashes (`/`). Usually, when we talk about paths, we talk about _relative paths_. Relative paths are _relative to_ (depend on) our working directory. For instance, in Figure 1.1, our current working directory (denoted by `-->`) is "code". The relative path of `fun.js` would therefore be `js/fun.js`. 

So, what if we change directories, and then try to use the same relative path? Will it work? Unfortunately not. Because relative paths depend on our current working directory, they only work if we stay in that same directory. To get around this, we use _absolute paths_.

An absolute path tells us exactly where a file or folder is relative to the root directory (`/`), no matter what our working directory is at the moment. We'll talk more about the root directory later. Absolute paths always start with `/` and can be used anywhere on the file system. Absolute paths of all the files and folders in Figure 1.1 are provided.

In the first exercise we are going to learn about some basic _commands_. Commands are how we tell the terminal (read: computer) what we want to do. We can tell when the terminal is ready to accept commands when we see a `$` with a blinking cursor next to it. The `$` is known as the _prompt_, which means that the terminal is ready to accept commands.

Every command actually represents a program. These programs are much smaller and less complex than something like Chrome or iTunes, but they are programs nonetheless. Usually, these programs will finish their job so quickly that we won't even be able to notice they were running. Generally, we will enter a command and see the output in the terminal immediately, with another _prompt_ (`$`) right below the output of the command we last executed. 

Sometimes, we won't see the prompt pop back up immediately after we enter a command. Usually, this means that the program run by the command we just entered is _hanging_, or not finishing like it's supposed to and we can't execute our next command. Just like you would hit Cmd+Q to quit iTunes, you can hit Ctrl+C to quit, or _terminate_ a program in the terminal. If that doesn't work, you can "force quit" the program running in your terminal with Ctrl+Z.

Exercises
--------
### 1 - Open the Terminal
So, first off, we need to open up the Terminal application. You can do this by hitting Cmd+Space to open Spotlight, then typing in "terminal". Terminal should be one of the first applications that pops up. Select it and hit Enter to open the Terminal. When you open the terminal, you should see a `$` with a blinking cursor next to it. The `$` prompt means that the terminal is ready to accept commands.

### 2 - Where are we?
Word. So now you should see a black window with a blinking cursor. It looks like something you'd see in a hacker movie, right? Anyway, let's orient ourselves. We can do this by entering the `pwd` command, which stands for "Print Working Directory". This will tell us the absolute path of our current working directory. We run a command in the terminal by typing it then pressing Enter. So, type

    :::bash
    $ pwd

into your terminal and hit Enter. The terminal should spit  our a sequence (which correspond to the names of folders) of words separated by slashes. For example, when I enter `pwd` in my terminal, it spits out:

    :::bash
    /Users/will

The weird string of words separated by slashes is what's called a _path_ or _filepath_, as we discussed earlier. It's how the comptuter locates files and folders internally. We are currently in what is called the home directory. We will be using the home directory as our basecamp for exploring the computer. So what's in our home directory? Well we can find out in two ways:

1. using Finder
  - open up Spotlight again by hitting Cmd+Space, and type in "finder". Select "Finder" 
  - click on your name with the little house icon next to it in the left-hand side pane. 
2. using the "ls" command
  - type `ls` into the terminal
  - hit Enter

Notice any similarities between what you see in Finder and what is spit out by the Terminal?

### 3 - Let's Make a Folder
To make a new directory, we use the `mkdir` command. But how do we tell the computer what we want our folder to be called? We need to give the `mkdir` command an _argument_. For instance:

    :::bash
    $ mkdir my_folder

where "my_folder" can be replaced with whatever you want call your folder. So, we want to make a directory called "code", where we will put most of the code in this course. First, let's make sure that we're in the correct directory (our home directory). so, type in 

    :::bash
    $ pwd

it should say `/Users/your_name`. If it doesn't, type in `cd ~` and hit Enter (we'll talk about what that does later). Now we know we're in the right place, let's make our code directory:

    :::bash
    $ mkdir code

now, enter the `ls` command and "code" should appear. 

### 4 - Changing Directories
The way we move around the filesystem is by changing directories. Predictably, the command `cd` allows us to change directories, with the directory we want to enter as the _argument_. Now, let's go into the directory we just created:

    :::bash
    $ cd code


### 5 - Special Directories
#### 5.1 - Current Directory: `.`

#### 5.2 - Parent Directory: `..`
Now that we now how to go into folders within folders (i.e. down directory "tree" we talked about in class), we need to figure out how to go back up one level. In other words, we call sub-folders (folders within a the current folder/directory) as _children_ of the containing them. Similarly, we call the folder which contains the child its _parent_ folder or directory. To change the current directory to the current directory's _parent_, we use the special directory `..` as a parameter. You can essentially think of `..` as "current directory's parent". So, let's enter the parent of "code" (should be our _home_ directory)

    :::bash
    $ cd ..


#### 5.3 - Home Directory: `~`

#### 5.4 - Root Directory: `/`


### 6 - Characters To Avoid in the Terminal
  * Space: `' '`

### 7 - Helpful Commands
  * `cd` <directory_name>
  * `pwd`
  * `mkdir` <folder_name>
  * `ls`

### 8 - Helpful Resources
  * [Apple's Command Line Primer](https://developer.apple.com/library/mac/documentation/OpenSource/Conceptual/ShellScripting/CommandLInePrimer/CommandLine.html)

Congratulations! You should now know how to navigate the file system and use the terminal!
