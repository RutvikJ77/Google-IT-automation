#!/usr/bin/env python3

#From the reportlab package importing necessary functions to generate a python report
from reportlab.platypus import Paragraph, Spacer, Image, SimpleDocTemplate
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(file, title, add_info):
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(file)
    rep_title = Paragraph(title, styles['h1'])
    rep_info = Paragraph(add_info, styles['BodyText'])
    empty_line = Spacer(1,20)

    report.build([rep_title, empty_line, rep_info, empty_line])