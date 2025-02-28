# Which parts of your proposal/sketch you have implemented in your dashboard so far and explain what is not yet implemented.

We implemented all of the required inputs and output components in our dashboard. However, we made some changes to the visualization choices, which is explained below.

# What you have done differently than in your proposal/sketch explain why (e.g. implementation difficulty, explanation for why the new approach is more effective, etc).

- Instead of all of the four filters of Experience Level, Employment Type, Job Title and Compnay Location, we excluded Job Title as a filter input in our dashboard. Since the Job Title contains about 3000 different names in the dataset, it is difficult for users to find the exact one they have. Also, we find the Salary By Job Title chart in our original proposal is redundant since there are too many different names. Thus, we decided to use a sorted bar chart of the top 10 job titles by salary to deliver the information about job title information. A sorted bar chart is more effective since it gives the job seekers to have a better understanding of what kind of job titles may have higher salary which helps them to make better decision.
- Instead of using a pie chart of Salary by Experience Level, we used a ranked bar chart to deliver the similar information. It effectively helps users to find out how experience level gonna affect their salary, while the pie chart cannot show such information and it only gives user a sense of the proportion of people by experience level .
- Since we already have a bar chart of salary by employment type, we don't need the pie chart to show the same information. Thus, we removed it.
- We added two new graphs to the dashboard. One is the Average Salary card and one is a line chart of salary by years. Both of them can be filtered by Experience Level, Employment Type and Company Location. It effectively shows how the average salary changes over years and help them to see whether the salary is expected by them.

# Do you have anything that is not working in your dashboard? Identify them so that we can distinguish between features in development and bugs.

No.

# What you think your dashboard does well currently? what its limitations are? What are good potential future improvements and additions?

Our dashboard effectively included most of the information that the Data Science job seeker may want to know such as the salary changes by year, how different indicators may affect the salary (e.g. employment type, job title, company size, experience level). However, the limitation is that we only have 4 years data (2020-2023), which makes the dataset not efficient to show the salary changes by year. In the future, we may add more data into the dataset.
