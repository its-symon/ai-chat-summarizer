from summarizer.read_chat_log import read_chat_log
from summarizer.message_statistics import calculate_statistics
from summarizer.keyword_analizer import extract_keywords


if __name__ == "__main__":
    user_msgs, ai_msgs = read_chat_log("Assignment/chat.txt")
    # print(user_msgs)
    # print(ai_msgs)
    # print(calculate_statistics(user_msgs, ai_msgs))
    print(extract_keywords(user_msgs, ai_msgs))