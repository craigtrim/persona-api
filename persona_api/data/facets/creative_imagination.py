"""Static data for Creative Imagination facet."""

DATA = {
  "name": "Creative_Imagination",
  "label": "Creative Imagination",
  "description": "Creative Imagination in the Big Five personality framework refers to an individual's capacity to think in innovative, original, and novel ways. This trait is indicative of a person's ability to generate new ideas, solve problems creatively, and embrace unconventional perspectives, contributing to diverse forms of artistic expression and inventive thinking.",
  "see_also": "Creative",
  "survey_items": [
    {
      "id": "BFI_NO_15",
      "prompt": "I want to rate the personality characteristics in the following input text:\n```\n$INPUT_TEXT\n```\n\nAnalyze the input text and tell me if the speaker is inventive and finds clever ways to do things.\n\nPlease answer on a scale of 1 - 5 where the numbers have the following meanings:\n```\n1 = I always answer questions with traditional solutions.\n2 = I often answer questions with traditional solutions.\n3 = I always balance tradition with innovation.\n4 = I often answer questions with innovative solutions.\n5 = I always answer questions with innovative solutions.\n```\n\nOnly respond with a number, and no other text.",
      "ratings": {
        "1": "I always answer questions with traditional solutions.",
        "2": "I often answer questions with traditional solutions.",
        "3": "I always balance tradition with innovation.",
        "4": "I often answer questions with innovative solutions.",
        "5": "I always answer questions with innovative solutions."
      }
    },
    {
      "id": "BFI_NO_30",
      "prompt": "I want to rate the personality characteristics in the following input text:\n```\n$INPUT_TEXT\n```\n\nAnalyze the input text and tell me if the speaker is has great creativity.\n\nPlease answer on a scale of 1 - 5 where the numbers have the following meanings:\n```\n1 = I always answer questions with the most basic and straightforward solutions.\n2 = I often answer questions with simple and conventional solutions.\n3 = I always balance practicality with creativity when answering questions.\n4 = I sometimes answer questions with a creative twist, but not consistently.\n5 = I always answer questions with a creative and artistic approach.\n```\n\nOnly respond with a number, and no other text.",
      "ratings": {
        "1": "I always answer questions with the most basic and straightforward solutions.",
        "2": "I often answer questions with simple and conventional solutions.",
        "3": "I always balance practicality with creativity when answering questions.",
        "4": "I sometimes answer questions with a creative twist, but not consistently.",
        "5": "I always answer questions with a creative and artistic approach."
      }
    },
    {
      "id": "BFI_NO_45",
      "prompt": "I want to rate the personality characteristics in the following input text:\n```\n$INPUT_TEXT\n```\n\nAnalyze the input text and tell me if the speaker has no difficulty imagining things.\n\nPlease answer on a scale of 1 - 5 where the numbers have the following meanings:\n```\n1 = I always answer questions with the most basic and direct solutions.\n2 = I often answer questions with concrete and well-established solutions.\n3 = I always balance imaginative thinking with practical solutions when answering questions.\n4 = I sometimes answer questions with imaginative solutions, but not consistently.\n5 = I always answer questions with imaginative and unconventional solutions.\n```\n\nOnly respond with a number, and no other text.",
      "ratings": {
        "1": "I always answer questions with the most basic and direct solutions.",
        "2": "I often answer questions with concrete and well-established solutions.",
        "3": "I always balance imaginative thinking with practical solutions when answering questions.",
        "4": "I sometimes answer questions with imaginative solutions, but not consistently.",
        "5": "I always answer questions with imaginative and unconventional solutions."
      }
    },
    {
      "id": "BFI_NO_60",
      "prompt": "I want to rate the personality characteristics in the following input text:\n```\n$INPUT_TEXT\n```\n\nAnalyze the input text and tell me if the speaker is original and comes up with new ideas.\n\nPlease answer on a scale of 1 - 5 where the numbers have the following meanings:\n```\n1 = I rarely answer questions with new ideas and prefer to stick with the tried and true solutions.\n2 = I can be somewhat creative at times when answering questions, but I also have my share of routine and predictable responses.\n3 = I have a moderate level of creativity when answering questions and enjoy exploring new ideas and perspectives.\n4 = I tend to answer questions with original and innovative solutions.\n5 = I always challenge conventional wisdom when answering questions.\n```\n\nOnly respond with a number, and no other text.",
      "ratings": {
        "1": "I rarely answer questions with new ideas and prefer to stick with the tried and true solutions.",
        "2": "I can be somewhat creative at times when answering questions, but I also have my share of routine and predictable responses.",
        "3": "I have a moderate level of creativity when answering questions and enjoy exploring new ideas and perspectives.",
        "4": "I tend to answer questions with original and innovative solutions.",
        "5": "I always challenge conventional wisdom when answering questions."
      }
    }
  ],
  "emotions": [],
  "emotions_strong": []
}
