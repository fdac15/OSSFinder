
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
- Suplement the existing Github search features.
- Programers, both individual and teams, stand to benefit from:
  - **picking the right tool for the job**  
  - **picking the tool with the lowest possible learning curve**

***
***

## Usage and Workflow
- See the wireframe: http://oi60.tinypic.com/2a8esg6.jpg

***
***

## Deliverables, Timeline, Responsibilities

### Deliverables and Timeline

1. Datastore of open source software projects; Friday October 23; Muhammed, Yuxing
  - retrieve a subset of Github repos with all of their user interactions (stars, forks, watches, issues, pull requests, commits)
  - store in MongoDB for simple querying
2. Method for feature set extraction; Friday November 13; Muhammed, Yuxing, Alex
  - should be easily repeatable (i.e. set of python scripts)
  - currently two options: 
    - text-based feature search (like Google)
    - feature selection (choose one or more from a set of predefined features)
3. Method for similarity analysis; Friday November 20; Muhammed, Yuxing, Alex
  - parse stored repos to determine a scale of similarity among them
  - should be easily repeatable (i.e. set of python scripts)
  - store the similarity values in the datastore
  - current proposed approach:
    - create a point system based on user interactions
    - e.g. same user commits to two repos r1 and r2, then relationship(r1,r2) += 5
    - create n^2 relationships among repos
4. Simple interface to query the analysis results; Friday November 30; Alex
  - web-based
  - structured like the wireframe linked above
  - make it at least temporarily available on cloud hosting (e.g. AWS or DigitalOcean) for users to try.

### Responsibilities

- Short answer: To Be Determined
- Long answer: Deliverables 1 and 4 are a matter of implementing systems with which our group collectively has prior experience. Deliverables 2 and 3 will be a learning and exploration experience for each of us. So separating this work will depend where each of us gains the most traction the earliest in the learning process.

***
***
