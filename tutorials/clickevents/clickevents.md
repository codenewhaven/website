[TOC]

More cubes in Javascript
---

We already have a rotating cube! 
What if we wanted to change features of the cube when we click on it?

You can add "Click Events" to your code!

1. Open cubes.js and cubes.html
   If you do not have these files, refer back to the first javascript tutorial and make sure you get these files on your computer and working

2. Adding a click event:

Add an event listener which basically tells your file that you will respond to an event. In this case the event is clicking down a mouse, known as 'mousedown'

	document.addEventListener( 'mousedown', onDocumentMouseDown, false );

There are other events you can include, such as right mouse click, mouse over, etc... But we will only look at clicking the mouse down today

3. Add an event function

This function will be called when an event occurs, in our case when the mouse is clicked down.

	document.addEventListener( 'mousedown', onDocumentMouseDown, false );
	function onDocumentMouseDown( event ) {
        event.preventDefault();
        cube.scale.x /= 2;
        cube.scale.y /= 2;
    }

What happens when you click the mouse? Add these lines to your code and see for yourself!

Let's explore other options!

How can you change your code to double the size of your cube when you click your mouse?

How about changing the color of your cube?






