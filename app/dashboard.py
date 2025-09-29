import streamlit as st
import pandas as pd
import os
import plotly.express as px

# Set the main configuration for the app
st.set_page_config(
    page_title="GrindGraph: Fitness Data Analytics",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Function to load and merge data (REUSE YOUR NOTEBOOK CODE HERE!)
@st.cache_data
def load_data():
    # --- PATHS ---
    # Adjust these paths if your project structure is different!
    folder1 = "C:/GrindGraph/data/mturkfitbit_export_3.12.16-4.11.16/Fitabase Data 3.12.16-4.11.16"
    folder2 = "C:/GrindGraph/data/mturkfitbit_export_4.12.16-5.12.16/Fitabase Data 4.12.16-5.12.16"

    # --- 1. Load and Merge Activity Data ---
    df1_activity = pd.read_csv(os.path.join(folder1, "dailyActivity_merged.csv"))
    df2_activity = pd.read_csv(os.path.join(folder2, "dailyActivity_merged.csv"))
    df = pd.concat([df1_activity, df2_activity], ignore_index=True)
    
    # Data Cleaning and Feature Engineering (Activity)
    df.rename(columns={'ActivityDate': 'Date'}, inplace=True)
    df['Date'] = pd.to_datetime(df['Date'])
    df['Weekday'] = df['Date'].dt.day_name()
    
    # --- 2. Load, Aggregate, and Merge Sleep Data ---
    
    try:
        # Load the granular minuteSleep data (using the correct file name you identified)
        df_sleep1 = pd.read_csv(os.path.join(folder1, "minuteSleep_merged.csv"))
        df_sleep2 = pd.read_csv(os.path.join(folder2, "minuteSleep_merged.csv"))

        minute_sleep_data = pd.concat([df_sleep1, df_sleep2], ignore_index=True)

        # Clean and format the date column
        minute_sleep_data['ActivityDate'] = pd.to_datetime(minute_sleep_data['date']).dt.date
        
        # Aggregate the minute data to daily totals
        daily_sleep_summary = minute_sleep_data.groupby(['Id', 'ActivityDate']).agg(
            TotalMinutesAsleep=('value', 'sum')
        ).reset_index()

        daily_sleep_summary['ActivityDate'] = pd.to_datetime(daily_sleep_summary['ActivityDate'])
        
        # Merge the main activity DataFrame (df) with the new daily sleep summary
        # Merge on 'Id' and the corrected date columns
        df_merged = pd.merge(df, daily_sleep_summary[['Id', 'ActivityDate', 'TotalMinutesAsleep']], 
                            left_on=['Id', 'Date'], 
                            right_on=['Id', 'ActivityDate'], 
                            how='left')
        
        # Drop the redundant ActivityDate column from the merge
        df_merged.drop(columns=['ActivityDate'], inplace=True)
        
        return df_merged
        
    except FileNotFoundError as e:
        st.error(f"FATAL ERROR: Sleep file not found. Check path: {e}")
        # If sleep data fails to load, still return the main activity data 
        # but the sleep column will be missing, causing the KeyError later.
        # This is why the path must be right!
        return df 

# The rest of the dashboard.py code remains the same.
# Load the data
df = load_data()

# --- DASHBOARD LAYOUT ---

# Title Section
st.title("⚡ GrindGraph: Daily Activity Insights")
st.markdown("A portfolio project analyzing FitBit Fitness Tracker data.")

# Sidebar Filters (Example)
st.sidebar.header("Data Filter")

# Example 1: Date Range Selector
min_date = df['Date'].min().date()
max_date = df['Date'].max().date()
date_range = st.sidebar.date_input(
    "Select Date Range",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)

# Example 2: Activity Level Slider
max_steps = int(df['TotalSteps'].max())
step_filter = st.sidebar.slider(
    "Minimum Steps",
    min_value=0,
    max_value=max_steps,
    value=5000,
    step=500
)

# Apply filters to the DataFrame
if len(date_range) == 2:
    start_date, end_date = pd.to_datetime(date_range[0]), pd.to_datetime(date_range[1])
    df_filtered = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]
