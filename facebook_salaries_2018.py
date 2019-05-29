from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://h1bdata.info/index.php?em=Facebook&year=2018'

# Opening up connection, grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# html parsing
page_soup = soup(page_html, "html.parser")

tr = page_soup.findAll('tr')

filename = "Facebook_Salaries_2018.csv"
f = open(filename, "w")

headers = "Job_Role,Pay,Location,State,Submit_Date,Submit_Date_Mo,Submit_Date_Yr,Hire_Date,Hire_Date_Mo,Hire_Date_Yr\n"
f.write(headers)

# Loop

for data in tr[1:]:
    job_role = data.contents[1]
    pay = data.contents[2]
    location = data.contents[3]
    state = data.contents[3]
    submit_date = data.contents[4]
    sdm = data.contents[4]
    sdy = data.contents[4]
    hire_date = data.contents[5]
    hdm = data.contents[5]
    hdy = data.contents[5]

    f.write(job_role.text.replace(",", "").replace("1","").replace("2","").replace("3","").replace("4","").replace("5","").replace("6","").replace("7","").replace("8","").replace("9","").replace("0","").replace(".","").replace("(","").replace(")","")
            + "," + pay.text.replace(",", "") + "," + location.text.replace(",", "") + "," + state.text[-2:] + "," +
            submit_date.text + "," + sdm.text[:2] + "," + sdy.text[-4:] + "," +
            hire_date.text + "," + hdm.text[:2] + "," + hdy.text[-4:] + "\n")

f.close()
