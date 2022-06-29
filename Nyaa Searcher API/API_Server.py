from autoscraper import AutoScraper
from flask import Flask, request

scraper = AutoScraper()
scraper.load('Nyaa-search-result.txt')
app = Flask(__name__)

