"""Static data for Trust facet."""

DATA = {
  "name": "Trust",
  "label": "Trust",
  "description": "Trust can be considered both an emotion and a trait. As an emotion, trust is a feeling of confidence or reliance in another person or thing. When we trust someone, we feel comfortable and secure in their presence, and we believe that they will act in a way that is consistent with our expectations. As a trait, trustworthiness is a characteristic that enables people to gain the trust of others. Trustworthiness involves being honest, reliable, and responsible, and consistently behaving in a way that inspires confidence in others. Individuals who possess this trait are more likely to build strong relationships and develop a positive reputation in their personal and professional lives. In summary, trust can be considered both an emotion and a trait, with trustworthiness being the trait that enables people to earn trust from others.",
  "see_also": "Trust",
  "survey_items": [
    {
      "id": "BFI_NO_12",
      "prompt": "I want to rate the personality characteristics in the following input text:\n```\n$INPUT_TEXT\n```\n\nAnalyze the input text and tell me if the speaker overlooks faults in others.\n\nPlease answer on a scale of 1 - 5 where the numbers have the following meanings:\n```\n1 = I am an extremely critical person and often find fault with others, even over minor issues.\n2 = I tend to find fault with others and can be somewhat critical at times.\n3 = I am neither particularly critical nor forgiving of others.\n4 = I can be critical of others at times, but I try not to dwell on their faults.\n5 = I am a very forgiving person and rarely find fault with others.\n```\n\nOnly respond with a number, and no other text.",
      "ratings": {
        "1": "I am an extremely critical person and often find fault with others, even over minor issues.",
        "2": "I tend to find fault with others and can be somewhat critical at times.",
        "3": "I am neither particularly critical nor forgiving of others.",
        "4": "I can be critical of others at times, but I try not to dwell on their faults.",
        "5": "I am a very forgiving person and rarely find fault with others."
      }
    },
    {
      "id": "BFI_NO_27",
      "prompt": "I want to rate the personality characteristics in the following input text:\n```\n$INPUT_TEXT\n```\n\nAnalyze the input text and tell me if the speaker is has a forgiving nature.\n\nPlease answer on a scale of 1 - 5 where the numbers have the following meanings:\n```\n1 = I always provide extremely critical feedback and focus on fault-finding.\n2 = I can be critical in my responses\n3 = I avoid critical feedback\n4 = I can be critical in my responses, but I am always kind\n5 = I am very forgiving and never find fault\n```\n\nOnly respond with a number, and no other text.",
      "ratings": {
        "1": "I always provide extremely critical feedback and focus on fault-finding.",
        "2": "I can be critical in my responses",
        "3": "I avoid critical feedback",
        "4": "I can be critical in my responses, but I am always kind",
        "5": "I am very forgiving and never find fault"
      }
    },
    {
      "id": "BFI_NO_42",
      "prompt": "I want to rate the personality characteristics in the following input text:\n```\n$INPUT_TEXT\n```\n\nAnalyze the input text and tell me if the speaker is trusting of others’ intentions.\n\nPlease answer on a scale of 1 - 5 where the numbers have the following meanings:\n```\n1 = I am an extremely suspicious person and frequently mistrust others' intentions.\n2 = I tend to be suspicious of others and often feel like people have hidden agendas.\n3 = I have a moderate level of suspicion and sometimes question others' motives.\n4 = I can be somewhat suspicious at times, but I usually try to give others the benefit of the doubt.\n5 = I am a very trusting person and rarely suspect others of having bad intentions.\n```\n\nOnly respond with a number, and no other text.",
      "ratings": {
        "1": "I am an extremely suspicious person and frequently mistrust others' intentions.",
        "2": "I tend to be suspicious of others and often feel like people have hidden agendas.",
        "3": "I have a moderate level of suspicion and sometimes question others' motives.",
        "4": "I can be somewhat suspicious at times, but I usually try to give others the benefit of the doubt.",
        "5": "I am a very trusting person and rarely suspect others of having bad intentions."
      }
    },
    {
      "id": "BFI_NO_57",
      "prompt": "I want to rate the personality characteristics in the following input text:\n```\n$INPUT_TEXT\n```\n\nAnalyze the input text and tell me if the speaker assumes the best about people.\n\nPlease answer on a scale of 1 - 5 where the numbers have the following meanings:\n```\n1 = I am very suspicious of others and rarely assume the best about people.\n2 = I can be somewhat trusting at times, but I also have my share of skepticism and cynicism.\n3 = I have a moderate level of trust in others and usually try to assume the best about people's intentions.\n4 = I tend to be quite trusting and often give others the benefit of the doubt.\n5 = I am an extremely trusting person and always assume the best about people's motives and actions.\n```\n\nOnly respond with a number, and no other text.",
      "ratings": {
        "1": "I am very suspicious of others and rarely assume the best about people.",
        "2": "I can be somewhat trusting at times, but I also have my share of skepticism and cynicism.",
        "3": "I have a moderate level of trust in others and usually try to assume the best about people's intentions.",
        "4": "I tend to be quite trusting and often give others the benefit of the doubt.",
        "5": "I am an extremely trusting person and always assume the best about people's motives and actions."
      }
    }
  ],
  "emotions": [],
  "emotions_strong": []
}
