[TOC]

# Interactive Websites

Obviously, websites are more complicated than the simple HTML stuff
we have done so far. You want to do more than post pictures and
links. You want some form of interactivity. On Facebook, when you
click Like on a post, the page changes for you and your friends.
Wouldn't that be nice?

## Example: Facebook Liking

Somewhere, Facebook has an instruction like this:

    When the user clicks LIKE on a POST, UPDATE list of users who liked the post.

It's probably in their testing code. If Facebook fails to do that, something
is wrong. So what does Facebook need to do in order to make that happen?
Think about it:

    When you click "Like," Facebook needs to:

    - Change link on screen to say "Liked"
    - Disable clicking link on screen
    - Update number of "likes" on the screen

**But those changes only happen on your computer.**

Facebook also needs to change its internal representations
the post, so that future users see that you "liked" it.

    When you click "Like", Facebook servers need to:

    - Increment a counter somewhere that looks like [<postID>, <num_likes>]
    - When future users visit the page, make sure to display up-to-date count"

These changes happen away from your computer, on Facebook servers.

# Backend and Frontend

The changes on Facebook's server are called **backend** changes,
and the changes on your computer are called **frontend** changes.
In general, frontend code is HTML, Javascript, and CSS code that
runs in your browser.

Seriously. You `Cmd+Alt+U` to *view source* at any time, and see
the code your browser uses to **render** the Facebook website.

## Frontend

When you go to Facebook.com, your browser downloads an HTML file
that instructs it to do a bunch of things.

    1) Download all necessary images

    2) Download .css files with style instructions -- colors, shapes, etc.

    3) Download .js (Javascript) files for interactivity instructions.

Inside the .js files are instructions for how the browser should
respond to **events**, like the "event" of a user clicking "Like"
on a post. The Javascript code can tell the browser to do almost
anything.

In this case, it tells the browser to contact Facebook's servers
and tell them that you just liked this post. Somewhere, there is
a notification that looks like `{event: 'like', user: 'miles', postID: 12345}`.
The Javascript code tells the browser to send that notification to Facebook's
servers.

## Backend

The **backend** code running on Facebook's servers receives that event,
and decides what to do. In this case, Facebook needs to update the counter
of people who liked the post.

## The Difference

- Frontend code
    - Executes in your browser.
    - Only HTML, Javascript, and/or CSS. (Whatever your browser supports!)
- Backend code
    - Executes on external servers somewhere.
    - Written in any language. Python, C, C++, Java, PHP, Ruby, ...
    - Can be arbitrarily complicated, even running on thousands of computers.

The important thing to remember is that **you need backend code to persist
state between users. **That is, if you want to make a change so that everybody
visiting the website sees it, you need backend code.

# Interactivity without backend code

Hopefully you can see that building websites with lots of interactivity
can be complicated, especially when you want everybody to see the results
of the interactivity.

If you want to learn about backend programming, you should google for "Python"
and "Ruby". Let me know and I can show you.

In the meantime, we can do a lot of cool stuff with just Javascript. In the
past five years, web browsers have gotten fast enough that they can do a
lot of computation. In 2005, you would not find a web browser that could
render complicated graphics, because it did not have access to all the
resources on the computer.

Fortunately, people are using their web browser for more and more purposes,
so the browsers are becoming more powreful. You can build some pretty
cool things in the browser, using only Javascript.

## Warmup: Simple Javascript interactivity

(You can find examples of this in the examples/javascript folder.)

### Write some code, see what happens.

Make an HTML file for playing with, e.g. `scratch.html`. Put this in it:

    :::html
    <!doctype html>
    <html lang="en">
    <head>
       <meta charset="utf-8" />
       <title>Hello World</title>

       <!-- CSS for presentation. -->
       <style>
       h1 { font-size: 14px; color: hotpink; }
       button { color: red; }
       </style>
    </head>
    <body>
       <h1>Hello World</h1>
       <button>Click Me!</button>

       <!-- JavaScript for interactivity. -->
       <script>

       // Get a handle on the first button element in the document.
       var button = document.querySelector( "button" );

       // If a user clicks on it, say hello!
       button.addEventListener( "click", function( ev ) {
           alert( "Hello" );
       }, false);

       </script>
    </body>
    </html>


