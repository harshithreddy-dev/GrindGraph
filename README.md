⚡ GrindGraph: Visualizing the Fitness Grind (No Cap)
"If it ain't on the dashboard, did you even grind?" This project is the vibe check for fitness data.

Project ✨
GrindGraph isn't just an app; it's a deep dive into daily hustle data using Python and Streamlit. We took a raw FitBit dataset, merged a chaotic minute-by-minute sleep log, and delivered actionable tea on activity habits, sleep correlation, and calorie burns.

It's 100% portfolio-ready, showing skills in data wrangling, advanced EDA, and full-stack data deployment.

🌐 Live Dashboard (It Slaps)	🔗 GitHub Repo (You Are Here)
https://grindgraph.streamlit.app/	https://github.com/harshithreddy-dev/GrindGraph

Export to Sheets
🛠️ The Stack (The Tools That Ate)
We kept the tech stack clean and efficient to maximize impact:

Category	Tools Used	Why It's the Goat 🐐
Data Engine	Python, Pandas, NumPy	For merging those messy, mismatched CSVs and cleaning the data (iykyk).
Visualization	Plotly Express	Because static charts are cringe. Plotly gives us those smooth, interactive, zoomable visuals.
Deployment	Streamlit	Turning a Python script into a public, shareable web app in minutes.
Environment	Jupyter, venv	Local testing, robust environment isolation, and clean dependencies.

Export to Sheets
📈 Key Insights & Visuals
The dashboard features three main interactive visualizations designed to extract the most valuable insights:

1. Steps vs. Calories (The Energy Check)
What it shows: The fundamental link between physical activity and energy output.

The Tea: We use color to show Very Active Minutes, proving that intensity matters way more than just clocking steps.

2. Average Steps by Day of Week (The Habit Vibe)
What it shows: Which days are peak grind and which days people take a chill pill.

The Tea: Pinpoints the "Weekend Warrior" effect in the user population, vital for targeted fitness campaigns.

3. Sleep vs. Activity (The Secret Sauce)
What it shows: The correlation between Total Minutes Asleep and Total Steps taken.

The Tea: Discovers the optimal sleep "sweet spot" (typically 5 to 10 hours) required to maximize daily activity, proving balanced rest fuels the best performance.

⚙️ Get the Local Setup (Run It Back)
Wanna clone it and run it on your own machine? It's simple:

Clone the Repo:

Bash

git clone https://github.com/harshithreddy-dev/GrindGraph.git
cd GrindGraph
Setup the Environment:

Bash

python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate # Mac/Linux
Install Dependencies:

Bash

pip install -r requirements.txt
Data Check: Make sure the original downloaded FitBit CSVs (including the two merged folders) are placed inside the data/ directory.

Run the Dashboard:

Bash

cd app
streamlit run dashboard.py
(The app will open automatically at http://localhost:8501).

✍️ Author
This project was built by:

Harshith – [Your LinkedIn Profile Link] – [Your Personal Website or Portfolio Link]

Thanks for checking out the GrindGraph! ✌️
