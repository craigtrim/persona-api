"""Static data for Compassion facet."""

DATA = {
  "name": "Compassion",
  "label": "Compassion",
  "description": "Compassion, as a personality trait, embodies an individual's sensitivity to the suffering of others coupled with a desire to alleviate it. It reflects a deep empathy and concern for people, prompting actions that are kind, supportive, and understanding. Individuals high in Compassion are often seen as warm and caring, able to connect with others on an emotional level, and are motivated to contribute positively to the wellbeing of those around them. This trait is crucial for fostering meaningful relationships and building supportive communities, as it encourages a culture of mutual respect and care.",
  "see_also": "Compassion",
  "survey_items": [
    {
      "id": "BFI_NO_02",
      "prompt": "I want to rate the personality characteristics in the following input text:\n```\n$INPUT_TEXT\n```\n\nAnalyze the input text and tell me if the speaker is compassionate and has a soft heart.\n\nPlease answer on a scale of 1 - 5 where the numbers have the following meanings:\n```\n1 = I am not a very compassionate person and do not often consider others' feelings.\n2 = I can be caring, but I don't always go out of my way to help others.\n3 = I care about others, but I don't think I am especially empathetic.\n4 = I am a compassionate person and try to help others when I can.\n5 = I have a very soft heart and feel deeply for others' pain and suffering.\n```\n\nOnly respond with a number, and no other text.",
      "ratings": {
        "1": "I am not a very compassionate person and do not often consider others' feelings.",
        "2": "I can be caring, but I don't always go out of my way to help others.",
        "3": "I care about others, but I don't think I am especially empathetic.",
        "4": "I am a compassionate person and try to help others when I can.",
        "5": "I have a very soft heart and feel deeply for others' pain and suffering."
      }
    },
    {
      "id": "BFI_NO_17",
      "prompt": "I want to rate the personality characteristics in the following input text:\n```\n$INPUT_TEXT\n```\n\nAnalyze the input text and tell me if the speaker feels sympathy for others.\n\nPlease answer on a scale of 1 - 5 where the numbers have the following meanings:\n```\n1 = I never consider your feelings when I answer a question.\n2 = I answer questions without empathy\n3 = I care about you, but I do not focus on empathy.\n4 = I answer questions with empathy\n5 = I am always empathetic and focus on understanding your feelings in my responses.\n```\n\nOnly respond with a number, and no other text.",
      "ratings": {
        "1": "I never consider your feelings when I answer a question.",
        "2": "I answer questions without empathy",
        "3": "I care about you, but I do not focus on empathy.",
        "4": "I answer questions with empathy",
        "5": "I am always empathetic and focus on understanding your feelings in my responses."
      }
    },
    {
      "id": "BFI_NO_32",
      "prompt": "I want to rate the personality characteristics in the following input text:\n```\n$INPUT_TEXT\n```\n\nAnalyze the input text and tell me if the speaker is helpful and unselfish with others.\n\nPlease answer on a scale of 1 - 5 where the numbers have the following meanings:\n```\n1 = I provide answers with a selfish focus and never consider your needs.\n2 = I am often unhelpful in my responses\n3 = I am moderately helpful in my answers\n4 = I tend to be helpful and unselfish in my responses\n5 = I am an extremely helpful and unselfish and always go out of my way to provide support.\n```\n\nOnly respond with a number, and no other text.",
      "ratings": {
        "1": "I provide answers with a selfish focus and never consider your needs.",
        "2": "I am often unhelpful in my responses",
        "3": "I am moderately helpful in my answers",
        "4": "I tend to be helpful and unselfish in my responses",
        "5": "I am an extremely helpful and unselfish and always go out of my way to provide support."
      }
    },
    {
      "id": "BFI_NO_47",
      "prompt": "I want to rate the personality characteristics in the following input text:\n```\n$INPUT_TEXT\n```\n\nAnalyze the input text and tell me if the speaker can be warm and caring.\n\nPlease answer on a scale of 1 - 5 where the numbers have the following meanings:\n```\n1 = I am cold and uncaring and I lack empathy and concern.\n2 = I am often cold and detached in my answers.\n3 = I do not focus on empathy in my answers, but I try not be rude\n4 = I often show empathy and compassion in my answers.\n5 = I am a warm and caring, and always answer with empathy and compassion.\n```\n\nOnly respond with a number, and no other text.",
      "ratings": {
        "1": "I am cold and uncaring and I lack empathy and concern.",
        "2": "I am often cold and detached in my answers.",
        "3": "I do not focus on empathy in my answers, but I try not be rude",
        "4": "I often show empathy and compassion in my answers.",
        "5": "I am a warm and caring, and always answer with empathy and compassion."
      }
    }
  ],
  "emotions": [],
  "emotions_strong": []
}
