# Internal-Consistency-Engine
Working directory for Internal Consistency Engine Development.

## Project Goals
* Provide a REST API for interaction with the engine.
* Organize content into Page-Cell structure
* Separate content based on Universe Context within Multiverse Context
* Allow users to have multiple, distinct frames of reference for accessing content.
* Control access to content on a per-cell, per frame of reference basis.

## Structural Plan
* Internal-Consistency-Engine contains the entire project
* /api/ contains the definition for all defined api endpoints
* /bootstraps/ contains the functions necessary for each portion of the application to load configurations and begin operating
* /configs/ contains local configuration flat-files and is generated as part of application setup
* /helper/ contains helper classes that encapsulate tools, reducing dependency on specific vendors
* /internal_consistency_engine/ contains the core application files
* /test_api/ contains the test scripts for the api endpoints
* /app.py provides the entry point for launching the application
* /pyproject.toml is in the form required by setuptools and should not be changed
* /README.md is this document
* /requirements.txt is a listing of the dependencies of this library
* /setup.cfg defines the library and includes details on the correct setup of the application

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
	* Loads and runs /app.py
	* ~~Downloads Git Repository~~
	* ~~Finds ENVIRONMENT file and acts on the included instructions~~
		* ~~Finishes with launching the application~~
* Working Secure Authentication
	* Allows user login over OAuth
	* Maintains tokens for repeated access
		* Stores tokens beyond a single session to permit automated API access
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
* Upon loading, the application checks the included command line arguments for relevant configuration information
  * Overriding defaults with any provided configuration details, loads and checks /configs/environment.json
	* If /config/environment.json does not exist, it creates the invalid default configuration files.
	* If /config/environment.json does exist, it checks for a valid SERVICE_NAME
	* If /config/environment.json contains a key named SERVICE_NAME with a non-empty value, assumes all other keys in the file are new or updated configurations and stores them.