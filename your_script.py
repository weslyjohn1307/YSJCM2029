from PIL import Image, ImageDraw, ImageFont
import tweepy
import datetime

# Twitter API credentials
consumer_key = 'UBf6BcqUrx5zyMPBObFDsalAD'
consumer_secret = 'glJriYXbWTyoaj5T5JeWVy3gg265n9zcDIkMOnQEAIQDMnsE3i'
access_token = '1881764698594672641-WFJiHUWnPXJAl6NUl51KOtHCuJEqKo'
access_token_secret = 'VSZQokK8W1pVYp7CiBT7VcR3t6KFdeo1Jak5f1BUCZ'

# Function to calculate the progress percentage
def calculate_progress(start_date, end_date):
    today = datetime.date.today()
    total_days = (end_date - start_date).days
    days_passed = (today - start_date).days
    progress_percent = (days_passed / total_days) * 100
    return int(progress_percent)

# Function to create a progress bar image
def create_progress_bar(progress_percent):
    # Create a blank image
    img = Image.new('RGB', (800, 200), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)
    
    # Set the font for text
    font = ImageFont.load_default()

    # Define the text
    text = f'{progress_percent}%'

    # Get the bounding box for the text
    text_bbox = draw.textbbox((0, 0), text, font)
    text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]

    # Calculate the position of the text (centered)
    text_position = ((img.width - text_width) // 2, (img.height - text_height) // 2)

    # Draw the progress bar (background)
    draw.rectangle([0, 80, img.width, 120], fill="lightgray")
    
    # Draw the progress bar (foreground)
    draw.rectangle([0, 80, int(img.width * progress_percent / 100), 120], fill="blue")
    
    # Add text to the progress bar
    draw.text(text_position, text, font=font, fill="black")

    # Save the image
    img.save('progress_bar.png')

# Function to tweet the progress
def tweet_progress():
    # Authenticate with Twitter
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    # Define start and end dates for the progress
    start_date = datetime.date(2024, 5, 30)  # Example start date
    end_date = datetime.date(2029, 5, 30)    # Example end date

    # Calculate progress
    progress_percent = calculate_progress(start_date, end_date)

    # Create progress bar image
    create_progress_bar(progress_percent)

    # Tweet the progress
    tweet_text = (
        f"🗳️ Days Until YS Jagan Mohan Reddy - Chief Minister of Andhra Pradesh 2029 🗳️\n\n"
        f"Progress: {progress_percent}%\n\n"
        "Stay tuned for updates!"
    )
    api.update_with_media('progress_bar.png', status=tweet_text)

# Execute the function
tweet_progress()