(Exampe from http://learn.jquery.com/javascript-101/getting-started/)

Open `scratch.html` in your browser, e.g. Google Chrome, click the button.

What happened? You should get an "alert" in your browser when you click the
link. The HTML page (`scratch.html`) told your browser that when you click
on the button, it should alert you.

The Javascript on Facebook.com is effectively doing this same thing, except
the logic for what to do is more complicated than "display an alert". The
important thing to notice is that the Javascript tells your browser
how to **respond to an event** -- in this case, clicking a button.

### How the code works

Let's break down the code. The first interesting thing that happens is:

    :::html
    <!-- CSS for presentation. -->
    <style>
    h1 { font-size: 14px; color: hotpink; }
    button { color: red; }
    </style>

This is *CSS* code. CSS stands for "cascading style sheets", and it's
a language for telling the browser how to decide what elements on
the page should look like. In this case, it's saying:

**"Render all `<h1>....</h1>` elements in `font-size:14px` and `color:hotpink`"**

Now whenever the HTML code uses a `<h1>...</h1>` tag, like when it says
`<h1>Hello World</h1>`, the browser knows how to display it. The reason
you see hot pink "Hello World" in the page is because your CSS code
tells the browser to display it that way.

Notice it also says to render any `<button>...</button>` tag as `color:red`.
This is why the button is red.

Next interesting thing is in the `<body>` of the document, which contains the
HTML for the elements you see on screen.

    <h1>Hello World</h1>
    <button>Click Me!</button>

This code is important because now the browser knows that the page includes
a `<button>` element. Now, the Javascript code can reference the `<button>`
element because it knows that the browser is aware of it.

The Javascript code is everything in the `<script>...</script>` tag:

    :::html
    <!-- JavaScript for interactivity. -->
    <script>

    // Get a handle on the first button element in the document.
    var button = document.querySelector( "button" );

    // If a user clicks on it, say hello!
    button.addEventListener( "click", function( ev ) {
        alert( "Hello" );
    }, false);

    </script>

When your browser sees the `<script>` tag, it knows the code is Javascript,
not HTML. Javascript is a powerful programming language that can perform
a lot of logic. Here, the logic is pretty simple, but can get complex.

First...

    var button = document.querySelector( "button" );

Your browser creates a **variable** named button, and assigns
the value `document.querySelector("button")` to it. Your
Javascript could also say, for example:

    var name = "Miles";

And that would tell the browser to store the value `"Miles"`, a "string",
in the variable called `name`. Any time I use the variable `name`, the
browser knows to substitute it for `"Miles"`. e.g. if I write
`alert(name);`, the browser will popup an alert that says "Miles".

In this case, the value of the variable is `document.querySelector("button")`
instead of "Miles". The concept is the same, but this `querySelector` is
an **object** that tells the browser how to find the `<button>` tag. So,
effectively, it points to the button tag on the page.

Now, when the browser reads

    button.addEventListener(...)

It knows that it is adding an "event listener" to the `<button>` tag.
This `addEventListener()` is a **function**, and it tells the browser
to listen to an event. Notice the expanded version is:

    button.addEventListener( "click", function (ev) { ....}, false);

This function takes three **arguments**. The first is `"click"`, which tells
the function to do something when a `"click"` event happens. The second argument
is `function (ev) { ... }`, which is the definition of ANOTHER function, called
a **callback function**. Our `addEventListener()` function tells the browser
that when it registers a `click` event, it should call the `function (ev) { ... }`
function. Finally, the third argument is `false`, which is just some flag somewhere.
I don't know exactly what it means.... you should look it up!

So, let's dig into the callback function a little more.

    function (ev) {
        alert("Hello");
    }

This is a simple function. The person writing it knows that when the browser
calls it, the user just clicked a button. This is true because the `addEventListener`
function told the browser that's what it needs to do.

The person writing the function also knows that the browser will provide
a value for the `ev` argument, which represents an **event** object, in this
case a click. Because this function is so simple, it does nothing with the `ev`
object, but it could.

In this case, all the function does is call `alert("Hello")`, which is
what you see on your screen.

### Separate the Javascript from the HTML

Let's try something. Modify your `scratch.html` to look like this:

    :::html
    <!doctype html>
    <html lang="en">
    <head>
        <meta charset="utf-8" />
        <title>Hello World</title>

        <link rel="stylesheet" type="text/css" href="style.css" />
    </head>
    <body>
        <h1>Hello World</h1>
        <button>Click Me!</button>

        <script src="button.js" type="text/javascript" />

    </body>
    </html>

Notice we removed the CSS and Javascript code, and replaced
it with links to the documents.

    <link rel="stylesheet" type="text/css" href="style.css" />

    ....

    <script src="button.js" type="text/javascript" />

These are special tags that tell your browser to load code
from those files. Right now, you do not have those
files. If you refresh your browser on `scratch.html`,
you will just see "Hello World" with no colors or
interactivity.

To enable all this, you need to make the files so that your
browser knows how to find them.

Make a file called `style.css` and put your CSS code in it:

    <!-- CSS for presentation. -->
    <style>
    h1 { font-size: 14px; color: hotpink; }
    button { color: red; }
    </style>

Make a file called `button.js` and put your Javascript code in it:

    // Get a handle on the first button element in the document.
    var button = document.querySelector( "button" );

    // If a user clicks on it, say hello!
    button.addEventListener( "click", function( ev ) {
        alert( "Hello" );
    }, false);

**Make sure that `scratch.html`, `button.js`, and `style.css` are
all in the same folder.***

You should now have a file hierarchy that looks (something) like this:

    ~miles/Desktop
        scratch.html
        style.css
        button.js

When your browser renders `scratch.html`, and sees a `<link>` or `<script>`
tag pointing to the file `style.css` or `button.js`, it knows to check
the same directory as `scratch.html`.

# Something Cool: 3D Cubes in your Browser!

You are not limited to only linking to files in the same directory.
You could also say something like `../button.js` for "loop up one folder,"
or `http://www.google.com/button.js` for "download `button.js` from this  URL."

Javascript is a very raw language, but you can do a lot with it. People have
already done a lot with it, and put their useful code into packages of
code called *libraries*. A *library* of Javascript code is basically a
pre-programmed set of functions that you can call from your own Javascript
code.

A few Javascript libraries:

- [JQuery.js](http://jquery.com/) is a popular library for manipulating HTML elements
- [Angular.js](https://angularjs.org/) for coding HTML that responds to backend changes
- [Three.js](http://threejs.org) for drawing and rendering 3D objects.

These libraries are all open-source code, which means anybody can see their
code, and anybody can edit it (if approved by the maintainer.) For example
you can see the GitHub pages of the above projects:

- [jQuery GitHub Page](https://github.com/jquery/jquery)
- [Angular GitHub Page](https://github.com/angular/angular)
- [Three.js GitHub Page](https://github.com/mrdoob/three.js/)

If you want, you can `git pull` the repositories of those projects, and have
all their code at your fingertips. Then, you could use their code in your
websites via the `<script>...</script>` tags like above.

But why would you bother downloading any of these libraries, if the code
will always be the same? Fortunately, you do not have to download them.
Because you can tell your browser to fetch a Javascript page from anywhere,
including an external website, you can use external URL's.

Google is nice enough to provide hosting for these projects. You can
see a
[full list of projects](https://developers.google.com/speed/libraries/devguide)
 that Google supports. This is great, because it allows us to write code like:

    <script src="//ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>

Or

    <script src="//ajax.googleapis.com/ajax/libs/angularjs/1.2.26/angular.min.js"></script>

Or

    <script src="//ajax.googleapis.com/ajax/libs/threejs/r67/three.min.js"></script>

These tags all tell your browser to go to Google's hosted version of
the library, and download it. It's the same as if you downloaded it onto
your computer, and then pointed the browser to the local version.

Let's try this with three.js

## Goal

We want to make a website that leverages the functionality provided to us
by the `three.js` library. This is a great library, which provides a "wrapper"
around very complicated, low-level code that tells your computer how to display
graphics.

If you want 3D graphics in your web browser, you want to use three.js.

You can see
[examples of three.js pages](http://threejs.org/examples/#webgl_interactive_draggablecubes)
on the three.js website. If you click on any one of those examples,
you can click "View Source" to see how they're made.

Our goal is to replicate one of the three.js examples on our own
computer. The code we are using is copied directly from the
["intro to three.js"](http://threejs.org/docs/index.html#Manual/Introduction/Creating_a_scene) turorial.

## Setup

Make a folder on your Desktop, call it `whatever`. In that folder,
make a file called `cubes.html` and `cubes.js`. On your terminal, this means:

    cd ~/Desktop
    mkdir whatever
    cd whatever
    touch cubes.html
    touch cubes.js

Now, you should have a file structure that looks like this:

    ~/Desktop/
        whatever/
            cubes.html
            cubes.js

## Make the HTML file

In your `cubes.html` file, put the following:

    <html>
    <head>
        <title>My first Three.js app</title>
        <style>canvas { width: 100%; height: 100% }</style>
    </head>
    <body>
        <script src="http://ajax.googleapis.com/ajax/libs/threejs/r67/three.min.js"></script>
        <script src="cubes.js"></script>
    </body>
    </html>

By now you should have some idea of what we are doing here. The two important
lines are:

    <script src="http://ajax.googleapis.com/ajax/libs/threejs/r67/three.min.js"></script>
    <script src="cubes.js"></script>

This tells the browser to "download the threes.js library from google", and then
"download my cubes.js code from this local folder."

## Make the Javascript file

Obviously, we also need the `cubes.js` file. So, make a `cubes.js` file and
put the following in it:

    :::javascript
    var scene = new THREE.Scene();
    var camera = new THREE.PerspectiveCamera(75, window.innerWidth/window.innerHeight, 0.1, 1000);

    var renderer = new THREE.WebGLRenderer();
    renderer.setSize(window.innerWidth, window.innerHeight);
    document.body.appendChild(renderer.domElement);

    var geometry = new THREE.BoxGeometry(1,1,1);
    var material = new THREE.MeshBasicMaterial({color: 0x00ff00});
    var cube = new THREE.Mesh(geometry, material);
    scene.add(cube);

    camera.position.z = 5;

    var render = function () {
       requestAnimationFrame(render);

       cube.rotation.x += 0.1;
       cube.rotation.y += 0.1;

       renderer.render(scene, camera);
    };

    render();


Now, you should have something in all of your files:

    ~/Desktop/
        whatever/
            cubes.html  <--- Has HTML code that links cubes.js
            cubes.js    <--- Has Javascript code that calls three.js library

Save the files and open `cubes.html` in your browser. You should see
something pretty cool.

There's a lot happening here and we can talk about it in class.

