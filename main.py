from dotenv import load_dotenv
load_dotenv()
import pandas as pd
import os
from llama_index.experimental.query_engine import PandasQueryEngine
from prompts import new_prompt, instruction_str, context
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.core.agent import ReActAgent
from llama_index.llms.openai import OpenAI


api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY is not set in the environment variables.")

# Initialisiere das OpenAI-Objekt mit dem API-Schlüssel
llm = OpenAI(api_key=api_key, model="gpt-4o")

def create_query_engine(csv_filename, folder="csv", instruction_str=None, new_prompt=None):
    csv_path = os.path.join(folder, csv_filename)
    df = pd.read_csv(csv_path)
    query_engine = PandasQueryEngine(df=df, verbose=True, instruction_str=instruction_str)
    if new_prompt:
        query_engine.update_prompts({"pandas_prompt": new_prompt})
    return query_engine

# Erstelle Query-Engines für jede CSV-Datei
horoscope_qe = create_query_engine("1_horoscope.csv", instruction_str=instruction_str, new_prompt=new_prompt)
zodiac_qe = create_query_engine("1_zodiac_compatibility.csv", instruction_str=instruction_str, new_prompt=new_prompt)
risk_of_death_qe = create_query_engine("3_risk_of_death.csv", instruction_str=instruction_str, new_prompt=new_prompt)
traffic_accidents_qe = create_query_engine("6_accidents_2005_to_2007.csv", instruction_str=instruction_str, new_prompt=new_prompt)
life_expectancy_qe = create_query_engine("3_life_expectancy_at_birth.csv", instruction_str=instruction_str, new_prompt=new_prompt)
life_and_death_qe = create_query_engine("3_life_and_death.csv", instruction_str=instruction_str, new_prompt=new_prompt)
income_qe = create_query_engine("7_credit_card_approval.csv", instruction_str=instruction_str, new_prompt=new_prompt)
marriage_qe = create_query_engine("2_divorce_marriage.csv", instruction_str=instruction_str, new_prompt=new_prompt)

def create_query_engine_tool(query_engine, name, description):
    return QueryEngineTool(
        query_engine=query_engine,
        metadata=ToolMetadata(
            name=name,
            description=description
        ),
    )
    
tools = [
    create_query_engine_tool(horoscope_qe, "horoscope_data", "This gives detailed information horoscope data"),
    create_query_engine_tool(zodiac_qe, "zodiac_compatibility_data", "This gives detailed information about zodiac compatibility"),
    create_query_engine_tool(risk_of_death_qe, "risk_of_death_data", "This gives detailed information about death and medical data"),
    create_query_engine_tool(traffic_accidents_qe, "traffic_accidents_data", "This gives detailed information about traffic accidents"),
    create_query_engine_tool(life_expectancy_qe, "life_expectancy_data", "This gives detailed information about life expectancy"),
    create_query_engine_tool(life_and_death_qe, "life_and_death_data", "This gives detailed information about the live and death of various people"),
    create_query_engine_tool(income_qe, "income_data", "This gives detailed information about income, jobs, age, etc. of various people"),
    create_query_engine_tool(marriage_qe, "marriage_data", "This gives detailed information about the marriage and divorce of various people"),
]

agent = ReActAgent.from_tools(tools, llm=llm, verbose=True, context=context)

def format_prompt(prompt, user_description):
    return f"{context}\nThought: I need to process the user request and provide an answer.\nAction: query_engine\nInput: {user_description}\n\n{prompt}"

def execute_query(df, query):
    try:
        result = df.loc[
            (df[query['columns'][0]] == query['values'][0]) &
            (df[query['columns'][1]] == query['values'][1]) &
            (df[query['columns'][2]] == query['values'][2]) &
            (df[query['columns'][3]] == query['values'][3]),
            query['output_column']
        ]
        return result
    except KeyError as e:
        return str(e)