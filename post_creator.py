import csv
import time
from random import randrange
from datetime import datetime, timezone, timedelta

DAY = '2023-04-21'
posts = []

def convert_time(day, csv_time):
    start_string = "%s %s" % (day, csv_time)
    start_time = datetime.strptime(start_string, '%Y-%m-%d %I:%M %p')
    start_timezone = start_time.replace(tzinfo=timezone(timedelta(hours=7)))
    unix_time = time.mktime(start_timezone.timetuple()) + randrange(30)

    return unix_time

def export_posts(posts):
    with open('posts.py', 'w') as file:
        for post in posts:
            file.write("mastodon.status_post(status='%s', scheduled_at=datetime.fromtimestamp(%s)) \n" % (post[0], post[1]))

def livestream_lineup():
    with open('weekend_1_day_3-livestream.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            content = "LIVESTREAM ALERT: " + row['artist'] + " is expected to appear on the " + row['stage'] + " stream. #Coachella #Couchella " + row['url']
            scheduled_time = convert_time(DAY,row['start'])
            posts.append([content, scheduled_time])

def lineup():
    with open('weekend_1_day_3-sets.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
    
        for row in reader:
            if row['end'] != 'CLOSE':
                if row['stage'] == 'Coachella Stage' or row['stage'] == 'Outdoor Theater':
                    content = row['artist'] + " is now playing at the " + row['stage'] + ". #Coachella"
                    scheduled_time = convert_time(DAY,row['start'])
                    posts.append([content, scheduled_time])
                    content = row['artist'] + " has finished playing at the " + row['stage'] + ". " + row['artist'] + " played from " + row['start'] + " to " + row['end'] + ". #coachella"
                    scheduled_time = convert_time(DAY,row['end'])
                    posts.append([content, scheduled_time])
                else:
                    content = row['artist'] + " is now playing at " + row['stage'] + ". #Coachella"
                    scheduled_time = convert_time(DAY,row['start'])
                    posts.append([content, scheduled_time])
                    content = row['artist'] + " has finished playing at " + row['stage'] + ". " + row['artist'] + " played from " + row['start'] + " to " + row['end'] + ". #coachella"
                    scheduled_time = convert_time(DAY,row['end'])
                    posts.append([content, scheduled_time])

livestream_lineup()
#lineup()
export_posts(posts)
