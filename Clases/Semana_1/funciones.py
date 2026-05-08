# Imports necesarios para las funciones
import json
import os
import time
import traceback
import re
from pathlib import Path
from io import StringIO, BytesIO
import contextlib
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import requests
import google.generativeai as genai
import urllib.request
