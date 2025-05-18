import os

def read_all_chat_log(folder_path):
    user_msgs = []
    ai_msgs = []

    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()

            for line in lines:
                line = line.strip()
                if line.startswith("User:"):
                    user_msgs.append(line.replace("User:", "").strip())
                elif line.startswith("AI:"):
                    ai_msgs.append(line.replace("AI:", "").strip())

    return user_msgs, ai_msgs