else:
    df_filtered = df

df_filtered = df_filtered[df_filtered['TotalSteps'] >= step_filter]


# Display the Filtered Data (Basic check)
st.subheader("Data Overview")
st.dataframe(df_filtered.head())

# Placeholder for Visualizations
st.subheader("Key Visualizations will go here!")
st.markdown("---")

# ... (continue after the filters section and st.dataframe(df_filtered.head()))

st.subheader("1. Steps vs. Calories Burned: Activity Intensity")

# Create the Plotly Scatter Plot
fig_scatter = px.scatter(
    df_filtered,
    x="TotalSteps",
    y="Calories",
    color="VeryActiveMinutes", # Use a third variable for color intensity
    size="TotalDistance",
    hover_data=['Date', 'Weekday'],
    template="seaborn", # Use a clean template
    title="Total Steps vs. Calories (Colored by Very Active Time)"
)

fig_scatter.update_layout(height=500, width=800)
fig_scatter.update_traces(marker=dict(line=dict(width=0.5, color='DarkSlateGrey')))

# Display the chart in Streamlit
st.plotly_chart(fig_scatter, use_container_width=True)

st.markdown("---")
# --- 2. Average Steps by Day of Week: Habit Analysis ---

st.subheader("2. Average Steps by Day of Week: Habit Analysis")

# Calculate the average steps for the filtered date range/step count
avg_steps_weekday = df_filtered.groupby("Weekday")["TotalSteps"].mean().reset_index()

# Define the correct order for the days of the week
day_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Reindex the DataFrame to ensure days are plotted in the correct order
avg_steps_weekday['Weekday'] = pd.Categorical(
    avg_steps_weekday['Weekday'], categories=day_order, ordered=True
)
avg_steps_weekday = avg_steps_weekday.sort_values('Weekday')

# Create the Plotly Bar Chart
fig_bar = px.bar(
    avg_steps_weekday,
    x="Weekday",
    y="TotalSteps",
    color="TotalSteps",
    color_continuous_scale=px.colors.sequential.Viridis,
    text_auto='.2s', # Display the value on top of the bar
    template="plotly_white",
    title="Average Steps by Day of the Week (Based on Filtered Data)"
)

fig_bar.update_layout(
    xaxis_title=None, 
    yaxis_title="Average Total Steps", 
    height=500
)

# Display the chart in Streamlit
st.plotly_chart(fig_bar, use_container_width=True)

st.markdown("---")

# --- 3. Sleep vs. Activity Correlation ---

st.subheader("3. Sleep vs. Activity Correlation")

# Ensure we only plot rows where sleep data is available
df_sleep_clean = df_filtered.dropna(subset=['TotalMinutesAsleep'])

if not df_sleep_clean.empty:
    fig_sleep = px.scatter(
        df_sleep_clean,
        x="TotalMinutesAsleep",
        y="TotalSteps",
        color="Calories", # Color by Calories to show energy burn intensity
        size="TotalDistance",
        hover_data=['Date', 'Weekday', 'VeryActiveMinutes'],
        template="plotly_dark", # Use a dark template for a different look
        title="Total Steps vs. Total Minutes Asleep (Colored by Calories Burned)"
    )

    fig_sleep.update_layout(
        xaxis_title="Total Minutes Asleep",
        yaxis_title="Total Steps",
        height=500
    )

    # Display the chart in Streamlit
    st.plotly_chart(fig_sleep, use_container_width=True)

    # Final Insight/Summary
    st.markdown("""
    **Analyst Insight:** This visualization often shows that the highest step counts occur 
    within a 'sweet spot' of sleep (typically 5 to 10 hours), suggesting that extreme 
    under- or over-sleeping is detrimental to peak daily performance.
    """)

else:
    st.warning("Sleep data not available for the current filters. Try widening the date range.")

st.markdown("---")