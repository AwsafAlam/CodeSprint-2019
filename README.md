# SearchEngine | FalguniCodeSprint-2019

This is a search engine that was developed for the [FalguniCodeSprint2019](https://www.evensi.com/falguni-code-sprint-2019/291788749). 

---

## Problem Statement

*NotSoUniversal Search Engine*

From the very beginning of backpack, we wanted to build a universal product search engine, and are working hard to make that happen. In this project, you’ll build a not-so-universal subset of that search engine.

Since we have to start somewhere, instead of every sites, we will scrape amazon only. And amazon has like almost quarter billion products. For this project though, you want to build a search engine with just 10k most popular products (how you want to define popular is entirely up to you!). Your goal is to scrape data from their product pages in this format. We’ve provided some examples here for you to look at.

Think of the project in this way: you want to deploy a minimal search engine for your users by tomorrow. Do whatever you need to do. Done is better than perfect! So it’s better not to fret over implementing the fastest or most clever solution from the start. You can always iterate on it later.

#### Deliverable

By the end of the project, your user should have a search page where they can search and browse 10k popular amazon products. The UI doesn’t need to be super polished and beautiful as long as it’s functional. You should have data for (almost) all of the 10k items in the given format. Few products might be unavailable or stocked out by now, that’s fine. You should also have some insights/ideas for these questions,
How long does it take for your program to scrape each product on avg? What could be some possible ways to make it even faster?

Did you get flagged as robot while scraping? What % of the time? How to get around/minimize that?

How to scale this to 100k products? Or 1M? 10M? 100M?

*Hint*

- Getting flagged as bot much? Heard of browser automation/headless chrome?
- For search engine, you can check out elasticsearch, vespa or solr. There are other alternatives as well. Whichever you want, the world is an open playground!

## Implementation

For this codesprint, we developed a web crawler that continuously scrapes [Amazon](https://www.amazon.com/) web pages for product description, price, images etc, and stores them in our database. we used Firebase database for data storage. The user can access using a web front-end developed in django framework. This will fetch data from the Firebase backend, and show to the user.

We prepared a mvp for [presentation](https://docs.google.com/presentation/d/1mJd-tliH_aaIJ9IL-4Pju09PfmpIefvBNAUP7U0afDE/edit?usp=sharing)

## Future Works

- Implement elastic search
- Increase efficiency of crawler
- Improve Django frontend

## Contributions

- [Md. Awsaf Alam](awsafalam@gmail.com)
- [Md. Razibul Hasan Mithu](mithu15-882@diu.edu.bd)
- [Muiz Ahmed Khan](muiz.khan@northsouth.edu)
- [Mahmudul Islam](mahmudulislam97@gmail.com)
