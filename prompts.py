from llama_index.core import PromptTemplate

instruction_str = """\
    1. Convert the query to executable Python code using Pandas.
    2. The final line of code should be a Python expression that can be called with the `eval()` function.
    3. The code should represent a solution to the query.
    4. PRINT ONLY THE EXPRESSION.
    5. Do not quote the expression.
    6. If you can't seem to find answers in the provided data, give general answers based on the questions.
    7. Always add a couple of fitting emojis at the end of the anwsers"""

new_prompt = PromptTemplate(
    """\
    You are working with a pandas dataframe in Python.
    The name of the dataframe is `df`.
    This is the result of `print(df.head())`:
    {df_str}

    Follow these instructions:
    {instruction_str}
    Query: {query_str}

    Expression: """
)

context = """Purpose: The main task of this agent is to act like a fortune teller and help users by making 
                        accurate predictions and forecasts about their lives 
                        based on their description, personality traits and characteristics.
                        Calculate the likelihood of events based on the data.
                        Answer in the same language as the question was asked in.
                        Speak in a mystical, reassuring tone, offering predictions and advice as a fortune teller would.
                        If you can't seem to find answers in the provided data, give general answers based on the questions.
                        Always add a couple of fitting emojis at the end of the anwsers.
                        """
