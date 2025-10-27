# How to Add Your Content to the Portfolio

This guide will help you add your profile picture, work experience, and additional projects to your portfolio.

## 1. Adding Your Profile Picture

### Option A: Download from LinkedIn
1. Open your LinkedIn profile: https://www.linkedin.com/in/chiti-nkhuwa-62b414159/
2. Right-click on your profile picture
3. Select "Save image as..."
4. Rename it to `profile_picture.jpg`
5. Place it in the `assets/` folder

### Option B: Use an Existing Photo
1. Place your photo in the `assets/` folder
2. Name it `profile_picture.jpg`
3. The app will automatically display it on the Home page

**Supported formats:** JPG, PNG

---

## 2. Adding Work Experience from LinkedIn

1. Open `streamlit_app.py`
2. Find the section marked "Work Experience" (around line 97)
3. Replace the placeholder text `[JOB TITLE]`, `[COMPANY NAME]`, `[MONTH YEAR]` with your actual information

### Example:
```python
st.markdown("### Data Scientist")
st.markdown("**Company:** Tech Company Inc.")
st.markdown("**Duration:** January 2022 - Present")
st.markdown("""
**Description:**
- Developed machine learning models for business analytics
- Led data science initiatives across multiple projects
- Mentored junior data scientists
""")
```

4. Add additional positions by copying the format above
5. Add more sections for each position on your LinkedIn

---

## 3. Adding More GitHub Projects (Projects 5-8)

1. Open `streamlit_app.py`
2. Find the "Additional Projects" section (around line 72)
3. Replace the placeholder text with your actual projects

### Example for Project 5:
```python
show_project_card(
    title="Project Title Here",
    summary="Brief description of your project and what it does.",
    link="https://github.com/ChitiNkhuwa/your-repo-name"
)
```

4. Repeat for projects 6, 7, and 8

---

## 4. Getting Your GitHub Projects

Visit your GitHub profile to see all your repositories:
- https://github.com/ChitiNkhuwa

Pick 8 projects you want to feature:
- 4 should go in "Featured Projects" (already done)
- 4 should go in "Additional Projects" (need to add)

---

## Quick Start Checklist

- [ ] Add profile picture to `assets/profile_picture.jpg`
- [ ] Update Work Experience section with actual positions
- [ ] Add 4 more projects to the "Additional Projects" section
- [ ] Test the app locally: `streamlit run streamlit_app.py`
- [ ] Push to GitHub and deploy!

---

## Tips

- Keep project descriptions concise (1-2 sentences)
- Focus on key technologies and achievements in work experience
- Use clear, action-oriented language
- Highlight measurable outcomes when possible

