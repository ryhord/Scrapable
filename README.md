#Web Scraping

This application's end goal is to make scraping information from sites much easier.

Currently, the application is built as a Flask web app. Future plans include creating
a Chrome extension that will feed user input to the web app.

##Interface

The app's interface is fairly straight forward. On the user input screen, enter
the url of the page you would like to extract data from. In the second field,
enter an html tag or a css selector that best correlates with the kind info
you want to extract from the page.

As it stands, it can be difficult to return precisely only and all of the specific
information you want. It is largely due to how the page was built in the first place.
Finding a possible way to compensate for inconsistent page design is another future
feature.