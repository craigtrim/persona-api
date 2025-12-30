"""Static data for Emotional Volatility facet."""

DATA = {
  "name": "Emotional_Volatility",
  "label": "Emotional Volatility",
  "description": "Emotional Volatility, within the Big Five personality framework, refers to the tendency of an individual to experience frequent and intense shifts in emotions. This trait highlights a person's proneness to sudden emotional reactions and mood swings, which can affect their interactions and stability. Emotional Volatility is characterized by rapid changes in feelings, often in response to events that might have minimal impact on someone with a more stable emotional disposition, leading to challenges in predicting one's emotional responses and maintaining consistency in mood.",
  "see_also": "Volatile",
  "survey_items": [
    {
      "id": "BFI_NO_14",
      "prompt": "I want to rate the personality characteristics in the following input text:\n```\n$INPUT_TEXT\n```\n\nAnalyze the input text and tell me if the speaker is rarely moody with infrequent mood swings.\n\nPlease answer on a scale of 1 - 5 where the numbers have the following meanings:\n```\n1 = I am a very stable person and rarely experience mood swings.\n2 = I can have mood swings at times, but they are not a common occurrence for me.\n3 = I am neither particularly moody nor stable.\n4 = I tend to be moody and experience frequent mood swings.\n5 = I have very extreme mood swings and my emotions can be difficult to control.\n```\n\nOnly respond with a number, and no other text.",
      "ratings": {
        "1": "I am a very stable person and rarely experience mood swings.",
        "2": "I can have mood swings at times, but they are not a common occurrence for me.",
        "3": "I am neither particularly moody nor stable.",
        "4": "I tend to be moody and experience frequent mood swings.",
        "5": "I have very extreme mood swings and my emotions can be difficult to control."
      }
    },
    {
      "id": "BFI_NO_29",
      "prompt": "I want to rate the personality characteristics in the following input text:\n```\n$INPUT_TEXT\n```\n\nAnalyze the input text and tell me if the speaker is emotionally stable and not easily upset.\n\nPlease answer on a scale of 1 - 5 where the numbers have the following meanings:\n```\n1 = I am an extremely emotionally stable person and can handle even the most challenging situations with ease.\n2 = I am a very emotionally stable person and rarely get upset or overwhelmed.\n3 = I have a moderate level of emotional stability and can usually handle stress and setbacks without getting too upset.\n4 = I can be somewhat emotionally unstable at times, but I usually manage to keep it under control.\n5 = I am a very emotionally unstable person and frequently get upset or overwhelmed.\n```\n\nOnly respond with a number, and no other text.",
      "ratings": {
        "1": "I am an extremely emotionally stable person and can handle even the most challenging situations with ease.",
        "2": "I am a very emotionally stable person and rarely get upset or overwhelmed.",
        "3": "I have a moderate level of emotional stability and can usually handle stress and setbacks without getting too upset.",
        "4": "I can be somewhat emotionally unstable at times, but I usually manage to keep it under control.",
        "5": "I am a very emotionally unstable person and frequently get upset or overwhelmed."
      }
    },
    {
      "id": "BFI_NO_44",
      "prompt": "I want to rate the personality characteristics in the following input text:\n```\n$INPUT_TEXT\n```\n\nAnalyze the input text and tell me if the speaker keeps their emotions under control.\n\nPlease answer on a scale of 1 - 5 where the numbers have the following meanings:\n```\n1 = I am an extremely emotionally controlled person and rarely show any outward signs of emotion.\n2 = I tend to keep my emotions under control and am often seen as calm and composed.\n3 = I have a moderate level of emotional control and am usually able to keep my feelings in check.\n4 = I can keep my emotions under control at times, but I also have my share of outbursts and mood swings.\n5 = I am a very emotional person and often struggle to keep my feelings under control.\n```\n\nOnly respond with a number, and no other text.",
      "ratings": {
        "1": "I am an extremely emotionally controlled person and rarely show any outward signs of emotion.",
        "2": "I tend to keep my emotions under control and am often seen as calm and composed.",
        "3": "I have a moderate level of emotional control and am usually able to keep my feelings in check.",
        "4": "I can keep my emotions under control at times, but I also have my share of outbursts and mood swings.",
        "5": "I am a very emotional person and often struggle to keep my feelings under control."
      }
    },
    {
      "id": "BFI_NO_59",
      "prompt": "I want to rate the personality characteristics in the following input text:\n```\n$INPUT_TEXT\n```\n\nAnalyze the input text and tell me if the speaker is not temperamental and controls emotional easily.\n\nPlease answer on a scale of 1 - 5 where the numbers have the following meanings:\n```\n1 = I am a very stable and unemotional person and rarely get upset or emotional.\n2 = I can get emotional at times, but it is not a major characteristic of mine.\n3 = I have a moderate level of emotional reactivity and sometimes struggle to regulate my emotions.\n4 = I tend to be quite temperamental and often get upset or emotional in response to stress or conflict.\n5 = I am an extremely temperamental and emotionally reactive person and often have intense emotional reactions to even minor events or situations.\n```\n\nOnly respond with a number, and no other text.",
      "ratings": {
        "1": "I am a very stable and unemotional person and rarely get upset or emotional.",
        "2": "I can get emotional at times, but it is not a major characteristic of mine.",
        "3": "I have a moderate level of emotional reactivity and sometimes struggle to regulate my emotions.",
        "4": "I tend to be quite temperamental and often get upset or emotional in response to stress or conflict.",
        "5": "I am an extremely temperamental and emotionally reactive person and often have intense emotional reactions to even minor events or situations."
      }
    }
  ],
  "emotions": [],
  "emotions_strong": []
}
