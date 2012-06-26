Homework Description
---------------------

In order to be graded correctly for this homework, there are a few things to keep in mind.

We'll be grading your web app by posting to your form and then checking the HTTP Response we receive.

There are a few main issues you need to keep in mind in order for this to work:

* The form elements where the user inputs their username, password, password again, and email address must be named "username", "password", "verify", and "email", respectively.
* The form method must be POST, not GET.
* Upon invalid user input, your web app should re-render the form for the user.
* Upon valid user input, your web app should redirect to a welcome page for the user.
* You must enter the full url into the supplied textbox above, including the path. For example, our example app is running at http://udacity-cs253.appspotcom/unit2/signup, but if we instead only entered http://udacity-cs253.appspot.com/ then the grading script would not work.

Code Description
--------------------

I chose to write this in django instead of webapp2, which is what Steve is using in the course.

This is hosted `on heroku <http://sharp-snow-6580.herokuapp.com/signup>`_.