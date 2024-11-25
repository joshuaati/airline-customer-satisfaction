# Airline Customer Satisfaction
Training a machine learning model to predict customer satisfaction

### Problem Statement:
"Can we predict customer satisfaction based on their demographic information, travel details, and service ratings?"

### Objective:
The goal is to build a classification model that predicts whether a customer is satisfied or not based on various input features such as flight experience, service quality, and demographic data.

#### How Solving This Problem Helps the Airlines:
##### Improve Customer Retention:

Understanding the key factors influencing satisfaction can help airlines improve their services for loyal and disloyal customers.
By targeting disloyal customers who are likely unsatisfied, the airline can implement retention strategies (e.g., personalized offers or enhanced services).

#####  Optimize Resource Allocation:

Airlines can identify which aspects of their service (e.g., inflight entertainment, seat comfort, or inflight wifi) most strongly impact satisfaction.
Investments can then be prioritized in areas that most influence positive customer experiences.
Personalize Customer Experience:


##### Reduce Negative Feedback:

By predicting dissatisfaction, airlines can proactively address potential issues, reducing negative feedback and improving their brand reputation.

---

Link to dataset - https://www.kaggle.com/datasets/teejmahal20/airline-passenger-satisfaction/data

---

#### To execute project 
Run `docker build -t midterm-project . --no-cache`

then run `docker run -it --rm -p 9696:9696 midterm-project`

After this the server should be running. You can run `python predict-test.py` to run a sample file and it would give a prediction.