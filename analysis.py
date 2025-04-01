# Loading in required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

nobel = pd.read_csv('/Users/viragnemeth/Projects/Python/Brief-Analysis-of-Nobel-Prize-Winners/nobel.csv')
print(nobel.columns)

# What is the most commonly awarded gender and birth country?
top_gender = nobel['sex'].value_counts().index[0]
top_country = nobel['birth_country'].value_counts().index[0]

print("\n The gender with the most Nobel laureates is :", top_gender)
print(" The most common birth country of Nobel laureates is :", top_country)

# Which decade had the highest ratio of US-born Nobel Prize winners to total winners in all categories?
nobel['usa_born_winner'] = nobel['birth_country'] == 'United States of America'
nobel['decade'] = (np.floor(nobel['year'] / 10) * 10).astype(int)
prop_usa_winners = nobel.groupby('decade', as_index=False)['usa_born_winner'].mean()
max_decade_usa = prop_usa_winners[prop_usa_winners['usa_born_winner'] == prop_usa_winners['usa_born_winner'].max()]['decade'].values[0]
print('The highest proportion of US-born winners was in ', max_decade_usa)

plt_usa_winners = sns.lineplot(data=prop_usa_winners, x='decade', y='usa_born_winner', marker='o')
plt_usa_winners.set_title('The highest proportion of US-born winners')
plt_usa_winners.set_ylabel('% US Born Winners')
plt_usa_winners.set_xlabel('Decade')
plt_usa_winners.grid(True)
plt.show()

# Which decade and Nobel Prize category combination had the highest proportion of female laureates?
nobel['female_winner'] = nobel['sex'] == 'Female'
prop_female_winners = nobel.groupby(['decade', 'category'], as_index=False).agg({'female_winner': 'mean'})
max_female_decade_category = prop_female_winners[prop_female_winners['female_winner'] == prop_female_winners['female_winner'].max()][['decade', 'category']]
max_female_dict = {max_female_decade_category['decade'].values[0].astype(int): max_female_decade_category['category'].values[0]}
print(max_female_dict)

# Plotting female winners with % winners on the y-axis
plt_fem = sns.lineplot(x='decade', y='female_winner', hue='category', data=prop_female_winners, marker='o')
plt_fem.set_title('Proportion of Female Nobel Prize Winners by Decade')
plt_fem.set_ylabel('% Female Winners')
plt_fem.set_xlabel('Decade')
plt_fem.legend(title='Category')
plt_fem.grid(True)
plt.show()

# Finding the first woman to win a Nobel Prize
female_nobel = nobel[nobel['female_winner']]
earliest_year = female_nobel['year'].min()
first_female_winner = female_nobel[female_nobel['year'] == earliest_year]
first_woman_name = first_female_winner['full_name'].values[0]
first_woman_category = first_female_winner['category'].values[0]
print(f"\n The first woman to win a Nobel prize was {first_woman_name}, in the {first_woman_category} category.")

# Which individuals or organizations have won more than one Nobel Prize throughout the years?
winners_count = nobel['full_name'].value_counts()
multiple_winners = winners_count[winners_count >= 2]
repeat_list = list(multiple_winners.index) 
print(repeat_list)

# Plotting the individuals and organizations with multiple wins
multiple_winners_df = multiple_winners.reset_index()
multiple_winners_df.columns = ['Winner', 'Count']

sns.barplot(data=multiple_winners_df, x='Winner', y='Count', palette='pastel')
plt.title('Top 20 Nobel Prize winners')
plt.xlabel('Winners')
plt.ylabel('Number of wins')
plt.xticks(rotation=90)
plt.yticks(range(1, int(multiple_winners_df['Count'].max()) + 1))
plt.show()