
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

- There is an overwhelming ammount of open-source software on the Internet.
- Programmers, both individual and teams, stand to benefit from picking:
  - **the right tool for the job**  
  - **the tool with the lowest possible learning curve**

***
***

## Usage and Workflow
- See the wireframe: http://oi60.tinypic.com/2a8esg6.jpg


***
***

## Deliverables, Timeline, Responsibilities

### Deliverables
1. Datastore of open source software projects
  - clone, parse, store top 1000 Github projects, ordered by number of stars
  - include project attributes like primary language, intended platform, contribution statistics
2. Method for feature set extraction
  - parse each stored project for features that it implements
  - should be easily repeatable
  - store the feature sets in the datastore
3. Method for similarity analysis
  - parse stored projects to determine a scale of similarity among them
  - should be easily repeatable
  - store the similarity values in the datastore
4. Minimal interface to query the analysis results
  - web-based
  - similar to the wireframe provided above

***
***
