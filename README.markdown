GitHub Alfred 2 Workflow
======================

Alfred 2 workflow for interacting with GitHub.

Examples
--------

All actions provide autocomplete to filter from the list of accounts and repos
that your account has access to.

Open a GitHub project's home page:

    repo pbyrne/dotfiles

Open a GitHub project's pull requests page:

    pulls pbyrne/dotfiles

Open a GitHub project's issues page:

    issues pbyrne/dotfiles

WARNING
-------

I'm using this project as an opprotunity to learn Python. The code will
probably be terrible. Use at your own risk.

TODO
----

- [ ] Capture username and password and access the GitHub API to request an auth token, then store it inside the workflow.
- [ ] Use this auth token to fetch the list of repos the user has access to.
- [ ] Use this list to provide auto-complete for one of the triggers.
