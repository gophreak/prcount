#!/usr/local/bin/python3

# <bitbar.title>PR Lister</bitbar.title>
# <bitbar.version>v1.0</bitbar.version>
# <bitbar.author>Raymond Jones</bitbar.author>
# <bitbar.author.github>gophreak</bitbar.author.github>
# <bitbar.desc>Plugin which will use GitHub API to get a list of open PRs from your account/repo list</bitbar.desc>
# <bitbar.dependencies>python3</bitbar.dependencies>

from environs import Env
from prslib import github
from prslib import printer

env = Env()
env.read_env()

repos = github.GitHub(env('API_TOKEN')).getRepos(env('ACCOUNT_NAME'), env('ACCOUNT_REPOSITORIES').split(';'))

printer.summary('PRs', repos, int(env('PR_TOTAL_THRESHOLD')))
printer.newOption()
printer.each(repos)
