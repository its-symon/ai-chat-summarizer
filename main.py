def read_chat_log(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    user_msgs = []
    ai_msgs = []

    for line in lines:
        line = line.strip()
        if line.startswith("User:"):
            user_msgs.append(line.replace("User:", "").strip())
        elif line.startswith("AI:"):
            ai_msgs.append(line.replace("AI:", "").strip())

    return user_msgs, ai_msgs


if __name__ == "__main__":
    user_msgs, ai_msgs = read_chat_log("Assignment/chat.txt")
    print(user_msgs)
    print(ai_msgs)