import requests
import settings
import web


headers = {"Authorization": "Bearer " + settings.key}

def run_query(query): # A simple function to use requests.post to make the API call. Note the json= section.
    request = requests.post('https://api.github.com/graphql', json={'query': query}, headers=headers)
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, query))
 
def format_query(login):
    query = """
    {{
        user(login: "{}") {{
            avatarUrl
        }}
    }}
    """
    queryFormatted = query.format(login)
    return queryFormatted

userName = "izzyco" 
query = format_query(userName)
result = run_query(query)
avatarUrlReturned = result["data"]["user"]["avatarUrl"]
#result = run_query(queryFormatted) # Execute the query
#avatarUrlReturned = result["data"]["user"]["avatarUrl"] # Drill down the dictionary

urls = (
'/user', 'index'
)
class index:
    def GET(self):
        i = web.input(name=None)
        if i.name != None:
            query = format_query(i.name)
            result = run_query(query)
            avatarUrlReturned = result["data"]["user"]["avatarUrl"]
            return render.index(avatarUrlReturned)
        else:
            return render.index(i.name)
if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
render = web.template.render('templates/')




