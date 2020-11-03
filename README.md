# Diagram as Code - demo

> This repo contains some demo code to demonstrate the Diagrams as Code tool 'diagram'

Our goal here is to add our diagrams to our source repository for two main reasons;

1. Source of truth
2. We naturally get an audit log from git

## Credit

Most of the code has been obtained from a great blog post by Dylan Roy, [Create Beautiful Architecture Diagrams with Python], so all credits go to him.

[Create Beautiful Architecture Diagrams with Python]: https://towardsdatascience.com/create-beautiful-architecture-diagrams-with-python-7792a1485f97

## Prequesites

This demo requires the following tools to be installed.

- python3
- graphviz
- diagram

## Demo

This demo shows the steps involved to create a diagram using code.

### Step 1: Creating The Diagram Workspace

This will simply render a blank diagram with the designated label.

    python3 demo1.py

### Step 2: Adding The Nodes

Now that we have our workspace it’s time to add the nodes that we need for our website. Each one of our nodes are pictured, and these are the “ingredients” for the architecture  we want to build. The next steps will be to organise some of our nodes into logical groupings, and then link each of the nodes with edges.

    python3 demo2.py

### Step 3: Grouping The Nodes

For this example we will just group the load balanced web servers. In a good number of the diagrams I have created in the past this was not always necessary, but as your architecture grows grouping these nodes within clusters usually enhances readability.

    python3 demo3.py

### Step 4: Linking It All Together

In this final step we will not link the nodes that we have just arranged to be leveraged in our architecture. So we are defining the flow to each node with double arrows, and you are done!

    python3 demo4.py


