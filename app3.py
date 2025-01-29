# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 11:59:06 2025

@author: TemitopeE
"""
#https://docs.streamlit.io/develop/api-reference/widgets
import streamlit as st
import pandas as pd

# Title of the app
st.title("Researcher Profile Page")

# Collect basic information
name = "Dr. Ekundayo T Cyrus"
field = "Microbiology (Public Health & Environmental Microbiology with focus on Microbial Computational Intelligence)"
institution = "University of Medical Sciences Ondo, Nigeria"
postal = "Departments of (a). Microbiology,  (b). Science Laboratory Technology, and  (c). Pharmaceutical Microbiology & Biotechnology, Faculties of Science and Pharmacy, Odosida Campus Ondo City and Laje Campus Ondo City, respectively."
Vision = "*My vision is to promote computational intelligence research thrusts within my expertise and create new research opportunities by drawing and fusing strengths from different disciplines into a holistic pan-disciplinary research program. The key priorities are ensuring the highest standards of research ethics, innovating, and pioneering new research initiatives.*"
objective = "*My research is both pan-disciplinary and applied in nature to addresses real-world societal problems.*"
# Display basic profile information
st.header("Researcher Overview")
st.write(f"**Name:** {name}")
st.write(f"**Field of Research:** {field}")
st.write(f"**Institution:** {institution}")
st.write(f"**Address:** {postal}")
st.write(f"**Career Vision:** {Vision}")
st.write(f"**Career Objective:** {objective}")
#Research links
st.header("Research links")
Researchgate = " https://www.researchgate.net/profile/Temitope_Ekundayo"
Googlescholar = " https://scholar.google.com/citations?user=o_hvFk8AAAAJ&hl=en"
Scopus  = "https://www.scopus.com/authid/detail.uri?authorId=57204841448"
#Display researh links
st.write(f"**ResearchGate:** {Researchgate}")
st.write(f"**Google scholar:** {Googlescholar}")
st.write(f"**Scopus ID:** {Scopus}")
# Education 
st.header("Education")
phd = "**PhD** (Microbiology), University of Fort Hare, 2019"
msc = "**MTech** (Environmental Microbiology), Federal University of Technology Akure, 2015"
bsc = "**BTech** (Microbiology), Federal University of Technology Akure, 2011"
# Display educational information
st.write(f" {phd}")
st.write(f" {msc}")
st.write(f" {bsc}")

# Membership of Professional Bodies
st.header("Membership of Professional Bodies:")
sasm = "(i)	South African Society for Microbiology"
nsm = "(ii)	Nigerian Society for Microbiology"
asm = "(iii)	American Society for Microbiology"
ami = "(iv)	Applied Microbiology International"
fems = "(v)	Federation of European Microbiology Societies"
ngbn = "(vi)	Nigerian Bioinformatics and Genomics Network"
bsac = "(vii)	British Society for Antimicrobial Chemotherapy"
iafp = "(viii)	International Association for Food Protection"
gbd = "(ix)	Global Burden of Disease Collaborator Network, Institute for Health Metrics and Evaluation | University of Washington."

# Display Membership of Professional Bodies
st.write(f" {sasm}")
st.write(f" {nsm}")
st.write(f" {asm}")
st.write(f" {ami}")
st.write(f" {fems}")
st.write(f" {ngbn}")
st.write(f" {bsac}")
st.write(f" {iafp}")
st.write(f" {gbd}")

# Add a section for publications
st.header("Publications")
uploaded_file = st.file_uploader("Upload a CSV of Publications", type="csv")

if uploaded_file:
    publications = pd.read_csv(uploaded_file)
    st.dataframe(publications)

    # Add filtering for year or keyword
    keyword = st.text_input("Filter by keyword", "")
    if keyword:
        filtered = publications[
            publications.apply(lambda row: keyword.lower() in row.astype(str).str.lower().values, axis=1)
        ]
        st.write(f"Filtered Results for '{keyword}':")
        st.dataframe(filtered)
    else:
        st.write("Showing all publications")

# Add a section for visualizing publication trends
st.header("Publication Trends")
if uploaded_file:
    if "Year" in publications.columns:
        year_counts = publications["Year"].value_counts().sort_index()
        st.bar_chart(year_counts)
    else:
        st.write("The CSV does not have a 'Year' column to visualize trends.")

# Add a contact section
st.header("Contact Information")
email = "ekundyotcyrus@gmail.com"
st.write(f"You can reach {name} at {email}.")
