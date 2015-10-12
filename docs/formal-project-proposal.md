
# Final Project Proposal: OSSFinder
## Open Source Software Recommendation Engine

Final Project, COSC 445/545
Alex Klibisz, Muhammed Benkhayal, Yuxing Ma


***
***

## Objective

OSSFinder is a recommendation engine application for open source software that will allow a user to search an index of open source software projects and receive recommendations based on:  
1. desired features  
2. similarity to libraries to which the user is already familiar

***
***

## Motiviation

- There is an overwhelming amount of open-source software on the Internet.
- Programers, both individual and teams, stand to benefit from:
  - **picking the right tool for the job**  
  - **picking the tool with the lowest possible learning curve**
- Github provides a powerful API, but lacks powerful search features for narrowing down the many projects it hosts. We want to attempt to suplement this.
***
***

## Usage and Workflow
- See the wireframe: http://oi60.tinypic.com/2a8esg6.jpg

***
***

## Deliverables, Timeline, Responsibilities

### Deliverables and Timeline

1. Datastore of open source software projects, Friday October 23
  - clone and parse top 1000 Github projects, ordered by number of stars using the Github API.
  - include project attributes: primary language, intended platform, contribution statistics.
  - store in MongoDB
2. Method for feature set extraction, Friday November 13
  - parse each stored project for features that it implements
  - should be easily repeatable (i.e. set of python scripts)
  - store the feature sets in the datastore
3. Method for similarity analysis, Friday November 20
  - parse stored projects to determine a scale of similarity among them
  - should be easily repeatable (i.e. set of python scripts)
  - store the similarity values in the datastore
4. Simple interface to query the analysis results, Friday November 30
  - web-based
  - structured like the wireframe linked above
  - make it at least temporarily available on a cloud server (e.g. AWS or DigitalOcean) for classmates, users to try.

### Responsibilities

- Short answer: To Be Determined
- Long answer: Deliverables 1 and 4 are a matter of implementing minimal systems with which our group collectively has prior experience. Deliverables 2 and 3 will be a learning and exploration experience for each of us. So separating this work will depend where each of us gains the most traction the earliest in the learning process.

***
***
