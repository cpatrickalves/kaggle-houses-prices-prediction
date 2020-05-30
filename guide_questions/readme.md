# Guide-questions

It's is important to answer some guide-questions before to start any Data Science project.

1. **Which problem do we wanna solve?** Predict house prices based in more than a hundred of aspects (variables).

2. **Why this project is important?** Guide buyers/sellers to pay/demand fair house prices.

3. **How the solution of this project will be used in practice?** When clients offer their houses on our site, they can be oriented to increase or decrease their offers in order to keep them competitive.  

4. **Does the previous question help to understand the limits to put the solution into production?** It's necessary to select which aspects of a house (feature selection) are more important to predict the price of an offer. The dataset has 163 variables. Besides to become any model "heavy" to use in production, no client will be feel comfortable to fill a form with this amount of fields to use this service.

5. **Which value does it generate to business?** In general, buyers or sellers don't have any idea how much they could pay or demand in an offer for a house. This service can be attractive to clients that don't have knwoledge of the real state market. It's can be a non-free service.

6. **How do we measure success or failure of this project?** We can count how many clients demand this service over the total of offers in the site. If the service is non-free, how much revenue is generated? 

7. **Which are the metrics of business/products we will affect?**
 - Primary metrics: Clients that use the service / total clients
 - Secundary metrics: Increase of revenue after activate the service.