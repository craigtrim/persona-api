"""Static data for Depression facet."""

DATA = {
  "name": "Depression",
  "label": "Depression",
  "description": "Depression is typically considered to be more of a mood disorder or a clinical condition rather than an emotion or a trait. Emotions are usually more short-lived and can shift and change quickly based on different stimuli, whereas depression is a persistent feeling of sadness, hopelessness, and a lack of interest in enjoyable activities that can last for weeks, months, or even years. Traits, on the other hand, refer to enduring personality characteristics that are relatively stable over time. While people who experience depression may have certain traits, such as low self-esteem or negative thinking patterns, depression itself is typically not considered a trait. However, it is important to note that depression can manifest differently for different individuals and can be influenced by various factors, including genetics, environment, and personal experiences.",
  "see_also": "Depressed",
  "survey_items": [
    {
      "id": "BFI_NO_09",
      "prompt": "I want to rate the personality characteristics in the following input text:\n```\n$INPUT_TEXT\n```\n\nAnalyze the input text and tell me if the speaker stays optimistic after experiencing a setback.\n\nPlease answer on a scale of 1 - 5 where the numbers have the following meanings:\n```\n1 = I am an extremely optimistic person and always try to find the silver lining in any situation.\n2 = I tend to be optimistic and can usually find a way to stay positive even after experiencing a setback.\n3 = I am neither particularly optimistic nor pessimistic.\n4 = I can get discouraged at times, but I usually bounce back pretty quickly.\n5 = I am a very pessimistic person and have trouble seeing the bright side of things.\n```\n\nOnly respond with a number, and no other text.",
      "ratings": {
        "1": "I am an extremely optimistic person and always try to find the silver lining in any situation.",
        "2": "I tend to be optimistic and can usually find a way to stay positive even after experiencing a setback.",
        "3": "I am neither particularly optimistic nor pessimistic.",
        "4": "I can get discouraged at times, but I usually bounce back pretty quickly.",
        "5": "I am a very pessimistic person and have trouble seeing the bright side of things."
      }
    },
    {
      "id": "BFI_NO_24",
      "prompt": "I want to rate the personality characteristics in the following input text:\n```\n$INPUT_TEXT\n```\n\nAnalyze the input text and tell me if the speaker feels secure and comfortable with self.\n\nPlease answer on a scale of 1 - 5 where the numbers have the following meanings:\n```\n1 = I am an extremely self-assured person and always feel confident in myself and my abilities.\n2 = I am a very secure and confident person and rarely doubt myself.\n3 = I have a moderate level of self-confidence and feel generally secure with myself.\n4 = I can be insecure at times, but I generally feel comfortable with who I am.\n5 = I am a very insecure person and often struggle with self-doubt.\n```\n\nOnly respond with a number, and no other text.",
      "ratings": {
        "1": "I am an extremely self-assured person and always feel confident in myself and my abilities.",
        "2": "I am a very secure and confident person and rarely doubt myself.",
        "3": "I have a moderate level of self-confidence and feel generally secure with myself.",
        "4": "I can be insecure at times, but I generally feel comfortable with who I am.",
        "5": "I am a very insecure person and often struggle with self-doubt."
      }
    },
    {
      "id": "BFI_NO_39",
      "prompt": "I want to rate the personality characteristics in the following input text:\n```\n$INPUT_TEXT\n```\n\nAnalyze the input text and tell me if the speaker often feels happy.\n\nPlease answer on a scale of 1 - 5 where the numbers have the following meanings:\n```\n1 = I am a very happy person and rarely feel sad or down.\n2 = I can feel sad at times, but it is not a major concern for me.\n3 = I have a moderate level of sadness and sometimes struggle with negative emotions.\n4 = I tend to feel sad often and often struggle with depression or other mood disorders.\n5 = I am an extremely sad person and frequently struggle with feelings of hopelessness or despair.\n```\n\nOnly respond with a number, and no other text.",
      "ratings": {
        "1": "I am a very happy person and rarely feel sad or down.",
        "2": "I can feel sad at times, but it is not a major concern for me.",
        "3": "I have a moderate level of sadness and sometimes struggle with negative emotions.",
        "4": "I tend to feel sad often and often struggle with depression or other mood disorders.",
        "5": "I am an extremely sad person and frequently struggle with feelings of hopelessness or despair."
      }
    },
    {
      "id": "BFI_NO_54",
      "prompt": "I want to rate the personality characteristics in the following input text:\n```\n$INPUT_TEXT\n```\n\nAnalyze the input text and tell me if the speaker rarely feels depressed or blue.\n\nPlease answer on a scale of 1 - 5 where the numbers have the following meanings:\n```\n1 = I am a very positive person and rarely feel depressed or blue.\n2 = I can feel down or blue at times, but it is not a major concern for me.\n3 = I have a moderate level of sadness or depression and sometimes struggle to stay positive.\n4 = I tend to feel depressed or blue fairly often and often struggle with negative thoughts and emotions.\n5 = I am an extremely depressed and blue person and frequently experience intense feelings of sadness and despair.\n```\n\nOnly respond with a number, and no other text.",
      "ratings": {
        "1": "I am a very positive person and rarely feel depressed or blue.",
        "2": "I can feel down or blue at times, but it is not a major concern for me.",
        "3": "I have a moderate level of sadness or depression and sometimes struggle to stay positive.",
        "4": "I tend to feel depressed or blue fairly often and often struggle with negative thoughts and emotions.",
        "5": "I am an extremely depressed and blue person and frequently experience intense feelings of sadness and despair."
      }
    }
  ],
  "emotions": [],
  "emotions_strong": []
}
