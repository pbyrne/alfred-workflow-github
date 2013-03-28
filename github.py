import requests
import json

class Client:
  def __init__(self, username, token):
    self.username = username
    self.token = token

  def repo_names(self):
    return [repo['full_name'] for repo in self.repositories()]

  def repositories(self):
    return self.perform_request("user/repos")

  def request_url(self, action):
    return "https://api.github.com/%s?access_token=%s" % (action, self.token)

  def perform_request(self, action):
    return json.loads(requests.get(self.request_url(action)).text)




