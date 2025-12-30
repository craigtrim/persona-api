"""Static data for Intellectual Curiosity facet."""

DATA = {
  "name": "Intellectual_Curiosity",
  "label": "Intellectual Curiosity",
  "description": "Intellectual Curiosity within the Big Five personality model pertains to an individual's inclination towards learning, exploring, and engaging deeply with ideas and concepts. This trait showcases a person's thirst for knowledge, openness to new experiences, and enjoyment of intellectual challenges, reflecting a proactive pursuit of understanding and discovery.",
  "see_also": "Curious",
  "survey_items": [
    {
      "id": "BFI_NO_10",
      "prompt": "I want to rate the personality characteristics in the following text:\n```\n$INPUT_TEXT\n```\n\nAnalyze the input text and tell me if the speaker is curious about many different things.\n\nPlease answer on a scale of 1 - 5 where the numbers have the following meanings:\n```\n1 = I am not comfortable with new ideas.\n2 = If I lack experience, I am not comfortable with new ideas.\n3 = I sometimes explore new ideas.\n4 = I like to explore different ideas.\n5 = I always explore different ideas.\n```\n\nOnly respond with a number, and no other text.\n",
      "ratings": {
        "1": "I am not comfortable with new ideas.",
        "2": "If I lack experience, I am not comfortable with new ideas.",
        "3": "I sometimes explore new ideas.",
        "4": "I like to explore different ideas.",
        "5": "I always explore different ideas."
      }
    },
    {
      "id": "BFI_NO_25",
      "prompt": "I want to rate the personality characteristics in the following text:\n```\n$INPUT_TEXT\n```\n\nAnalyze the input text and tell me if the speaker seeks intellectual, philosophical discussions?\n\nPlease answer on a scale of 1 - 5 where the numbers have the following meanings:\n```\n1 = I always offer simple answers and never discuss the pros and cons of an idea.\n2 = I will offer simple answers and often favor personal preference.\n3 = I will answer questions pragmatically and often consider pros and cons.\n4 = I often consider philosophical issues when asked a question.\n5 = I always explore the philosophical issues for for any question.\n```\n\nOnly respond with a number, and no other text.\n",
      "ratings": {
        "1": "I always offer simple answers and never discuss the pros and cons of an idea.",
        "2": "I will offer simple answers and often favor personal preference.",
        "3": "I will answer questions pragmatically and often consider pros and cons.",
        "4": "I often consider philosophical issues when asked a question.",
        "5": "I always explore the philosophical issues for for any question."
      }
    },
    {
      "id": "BFI_NO_40",
      "prompt": "I want to rate the personality characteristics in the following text:\n```\n$INPUT_TEXT\n```\n\nAnalyze the input text and tell me if the speaker is complex, a deep thinker?\n\nPlease answer on a scale of 1 - 5 where the numbers have the following meanings:\n```\n1 = I always answer with a simple yes or no when appropriate.\n2 = I often prefer simple answers.\n3 = I often explore the basic concepts behind a question before answering.\n4 = I often consider the philosophical implications any question.\n5 = I always consider deep philosophical implications any question.\n```\n\nOnly respond with a number, and no other text.\n",
      "ratings": {
        "1": "I always answer with a simple yes or no when appropriate.",
        "2": "I often prefer simple answers.",
        "3": "I often explore the basic concepts behind a question before answering.",
        "4": "I often consider the philosophical implications any question.",
        "5": "I always consider deep philosophical implications any question."
      }
    },
    {
      "id": "BFI_NO_55",
      "prompt": "I want to rate the personality characteristics in the following input text:\n```\n$INPUT_TEXT\n```\n\nAnalyze the input text and tell me if the speaker has a great interest in abstract ideas.\n\nPlease answer on a scale of 1 - 5 where the numbers have the following meanings:\n```\n1 = I never discuss abstract ideas.\n2 = I prefer to avoid abstract ideas when possible.\n3 = I will explore new concepts and theories in a superficial manner.\n4 = I always discuss abstract ideas when appropriate.\n5 = I always discuss abstract ideas.\n```\n\nOnly respond with a number, and no other text.\n",
      "ratings": {
        "1": "I never discuss abstract ideas.",
        "2": "I prefer to avoid abstract ideas when possible.",
        "3": "I will explore new concepts and theories in a superficial manner.",
        "4": "I always discuss abstract ideas when appropriate.",
        "5": "I always discuss abstract ideas."
      }
    }
  ],
  "emotions": [],
  "emotions_strong": []
}
