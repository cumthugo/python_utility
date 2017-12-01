from selenium import webdriver
import time
import os
import pandas as pd
import datetime

username = "qli23"
password = "njtcn0121"

DownloadDir = r'C:\Users\yzhang66\Downloads'

def del_csv(root_dir=r'C:\Users\yzhang66\Downloads'):
    file_list = os.listdir(root_dir)
    for f in file_list:
        file_path = os.path.join(root_dir, f)
        if os.path.isfile(file_path):
            if f.endswith(".csv") or f.endswith(".CSV") or f.endswith(".csvx"):
                os.remove(file_path)
                #print " File removed! " + file_path
       
def correctSubtitleEncoding(filename, newFilename, encoding_from, encoding_to='UTF-8'):
    with open(filename, 'r', encoding=encoding_from) as fr:
        with open(newFilename, 'w', encoding=encoding_to) as fw:
            for line in fr:
                fw.write(line[:-1]+'\n')

date = datetime.date.today().strftime("%Y%m%d")           
del_csv(DownloadDir)

b = webdriver.Chrome(executable_path=r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
b.get("http://136.18.229.13/login")
b.find_element_by_id("username").send_keys(username)
b.find_element_by_id("password").send_keys(password)
b.find_element_by_name("login").click()
b.get("http://136.18.229.13/projects")

projects_obj = b.find_elements_by_partial_link_text("COMMON")

projects_name = []

has_nc_projects = []
for pro_obj in projects_obj:
    projects_name.append(pro_obj.text)

for pName in projects_name:
    b.get("http://136.18.229.13/projects")
    try:
        b.find_element_by_link_text(pName).click()
        b.find_element_by_link_text("NCs").click()
        t = b.find_element_by_xpath(r'//*[@id="content"]/p[1]')
        if t.text == u'没有任何数据可供显示':
            print(pName  + ' has no NCs!')
        else:
            b.find_element_by_link_text("CSV").click()
            b.find_element_by_xpath(r'//*[@id="csv-export-form"]/p[3]/input[1]').click()
            time.sleep(1)
            has_nc_projects.append(pName)
    except:
        print('not found')
b.quit()

all_NCs = pd.DataFrame()
for pName in has_nc_projects:
    file_path_a = os.path.join(DownloadDir, pName.replace(':','-')+'_NCs.csv')
    correctSubtitleEncoding(file_path_a,file_path_a+'x','gbk')
    csvframe = pd.read_csv(file_path_a+'x')
    csvframe.insert(1,'Project',pName[11:])
    print(pName,'is mergeing')
    if all_NCs.empty:
        print('nc is empty')
        all_NCs = csvframe
    else:
    #all_NCs.merge(csvframe,on=u'#')
        all_NCs = pd.concat([all_NCs,csvframe])
all_NCs.index = all_NCs['#']
all_NCs.index.name = 'id'
del all_NCs['#']
all_NCs.to_excel(os.path.join(DownloadDir, 'All_NCs_'+ date + '.xlsx'))
del_csv(DownloadDir)
print('Done')
