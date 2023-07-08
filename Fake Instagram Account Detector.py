import requests

def check_fake_account(username):
    # Make a GET request to the Instagram API to fetch user information
    response = requests.get(f"https://www.instagram.com/{username}/?__a=1")

    if response.status_code == 200:
        data = response.json()
        user_data = data["graphql"]["user"]

        follower_count = user_data["edge_followed_by"]["count"]
        following_count = user_data["edge_follow"]["count"]
        post_count = user_data["edge_owner_to_timeline_media"]["count"]
        average_likes = sum([post["node"]["edge_liked_by"]["count"] for post in user_data["edge_owner_to_timeline_media"]["edges"]]) / post_count
        average_comments = sum([post["node"]["edge_media_to_comment"]["count"] for post in user_data["edge_owner_to_timeline_media"]["edges"]]) / post_count

        follower_following_ratio = follower_count / following_count
        engagement_rate = (average_likes + average_comments) / follower_count

        if follower_following_ratio > 10 and engagement_rate < 0.05:
            print(f"The account '{username}' is likely a fake account.")
        else:
            print(f"The account '{username}' seems to be genuine.")
    else:
        print("Unable to fetch user information. Please check the username or try again later.")


if __name__ == "__main__":
    username = input("Enter the Instagram username to check: ")
    check_fake_account(username)
