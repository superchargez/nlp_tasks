import re
import pandas as pd

def separate_chats(file_name):
    with open(file_name, 'r') as file:
        data = file.read()
    chats = re.split('(?i)(chat link)', data)
    chats = [chat for chat in chats if chat.strip()]
    result = []
    for i in range(0, len(chats), 2):
        result.append(chats[i] + chats[i+1])
    return result

chats = separate_chats("chats_test.txt")

all_chat_history = []

for chat in chats:
    # Remove trailing blank lines from the chat
    chat = chat.rstrip()

    messages = chat.split('\n \n')

    chat_history = []

    for message in messages:
        lines = message.split('\n')
        if len(lines) > 2:
            name = lines[0]
            date = lines[-1]
            text = '\n'.join(lines[1:-1])
            if not re.search(r'\d{1,2}/\d{1,2}/\d{4},\s\d{1,2}:\d{2}:\d{2}\s[AP]M', date):
                date = lines[-2]
                text = '\n'.join(lines[1:-2])
            if re.search(r'\d{1,2}/\d{1,2}/\d{4},\s\d{1,2}:\d{2}:\d{2}\s[AP]M', date):
                chat_history.append({'name': name, 'date': date, 'text': text})

    # Append the chat history to the list of all chat histories
    all_chat_history.extend(chat_history)

# Create a DataFrame from all the chat histories
df = pd.DataFrame(all_chat_history)

# Print the DataFrame
# print(df)
# df

# Filter the DataFrame to only include rows where the name does not contain a 5-character alphanumeric string or 'PTCL' or 'server'
customer_messages = df[~df['name'].str.contains(r'\b[a-zA-Z0-9]{5}\b|PTCL|server', case=False)]

# Print the filtered DataFrame
# print(customer_messages)
customer_messages
