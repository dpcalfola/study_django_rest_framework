# Django Rest Framework docs

<br>

### Goals 
* Auto generate docs (with third party library)
  * drf-spectacular

* Generates schema
  * schema means in here:
    * Document in format of JSON or YAML

* Browsable web interface
  * Make test requests


### Task

* Generate "schema" file
* Parse schema into GUI



### OpenAPI schema
* Standard for describing APIs
* Supported by most API documentation tools
* Uses popular formats: YAML/JSON


### Schema structure
* Endpoint - api/stuff/price/
  * Type of request or method - get, post ...
    * description
    * parameters
  * security
    * tokenAuth
  * response - '200'



### Terms
* endpoint: request address
* swagger: A tool of converting docs to human-readable 