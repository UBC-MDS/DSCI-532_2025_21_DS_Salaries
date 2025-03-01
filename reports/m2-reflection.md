# Which parts of your proposal/sketch you have implemented in your dashboard so far and explain what is not yet implemented.

We have successfully implemented all the required input and output components outlined in our proposal. However, we made some adjustments to the visualization choices based on usability considerations, data characteristics, and effectiveness in conveying insights. These changes are detailed below.

# Changes from Proposal and Justification

## Removal of Job Title as a Filter

Initially, we planned to include Experience Level, Employment Type, Job Title, and Company Location as filters. However, we removed Job Title due to its high cardinality (over 3,000 unique titles).
Users would struggle to locate their exact job title in a dropdown list, making it an inefficient filter. Instead, we introduced a sorted bar chart displaying the top 10 job titles by salary, providing a clearer, more actionable insight for job seekers to assess which titles tend to have higher salaries.

## Bar Chart Instead of Pie Chart for Salary by Experience Level

Our original design included a pie chart for Salary by Experience Level, but we found that it was not effective in showing salary differences across levels. A ranked bar chart was used instead, as it better highlights how experience level impacts salary rather than just showing proportions.

## Removal of Pie Chart for Salary by Employment Type

Since we already have a bar chart visualizing Salary by Employment Type, the proposed pie chart was redundant. The bar chart provides a more meaningful salary comparison across employment types.

## Addition of Two New Visualizations

We introduced two additional visualizations that were not in our original proposal:
- Average Salary Card: Displays the filtered average salary dynamically, giving users immediate insight into salary trends.
- Line Chart for Salary Trends Over Time: Shows how salaries have changed from 2020 to 2023, filtered by Experience Level, Employment Type, and Company Location. This helps users assess salary progression over the years and align their expectations.

# Known Issues or Bugs

Currently, all dashboard functionalities are working as expected, and there are no known bugs or incomplete features.

# Strengths, Limitations, and Future Improvements

## What Our Dashboard Does Well
Provides comprehensive salary insights for Data Science job seekers, helping them assess:
- Salary trends over time. 
- The impact of employment type, company size, and experience level on salaries. 
- Which job titles tend to have the highest salaries.
- Uses effective and interactive visualizations to enhance user experience.

## Limitations and Future Enhancements
- The dataset only covers four years (2020-2023), limiting the long-term salary trend analysis.
    - Future Improvement: Incorporate newer salary data to provide a more complete salary evolution trend.

- Currently, the bar charts remain static, meaning users cannot interact with them beyond filtering other elements.
    - Future Improvement: Consider interactive sorting or drill-down capabilities to make the bar charts more dynamic.