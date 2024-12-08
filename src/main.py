from typing import Union

from .utils import logger


def get_meaning_of_life(question: str) -> Union[int, str]:
    """Returns the answer to life, universe and everything.

    Args:
        question: An existential question

    Returns:
        42 if the question is about life, error message otherwise
    """
    logger.glitch(f"Reflecting on question: {question}")

    if "life" in question.lower():
        return 42

    raise ValueError("Question not deep enough 🧠")


if __name__ == "__main__":
    result = get_meaning_of_life("What is the meaning of life?")
    logger.success(f"The answer is {result}")
