'''
Aggregate the relationships across the multiple relationship collections
to create a single collection that can be searched more easily.

The entries should be formatted as:
{
  repo_a: "twbs/bootstrap",
  repo_b: "zurb/foundation-sites",
  watchers: 123,
  forks: 123,
  commits: 123,
  issues: 123,
  pull_requests: 123,
  total: (123 + 123 + 123 + 123 + 123)
}

These entries should be stored in the collection rel_aggregate

'''
