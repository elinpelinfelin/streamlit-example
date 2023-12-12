# pip install trubrics

import os
from trubrics import Trubrics

trubrics = Trubrics(
    project="default",
    email=os.environ["TRUBRICS_EMAIL"],
    password=os.environ["TRUBRICS_PASSWORD"],
)

user_prompt = trubrics.log_prompt(
    config_model={"model": "gpt-3.5-turbo"},
    prompt="Tell me a joke",
    generation="Why did the chicken cross the road? To get to the other side.",
)

user_feedback = trubrics.log_feedback(
    component="default",
    model=user_prompt.config_model.model,
    prompt_id=user_prompt.id,
    user_response={
        "type": "thumbs",
        "score": "👎",
        "text": "Not a very funny joke...",
    }
)