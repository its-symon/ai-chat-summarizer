
def calculate_statistics(user_msgs, ai_msgs):
    return {
        "total_messages": len(user_msgs) + len(ai_msgs),
        "user_messages": len(user_msgs),
        "ai_messages": len(ai_msgs),
    }