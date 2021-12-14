# Packages
import streamlit as st 
import pandas as pd

# Database Manage
import sqlite3 
conn = sqlite3.connect('data/world.sqlite')
c = conn.cursor()


# Fn Execution
def sql_executor(raw_code):
	c.execute(raw_code)
	data = c.fetchall()
	return data 


city = ['ID,', 'Name,', 'CountryCode,', 'District,', 'Population']
country = ['Code,', 'Name,', 'Continent,', 'Region,', 'SurfaceArea,', 'IndepYear,', 'Population,', 'LifeExpectancy,', 'GNP,', 'GNPOld,', 'LocalName,', 'GovernmentForm,', 'HeadOfState,', 'Capital,', 'Code2']
countrylanguage = ['CountryCode,', 'Language,', 'IsOfficial,', 'Percentage']




def main():
	st.title("Practice SQL")

	menu = ["Home","About"]
	choice = st.sidebar.selectbox("Menu",menu)

	if choice == "Home":
		st.subheader("Home-Page")
		st.text("Group 13: Muhammad Sohaib, Abid Hussain, 結城, 飞呀, 少年唯有一JIAN ")
		# Columns/Layout
		col1,col2 = st.beta_columns(2)

		with col1:
			with st.form(key='query_form'):
				raw_code = st.text_area("SQL Code here")
				submit_code = st.form_submit_button("Execute")

			# Table of Info

			with st.beta_expander("Table Information"):
				table_info = {'city':city,'country':country,'countrylanguage':countrylanguage}
				st.json(table_info)
			
		# Results Layouts
		with col2:
			if submit_code:
				st.info("Query Submitted")
				st.code(raw_code)

				# Results 
				query_results = sql_executor(raw_code)
				with st.beta_expander("Results"):
					st.write(query_results)

				with st.beta_expander("Pretty Table"):
					query_df = pd.DataFrame(query_results)
					st.dataframe(query_df)


	else:
		st.subheader("About")

		st.text("Built with Streamlit & Pandas")
		st.text("Group 13: Muhammad Sohaib, Abid Hussain, 結城, 飞呀, 少年唯有一JIAN")



if __name__ == '__main__':
	main()

