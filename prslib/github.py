import urllib.request
import functools, operator, collections
import json
import re

from prslib import prmodel

class GitHub:

  baseAPI = 'https://api.github.com'
  baseWeb = 'https://github.com'

  def __init__(self, token):
    self.token = token

  def getRepos(self, account, repositories):
    repos = []

    for repo in repositories:
      api = self.buildAPI(account, repo)
      prs = self.removeDrafts(self.call(api))

      name = self.formatName(repo)
      url = self.buildURL(account, repo)
      num = len(prs)

      repos.append(prmodel.PRData(name, account, repo, url, num))

    return repos

  def buildAPI(self, account, repo):
    return '%s/repos/%s/%s/pulls' % (self.baseAPI, account, repo)

  def buildURL(self, account, repo):
    return '%s/%s/%s/pulls' % (self.baseWeb, account, repo)

  def call(self, url):
      headers = {'Authorization': 'token ' + self.token, 'Accept': 'application/vnd.github.inertia-preview+json'}
      req = urllib.request.Request(url, None, headers)
      response = urllib.request.urlopen(req)

      return json.loads(response.read())

  def formatName(self, name):
    return self.ucwords(name.replace('-', ' '))

  def ucwords(self, s):
    return " ".join([w[0].upper() + w[1:] for w in re.split(' ', s)])


  def removeDrafts(self, prs):
    clean = []
    for pr in prs:
      prData = self.call(pr['url'])
      if prData['mergeable_state'] != 'draft':
        clean.append(pr)

    return clean
