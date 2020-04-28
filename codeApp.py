import requests
import settings
import web
import os
import socket

localHost = socket.gethostname()

if (localHost == settings.my_hostname):
    headers = {"Authorization": "Bearer " + settings.key}
else:
    headers = {"Authorization": "Bearer " + os.environ['APIKEY']}

def run_query(query): # A simple function to use requests.post to make the API call. Note the json= section.
    request = requests.post('https://api.github.com/graphql', json={'query': query}, headers=headers)
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, query))
 
def format_queryUser(login):
    query = """
    {{
        user(login: "{}") {{
            avatarUrl
            bio
            isEmployee
            url
        }}
    }}
    """
    queryFormatted = query.format(login)
    return queryFormatted


querySample = """
    {
    user(login: "izzyco") {
        avatarUrl
        bio
        }
    }
"""

#result = run_query(queryFormatted) # Execute the query
#avatarUrlReturned = result["data"]["user"]["avatarUrl"] # Drill down the dictionary

urls = (
'/user', 'users',
'/', 'home'
)
class users:
    def GET(self):
        i = web.input(name=None)
        if i.name != None:
            query = format_queryUser(i.name)
            result = run_query(query)
            avatarUrlReturned = result["data"]["user"]["avatarUrl"]
            bioReturned = result["data"]["user"]["bio"]
            employeeReturned = result["data"]["user"]["isEmployee"]
            urlReturned = result["data"]["user"]["url"]

            pyDict = {}
            pyDict['avatarUrl'] = avatarUrlReturned
            pyDict['bio'] = bioReturned
            pyDict['isStaff'] = employeeReturned
            pyDict['url'] = urlReturned 
            return render.users(pyDict)
        else:
            return render.users(i.name)
class home:
    def GET(self):
        return render.home()
if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
render = web.template.render('templates/')




