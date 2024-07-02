from . import contact_bp
from flask import Flask, render_template, redirect, url_for, request, flash, session
from models import db, Contact
from .forms import ContactForm