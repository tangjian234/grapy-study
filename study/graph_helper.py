

from requests_oauthlib import OAuth2Session

graph_url = 'https://graph.microsoft.com/v1.0'

#The get_user method makes a GET request to the Microsoft Graph /me endpoint to get the user's profile, using the access token you acquired previously.
def get_user(token):
  graph_client = OAuth2Session(token=token)
  # Send GET to /me
  user = graph_client.get('{0}/me'.format(graph_url))
  # Return the JSON result
  return user.json()


# Call the Graph API to get calender events. 
def get_calendar_events(token):
    graph_client = OAuth2Session(token=token)

    # Configure query parameters to
    # modify the results
    query_params = {
        '$select': 'subject,organizer,start,end',
        '$orderby': 'createdDateTime DESC'
    }

    # Send GET to /me/events
    events = graph_client.get('{0}/me/events'.format(graph_url), params=query_params)
    # Return the JSON result
    return events.json() 


#https://graph.microsoft.com/v1.0/me/drive/root/children?$select=file,name,createdBy,fileSystemInfo
def get_onedrive_files_detail(token):
    graph_client = OAuth2Session(token=token)
  # Configure query parameters to
    # modify the results
    query_params = {
        #'$select': 'file'
        '$select': 'file,name,createdBy,fileSystemInfo'
        #'$orderby': 'name DESC'
    }

    # Send GET to 
    files = graph_client.get('{0}/me/drive/root/children'.format(graph_url), params=query_params)
    # Return the JSON result
    return files.json() 

# https://graph.microsoft.com/v1.0/me/events?$select=subject,organizer,attendees,start,end,location
def get_calendar_events_detail(token):
    graph_client = OAuth2Session(token=token)
  # Configure query parameters to
    # modify the results
    query_params = {
        '$select': 'subject,organizer,location,attendees,start,end',
        '$orderby': 'createdDateTime DESC'
    }

    # Send GET to /me/events
    events = graph_client.get('{0}/me/events'.format(graph_url), params=query_params)
    # Return the JSON result
    return events.json() 



def get_profile_items(token):
    graph_client = OAuth2Session(token=token)

    # Configure query parameters to
    # modify the results
    query_params = {
        '$select': 'displayName,id,userPrincipalName,jobTitle'
    }

    # Send GET to /me/item
    item = graph_client.get('{0}/me'.format(graph_url), params=query_params)
    # Return the JSON result
    return item.json() 
