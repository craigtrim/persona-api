"""Static data for Assertiveness facet."""

DATA = {
  "name": "Assertiveness",
  "label": "Assertiveness",
  "description": "Assertiveness within the Big Five personality framework refers to the degree to which an individual is able to communicate their thoughts, needs, and desires confidently and clearly. It signifies a person's comfort in expressing their own opinions and standing up for themselves while maintaining respect for the views and rights of others. Individuals high in Assertiveness are typically proactive in voicing their ideas and are capable of leadership roles, as they can guide discussions and decisions without hesitation. This trait is crucial for effective interpersonal communication and is often associated with leadership qualities, as it enables individuals to navigate social and professional situations effectively, ensuring their voice is heard and their goals are pursued assertively.",
  "see_also": "Assertive",
  "survey_items": [
    {
      "id": "BFI_NO_06",
      "prompt": "I want to rate the personality characteristics in the following input text:\n```\n$INPUT_TEXT\n```\n\nAnalyze the input text and tell me if the speaker is has an assertive personality.\n\nPlease answer on a scale of 1 - 5 where the numbers have the following meanings:\n```\n1 = I am very passive and tend to let others make decisions for me.\n2 = I can be assertive at times, but I don't always feel comfortable taking charge.\n3 = I have a moderate level of assertiveness.\n4 = I am generally an assertive person and feel comfortable taking charge.\n5 = I have an extremely assertive personality and am always the one in control.\n```\n\nOnly respond with a number, and no other text.",
      "ratings": {
        "1": "I am very passive and tend to let others make decisions for me.",
        "2": "I can be assertive at times, but I don't always feel comfortable taking charge.",
        "3": "I have a moderate level of assertiveness.",
        "4": "I am generally an assertive person and feel comfortable taking charge.",
        "5": "I have an extremely assertive personality and am always the one in control."
      }
    },
    {
      "id": "BFI_NO_21",
      "prompt": "I want to rate the personality characteristics in the following input text:\n```\n$INPUT_TEXT\n```\n\nAnalyze the input text and tell me if the speaker is dominant and acts as a leader.\n\nPlease answer on a scale of 1 - 5 where the numbers have the following meanings:\n```\n1 = I am a very submissive person and prefer to follow others' lead.\n2 = I can be a good follower, but I also have leadership potential.\n3 = I have a moderate level of dominance and can take charge when necessary.\n4 = I tend to be dominant and enjoy taking charge in most situations.\n5 = I am an extremely dominant person and often find myself in leadership positions.\n```\n\nOnly respond with a number, and no other text.",
      "ratings": {
        "1": "I am a very submissive person and prefer to follow others' lead.",
        "2": "I can be a good follower, but I also have leadership potential.",
        "3": "I have a moderate level of dominance and can take charge when necessary.",
        "4": "I tend to be dominant and enjoy taking charge in most situations.",
        "5": "I am an extremely dominant person and often find myself in leadership positions."
      }
    },
    {
      "id": "BFI_NO_36",
      "prompt": "I want to rate the personality characteristics in the following input text:\n```\n$INPUT_TEXT\n```\n\nAnalyze the input text and tell me if the speaker finds it easy to influence people.\n\nPlease answer on a scale of 1 - 5 where the numbers have the following meanings:\n```\n1 = I am an extremely non-influential person and rarely succeed in persuading others.\n2 = I tend to have difficulty influencing others and often struggle to get my point across.\n3 = I have a moderate level of influence and can sometimes persuade others, but not always.\n4 = I can be influential at times, but I also respect others' opinions and perspectives.\n5 = I am a very influential person and often find it easy to persuade others.\n```\n\nOnly respond with a number, and no other text.",
      "ratings": {
        "1": "I am an extremely non-influential person and rarely succeed in persuading others.",
        "2": "I tend to have difficulty influencing others and often struggle to get my point across.",
        "3": "I have a moderate level of influence and can sometimes persuade others, but not always.",
        "4": "I can be influential at times, but I also respect others' opinions and perspectives.",
        "5": "I am a very influential person and often find it easy to persuade others."
      }
    },
    {
      "id": "BFI_NO_51",
      "prompt": "I want to rate the personality characteristics in the following input text:\n```\n$INPUT_TEXT\n```\n\nAnalyze the input text and tell me if the speaker prefers to take charge.\n\nPlease answer on a scale of 1 - 5 where the numbers have the following meanings:\n```\n1 = I prefer to let others take charge and rarely assert myself in group situations.\n2 = I tend to prefer following others and being part of a team rather than taking charge myself.\n3 = I have a moderate level of leadership ability and can take charge when needed but also enjoy following others.\n4 = I can be a leader when necessary, but I also don't mind letting others take charge.\n5 = I prefer to take charge and be the leader in most situations.\n```\n\nOnly respond with a number, and no other text.",
      "ratings": {
        "1": "I prefer to let others take charge and rarely assert myself in group situations.",
        "2": "I tend to prefer following others and being part of a team rather than taking charge myself.",
        "3": "I have a moderate level of leadership ability and can take charge when needed but also enjoy following others.",
        "4": "I can be a leader when necessary, but I also don't mind letting others take charge.",
        "5": "I prefer to take charge and be the leader in most situations."
      }
    }
  ],
  "emotions": [],
  "emotions_strong": []
}
