# CompanyProfileCrawler

## Brief Description of Crawler Design

The links to each company will be retrieved from a given page. All links will be enqueued to a queue by one thread which keeps going through the page containing the links.

A thread pool retrieve the links from the queue, read the page, store the company profile in Mongo DB.

There will a "Event" object used to block the main thread. After all links are retrieved, this "Event" will be cleared, no longer blocking the main thread.

After "Event" is set AND queue is empty, the main thread exit.


Now this is finished as my first web crawler. Just figured out what to do next. And Let's keep going.