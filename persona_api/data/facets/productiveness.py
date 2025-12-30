"""Static data for Productiveness facet."""

DATA = {
  "name": "Productiveness",
  "label": "Productiveness",
  "description": "Productiveness in the context of personality traits reflects an individual's efficiency and effectiveness in completing tasks and achieving goals. It embodies a strong work ethic and a focused approach to tasks at hand, highlighting a person's ability to stay engaged, maintain high levels of energy, and produce significant outcomes over time. Individuals who score high on Productiveness are often driven, disciplined, and capable of managing their time and resources wisely to maximize output. This trait is critical for success in both personal and professional spheres, as it relates directly to one's capacity to fulfill commitments and contribute value through their efforts.",
  "see_also": "Productive",
  "survey_items": [
    {
      "id": "BFI_NO_08",
      "prompt": "I want to rate the personality characteristics in the following input text:\n```\n$INPUT_TEXT\n```\n\nAnalyze the input text and tell me if the speaker tends to be motivated.\n\nPlease answer on a scale of 1 - 5 where the numbers have the following meanings:\n```\n1 = I provide extremely slow and unmotivated answers to questions.\n2 = I tend to give somewhat lazy responses and might struggle to provide thorough answers.\n3 = I maintain a moderate level of motivation in my responses and may occasionally procrastinate.\n4 = I can be slow in my responses at times, but I usually provide satisfactory answers.\n5 = I always deliver prompt, motivated, and well-thought-out answers to questions.\n```\n\nOnly respond with a number, and no other text.",
      "ratings": {
        "1": "I provide extremely slow and unmotivated answers to questions.",
        "2": "I tend to give somewhat lazy responses and might struggle to provide thorough answers.",
        "3": "I maintain a moderate level of motivation in my responses and may occasionally procrastinate.",
        "4": "I can be slow in my responses at times, but I usually provide satisfactory answers.",
        "5": "I always deliver prompt, motivated, and well-thought-out answers to questions."
      }
    },
    {
      "id": "BFI_NO_23",
      "prompt": "I want to rate the personality characteristics in the following input text:\n```\n$INPUT_TEXT\n```\n\nAnalyze the input text and tell me if the speaker has no difficulty getting started on tasks.\n\nPlease answer on a scale of 1 - 5 where the numbers have the following meanings:\n```\n1 = I provide extremely delayed and procrastinative answers to questions.\n2 = I tend to give somewhat delayed responses due to procrastination.\n3 = I maintain a moderate level of procrastination in my answers and might occasionally take longer to respond.\n4 = I can sometimes be slow in my responses but usually manage to provide answers in a timely manner.\n5 = I always deliver prompt, proactive, and timely answers to questions.\n```\n\nOnly respond with a number, and no other text.",
      "ratings": {
        "1": "I provide extremely delayed and procrastinative answers to questions.",
        "2": "I tend to give somewhat delayed responses due to procrastination.",
        "3": "I maintain a moderate level of procrastination in my answers and might occasionally take longer to respond.",
        "4": "I can sometimes be slow in my responses but usually manage to provide answers in a timely manner.",
        "5": "I always deliver prompt, proactive, and timely answers to questions."
      }
    },
    {
      "id": "BFI_NO_38",
      "prompt": "I want to rate the personality characteristics in the following input text:\n```\n$INPUT_TEXT\n```\n\nAnalyze the input text and tell me if the speaker is efficient and gets things done.\n\nPlease answer on a scale of 1 - 5 where the numbers have the following meanings:\n```\n1 = I provide very slow and inefficient answers to questions.\n2 = I can be efficient at times, but may occasionally be slow or procrastinate in my responses.\n3 = I maintain a moderate level of efficiency in my answers and generally respond in a timely manner.\n4 = I tend to give efficient and productive answers to questions.\n5 = I always deliver prompt, efficient, and well-thought-out answers to questions.\n```\n\nOnly respond with a number, and no other text.",
      "ratings": {
        "1": "I provide very slow and inefficient answers to questions.",
        "2": "I can be efficient at times, but may occasionally be slow or procrastinate in my responses.",
        "3": "I maintain a moderate level of efficiency in my answers and generally respond in a timely manner.",
        "4": "I tend to give efficient and productive answers to questions.",
        "5": "I always deliver prompt, efficient, and well-thought-out answers to questions."
      }
    },
    {
      "id": "BFI_NO_53",
      "prompt": "I want to rate the personality characteristics in the following input text:\n```\n$INPUT_TEXT\n```\n\nAnalyze the input text and tell me if the speaker is persistent and works until the task is finished.\n\nPlease answer on a scale of 1 - 5 where the numbers have the following meanings:\n```\n1 = I often provide incomplete and lazy answers to questions.\n2 = I can be persistent in my responses, but may occasionally be distracted or procrastinate.\n3 = I maintain a moderate level of persistence in my answers and generally try to provide complete responses.\n4 = I tend to give persistent and thorough answers to questions, even if it takes more effort.\n5 = I always deliver thorough and persistent answers, ensuring every question is fully addressed.\n```\n\nOnly respond with a number, and no other text.",
      "ratings": {
        "1": "I often provide incomplete and lazy answers to questions.",
        "2": "I can be persistent in my responses, but may occasionally be distracted or procrastinate.",
        "3": "I maintain a moderate level of persistence in my answers and generally try to provide complete responses.",
        "4": "I tend to give persistent and thorough answers to questions, even if it takes more effort.",
        "5": "I always deliver thorough and persistent answers, ensuring every question is fully addressed."
      }
    }
  ],
  "emotions": [],
  "emotions_strong": []
}
