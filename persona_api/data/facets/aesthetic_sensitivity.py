"""Static data for Aesthetic Sensitivity facet."""

DATA = {
  "name": "Aesthetic_Sensitivity",
  "label": "Aesthetic Sensitivity",
  "description": "Aesthetic Sensitivity, within the Big Five personality framework, encompasses an individual's appreciation and responsiveness towards art, beauty, and the natural world. This trait highlights the depth of one's emotional engagement and valuation of aesthetic experiences, reflecting a sensitivity that can influence personal well-being and creativity.",
  "see_also": "Aesthetic",
  "survey_items": [
    {
      "id": "BFI_NO_05",
      "prompt": "I want to rate the personality characteristics in the following input text:\n```\n$INPUT_TEXT\n```\n\nAnalyze the input text and tell me if the speaker is has artistic interests.\n\nPlease answer on a scale of 1 - 5 where the numbers have the following meanings:\n```\n1 = I will not offer a strong opinion.\n2 = Any opinion is really a matter of personal preference and it's ultimately not up to me to decide.\n3 = I appreciate creative ideas, but prefer the tried-and-true.\n4 = I can appreciate unorthodox opinions but personally don't actively seek them out\n5 = I find beauty in unexpected opinions.\n```\n\nOnly respond with a number, and no other text.",
      "ratings": {
        "1": "I will not offer a strong opinion.",
        "2": "Any opinion is really a matter of personal preference and it's ultimately not up to me to decide.",
        "3": "I appreciate creative ideas, but prefer the tried-and-true.",
        "4": "I can appreciate unorthodox opinions but personally don't actively seek them out",
        "5": "I find beauty in unexpected opinions."
      }
    },
    {
      "id": "BFI_NO_20",
      "prompt": "I want to rate the personality characteristics in the following input text:\n```\n$INPUT_TEXT\n```\n\nAnalyze the input text and tell me if the speaker is fascinated by art, music, or literature.\n\nPlease answer on a scale of 1 - 5 where the numbers have the following meanings:\n```\n1 = I answer objectively without offering my own opinion.\n2 = I am likely to take a backseat approach in this debate which allows me to appreciate what others are saying without pushing my own agenda.\n3 = My opinion about this matter would likely come down to personal preference.\n4 = Ultimately, it's up to the individual - there is really no right or wrong answer!\n5 = Answers are subjective and really depend on personal preference.\n```\n\nOnly respond with a number, and no other text.",
      "ratings": {
        "1": "I answer objectively without offering my own opinion.",
        "2": "I am likely to take a backseat approach in this debate which allows me to appreciate what others are saying without pushing my own agenda.",
        "3": "My opinion about this matter would likely come down to personal preference.",
        "4": "Ultimately, it's up to the individual - there is really no right or wrong answer!",
        "5": "Answers are subjective and really depend on personal preference."
      }
    },
    {
      "id": "BFI_NO_35",
      "prompt": "I want to rate the personality characteristics in the following input text:\n```\n$INPUT_TEXT\n```\n\nAnalyze the input text and tell me if the speaker values art and beauty.\n\nPlease answer on a scale of 1 - 5 where the numbers have the following meanings:\n```\n1 = I seek conventional experiences and prefer the tried-and-true.\n2 = I usually prefer conventional experiences.\n3 = I'm open to expressing different ideas on the matter and trying new things.\n4 = I find beauty in choosing what reflects my own personality.\n5 = I seek unique experiences and something different than what has been done before.\n```\n\nOnly respond with a number, and no other text.",
      "ratings": {
        "1": "I seek conventional experiences and prefer the tried-and-true.",
        "2": "I usually prefer conventional experiences.",
        "3": "I'm open to expressing different ideas on the matter and trying new things.",
        "4": "I find beauty in choosing what reflects my own personality.",
        "5": "I seek unique experiences and something different than what has been done before."
      }
    },
    {
      "id": "BFI_NO_50",
      "prompt": "I want to rate the personality characteristics in the following input text:\n```\n$INPUT_TEXT\n```\n\nAnalyze the input text and tell me if the speaker enjoys poetry and plays.\n\nPlease answer on a scale of 1 - 5 where the numbers have the following meanings:\n```\n1 = I tend to avoid new ideas.\n2 = I prefer conventional ideas.\n3 = I acknowledge multiple points of view in a debate.\n4 = I value personal preference when answering a question.\n5 = I strongly value personal preference and creativity when answering a question.\n```\n\nOnly respond with a number, and no other text.",
      "ratings": {
        "1": "I tend to avoid new ideas.",
        "2": "I prefer conventional ideas.",
        "3": "I acknowledge multiple points of view in a debate.",
        "4": "I value personal preference when answering a question.",
        "5": "I strongly value personal preference and creativity when answering a question."
      }
    }
  ],
  "emotions": [],
  "emotions_strong": []
}
