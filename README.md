# combot
a web app in testing phase using flask

late nov - dec 1st: got generator working
dec 3rd: figuring out concurrent call of generator functions 
dec 4th: add area text, and is able to generate with a fixed prefix, strip prefix
dec 5th:- redirected the user input into prefix
		- error: TypeError: 'dict' object is not callable
		- solution: jsonify return data
		- added css loader and loading page
		- it currently grabs the global var as prefix
		- Keydown ENTER problem with textline more than one
