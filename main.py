import pandas as pd
import requests
import numpy as np
from unidecode import unidecode


def read_html_with_lxml(file_path):
    # Read HTML content into DataFrame using read_html()
    df = pd.read_html(file_path, flavor='lxml')
    return df

def read_html_with_requests(file_url):
    # Fetch HTML content using requests
    response = requests.get(file_url)
    # Read HTML content into DataFrame using read_html()
    df = pd.read_html(response.content)[0]
    return df

# File URL
html_file_url = './user.html'

df = read_html_with_lxml(html_file_url)

id_subjects = []
name_subjects = []
tin_chi = []
hp = []
for i in range(len(df[1])):
    # Ten hoc ky
    if "Học kỳ" in str(df[1].iloc[i, 1]):
        continue
    if "Trung bình học kỳ" in str(df[1].iloc[i, 2]):
        continue
    if "Miễn" in str(df[1].iloc[i, 8]):
        continue
    if "PE012" in str(df[1].iloc[i, 1]):
        continue
    id_subjects.append(df[1].iloc[i, 1])
    name_subjects.append(unidecode(df[1].iloc[i, 2]))
    tin_chi.append(df[1].iloc[i, 3])
    hp.append(df[1].iloc[i, 8])
    
data = {'Ma Mon':id_subjects, 'Ten Mon':name_subjects, 'Tin Chi':tin_chi, 'Diem':hp}
 
df = pd.DataFrame(data)
df.to_csv('user.csv', index=True, encoding='utf8')
print(df)
