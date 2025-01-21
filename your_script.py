import tweepy
import datetime
from PIL import Image, ImageDraw, ImageFont

# Twitter API credentials (replace with your actual keys)
consumer_key = 'UBf6BcqUrx5zyMPBObFDsalAD'
consumer_secret = 'glJriYXbWTyoaj5T5JeWVy3gg265n9zcDIkMOnQEAIQDMnsE3i'
access_token = '1881764698594672641-WFJiHUWnPXJAl6NUl51KOtHCuJEqKo'
access_token_secret = 'VSZQokK8W1pVYp7CiBT7VcR3t6KFdeo1Jak5f1BUCZ8hN'

# Authenticate with Twitter
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# Function to create a progress bar image
def create_progress_bar(progress_percent):
    width = 500
    height = 100
    background_color = (255, 255, 255)
    progress_color = (0, 128, 0)
    text_color = (0, 0, 0)

    img = Image.new('RGB', (width, height), background_color)
    draw = ImageDraw.Draw(img)

    # Draw the progress bar background
    draw.rectangle([10, 40, width-10, 60], fill=(200, 200, 200))
    # Draw the progress bar foreground
    draw.rectangle([10, 40, 10 + int((width-20) * (progress_percent / 100)), 60], fill=progress_color)

    # Add text
    font = ImageFont.load_default()
    text = f"Progress: {progress_percent}%"
    text_width, text_height = draw.textsize(text, font)
    draw.text(((width - text_width) // 2, 25), text, fill=text_color, font=font)

    img.save("progress_bar.png")

# Calculate days left for the 2029 election
today = datetime.date.today()
target_date = datetime.date(2029, 5, 1)  # Example election date
days_left = (target_date - today).days

# Calculate progress (assuming 2029 election is the target)
start_date = datetime.date(2023, 1, 1)
total_days = (target_date - start_date).days
progress_percent = int(100 - (days_left / total_days) * 100)

# Create progress bar image
create_progress_bar(progress_percent)

# Construct tweet text
tweet_text = f"⏳ **Countdown to YS Jagan Mohan Reddy's Victory in 2029!**\n\n🚀 **Progress Update**: We’re getting closer every day! 🎯 Days Left: {days_left} days (Stay tuned!)\n🔥 Progress: [|||||||||||||||||| {progress_percent}%]\n\nAndhra Pradesh's future is looking brighter! #Election2029 #YSJagan #AndhraPradesh #PoliticalProgress #FutureInMaking"

# Post tweet with image
api.update_status_with_media(status=tweet_text, filename="progress_bar.png")
