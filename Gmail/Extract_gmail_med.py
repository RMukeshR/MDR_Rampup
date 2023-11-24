import imaplib
import email
from MDR_Rampup.Gmail.utils import email_id, password


imap_server = "imap.gmail.com"
# email_id = "mukesh992203@gmail.com"
# password = "zyydlpqfykduqttp"
imap = imaplib.IMAP4_SSL(imap_server)
imap.login(email_id,password)

# Assuming 'imap' is your IMAP connection object
imap.select("Inbox")
_, msgnums = imap.search(None, "All")

# List of keywords related to medical topics
medical_keywords = ["health", "medical", "doctor", "prescription", "treatment", "appointment", "diagnosis", "clinic"]

# Open a text file for writing
with open("/home/mukesh/Tensorflow/MDR_Rampup/Gmail/email_info_med.txt", "w") as file:
    for msgnum in msgnums[0].split():
        x, data = imap.fetch(msgnum, "(RFC822)")

        msg = email.message_from_bytes(data[0][1])

        subject = msg.get('Subject')
        
        # Check if the subject contains any medical keywords
        if any(keyword in subject.lower() for keyword in medical_keywords):
            file.write(f"message no. - {msgnum}\n")
            file.write(f"from - {msg.get('From')}\n")
            file.write(f"To - {msg.get('To')}\n")
            file.write(f"Date - {msg.get('Date')}\n")
            file.write(f"Subject - {subject}\n")
            file.write("contents:\n")

            for part in msg.walk():
                if part.get_content_type() == "text/plain":
                    file.write(part.as_string())
                    file.write("\n")  # Add a newline between each part
            
            file.write("\n")  # Add a newline between each part


# Print a message indicating that the information has been saved to the file
print("Email information has been saved to 'email_info.txt'")