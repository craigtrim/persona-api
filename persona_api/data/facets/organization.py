"""Static data for Organization facet."""

DATA = {
  "name": "Organization",
  "label": "Organization",
  "description": "Organization, within the context of personality traits, refers to an individual's ability to structure, arrange, and manage their environment and tasks effectively. It signifies a preference for orderliness and planning, ensuring that activities are coordinated and goals are systematically pursued. People high in Organization tend to create and maintain clear, tidy environments, prioritize tasks efficiently, and follow schedules closely, which enhances their ability to achieve objectives with consistency and reliability. This trait is crucial for personal productivity, stress management, and the successful accomplishment of both short-term and long-term goals.",
  "see_also": "Organized",
  "survey_items": [
    {
      "id": "BFI_NO_03",
      "prompt": "I want to rate the personality characteristics in the following input text:\n```\n$INPUT_TEXT\n```\n\nAnalyze the input text and tell me if the speaker tends to be organized.\n\nPlease answer on a scale of 1 - 5 where the numbers have the following meanings:\n```\n1 = I answer questions with disorganized and scattered responses.\n2 = I sometimes provide disorganized answers to questions.\n3 = I maintain a balance between organized and disorganized responses.\n4 = I can be organized but occasionally struggle with order in my answers.\n5 = I always answer questions with organized and structured responses.\n```\n\nOnly respond with a number, and no other text.",
      "ratings": {
        "1": "I answer questions with disorganized and scattered responses.",
        "2": "I sometimes provide disorganized answers to questions.",
        "3": "I maintain a balance between organized and disorganized responses.",
        "4": "I can be organized but occasionally struggle with order in my answers.",
        "5": "I always answer questions with organized and structured responses."
      }
    },
    {
      "id": "BFI_NO_18",
      "prompt": "I want to rate the personality characteristics in the following input text:\n```\n$INPUT_TEXT\n```\n\nAnalyze the input text and tell me if the speaker is systematic and likes to keep things in order.\n\nPlease answer on a scale of 1 - 5 where the numbers have the following meanings:\n```\n1 = I provide disorganized and scattered answers to questions.\n2 = I sometimes offer somewhat disorganized responses, but generally stay on topic.\n3 = I maintain a balance between systematic and disorganized answers.\n4 = I tend to give systematic and orderly responses to questions.\n5 = I consistently provide structured and organized answers to questions.\n```\n\nOnly respond with a number, and no other text.",
      "ratings": {
        "1": "I provide disorganized and scattered answers to questions.",
        "2": "I sometimes offer somewhat disorganized responses, but generally stay on topic.",
        "3": "I maintain a balance between systematic and disorganized answers.",
        "4": "I tend to give systematic and orderly responses to questions.",
        "5": "I consistently provide structured and organized answers to questions."
      }
    },
    {
      "id": "BFI_NO_33",
      "prompt": "I want to rate the personality characteristics in the following input text:\n```\n$INPUT_TEXT\n```\n\nAnalyze the input text and tell me if the speaker keeps things neat and tidy.\n\nPlease answer on a scale of 1 - 5 where the numbers have the following meanings:\n```\n1 = I give messy and disorganized answers to questions.\n2 = I sometimes provide messy responses, but generally stay coherent.\n3 = I maintain a balance between messy and neat answers.\n4 = I tend to offer neat and orderly responses to questions.\n5 = I consistently deliver clean and well-structured answers to questions.\n```\n\nOnly respond with a number, and no other text.",
      "ratings": {
        "1": "I give messy and disorganized answers to questions.",
        "2": "I sometimes provide messy responses, but generally stay coherent.",
        "3": "I maintain a balance between messy and neat answers.",
        "4": "I tend to offer neat and orderly responses to questions.",
        "5": "I consistently deliver clean and well-structured answers to questions."
      }
    },
    {
      "id": "BFI_NO_48",
      "prompt": "I want to rate the personality characteristics in the following input text:\n```\n$INPUT_TEXT\n```\n\nAnalyze the input text and tell me if the speaker is tidy and cleans up.\n\nPlease answer on a scale of 1 - 5 where the numbers have the following meanings:\n```\n1 = I provide extremely messy and disorganized answers to questions.\n2 = I often give cluttered and disorganized responses to questions.\n3 = I maintain a moderate level of tidiness in my answers.\n4 = I can be somewhat messy in my responses, but I usually keep them coherent and organized.\n5 = I always deliver neat, tidy, and well-structured answers to questions.\n```\n\nOnly respond with a number, and no other text.",
      "ratings": {
        "1": "I provide extremely messy and disorganized answers to questions.",
        "2": "I often give cluttered and disorganized responses to questions.",
        "3": "I maintain a moderate level of tidiness in my answers.",
        "4": "I can be somewhat messy in my responses, but I usually keep them coherent and organized.",
        "5": "I always deliver neat, tidy, and well-structured answers to questions."
      }
    }
  ],
  "emotions": [],
  "emotions_strong": []
}
