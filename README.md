# CompanyProfileCrawler

## Brief Description of Crawler Design

The links to each company will be retrieved from a given page. All links will be enqueued to a queue by one thread which keeps going through the page containing the links.

A thread pool retrieve the links from the queue, read the page, store the company profile in a json file.

There will a "Event" object used to block the main thread. After all links are retrieved, this "Event" will be cleared, no longer blocking the main thread.

After "Event" is cleared AND queue is empty, the main thread exit.
