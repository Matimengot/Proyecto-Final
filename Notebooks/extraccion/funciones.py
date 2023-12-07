#Hago una funcion que scrapee el resto de las temporadas

import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup as bs

#Cookies 
options=Options()
options.add_argument(r'user-data-dir=C:\Users\matia\anaconda3\Lib\site-packages\selenium\cookies') #Cargamos las cookies

def scrapeo_laliga(temporada):
    url = f'https://fbref.com/es/comps/12/{temporada}/stats/Estadisticas-{temporada}-La-Liga'
    PATH = 'driver/chromedriver.exe'
    driver = webdriver.Chrome(PATH, options=options)
    driver.get(url)
    html = driver.page_source
    soup = bs(html, 'html.parser')
    tables = soup.find_all('table')
    tdf = pd.read_html(str(tables[11]))
    jugadores = pd.concat(tdf)
    driver.quit()
    jugadores.columns = jugadores.columns.droplevel(0)

    return jugadores

def scrapeo_premier(temporada):
    url = f'https://fbref.com/es/comps/9/{temporada}/stats/Estadisticas-{temporada}-Premier-League'
    PATH = 'driver/chromedriver.exe'
    driver = webdriver.Chrome(PATH, options=options)
    driver.get(url)
    html = driver.page_source
    soup = bs(html, 'html.parser')
    tables = soup.find_all('table')
    tdf = pd.read_html(str(tables[11]))
    jugadores = pd.concat(tdf)
    driver.quit()
    jugadores.columns = jugadores.columns.droplevel(0)

    return jugadores

def scrapeo_serieA(temporada):
    url = f'https://fbref.com/es/comps/11/{temporada}/stats/Estadisticas-{temporada}-Serie-A'
    PATH = 'driver/chromedriver.exe'
    driver = webdriver.Chrome(PATH, options=options)
    driver.get(url)
    html = driver.page_source
    soup = bs(html, 'html.parser')
    tables = soup.find_all('table')
    tdf = pd.read_html(str(tables[11]))
    jugadores = pd.concat(tdf)
    driver.quit()
    jugadores.columns = jugadores.columns.droplevel(0)

    return jugadores