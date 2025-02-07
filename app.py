import streamlit as st
import tweepy
import pandas as pd

# Twitter API credentials (Replace with your own keys)
API_KEY = "......"
API_SECRET = "....."
ACCESS_TOKEN = "....."
ACCESS_SECRET = "....."

# Authenticate with Tweepy
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

def get_user_details(username):
    """Fetch user details given a Twitter username."""
    try:
        user = api.get_user(screen_name=username)
        return {
            "User ID": user.id,
            "Username": user.screen_name,
            "Account Creation Date": user.created_at,
            "Profile Description": user.description,
            "Profile Image URL": user.profile_image_url,
            "Number of Followers": user.followers_count,
            "Number of Followings": user.friends_count,
            "Follower-Following Ratio": round(user.followers_count / user.friends_count, 2) if user.friends_count else "N/A",
            "Verified Status": user.verified,
            "Number of Tweets": user.statuses_count,
            "Location": user.location
        }
    except Exception as e:
        st.error(f"Error fetching user details: {e}")
        return None

def get_followers_details(username, max_followers=200):
    """Fetch followers' details up to the given limit."""
    try:
        followers = api.followers(screen_name=username, count=max_followers)
        followers_data = []
        for user in followers:
            followers_data.append({
                "User ID": user.id,
                "Username": user.screen_name,
                "Account Creation Date": user.created_at,
                "Profile Description": user.description,
                "Profile Image URL": user.profile_image_url,
                "Number of Followers": user.followers_count,
                "Number of Followings": user.friends_count,
                "Follower-Following Ratio": round(user.followers_count / user.friends_count, 2) if user.friends_count else "N/A",
                "Verified Status": user.verified,
                "Number of Tweets": user.statuses_count,
                "Location": user.location
            })
        return followers_data
    except Exception as e:
        st.error(f"Error fetching followers details: {e}")
        return []

# Streamlit UI
st.title("Twitter User & Followers Data Collector")
username = st.text_input("Enter Twitter Username (without @):")

if st.button("Fetch Data") and username:
    user_data = get_user_details(username)
    if user_data:
        st.subheader("User Details")
        st.json(user_data)
        
        st.subheader("Fetching Followers Details...")
        followers_data = get_followers_details(username)
        if followers_data:
            df = pd.DataFrame(followers_data)
            st.dataframe(df)
            st.download_button("Download Followers Data", df.to_csv(index=False), "followers_data.csv", "text/csv")
