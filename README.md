# 🏡 Hennepin County Parcel Analysis

[![Tableau Views](https://img.shields.io/badge/%F0%9F%91%81%20500%2B%20Views-blue)](https://public.tableau.com/app/profile/adam.ali4282/viz/dasboard_17454428962790/Dashboard1)

This project showcases my end-to-end data skills: cleaning, visualization, and dashboard design — using real-world property data from Hennepin County, MN.

---

## 🔍 Project Summary

- Cleaned raw county parcel data with Python (`clean.py`)
- Built an interactive Tableau dashboard visualizing:
  - 📊 **Top cities by total market value**
  - ⚠️ **Cities with missing build year data**
  - 🌍 **Interactive parcel map by value and municipality**
  - 🏘️ **Property types by total market value (TreeMap)**
- Embedded the dashboard in a Flask web app
- **Published publicly** — [542+ views and counting](https://public.tableau.com/app/profile/adam.ali4282/viz/dasboard_17454428962790/Dashboard1)

---

## 📷 Screenshot

<img src="/Photos/screenshot.png" alt="Tableau Dashboard Screenshot" width="100%">

The screenshot above shows the dashboard layout, highlighting interactive maps and treemaps included in the final product.

---

## 📊 Live Demo

▶️ **[View the interactive dashboard on Tableau Public](https://public.tableau.com/app/profile/adam.ali4282/viz/dasboard_17454428962790/Dashboard1)**

Or view locally using Flask:

```bash
pip install flask
python app.py
```



⚠️ **Data Usage Notice**

The dataset utilized in this project is sourced from the [Hennepin County GIS Open Data Portal](https://gis-hennepin.hub.arcgis.com/datasets/7975aabf6e1e42998a40a4b085ffefdf_1/explore). It is provided free of charge and without the need for a license. However, it is not explicitly licensed under the MIT License. Users are encouraged to review the terms of use on the [Hennepin County GIS Open Data Portal](https://gis-hennepin.hub.arcgis.com/pages/open-data) before utilizing the data.

