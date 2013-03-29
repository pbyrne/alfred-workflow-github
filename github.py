"""Fetch information from GitHub through its API

This is an intentionally simple GitHub API client, built as much for
experimentation and learning as it is for functionality. Your mileage may vary.
"""

import requests
import json

class Client:
  def __init__(self, username, token):
    self.username = username
    self.token = token

  def repo_names(self):
    """Array of names of repositories you have access to"""
    return [repo['full_name'] for repo in self.repositories()]

  def org_names(self):
    """Array of names of orgs you have access to"""
    return [org['login'] for org in self.orgs()]

  def repositories(self):
    """Array of Dicts of information about repositores you have access to"""
    return self.get("user/repos")

  def org_repositories(self):
    org_repos = []
    for org_name in self.org_names():
      org_repos += self.get("orgs/%s/repos" % org_name)
    return org_repos

  def orgs(self):
    """Array of Dicts of information about organizations you belong to"""
    return self.get("user/orgs")

  def request_url(self, action):
    """URL to request information from the GitHub API"""
    return "https://api.github.com/%s?access_token=%s" % (action, self.token)

  def get(self, action):
    """Request information from GitHub and parse the returned JSON"""
    return json.loads(requests.get(self.request_url(action)).text)

