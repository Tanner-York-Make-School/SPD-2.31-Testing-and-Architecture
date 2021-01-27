# Debug Log

**Explain how you used the techniques covered (Trace Forward, Trace Backward, Divide & Conquer) to uncover the bugs in each exercise. Be specific!**

In your explanations, you may want to answer:

- What is the expected vs. actual output?
- If there is a stack trace, what useful information does it contain?
- Which technique did you use, on which line numbers?
- What assumptions did you have about each line of code, and which ones were proven to be wrong?

_Example: I noticed that the program should show pizza orders once a new order is made and that it wasn't showing any. So, I used the trace forward technique starting on line 13. I discovered the bug on line 27 was caused by a typo of 'pzza' instead of 'pizza'._

_Then I noticed another bug ..._

## Exercise 1

I noticed that I was getting an error for an invalid parameter 'toppings' for the PizzaTopping class and that pizza.size was returning None, meaning it wasn't being created properly or the creation wasn't returning the new object's data. I decided to fix the bug that I knew the location of (toppings parameter) and found that the actual parameter was 'topping_type.' After rerunning the code, I got a new error for the redirect route couldn't be found. This bug was also clear because the error stack trace showed me where it was and quickly found that it needed the name of the route rather than the route itself. I ran it again and didn't get an error. Finally, I was left with the initial error I found with the Pizza not being created properly and this was confirmed when there were no orders showing up on the home page. To fix this issue I decided to look into how Pizzas were being created and see if there were any issues there... There are, it turns out that bother the pizza name, size, and toppings are getting the wrong keys from the request form and that the toppings needed to be getlist rather than just get. After fixing these issues, I was able to save a pizza, see it on the home page, and fulfill the order.

## Exercise 2

I noticed that I was getting a key error for the name field in the request data and after checking the data I found that it was actually getting a 400 error for the response with the message 'Nothing to geocode.' That meant that there was an issue with the params for the request to the API and after checking them I found that both city and units were None. From there, I check the form data we were getting from the request and found that the request.args.get needed to be just 'city' and 'unit.' However, despite getting the proper data from the args, this did not fix the issue. Looking into the API docs, I found that the parameter for city actually needed to be q. Making that change fixed the errors with getting the data but know there was an issue with the temperature key. I found this bug by looking into the JSON that was returned by the API and saw that the key was actually 'temp' rather than 'temperature.' After fixing that bug, I was able to properly get a response and display the data on the frontend.

## Exercise 3

After initially running the code, I received an out of index error on line 37 of the utils file. First, I went to checked if either k or j was causing the issue and I quickly found that neither was because i was incorrectly being used rather than j. After changing i to j the error was fixed. However, I then got another error for list splicing needed to be integers rather than floats on line 51 of the same file. It was clear that the issue here was that the mid equation was returning a float rather than an integer so I changed the single slash to a double slash so that it would return an integer instead and fix the issue. That indeed caused no more errors to be thrown but there were still bugs because merge sort was not sorting the array properly. Since I didn't know where the bug was exactly I started from the start of merge sort to see if I could find the error going through the code. After checking if the algorithm is properly splitting the data and if it is merging correctly, I found that it was splitting correctly but it was not merging the arrays correctly. After adding a few print statements for the output, I found that the issue was accruing when it was setting leftover elements to the list. Looking at it again, I noticed that it was going through all the remaining elements but k was not changing so it would only be changing one index rather than multiple in a row. After fixing this bug, I ran the code and it ran as expected.