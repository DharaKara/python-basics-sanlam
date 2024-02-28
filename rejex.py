import re

# Rejex -> Regular Expression
# Pattern match in a string
# number = """
# 38795475, 4985048584, etc
# """
# abc…	Letters
# 123…	Digits
# \d	Any Digit
# \D	Any Non-digit character
# .	Any Character
# \.	Period
# [abc]	Only a, b, or c
# [^abc]	Not a, b, nor c
# [a-z]	Characters a to z
# [0-9]	Numbers 0 to 9
# \w	Any Alphanumeric character
# \W	Any Non-alphanumeric character
# {m}	m Repetitions
# {m,n}	m to n Repetitions
# *	Zero or more repetitions
# +	One or more repetitions
# ?	Optional character
# \s	Any Whitespace
# \S	Any Non-whitespace character
# ^…$	Starts and ends
# (…)	Capture Group
# (a(bc))	Capture Sub-group
# (.*)	Capture all
# (abc|def)	Matches abc or def

# quote = "To be or not to be"
# # r - raw

# # 1. search - present or not (boolean)
# is_be = re.search(r'be$', quote)
# output = "Present" if is_be else "Not resent"
# print(is_be, type(is_be))
# print(output)

# # 2. finaAll - tells you what is found
# quote1 = "funny funy funnnny"
# find_be = re.findall(r'fun[nz]{2}y', quote1)
# print(find_be)

# # 3. match
# text = "This \\ that \\ those"
# matches = re.findall("\\\\", text)
# # raw string - no need of escaping (no \ slash needed)
# matches_r = re.findall(r"\\", text)
# print(matches)
# print(matches_r)

# tweet = "The movie is great, but the spoiler was unexpected. Avoid sharing spoilers!"
# censor_tweet = re.sub(r'(spoiler|but)', '*' * 7, tweet, flags=re.IGNORECASE)
# print(censor_tweet)

# list_websites = "facebook.com, google.com, twitter.in"
# result = re.sub(r'(facebook).com', 'blacklist.com', list_websites)
# print(result)
# result1 = re.sub(r'(\w+)\s+(\.com)', r'\1.subdomain\2', list_websites)
# print(result1)

# names = ["John Doe", "Jane Smith", "Alice Johnson", "Chris Evans"]
# result = [re.sub(r'^(\w+) (\w+)$', r'\2, \1', name) for name in names]
# print(result)

# alternative way to do it without list comp
# result = []
# for name in names:
#     result.append(re.sub(r"(\w+)\s+(\w+)", r"\2, \1", name).strip())

# print(result)

# # Assignment
post = "Loving the #sunny weather in #California. #travel #fun"
# # Output --> ['#sunny', '#California', '#travel', '#fun']
hashtags = re.findall(r"#\w+", post)
print(hashtags)

# Virtual Environment (creates a copy of your python in your repository)
# print() 3.10.8
# print() 3.14 -- 3 years print(f"abc [abc]") breaking change

# ctrl + ~ --> Open/Close Terminal
# python -m venv myenv <- create local copy? yes
# .\myenv\Scripts\Activate.ps1
# deactivate
