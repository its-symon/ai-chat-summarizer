from summarizer.message_statistics import calculate_statistics
from summarizer.keyword_analizer import extract_keywords



def generate_summary(user_msgs, ai_msgs):
    stats = calculate_statistics(user_msgs, ai_msgs)
    top_keywords = extract_keywords(user_msgs, ai_msgs)

    if top_keywords:
        topic_keywords = [kw[0] for kw in top_keywords[:1]]
        nature = f"The user asked mainly about {' and '.join(topic_keywords)}."
    else:
        nature = "The conversation was general."

    print("Summary:")
    print(f"- The conversation had {stats['total_messages']} exchanges.")
    print(f"- {nature}")
    print("- Most common keywords:", ", ".join([word for word, _ in top_keywords]))
