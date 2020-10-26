Site where the test was applied: http://www.yahoo.com/ and http://www.google.com/

Measure 1 http request to google web application response time before test: Between 400 and 500 ms
Measure 1 http request to yahoo web application response time before test: Between 3200 and 3300 ms

Measure google web application response time during the test:
Measure yahoo web application response time during the test:


  a) Explain the test in details

    Number of Threads (or Users): Number of Threads are the total number of users that will connect to the web service at once,
    for our test we type 1000

    Loop Count: Loop Count is the number of times an individual user connects to the web service, for our test we select 1

    Ramp-Up Period: The time it takes in seconds for JMeter to model a new user. We’ll set this time to 5 seconds.

    In jmeter tool I added into a test plan a Thread group which represents one user using the application under test,
    so we set it to 1000 in order to create 1000 threads, then the count loop to 1, and the ramp-up to 50,
    and finally for the Thread group I set the duration time to 15 seconds in order to stop the requests.

    Then I review and check the results in jmeter and also I created an html report where I am able to check the responses times
    and analyze the following:

    Response Time Overview shows the number of requests for range of satisfying, so 212 requests where in a range of > 500 ms but
    less than 1500ms and just 13 request with response time > that 1500ms.our

    One thing I noticed is that latency increases each ms that pass.our


  b) Did the load test have an impact on web application response time?

    Yes, while the time was increasing the response time also was increasing ald the threads, so at the
    beginning of the test there is a good response time, but then the yahoo web page start to slow down its responses.

  c) What is the optimal application response time for modern-day web applications?

    Server and application response time refers to the amount of time it takes an application or a server to return
    the results of a submitted request to an end user.

    A one-second response time is generally the maximum acceptable limit, as users still likely won’t notice a delay. Anything more than one second is problematic

  d) Analyze few HTTP/S responses

  Pretty much of the responses returns 200 status code which means that are ok.
  The latency for each request is between 200 and 250ms
  The load time average is around 570 and 620ms.