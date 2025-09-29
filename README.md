# ⚡ GrindGraph: Visualizing the Fitness Grind

## Project Overview

**GrindGraph** is a comprehensive Data Analytics and Visualization project built using Python and Streamlit. It analyzes daily activity, sleep, and calorie expenditure data from a FitBit fitness tracker dataset to uncover user habits, correlations between lifestyle metrics, and key performance indicators. This project showcases proficiency in data wrangling, advanced EDA, and interactive dashboard deployment.

**Project Type:** Data Analytics & Visualization Portfolio Project
**Data Source:** FitBit Fitness Tracker Dataset (Two Merged Exports)
**Key Insight:** Identifying the 'sweet spot' for sleep duration that correlates with peak daily activity (steps).

| Live Dashboard Link | GitHub Repository |
| :--- | :--- |
| https://grindgraph.streamlit.app/?embed_options=light_theme,dark_theme | (https://github.com/harshithreddy-dev/GrindGraph) |

---

## 🛠️ Tech Stack & Tools

* **Python:** The core language for analysis and application logic.
* **Pandas & NumPy:** Essential libraries for data manipulation and cleaning.
* **Plotly Express:** Used for creating the three key interactive and aesthetic visualizations.
* **Streamlit:** Used for rapidly building and deploying the interactive web dashboard.
* **Jupyter:** Used for initial Exploratory Data Analysis (EDA).

---

## 📊 Key Analytical Features & Visualizations

The dashboard provides three primary interactive views to explore fitness habits:

1.  **Steps vs. Calories Burned (Scatter Plot):** Analyzes the strength and linearity of the relationship between steps and energy expenditure, highlighting how **Very Active Minutes** (color) contribute beyond simple step count.
2.  **Average Steps by Day of Week (Bar Chart):** Reveals user activity trends, identifying peak activity days (e.g., weekends) versus trough activity days (e.g., mid-week).
3.  **Sleep vs. Total Steps (Scatter Plot):** Explores the correlation between the **Total Minutes Asleep** and **Total Steps** taken the following day, pinpointing the sleep range required for optimal activity.

---

## ⚙️ Setup and Installation

To run this project locally, follow these steps:

1.  **Clone the Repository:**
    ```bash
    git clone [Link to this Repo]
    cd GrindGraph
    ```

2.  **Create and Activate Environment:**
    ```bash
    python -m venv venv
    # Windows:
    venv\Scripts\activate
    # Mac/Linux:
    source venv/bin/activate
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Data Setup:**
    * Download the FitBit Fitness Tracker Dataset (from Kaggle).
    * Place the two folders (`mturkfitbit_export_...`) containing the CSV files (including `dailyActivity_merged.csv` and `minuteSleep_merged.csv`) inside the **`data/`** directory.

5.  **Run the Dashboard:**
    ```bash
    cd app
    streamlit run dashboard.py
    ```
    The app will open automatically in your browser at `http://localhost:8501`.

---

## ✍️ Author

* **Harshith [Your Last Name]** - [Your LinkedIn Profile Link] - [Your Personal Website or Portfolio Link]
