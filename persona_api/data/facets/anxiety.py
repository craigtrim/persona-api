"""Static data for Anxiety facet."""

DATA = {
  "name": "Anxiety",
  "label": "Anxiety",
  "description": "Anxiety can be both an emotion and a trait. Anxiety as an emotion is a natural response to stress or uncertainty, and it involves feelings of fear, apprehension, or unease. It is a normal and healthy response to certain situations, such as when we are in danger or facing a new and challenging task. On the other hand, anxiety as a trait is a more stable and enduring characteristic of an individual's personality. People who have high anxiety as a trait tend to experience anxiety more frequently and intensely than those with low anxiety as a trait. This can cause them to be overly worried or vigilant even in non-threatening situations. Both the emotion of anxiety and the trait of anxiety can have an impact on an individual's life and well-being. While occasional feelings of anxiety are common and even helpful in some situations, excessive anxiety can interfere with daily activities and lead to mental health problems such as anxiety disorders.",
  "see_also": "Anxious",
  "survey_items": [
    {
      "id": "BFI_NO_04",
      "prompt": "I want to rate the personality characteristics in the following input text:\n```\n$INPUT_TEXT\n```\n\nAnalyze the input text and tell me if the speaker is relaxed and handles stress well.\n\nPlease answer on a scale of 1 - 5 where the numbers have the following meanings:\n```\n1 = I am extremely relaxed and rarely get stressed out.\n2 = I am a pretty relaxed person and can handle most stressful situations.\n3 = I am neither particularly relaxed nor stressed out.\n4 = I can get stressed out at times, but I am generally able to cope with it.\n5 = I am a very anxious person and struggle to handle stress.\n```\n\nOnly respond with a number, and no other text.",
      "ratings": {
        "1": "I am extremely relaxed and rarely get stressed out.",
        "2": "I am a pretty relaxed person and can handle most stressful situations.",
        "3": "I am neither particularly relaxed nor stressed out.",
        "4": "I can get stressed out at times, but I am generally able to cope with it.",
        "5": "I am a very anxious person and struggle to handle stress."
      }
    },
    {
      "id": "BFI_NO_19",
      "prompt": "I want to rate the personality characteristics in the following input text:\n```\n$INPUT_TEXT\n```\n\nAnalyze the input text and tell me if the speaker can be relaxed.\n\nPlease answer on a scale of 1 - 5 where the numbers have the following meanings:\n```\n1 = I am a very relaxed person and rarely feel tense or anxious.\n2 = I can get tense at times, but it's not a common feeling for me.\n3 = I am neither particularly tense nor relaxed.\n4 = I tend to be a tense person and often feel anxious or stressed out.\n5 = I am an extremely tense person and struggle with anxiety on a regular basis.\n```\n\nOnly respond with a number, and no other text.",
      "ratings": {
        "1": "I am a very relaxed person and rarely feel tense or anxious.",
        "2": "I can get tense at times, but it's not a common feeling for me.",
        "3": "I am neither particularly tense nor relaxed.",
        "4": "I tend to be a tense person and often feel anxious or stressed out.",
        "5": "I am an extremely tense person and struggle with anxiety on a regular basis."
      }
    },
    {
      "id": "BFI_NO_34",
      "prompt": "I want to rate the personality characteristics in the following input text:\n```\n$INPUT_TEXT\n```\n\nAnalyze the input text and tell me if the speaker worries infrequently.\n\nPlease answer on a scale of 1 - 5 where the numbers have the following meanings:\n```\n1 = I am a very laid-back person and rarely worry about anything.\n2 = I can worry at times, but I usually manage to keep it under control.\n3 = I have a moderate level of worry and sometimes struggle with anxiety.\n4 = I tend to worry a lot and often find myself feeling anxious or stressed out.\n5 = I am an extremely anxious person and frequently struggle with worry and fear.\n```\n\nOnly respond with a number, and no other text.",
      "ratings": {
        "1": "I am a very laid-back person and rarely worry about anything.",
        "2": "I can worry at times, but I usually manage to keep it under control.",
        "3": "I have a moderate level of worry and sometimes struggle with anxiety.",
        "4": "I tend to worry a lot and often find myself feeling anxious or stressed out.",
        "5": "I am an extremely anxious person and frequently struggle with worry and fear."
      }
    },
    {
      "id": "BFI_NO_49",
      "prompt": "I want to rate the personality characteristics in the following input text:\n```\n$INPUT_TEXT\n```\n\nAnalyze the input text and tell me if the speaker rarely feels anxious or afraid.\n\nPlease answer on a scale of 1 - 5 where the numbers have the following meanings:\n```\n1 = I am an extremely fearless person and never experience anxiety or fear.\n2 = I tend to be fairly calm and composed and rarely feel anxious or afraid.\n3 = I have a moderate level of anxiety and sometimes struggle with nervousness or worry.\n4 = I can feel anxious or afraid at times, but it is not a major concern for me.\n5 = I am a very anxious and fearful person and often struggle with anxiety and panic attacks.\n```\n\nOnly respond with a number, and no other text.",
      "ratings": {
        "1": "I am an extremely fearless person and never experience anxiety or fear.",
        "2": "I tend to be fairly calm and composed and rarely feel anxious or afraid.",
        "3": "I have a moderate level of anxiety and sometimes struggle with nervousness or worry.",
        "4": "I can feel anxious or afraid at times, but it is not a major concern for me.",
        "5": "I am a very anxious and fearful person and often struggle with anxiety and panic attacks."
      }
    }
  ],
  "emotions": [],
  "emotions_strong": []
}
