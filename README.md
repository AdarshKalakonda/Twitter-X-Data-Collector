# Twitter User & Followers Data Collector

This is a **Streamlit** web application that collects detailed data from a Twitter user's profile and their followers using the **Tweepy API**. This tool is useful for analyzing Twitter accounts, studying user behavior, and gathering data for research or marketing purposes. It can be especially beneficial for students or anyone working on data analysis or social media studies.

## Features:
The application collects and displays the following data:

### 1. **User Details**:
   - **User ID**: The unique identifier for the user.
   - **Username**: The Twitter handle of the user.
   - **Account Creation Date**: The date when the Twitter account was created.
   - **Profile Description**: The bio or description provided by the user.
   - **Profile Image URL**: The URL of the user’s profile image.
   - **Number of Followers**: The total number of followers the user has.
   - **Number of Followings**: The total number of accounts the user is following.
   - **Follower-Following Ratio**: The ratio of followers to followings, indicating the user’s social media influence.
   - **Verified Status**: Whether the user is verified (a public figure or notable entity).
   - **Number of Tweets**: The total number of tweets the user has posted.
   - **Location**: The location the user has listed on their profile (if provided).

### 2. **Followers' Details**:
   The app also collects data for the user's followers (up to 200 followers). For each follower, the following details are gathered:
   - **User ID**
   - **Username**
   - **Account Creation Date**
   - **Profile Description**
   - **Profile Image URL**
   - **Number of Followers**
   - **Number of Followings**
   - **Follower-Following Ratio**
   - **Verified Status**
   - **Number of Tweets**
   - **Location**

### 3. **CSV Export**:
   After collecting the follower data, users can export the information as a CSV file for further analysis.

## Use Cases:
This tool can be useful for various purposes:

### For Students:
- **Data Analysis Projects**: Students working on social media data analysis can use this tool to gather Twitter data for their research. It can help with studying trends in follower behavior, engagement, and social media influence.
- **Marketing Analysis**: For students studying marketing or communications, the data can be used to analyze influencer behavior and trends, which can help in understanding how accounts grow their following.
- **Twitter Bot Detection**: Students working on projects for detecting bots can use the data to study patterns in follower count, activity, and behavior.

### For Data Analysts and Researchers:
- **User Research**: Researchers can analyze the data of specific Twitter users to understand user behavior, engagement, and content distribution.
- **Competitor Analysis**: Businesses can use the tool to analyze competitors' Twitter accounts and followers to gain insights into their audience and engagement strategies.
- **Social Media Monitoring**: Social media managers can monitor accounts and track follower growth and trends over time.

### For Marketing and Influencers:
- **Audience Research**: Influencers can use the tool to analyze their followers’ demographics and social media behavior.
- **Targeted Marketing**: Marketers can gather data on potential influencer partnerships by evaluating the follower base of various Twitter accounts.

## How to Use:

### Prerequisites:
1. **Install Dependencies**:
   Before running the app, you need to install the required Python libraries. In the project directory, create a virtual environment (optional but recommended) and install the dependencies from the `requirements.txt` file:
   ```bash
   pip install -r requirements.txt
