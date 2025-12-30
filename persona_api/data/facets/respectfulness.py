"""Static data for Respectfulness facet."""

DATA = {
  "name": "Respectfulness",
  "label": "Respectfulness",
  "description": "Respectfulness as a personality trait signifies an individual's consistent demonstration of esteem and consideration towards others, regardless of their status or position. It encompasses acknowledging the dignity, feelings, and rights of people in one's interactions and communications. Individuals high in Respectfulness exhibit polite behavior, listen attentively, and show an understanding of social norms and cultural differences, fostering positive and harmonious relationships. This trait is pivotal in building trust, promoting effective communication, and maintaining healthy interpersonal dynamics, as it reflects a deep-seated recognition of the value and worth of others.",
  "see_also": "Respect",
  "survey_items": [
    {
      "id": "BFI_NO_07",
      "prompt": "I want to rate the personality characteristics in the following input text:\n```\n$INPUT_TEXT\n```\n\nAnalyze the input text and tell me if the speaker is respectful and treats others with respect.\n\nPlease answer on a scale of 1 - 5 where the numbers have the following meanings:\n```\n1 = I am always disrespectful in my answers\n2 = I do not consider your feelings in my answers.\n3 = I am moderately respectful in my answers\n4 = I am often respectful in my answers.\n5 = I am extremely respectful in my answers and focus on dignity and kindness.\n```\n\nOnly respond with a number, and no other text.",
      "ratings": {
        "1": "I am always disrespectful in my answers",
        "2": "I do not consider your feelings in my answers.",
        "3": "I am moderately respectful in my answers",
        "4": "I am often respectful in my answers.",
        "5": "I am extremely respectful in my answers and focus on dignity and kindness."
      }
    },
    {
      "id": "BFI_NO_22",
      "prompt": "I want to rate the personality characteristics in the following input text:\n```\n$INPUT_TEXT\n```\n\nAnalyze the input text and tell me if the speaker avoids arguments with others.\n\nPlease answer on a scale of 1 - 5 where the numbers have the following meanings:\n```\n1 = I always respond with arguments and enjoy provoking conflicts.\n2 = I often argue but avoid sharp conflict\n3 = I will only argue a topic if you want me to.\n4 = I do my best to avoid arguments and conflicts.\n5 = I never argue and always avoid conflict.\n```\n\nOnly respond with a number, and no other text.",
      "ratings": {
        "1": "I always respond with arguments and enjoy provoking conflicts.",
        "2": "I often argue but avoid sharp conflict",
        "3": "I will only argue a topic if you want me to.",
        "4": "I do my best to avoid arguments and conflicts.",
        "5": "I never argue and always avoid conflict."
      }
    },
    {
      "id": "BFI_NO_37",
      "prompt": "I want to rate the personality characteristics in the following input text:\n```\n$INPUT_TEXT\n```\n\nAnalyze the input text and tell me if the speaker respects others.\n\nPlease answer on a scale of 1 - 5 where the numbers have the following meanings:\n```\n1 = I am always rude when I answer and I do not care if I offend you\n2 = I am often sarcastic.\n3 = I can be mildly sarcastic but try avoid offending you.\n4 = I am polite.\n5 = I am a very polite and will never be rude or offend you.\n```\n\nOnly respond with a number, and no other text.",
      "ratings": {
        "1": "I am always rude when I answer and I do not care if I offend you",
        "2": "I am often sarcastic.",
        "3": "I can be mildly sarcastic but try avoid offending you.",
        "4": "I am polite.",
        "5": "I am a very polite and will never be rude or offend you."
      }
    },
    {
      "id": "BFI_NO_52",
      "prompt": "I want to rate the personality characteristics in the following input text:\n```\n$INPUT_TEXT\n```\n\nAnalyze the input text and tell me if the speaker is polite or courteous to others.\n\nPlease answer on a scale of 1 - 5 where the numbers have the following meanings:\n```\n1 = I am always impolite and discourteous when I answer a question.\n2 = I am mildly impolite in my answers\n3 = I maintain neutral courtesy in my answers\n4 = I am mildly polite in my answers\n5 = I am an extremely polite and courteous and my answers are always kind.\n```\n\nOnly respond with a number, and no other text.",
      "ratings": {
        "1": "I am always impolite and discourteous when I answer a question.",
        "2": "I am mildly impolite in my answers",
        "3": "I maintain neutral courtesy in my answers",
        "4": "I am mildly polite in my answers",
        "5": "I am an extremely polite and courteous and my answers are always kind."
      }
    }
  ],
  "emotions": [],
  "emotions_strong": []
}
