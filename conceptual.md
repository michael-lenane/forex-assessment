### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?
  The JavaScript language is like a rule set that is recognized and executed by the browser. Python on the other hand is not a language that interacta with servers.

- Given a dictionary like `{"a": 1, "b": 2}`: , list two ways you
  can try to get a missing key (like "c") _without_ your programming
  crashing.

  1. my_dict = {"a":1, "b":2}
     my_dict["c"] = 3

  2. my_dict = {"a":1, "b":2}
     my_dict.setitem

- What is a unit test?
  A unit test is a test of individual components of an application in isolation

- What is an integration test?
  An integration test is a test of the compatability of multiple components of an app as they are tested together as a group.

- What is the role of web application framework, like Flask?
  It is an organized framework that does most of the grunt work behind the scenes so that you don't have to. It utilizes pre=built functions and methods to be able to create and develop web functionality quicker than if you didn't have access to those specific functions and methods.

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?

- How do you collect data from a URL placeholder parameter using Flask?
  You can use the <> notation withe the variable that you are looking for to be placed within the arrows.

- How do you collect data from the query string using Flask?
  In the query string the arguments start after the "?" symbol and the data is stored as a key value pair. Key value pairs are seperated by the "&" symbol. Keys and values are seperated by the "=" symbol.

- How do you collect data from the body of the request using Flask?
  from flask import Request
  You can utilize the GET and POST methods of a form field, paired with an ID you can extract the values using session variables.

- What is a cookie and what kinds of things are they commonly used for?
  A cookie is a small bit of information saved on the server. They are commonly used to provide seamless access and usability to a site without having to enter information over and over upon revisiting a site.

- What is the session object in Flask?
  A session object in Flask is a dictionary used to store data using key value pairs (similar to cookies, but not exactly the same)

- What does Flask's `jsonify()` do?
  jsonify() in Flask serializes session data and ensures that it is in proper JSON format as a response so that the data can be interpreted.
