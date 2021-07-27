# Internal-Consistency-Engine
Working directory for Internal Consistency Engine Development.

## Structural Plan
* Provide a REST API for interaction with the engine.
* Organize content into Page-Cell structure
* Separate content based on Universe Context within Multiverse Context
* Allow users to have multiple, distinct frames of reference for accessing content.
* Control access to content on a per-cell, per frame of reference basis.

## Proof of Concept 
### Parts
* Project built using Python
* Project parts to be hosted in Docker Containers
* Database services provided by MongoDB
* Authentication services provided by OAuth
* Authorization details stored in database
* Content cells stored in database

### Goals
* Docker Container automated setup and launch
	* Loads and runs /app/app.py
	* ~~Downloads Git Repository~~
	* ~~Finds ENVIRONMENT file and acts on the included instructions~~
		* ~~Finishes with launching the application~~
* Working Secure Authentication
	* Allows user login over OAuth
	* Maintains tokens for repeated access
* Contexts do not collide
	* Identical subjects across multiple universes remain separate
	* Identical cells across multiple universes and subjects remain separate
	* Individual content cells correctly capture associated permissions and CSS
* REST API Functionality
	* Responses include only Authorized information
	* Responses include applicable HTML and CSS for the requested content
	* Responses correctly report on actions taken
	* Error messages don't leak unauthorized information
	* Logs don't leak unauthorized information

### Application Bootstrap Process
* Application loads and checks /config/environment.json
	* If /config/environment.json does not exist, it creates all of the blank configuration files.
	* If /config/environment.json does exist, checks the contents
		* If /config/environment.json contains the key {"CONFIGURED": False}, check the other configurations against the default values.
		* Otherwise, continue bootup using the Configured values.