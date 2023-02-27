#Import warnings
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

#import smptllib
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

#import csv
import csv

#import tk
import tkinter as tk

#Import pandas
import pandas as pd

#Import TexBlob
from textblob import TextBlob

# Load the CSV file
df = pd.read_csv('Your_csv_file_name')

#import time
import time

# Pre-process the data (optional)
# your Questions here in theis format(qestion sample below format)
df['You don’t feel happy even when good things happen?'] = df['You don’t feel happy even when good things happen?'].str.lower()
df['You don’t feel happy even when good things happen?'] = df['You don’t feel happy even when good things happen?'].str.replace('[^\w\s]','')



# Tokenize the text and perform sentiment analysis
#Apply Lambda
df['sentiment_values'] = df['In the past 4 weeks, about how often did you feel tired out for no good reason?'].apply(lambda x: TextBlob(x).sentiment[0])

#Values
df['tired_analysis'] = df['sentiment_values'].apply(lambda x: " you are about to be depressed" if x > 0 else ("you are happy" if x==0 else "you are normal"))

# Count the number of responses for each sentiment label
tired_counts = df['tired_analysis'].value_counts()


# Output the results
print ("calculating_values...")
time.sleep(2)
print ("doing_analysis...")
time.sleep(2)
print("Completed...")
time.sleep(2)

#Rewrite data to original csv file
df.to_csv('Your_csv_file_name', index=False)

print("Sending Emails....")

#send mail

# Read the CSV file
e = pd.read_csv("Your_csv_file_name")


# Log in to the SMTP server with an App Password
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login("your email id", "Your app password")

# Define the email subject

subject = "Result"

# Loop through each row in the CSV file and send an email to the recipient
for index, row in e.iterrows():
    result = row["tired_analysis"]
    print(row["Email ID"])
    
    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = 'email'
    msg['To'] = row["Email ID"]
    msg['Subject'] = subject
    
    # Body- you can change according to your need
    # Note in body - {row["Name"]} will print name in body from collectin it from csv file 
    body = f"""
    Hi {row["Name"]},

    Here is the result of your analysis.
    Your response for the google form that you have filled is given below:- 
    {result}

    Thanks & Regards.
    """

    # Attach the email body
    msg.attach(MIMEText(body, 'plain'))


    # Send the email
    server.sendmail(msg['From'], msg['To'], msg.as_string())

# Close the SMTP server connection
server.quit()

print("Emails sent successfully")

time.sleep(1)

print("opening text box")

time.sleep(2)

# Display the results in a text box
root = tk.Tk()
root.title("Tiredness Analysis Results")

text = tk.Text(root)
text.insert(tk.END, f"Tiredness Analysis Results:\n{tired_counts}")
text.pack()

root.mainloop()

time.sleep(1)
print("Completed")
