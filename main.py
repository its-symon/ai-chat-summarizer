from summarizer.read_chat_log import read_chat_log
from summarizer.message_statistics import calculate_statistics


if __name__ == "__main__":
    user_msgs, ai_msgs = read_chat_log("Assignment/chat.txt")
    print(user_msgs)
    print(ai_msgs)
    print(calculate_statistics(user_msgs, ai_msgs))