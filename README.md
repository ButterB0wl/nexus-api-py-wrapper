# nexus-api-py-wrapper

usage: nexus-api.py [-h] [-r REPO_URL] -e ENDPOINT -t {get,post,put,delete}

Defining the repo url is optional, it is localhost:8081 by default.

Enter the entire endpoint with all parameters, 

e.g. if the curl command is:

curl -u admin:admin123 -X GET 'http://localhost:8081/service/rest/v1/assets?repository=maven-central'

You would call the wrapper like so:

python3 nexus-api.py -t get -e assets?repository=maven-central

If any content is returned in the response, it is saved as a response.json in the same directory.
