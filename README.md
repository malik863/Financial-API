# Financial-API




## Postman endpoints test

### GET /api/transactions/:Test if you can retrieve a list of transactions.
- expected outcome : 200 OK

### POST /api/transactions/: Test if you can create a transaction.
 - expected outcome : 201 created

### GET /api/transactions/<transaction_id>/: Test if you can retrieve a specific transaction by its ID.
- expected outcome : 200 OK

### DELETE /api/transactions/<transaction_id>/: Test if you can delete a transaction.
- expected outcome : 204 No content

### PUT /api/transactions/<transaction_id>/: Test if you can update a transaction.
- expected outcome : 200 OK

### GET /api/users/: Test if you can retrieve the list of users.
- expected outcomes : 200 OK

### GET /api/users/<user_id>/transactions/: Test if you can retrieve transactions by a specific user.
- expected outcome : 200 OK

### GET /api/reports/: Test if you can generate a financial report for a given user, month, and year.
- expected outcome : 200 OK


## Approach
I broke the project into smaller, manageable pieces, focusing on each part individually before moving on. This allowed me to test each component and ensure it was working correctly before advancing to the next.

First, I started with planning, asking key questions like whether I needed separate models for users and transactions, or if I could connect them directly. I also considered whether reporting would require a separate model or if I could simply filter transactions by user, year, or month to generate reports.

I applied the same approach to the API design and views, starting with the transaction model and implementing its features first. This step-by-step process helped me understand the flow of the project and made it easier to debug and test each part. By focusing on one feature at a time, I avoided the confusion of handling all models and views simultaneously, which could lead to errors being harder to track and resolve.


### Challenges Faced During the Project
1- Organizational and Naming Errors
One of the challenges I faced was dealing with errors caused by simple, yet tricky mistakes such as disorganized folder structures or inconsistencies in naming conventions. For example, I encountered an issue where I referred to a field as transaction_date in one part of the code but used date in the serializer. This mismatch led to errors that took time to debug. These kinds of issues stemmed from minor oversights, but they significantly impacted the project and required careful attention to detail.

2- Understanding API Architecture
Grasping the overall architecture of the API was another challenge, particularly when it came to understanding the relationships between the URLs, views, and serializers. Connecting these components correctly was essential for the API to function properly. It took time to fully comprehend how the URLs mapped to the views, and how the views interacted with the models and serializers to handle requests. This understanding was crucial for the successful development of the API.

3- User Creation: 
I was unsure whether the users should be created from the client side (via an API endpoint) or strictly through the Django Admin panel. Deciding this was challenging because it depends on the requirements of the project. If the application is meant to allow end-users to register themselves, then the client-side user creation feature would be necessary. On the other hand, if user creation is restricted to administrators, then it would be simpler to handle everything from the Django Admin interface.

4- Report Functionality: 
I also faced the dilemma of whether the reporting feature should be a separate Django app with its own model, or if it should be integrated into the existing apps and models. Creating a separate app for reports would provide better modularity and scalability, but it might introduce additional complexity if the reporting is tightly linked to the existing models (such as transactions). 

5- User Model and Admin Panel Confusion
One significant challenge I encountered was with the user model and how it interacted with the Admin panel. When I created a custom user model for the app, I noticed that users in the Admin panel, such as the superuser, were being linked to the same user model as the app users who can create transactions. This created confusion, as I expected the Admin users (like superusers) to be separate from the regular users who would be making transactions in the app.


### Addressing the Challenges
When I encountered errors, I focused on understanding what the error message was trying to indicate and identified where it was occurring. If I couldn’t resolve it on my own, I would search for the error online or ask ChatGPT. By researching or troubleshooting various possible causes, I often found a solution by trying different approaches.

For concepts that were unclear, I turned to ChatGPT to explain them. Most of the time, this helped clarify my doubts and provided valuable guidance, allowing me to move forward with a better understanding of the project.
