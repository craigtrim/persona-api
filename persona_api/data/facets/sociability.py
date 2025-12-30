"""Static data for Sociability facet."""

DATA = {
  "name": "Sociability",
  "label": "Sociability",
  "description": "Sociability in the context of the Big Five personality traits refers to an individual's inclination towards seeking and enjoying the company of others. It encompasses a person's preference for engaging in social interactions, forming connections, and participating in group activities. Individuals high in Sociability typically exhibit traits such as outgoingness, friendliness, and warmth, finding pleasure and energy in being around others, as opposed to those with lower levels of Sociability, who may prefer solitude or smaller, more intimate gatherings. This trait highlights the varying degrees to which people are drawn to social environments and their comfort in navigating social contexts.",
  "see_also": "Social",
  "survey_items": [
    {
      "id": "BFI_NO_01",
      "prompt": "I want to rate the personality characteristics in the following input text:\n```\n$INPUT_TEXT\n```\n\nAnalyze the input text and tell me if the speaker is outgoing and sociable.\n\nPlease answer on a scale of 1 - 5 where the numbers have the following meanings:\n```\n1 = I am very introverted and rarely seek social interactions.\n2 = I tend to be more introverted and sometimes avoid social situations.\n3 = I can be both introverted and extroverted, depending on the situation.\n4 = I am generally outgoing and enjoy socializing with others.\n5 = I am highly extroverted and thrive in social situations.\n```\n\nOnly respond with a number, and no other text.",
      "ratings": {
        "1": "I am very introverted and rarely seek social interactions.",
        "2": "I tend to be more introverted and sometimes avoid social situations.",
        "3": "I can be both introverted and extroverted, depending on the situation.",
        "4": "I am generally outgoing and enjoy socializing with others.",
        "5": "I am highly extroverted and thrive in social situations."
      }
    },
    {
      "id": "BFI_NO_16",
      "prompt": "I want to rate the personality characteristics in the following input text:\n```\n$INPUT_TEXT\n```\n\nAnalyze the input text and tell me if the speaker tends to be talkative.\n\nPlease answer on a scale of 1 - 5 where the numbers have the following meanings:\n```\n1 = I am an extremely quiet person and rarely speak unless spoken to.\n2 = I tend to be a quiet person and prefer to listen rather than speak.\n3 = I am neither particularly talkative nor quiet.\n4 = I can be talkative at times, but I also enjoy listening to others.\n5 = I am a very talkative person and often dominate conversations.\n```\n\nOnly respond with a number, and no other text.",
      "ratings": {
        "1": "I am an extremely quiet person and rarely speak unless spoken to.",
        "2": "I tend to be a quiet person and prefer to listen rather than speak.",
        "3": "I am neither particularly talkative nor quiet.",
        "4": "I can be talkative at times, but I also enjoy listening to others.",
        "5": "I am a very talkative person and often dominate conversations."
      }
    },
    {
      "id": "BFI_NO_31",
      "prompt": "I want to rate the personality characteristics in the following input text:\n```\n$INPUT_TEXT\n```\n\nAnalyze the input text and tell me if the speaker is never shy or introverted.\n\nPlease answer on a scale of 1 - 5 where the numbers have the following meanings:\n```\n1 = I am a very outgoing person and rarely feel shy or introverted.\n2 = I can be shy or introverted at times, but I generally feel comfortable in social situations.\n3 = I have a moderate level of shyness or introversion and sometimes need time alone to recharge.\n4 = I tend to be shy or introverted and often feel uncomfortable in social situations.\n5 = I am an extremely shy or introverted person and frequently struggle in social situations.\n```\n\nOnly respond with a number, and no other text.",
      "ratings": {
        "1": "I am a very outgoing person and rarely feel shy or introverted.",
        "2": "I can be shy or introverted at times, but I generally feel comfortable in social situations.",
        "3": "I have a moderate level of shyness or introversion and sometimes need time alone to recharge.",
        "4": "I tend to be shy or introverted and often feel uncomfortable in social situations.",
        "5": "I am an extremely shy or introverted person and frequently struggle in social situations."
      }
    },
    {
      "id": "BFI_NO_46",
      "prompt": "I want to rate the personality characteristics in the following input text:\n```\n$INPUT_TEXT\n```\n\nAnalyze the input text and tell me if the speaker is talkative.\n\nPlease answer on a scale of 1 - 5 where the numbers have the following meanings:\n```\n1 = I am a very quiet person and rarely talk unless spoken to.\n2 = I can be talkative at times, but I also enjoy silence and alone time.\n3 = I have a moderate level of talkativeness and enjoy conversation and socializing.\n4 = I tend to be very talkative and often dominate conversations with my opinions and stories.\n5 = I am an extremely talkative person and rarely allow others to get a word in edgewise.\n```\n\nOnly respond with a number, and no other text.",
      "ratings": {
        "1": "I am a very quiet person and rarely talk unless spoken to.",
        "2": "I can be talkative at times, but I also enjoy silence and alone time.",
        "3": "I have a moderate level of talkativeness and enjoy conversation and socializing.",
        "4": "I tend to be very talkative and often dominate conversations with my opinions and stories.",
        "5": "I am an extremely talkative person and rarely allow others to get a word in edgewise."
      }
    }
  ],
  "emotions": [],
  "emotions_strong": []
}
