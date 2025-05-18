from summarizer.read_chat_log import read_all_chat_log  
from summarizer.message_statistics import calculate_statistics
from summarizer.keyword_analizer import extract_keywords
from summarizer.summary import generate_summary

if __name__ == "__main__":
    folder_path = "Assignment/"
    user_msgs, ai_msgs = read_all_chat_log(folder_path) 

    print("User Messages:")
    for msg in user_msgs:
        print(msg)

    print("AI Messages:")
    for msg in ai_msgs:
        print(msg)

    print("\nStatistics:")
    print(calculate_statistics(user_msgs, ai_msgs))
    print("\nKeywords:")
    print(extract_keywords(user_msgs, ai_msgs))
    generate_summary(user_msgs, ai_msgs)