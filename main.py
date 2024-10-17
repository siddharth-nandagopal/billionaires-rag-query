from billionaires_rag_query.billionaires_rag_query import run_question_test, BeautifulTableformat, eval_df


query = "How does the age distribution of billionaires compare across different countries?"
result_df1 = run_question_test(query, eval_df.copy())
table = BeautifulTableformat(query, result_df1, 150)
print(table)