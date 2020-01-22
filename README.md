# PR Count (PRS)

This project is to be used in conjunction with MacOS X BitBar pluging which allows you to summaries a total count of PRs for a
given set of repositories under an account.

You will need to produce your API token, along with account name and a semi-colon seperated list of repositories to check.

## Setup

Create a .env file with the following parameters:

```
API_TOKEN=YourGitHubTokenHere
ACCOUNT_NAME=YourAccountName
ACCOUNT_REPOSITORIES='repo1;repo2;repo3'
PR_TOTAL_THRESHOLD=5
```

`API_TOKEN` is the token used to be able to access GitHub via the API

`ACCOUNT_NAME` should be the account which holds all of the Repositories

`ACCOUNT_REPOSITORIES` is a semicolon ; separated list of repositories which you want to include

`PR_TOTAL_THRESHOLD` is used to turn the BitBar summary red when you cross this threshold.

## Installation

To install original copy, please run the following command from your terminal, inside of the plugin directory set for BitBar.

```
curl http://d2ewacsbya3usj.cloudfront.net/pr-check/installer.sh | sh
```

Follow the rules for setup to get the application actually running.


## Limitations

Currently, this first draft will only support a single Account of which all Repositories MUST belong.

This release will currenly only support GitHub, there are currently no plans to integrate other providers.
