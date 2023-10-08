import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import plotly.express as px
import altair as alt



def load_data(folder_name, file_extension):
    data = {}
    for file_name in os.listdir(folder_name):
        if file_name.endswith(file_extension):
            data_name = os.path.splitext(file_name)[0]
            data_path = os.path.join(folder_name, file_name)
            if file_extension == '.csv':
                data[data_name] = pd.read_csv(data_path)
            elif file_extension == '.json':
                data[data_name] = pd.read_json(data_path)
    return data

from datetime import datetime

# Retrieving computed temperature data for the year 2023
# Create an empty list to store concatenated DataFrames
temperature_data_frames = []

# Get the list of files in the "sleep" folder
sleep_files = os.listdir('sleep')

# Filter files corresponding to the year 2023 (from January to September)
for file_name in sleep_files:
    if file_name.startswith('Computed Temperature - 2023') and file_name.endswith('.csv'):
        file_path = os.path.join('sleep', file_name)
        df = pd.read_csv(file_path)
        temperature_data_frames.append(df)

# Concatenate all DataFrames into one dataframe
temperature_data = pd.concat(temperature_data_frames, ignore_index=True)

# Retrieving Daily Heart Rate Variability Summary data for the year 2023
# Create an empty list to store concatenated DataFrames
hrv_data_frames = []

# Get the list of files in the "sleep" folder
sleep_files = os.listdir('sleep')

# Filter files corresponding to the year 2023
for file_name in sleep_files:
    if file_name.startswith('Daily Heart Rate Variability Summary - 2023') and file_name.endswith('.csv'):
        file_path = os.path.join('sleep', file_name)
        df = pd.read_csv(file_path)
        hrv_data_frames.append(df)

# Concatenate all DataFrames into one DataFrame
hrv_data = pd.concat(hrv_data_frames, ignore_index=True)

# Retrieving Daily Respiratory Rate Summary data for the year 2023
# Create an empty list to store concatenated DataFrames
respiratory_rate_data_frames = []

# Get the list of files in the "sleep" folder
sleep_files = os.listdir('sleep')

# Filter files corresponding to the year 2023
for file_name in sleep_files:
    if file_name.startswith('Daily Respiratory Rate Summary - 2023') and file_name.endswith('.csv'):
        file_path = os.path.join('sleep', file_name)
        df = pd.read_csv(file_path)
        respiratory_rate_data_frames.append(df)

# Concatenate all DataFrames into one DataFrame
respiratory_rate_data = pd.concat(respiratory_rate_data_frames, ignore_index=True)

# Retrieving Heart Rate Variability Details data for the year 2023
# Create an empty list to store concatenated DataFrames
hrv_details_data_frames = []

# Get the list of files in the "sleep" folder
sleep_files = os.listdir('sleep')

# Filter files corresponding to the year 2023
for file_name in sleep_files:
    if file_name.startswith('Heart Rate Variability Details - 2023') and file_name.endswith('.csv'):
        file_path = os.path.join('sleep', file_name)
        df = pd.read_csv(file_path)
        hrv_details_data_frames.append(df)

# Concatenate all DataFrames into one DataFrame
hrv_details_data = pd.concat(hrv_details_data_frames, ignore_index=True)

# Retrieving Heart Rate Variability Histogram data for the year 2023
# Create an empty list to store concatenated DataFrames
hrv_histogram_data_frames = []

# Get the list of files in the "sleep" folder
sleep_files = os.listdir('sleep')

# Filter files corresponding to the year 2023 (from January to September)
for file_name in sleep_files:
    if file_name.startswith('Heart Rate Variability Histogram - 2023') and file_name.endswith('.csv'):
        file_path = os.path.join('sleep', file_name)
        df = pd.read_csv(file_path)
        hrv_histogram_data_frames.append(df)

# Concatenate all DataFrames into one DataFrame
hrv_histogram_data = pd.concat(hrv_histogram_data_frames, ignore_index=True)

# Retrieving Sleep Score data for the year 2023
# Path to the sleep_score CSV file
file_path = os.path.join('sleep', 'sleep_score.csv')

# Load the CSV file into a DataFrame
sleep_score_df = pd.read_csv(file_path)

# Convert the "timestamp" column to datetime
sleep_score_df['timestamp'] = pd.to_datetime(sleep_score_df['timestamp'])

# Filter rows for the year 2023
sleep_score_2023 = sleep_score_df[sleep_score_df['timestamp'].dt.year == 2023]

# Drop the "composition_score" column from sleep_score_2023
sleep_score_2023 = sleep_score_2023.drop(columns=['composition_score'])

# Drop the "duration_score" column from sleep_score_2023
sleep_score_2023 = sleep_score_2023.drop(columns=['duration_score'])


# Retrieving Active Zone Minutes data for the year 2023
# Create an empty list to store concatenated DataFrames
active_zone_minutes_data_frames = []

# Get the list of files in the "Physical Activity" folder
sleep_files = os.listdir('Physical Activity')

# Filter files corresponding to the year 2023 (from January to September)
for file_name in sleep_files:
    if file_name.startswith('Active Zone Minutes - 2023') and file_name.endswith('.csv'):
        file_path = os.path.join('Physical Activity', file_name)
        df = pd.read_csv(file_path)
        active_zone_minutes_data_frames.append(df)

# Concatenate all DataFrames into one DataFrame
active_zone_minutes_data = pd.concat(active_zone_minutes_data_frames, ignore_index=True)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Display


# Simple colored subheader
#st.markdown("<h2 style='color: #00B0B9; text-decoration: bold'>My Colored Subheader</h2>", unsafe_allow_html=True)


# Title of the application
st.title("Exploration of Daily Life")


st.sidebar.image("fitbit-logo.png",width=300)
st.sidebar.markdown("<h1 style='color: #00B0B9;text-align: center; text-decoration: bold'>Welcome to Carla Hameury’s project!</h1>", unsafe_allow_html=True)
#st.sidebar.image("logoLinkedIn.png", width=50)
st.sidebar.markdown("[Come visit my linkedIn](https://www.linkedin.com/in/carla-hameury)")
#st.sidebar.image("logo.png", use_container_width=True)
st.sidebar.markdown("[Come visit my GitHub](https://github.com/CarlaHmr)")

selected_value = st.sidebar.selectbox("Walk around in my app", ["I. Introduction", "II. Analysis of data", "III. Conclusion"])

if selected_value == "I. Introduction":
    # Introduction section
    st.markdown("<h1 style='color: #00B0B9;text-align: center; text-decoration: bold'>I. Introduction</h1>", unsafe_allow_html=True)
    

    st.markdown("""Welcome to our “Exploration of Daily Life” application. This app was designed to allow you to explore and analyze various aspects of your daily life using data collected over time by your smartwatch.
    \nDaily life is made up of many elements, such as sleep quality, stress level, physical activity, heart rate variability and many others. These things can have a significant impact on your overall well-being. This is why it is essential to understand and monitor these aspects of your daily life.
    \nMy app gives you a complete overview of this data by grouping it into different categories. You will be able to explore your sleep habits, stress levels, physical activity and much more. By examining this data over a period of time, here from January 1, 2023 to September 10, 2023, you may be able to discover interesting trends and make informed decisions to improve your quality of life.
    \nI invite you to explore the different sections of this application to obtain detailed information about your daily life.
    \nI hope this application will be useful to you and help you understand your daily life better.""")

    # Stress Data section
    st.markdown("<h1 style='color: #00B0B9;text-align: center; text-decoration: bold'>Stress Data</h1>", unsafe_allow_html=True)
    

    stress_data = load_data('stress', '.csv')

    # Check if 'Stress Score' exists in the data
    if 'Stress Score' in stress_data:
        # Select the first three columns
        stress_data_subset = stress_data['Stress Score'][['DATE', 'UPDATED_AT', 'STRESS_SCORE']]
        
        # Convert the "DATE" column to datetime
        stress_data_subset['DATE'] = pd.to_datetime(stress_data_subset['DATE'])
        
        # Filter data for the year 2023
        stress_data_2023 = stress_data_subset[stress_data_subset['DATE'].dt.year == 2023]
        
        # Display the selected data from the beginning (line 0)
        st.write(stress_data_2023.reset_index(drop=True))
    else:
        st.write("No stress data found.")

    st.markdown("""The stress data captured in our dataset is essential for understanding and assessing stress levels over time.
    \nThe 'DATE' column represents the date each stress measurement was recorded. Dates are saved in date and time format, which allows detailed temporal analysis.
    \nThe 'UPDATED_AT' column indicates the date and time of the last update of each stress measure. This information can be useful for tracking data freshness and identifying when metrics have been revised or updated.
    \nThe 'STRESS_SCORE' column contains numerical values representing the stress level recorded on each given date. The stress score varies between 0 and 100. The higher the score, the fewer physical signs of stress the body shows.""")

    # Sleep Data section
    st.markdown("<h1 style='color: #00B0B9; text-align: center; text-decoration: bold'>Sleep Data</h1>", unsafe_allow_html=True)

    # Sub-subtitle for the temperature section
    st.markdown("<h2 style='color: #00B0B9;text-align: center; text-decoration: bold'>Computed Temperature Data for 2023</h2>", unsafe_allow_html=True)
    

    if not temperature_data.empty:
        st.write(temperature_data)
    else:
        st.write("No temperature data for 2023 found.")

    st.markdown("""The 'type' column indicates the type of temperature measurement recorded. This information is important for differentiating between different types of temperature data.
    \nThe 'sleep_start' column records the sleep start time for each temperature record. This can be useful for associating temperature data with specific sleep periods.
    \nThe 'sleep_end' column records the sleep end time for each temperature record. As with 'sleep_start', this information allows temperature data to be linked to specific sleep periods.
    \nThe 'temperature_samples' column contains the values of the recorded temperature samples. They represent temperature measurements taken at different times.
    \nThe 'nightly_temperature' column contains the aggregated or average nighttime body temperature for each recording. It can be calculated from individual temperature samples and generally represents body temperature during the sleep period.
    \nThe 'baseline_relative_sample_sum' column records the sum of temperature samples relative to a baseline.
    \nThe 'baseline_relative_sample_sum_of_squares' column contains the sum of the squares of the deviations from the baseline. It can be used to assess the variability of temperature data relative to the baseline.
    \nThe 'baseline_relative_nightly_standard_deviation' column records the standard deviation of the temperature samples from the baseline for each nightly recording. It measures the dispersion of temperature data relative to the baseline during the night.
    \nThe 'baseline_relative_sample_standard_deviation' column shows the standard deviation of the temperature samples from the baseline across the entire record. It makes it possible to evaluate the overall variability of temperature data compared to the baseline.""")

    # Sub-subtitle for the Heart Rate Variability section
    st.markdown("<h2 style='color: #00B0B9;text-align: center; text-decoration: bold'>Heart Rate Variability Data for 2023</h2>", unsafe_allow_html=True)

    # Display the resulting DataFrame
    if not hrv_data.empty:
        st.write(hrv_data)
    else:
        st.write("No heart rate variability data for 2023 found.")

    st.markdown("""The 'timestamp' column records the date and time the heart rate variability measurements were recorded. The timestamp is essential for tracking the timeline of measurements and associating them with specific times.
    \nThe 'rmssd' column contains the values of the square root of the mean of the squares of the successive deviations between the R-R intervals (RRI) of the electrocardiogram (ECG) signal. RMSSD is a commonly used indicator to assess heart rate variability and is often associated with heart rate variation due to breathing (respiratory HRV).
    \nThe 'nremhr' column records heart rate measurements during the NREM (non-rapid eye movement) sleep phase of the sleep cycle. It can provide information on the stability of the autonomic nervous system during sleep.
    \nThe 'entropy' column contains entropy values that measure the complexity or irregularity of heart rate variability. Higher entropy may indicate more complex heart rate variability, which is often considered a sign of good cardiovascular health.""")

    # Sub-subtitle for the Heart Rate Variability Details section
    st.markdown("<h2 style='color: #00B0B9;text-align: center; text-decoration: bold'>Heart Rate Variability Details Data for 2023</h2>", unsafe_allow_html=True)

    # Display the resulting DataFrame
    if not hrv_details_data.empty:
        st.write(hrv_details_data)
    else:
        st.write("No heart rate variability details data for 2023 found.")

    st.markdown("""The 'timestamp' column records the date and time the heart rate variability measurements were recorded. The timestamp is essential for tracking the timeline of measurements and associating them with specific times.
    \nThe 'rmssd' column contains the values of the square root of the mean of the squares of the successive deviations between the R-R intervals (RRI) of the electrocardiogram (ECG) signal. RMSSD is a commonly used indicator to assess heart rate variability and is often associated with heart rate variation due to breathing (respiratory HRV).
    \nThe 'coverage' column can record data coverage, meaning the proportion of time for which heart rate variability measurements were obtained. High coverage is important to ensure reliable HRV analyses.
    \nThe 'low_frequency' column contains measurements of the low frequency component of heart rate variability. This component is often associated with the activity of the sympathetic nervous system.
    \nThe 'high_frequency' column contains measurements of the high frequency component of heart rate variability. This component is often associated with the activity of the parasympathetic nervous system.""")

    # Sub-subtitle for the Heart Rate Variability Histogram section
    st.markdown("<h2 style='color: #00B0B9;text-align: center; text-decoration: bold'>Heart Rate Variability Histogram Data for 2023</h2>", unsafe_allow_html=True)

    # Display the resulting DataFrame
    if not hrv_histogram_data.empty:
        st.write(hrv_histogram_data)
    else:
        st.write("No heart rate variability histogram data for 2023 found.")

    st.markdown("""The 'timestamp' column records the date and time the heart rate variability measurements were recorded. The timestamp is essential for tracking the timeline of measurements and associating them with specific times.
    \nThe 'bucket_values' column contains the heart rate variability histogram values. A histogram is a graphical representation of the distribution of data into intervals, or "bins." In this context, "bucket_values" represent the heart rate variability R-R interval (RRI) values.
    """)

    # Sub-subtitle for the Daily Respiratory Rate section
    st.markdown("<h2 style='color: #00B0B9;text-align: center;text-decoration: bold'>Daily Respiratory Rate Data for 2023</h2>", unsafe_allow_html=True)

    # Display the resulting DataFrame
    if not respiratory_rate_data.empty:
        st.write(respiratory_rate_data)
    else:
        st.write("No daily respiratory rate data for 2023 found.")

    st.markdown("""The 'timestamp' column records the date and time the heart rate variability measurements were recorded. The timestamp is essential for tracking the timeline of measurements and associating them with specific times.
    \nThe 'daily respiratory rate' column contains daily respiratory rate measurements. Respiratory rate is the number of breathing cycles (inhalation and exhalation) per minute.""")

    # Sub-subtitle for the Sleep Scores for the Year section
    st.markdown("<h2 style='color: #00B0B9;text-align: center; text-decoration: bold'>Sleep Scores Data for 2023</h2>", unsafe_allow_html=True)

    # Display the resulting DataFrame
    if not sleep_score_2023.empty:
        st.write(sleep_score_2023)
    else:
        st.write("No sleep score data for the year 2023 found.")

    st.markdown("""The 'sleep_log_entry_id' column contains a unique identifier associated with each sleep log entry. This identifier allows each sleep record to be uniquely tracked and associated with other data if necessary.
    \nThe 'timestamp' column records the date and time the sleep data was recorded. This makes it possible to situate each recording in time and to follow the evolution of sleep habits.
    \nThe 'overall_score' column contains an overall score assigned to sleep quality for each entry. The overall score is a summary measure that summarizes the overall quality of sleep. A higher score generally indicates better sleep.
    \nThe 'revitalization_score' column contains a score that assesses the extent to which sleep contributed to the person's revitalization.
    \nThe 'deep_sleep_in_minutes' column shows the total deep sleep duration in minutes for each recording. Deep sleep is an essential sleep phase for physical and mental recovery.
    \nThe 'resting_heart_rate' column records the resting heart rate at the time of sleep recording.
    \nThe 'restlessness' column can record a measure of restlessness during sleep.""")

    # Physical Activity section
    st.markdown("<h1 style='color: #00B0B9;text-align: center; text-decoration: bold'>Physical Activity Data</h1>", unsafe_allow_html=True)

    # Display the resulting DataFrame
    if not active_zone_minutes_data.empty:
        st.write(active_zone_minutes_data)
    else:
        st.write("No active zone minutes data for 2023 found.")

    st.markdown("""The 'date_time' column records the date and time when the minutes in the active area were recorded. This information helps track when these minutes were accumulated, which can be useful for analyzing daily and hourly trends.
    \nThe 'heart_zone_id' column indicates the heart rate zone in which the activity took place. Different heart rate zones are usually defined based on percentages of maximum heart rate, and they represent different intensities of physical activity. For example, one zone may correspond to light activity, while another may correspond to vigorous activity.
    \nThe 'total_minutes' column shows the total number of minutes spent in the specified heart rate zone.""")


elif selected_value == "II. Analysis of data":
    st.set_option('deprecation.showPyplotGlobalUse', False)
    # Analysis of data section
    st.markdown("<h1 style='color: #00B0B9;text-align: center; text-decoration: bold'>II. Analysis of data</h1>", unsafe_allow_html=True)
    # Stress Data section
    st.markdown("<h1 style='color: #00B0B9;text-align: center; text-decoration: bold'>Stress Data</h1>", unsafe_allow_html=True)

    stress_data = load_data('stress', '.csv')
    # Select the first three columns
    stress_data_subset = stress_data['Stress Score'][['DATE', 'UPDATED_AT', 'STRESS_SCORE']]
    # Convert the "DATE" column to datetime
    stress_data_subset['DATE'] = pd.to_datetime(stress_data_subset['DATE'])    
    # Filter data for the year 2023
    stress_data_2023 = stress_data_subset[stress_data_subset['DATE'].dt.year == 2023]

    st.markdown("<h2 style='color: #00B0B9;text-align: center; text-decoration: bold'>Overview of Stress Data</h2>", unsafe_allow_html=True)
    # Display the selected data from the beginning (line 0)
    st.write(stress_data_2023.reset_index(drop=True))

    # Statistical summary of stress data
    st.markdown("<h2 style='color: #00B0B9;text-align: center; text-decoration: bold'>Statistical Summary of Stress Data</h2>", unsafe_allow_html=True)
    st.write(stress_data_2023.describe())
    st.markdown("""There are 254 data points.
    \nThe average stress score is 73.0551, the minimum is 0 and the maximum is 92. The first quartile is 71.
    \nThis means that more than 75% of the time, my stress score is greater than or equal to 71.
    \nWhich means that 75% I am much closer to 0 than to 100. You could say that I am not someone who is often stressed. 
    \nAdditionally, the standard deviation is 16.106, this means that most stress scores are very close to the mean, suggesting low variability and high consistency in stress levels. Which confirms the previous interpretation.""")

    # Create a histogram of the 'STRESS_SCORE' column
    st.markdown("<h2 style='color: #00B0B9;text-align: center; text-decoration: bold'>Histogram of Stress Scores</h2>", unsafe_allow_html=True)
    plt.figure(figsize=(10, 6))
    sns.histplot(stress_data_2023['STRESS_SCORE'], bins=20, kde=True)
    plt.xlabel("Stress Score")
    plt.ylabel("Frequency")
    st.pyplot()
    st.markdown("""With the histogram, we notice that there are only 10 values between 0 and 5. These values can represent the times when I was the most stressed during this year, just as they can represent times when I was not wearing my watch. 
    \nWhen I am not wearing my watch, the score is automatically set to 0.
    \nApart from these values we notice that the rest of the time, my stress score is between 57.5 and 95. With most often a score between 70 and 85. These values are much closer to 100 than to 0, which again confirms the previous interpretation.""")

    # Create a box plot for stress scores
    st.markdown("<h2 style='color: #00B0B9;text-align: center; text-decoration: bold'>Box Plot of Stress Scores</h2>", unsafe_allow_html=True)
    plt.figure(figsize=(10, 6))
    sns.boxplot(x=stress_data_2023['STRESS_SCORE'])
    plt.xlabel("Stress Score")
    st.pyplot()
    st.markdown("""The box plot confirms that the 10 values between 0 and 5 are aberrate values, we can therefore deduce that these are the values of the moments when I was not wearing my watch.
    \nThe rest of the figure also confirms the previous interpretation.
    \nI am not someone who is regularly very stressed. 
    \nWhen I'm stressed, the latter is not extreme since at least my stress score reaches 57.5 (if we remove the outliers). When I am as relaxed as possible my stress score reaches up to 92.""")

    # Create a scatter plot between 'STRESS_SCORE' and 'UPDATED_AT'
    st.markdown("<h2 style='color: #00B0B9;text-align: center; text-decoration: bold'>Scatter Plot of Stress Scores vs. Update Dates</h2>", unsafe_allow_html=True)
    plt.figure(figsize=(12, 6))
    sns.scatterplot(x=stress_data_2023['UPDATED_AT'], y=stress_data_2023['STRESS_SCORE'], alpha=0.5)
    plt.xlabel("Update Date")
    plt.ylabel("Stress Score")
    plt.xticks(rotation=45)
    st.pyplot()
    st.markdown("""The scatter plot shows that my stress score follows a rather linear distribution with a rather high score.""")
    
    # Analyze the correlation between variables
    st.markdown("<h2 style='color: #00B0B9;text-align: center; text-decoration: bold'>Correlation Matrix</h2>", unsafe_allow_html=True)
    st.markdown("""It is not relevant here to make a correlation matrix between scores and dates.""")

    # Create a bar plot for stress score based on the month
    st.markdown("<h2 style='color: #00B0B9;text-align: center; text-decoration: bold'>Viewing my stress score based on the month</h2>", unsafe_allow_html=True)
    stress_data_2023['DATE'] = pd.to_datetime(stress_data_2023['DATE'])
    stress_data_2023['Month'] = stress_data_2023['DATE'].dt.month
    monthly_avg_stress = stress_data_2023.groupby('Month')['STRESS_SCORE'].mean()
    plt.figure(figsize=(10, 6))
    plt.bar(monthly_avg_stress.index, monthly_avg_stress.values)
    plt.xlabel('Month')
    plt.ylabel('Average Stress Score')
    plt.title('Average Stress Score by Month (2023)')
    plt.xticks(rotation=45) 
    st.pyplot()
    st.markdown("""We can see that my stress score varies little depending on the month. 
    \nThe months where I was the most stressed were January and February, months which corresponded to my return to mobility and school exams, which is consistent.
    \nLikewise, the other two months where I was the most stressed corresponded to June and July which were also school exam periods.""")

    # Sleep Data section
    st.markdown("<h1 style='color: #00B0B9;text-align: center; text-decoration: bold'>Sleep Data</h1>", unsafe_allow_html=True)

    # Sub-subtitle for the temperature section
    st.markdown("<h2 style='color: #00B0B9;text-align: center; text-decoration: bold'>- Computed Temperature Data for 2023</h2>", unsafe_allow_html=True)
    temperature_data['sleep_start'] = pd.to_datetime(temperature_data['sleep_start'], format='ISO8601', errors='coerce')
    temperature_data['sleep_end'] = pd.to_datetime(temperature_data['sleep_end'], format='ISO8601', errors='coerce')

    # Summary statistics for nightly_temperature'
    st.markdown("<h2 style='color: #00B0B9;text-align: center; text-decoration: bold'>Summary Statistics for Numeric Columns</h2>", unsafe_allow_html=True)
    st.write(temperature_data['nightly_temperature'].describe())
    st.markdown("""We have 261 values. On average at night my skin temperature is 33.6601°C. It varies between 30.5941°C and 35.7558°C. The standard deviation is 0.8569. 
    \nWhich proves that the data is not very dispersed compared to the average. This measurement is confirmed by the min and the max which are close but also by the different quartiles which are not very far apart.
    \nWe can deduce that the temperature of my skin during the night varies little.""")

    # Distribution of nightly_temperature
    st.markdown("<h2 style='color: #00B0B9;text-align: center; text-decoration: bold'>Distribution of Nightly Temperature</h2>", unsafe_allow_html=True)
    plt.figure(figsize=(8, 6))
    sns.histplot(temperature_data['nightly_temperature'], kde=True, color='skyblue')
    plt.xlabel('Nightly Temperature')
    plt.ylabel('Frequency')
    plt.title('Distribution of Nightly Temperature')
    st.pyplot()
    st.markdown("""On this distribution, we notice that the highest frequency corresponds to a temperature of approximately 33.6°C. 
    \nIn addition, we can see that the data is not very dispersed. The closer we get to the “extreme” values, the lower the frequencies.
    \nThe observation is the same as before.""")
    

    # Scatter plot of temperature_samples vs. nightly_temperature
    st.markdown("<h2 style='color: #00B0B9;text-align: center; text-decoration: bold'>Relationship between Temperature Samples and Nightly Temperature</h2>", unsafe_allow_html=True)
    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=temperature_data, x='temperature_samples', y='nightly_temperature', color='coral')
    plt.xlabel('Temperature Samples')
    plt.ylabel('Nightly Temperature')
    plt.title('Relationship between Temperature Samples and Nightly Temperature')
    st.pyplot()
    st.markdown("""The data is quite scattered. Looks like there is no real correlation between NightlyTemperature and Temperature Samples.
    \nLet's check this with a correlation matrix.""")

    # Correlation heatmap of numeric columns
    st.markdown("<h2 style='color: #00B0B9;text-align: center; text-decoration: bold'>Correlation Heatmap</h2>", unsafe_allow_html=True)
    # Select only the numeric columns
    numeric_columns = temperature_data.select_dtypes(include=['number'])
    plt.figure(figsize=(10, 8))
    correlation_matrix = numeric_columns.corr()
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
    plt.title('Correlation Heatmap (Numeric Columns Only)')
    st.pyplot()
    st.markdown("""The correlation coefficient between NightlyTemperature and Temperature Samples is indeed very very low. It is 0.048, we can say that there is no correlation between these two variables.
    \nWe notice a strong correlation. Indeed, the variables baseline_relative_nightly_standard_deviation and baseline_relative_sample_standard_deviation seem strongly positively correlated with a correlation coefficient of 0.94.
    \nLikewise, the variables nightly_temperature and baseline_relative_sample_sum seem strongly positively correlated with a correlation coefficient of 0.82.
    \nThere are no strong negative correlations. 
    \nThe strongest negative correlation is between baseline_relative_sample_sum_of_squares and baseline_relative_sample_sum. The correlation coefficient is -0.65 for these two variables.""")

    # Sub-subtitle for the Heart Rate Variability section
    st.markdown("<h2 style='color: #00B0B9;text-align: center; text-decoration: bold'>- Heart Rate Variability Data for 2023</h2>", unsafe_allow_html=True)

    # Summary statistics
    st.markdown("<h2 style='color: #00B0B9;text-align: center; text-decoration: bold'>Summary Statistics of HRV Data</h2>", unsafe_allow_html=True)
    st.write(hrv_data[['rmssd', 'nremhr', 'entropy']].describe())
    st.markdown("""We have 252 values.
    \nThe rmssd varies between 0 and 127.344, has a mean of 43.6 and a standard deviation of 31.78. The data is rather scattered.
    \nThe nremhr ranges between 50.302 and 82.528, has a mean of 61.5026 and a standard deviation of 6.214. The data is less scattered.
    \nFinally, entropy varies between 0 and 3.595, has a mean of 2.444 and a standard deviation of 0.7609. The data is not very scattered.""")

    # Histogram of RMSSD
    st.markdown("<h2 style='color: #00B0B9;text-align: center; text-decoration: bold'>Histogram of RMSSD</h2>", unsafe_allow_html=True)
    plt.figure(figsize=(8, 6))
    sns.histplot(data=hrv_data, x='rmssd', bins=20, kde=True)
    plt.xlabel('RMSSD')
    plt.ylabel('Frequency')
    st.pyplot()
    st.markdown("""We notice a large peak. In fact, the rmssd value that stands out the most is around 10miliseconds.
    \nThis means that the R-R intervals are relatively constant, which may indicate low heart rate variability.""")

    # Line plot of NREM HR
    st.markdown("<h2 style='color: #00B0B9;text-align: center; text-decoration: bold'>Line Plot of NREM HR</h2>", unsafe_allow_html=True)
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=hrv_data, x='timestamp', y='nremhr')
    plt.xlabel('Timestamp')
    plt.ylabel('NREM HR')
    plt.title('NREM HR Over Time')
    st.pyplot()
    st.markdown("""The line plot is irregular, we notice many peaks.
    \nThese peaks can indicate several things, either episodes of abnormal breathing (sleep apnea), frequent awakenings during the night or natural variability in heart rate.
    \nThe last option is to eliminate from the previous graph. Not suffering from sleep apnea to my knowledge, I think the explanation here is that I wake up frequently during the night.
    \nThis explanation was retained by eliminating the others but also because it is something that has already been pointed out to me on several occasions.""")

    # Pairplot of RMSSD, NREM HR, and Entropy
    st.markdown("<h2 style='color: #00B0B9;text-align: center; text-decoration: bold'>Pairplot of RMSSD, NREM HR, and Entropy</h2>", unsafe_allow_html=True)
    sns.pairplot(hrv_data[['rmssd', 'nremhr', 'entropy']])
    st.pyplot()
    st.markdown("""Entropy and rmssd appear to be correlated. Let's check this with a correlation matrix.""")

    # Select the relevant columns for the correlation matrix
    columns_to_correlate = ['rmssd', 'nremhr', 'entropy']

    # Create a sub-dataframe with these columns
    df_correlation = hrv_data[columns_to_correlate]

    # Calculate the correlation matrix
    correlation_matrix = df_correlation.corr()

    # Create a heatmap of the correlation matrix
    st.markdown("<h2 style='color: #00B0B9;text-align: center; text-decoration: bold'>Correlation heatmap of HRV data</h2>", unsafe_allow_html=True)
    plt.figure(figsize=(8, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
    plt.title('Correlation Matrix - Heart Rate Variability (HRV)')
    st.pyplot(plt)
    st.markdown("""With a correlation coefficient of 0.81, entropy and rmssd are indeed correlated. No other correlation emerges.""")


    # Sub-subtitle for the Heart Rate Variability Details section
    st.markdown("<h2 style='color: #00B0B9;text-align: center; text-decoration: bold'>- Heart Rate Variability Details Data for 2023</h2>", unsafe_allow_html=True)

    # Convert 'timestamp' column to datetime
    hrv_details_data['timestamp'] = pd.to_datetime(hrv_details_data['timestamp'])

    # Sort the DataFrame by 'timestamp'
    df_hrv_details = hrv_details_data.sort_values(by='timestamp')

    # Line plot of RMSSD over time
    st.markdown("<h2 style='color: #00B0B9;text-align: center; text-decoration: bold'>Line Plot of RMSSD Over Time</h2>", unsafe_allow_html=True)
    plt.figure(figsize=(10, 6))
    plt.plot(hrv_details_data['timestamp'], hrv_details_data['rmssd'], marker='o', linestyle='-')
    plt.xticks(rotation=45)
    plt.xlabel('Timestamp')
    plt.ylabel('RMSSD')
    plt.title('Line Plot of RMSSD Over Time')
    st.pyplot(plt)
    st.markdown("""We can see that in general my rmssd varies little depending on the month.
    \nWe see a slight increase around the months of August and September. We also notice a peak in the rmssd at the end of June.
    \nWe can therefore say that there is stability or low variability in the RMSSD during the year.
    \nThe slight increase may mean a potential improvement in heart rate variability at this time. The peak means a significant and temporary increase in RMSSD values at that time.""")

    # Pairplot for selected columns
    st.markdown("<h2 style='color: #00B0B9;text-align: center; text-decoration: bold'>Pairplot for Selected Columns</h2>", unsafe_allow_html=True)
    sns.pairplot(hrv_details_data[['rmssd', 'coverage', 'low_frequency', 'high_frequency']])
    st.pyplot(plt)
    st.markdown("""There appears to be a correlation between rmssd and high_frequency. But there don't seem to be any other notable correlations.
    \nLet's check this with a correlation matrix.""")

    # Correlation heatmap
    st.markdown("<h2 style='color: #00B0B9;text-align: center; text-decoration: bold'>Correlation Heatmap</h2>", unsafe_allow_html=True)
    correlation_matrix = hrv_details_data[['rmssd', 'coverage', 'low_frequency', 'high_frequency']].corr()
    plt.figure(figsize=(8, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
    plt.title('Correlation Heatmap')
    st.pyplot(plt)
    st.markdown("""There is, in fact, a strong positive correlation between the rmssd and high_frequency, with a correlation coefficient of 0.91.
    \nThere are no other notable correlations.""")


    # Sub-subtitle for the Heart Rate Variability Histogram section
    st.markdown("<h2 style='color: #00B0B9;text-align: center; text-decoration: bold'>- Heart Rate Variability Histogram Data for 2023</h2>", unsafe_allow_html=True)

    # Convert 'timestamp' column to datetime
    hrv_histogram_data['timestamp'] = pd.to_datetime(hrv_histogram_data['timestamp'])

    # Sort the DataFrame by 'timestamp'
    hrv_histogram_data= hrv_histogram_data.sort_values(by='timestamp')

    # Create a histogram
    fig = px.histogram(hrv_histogram_data, x='bucket_values', nbins=30, title='Histogram of Bucket Values')
    fig.update_xaxes(title='Bucket Values')
    fig.update_yaxes(title='Frequency')
    st.write(fig)
    st.markdown("""Given the quantity of data I made the decision to create an interactive representation allowing zooming.
    \nWe notice that the distribution is quite similar and varies little.""")


    # Sub-subtitle for the Daily Respiratory Rate section
    st.markdown("<h2 style='color: #00B0B9;text-align: center; text-decoration: bold'>- Daily Respiratory Rate Data for 2023</h2>", unsafe_allow_html=True)

    respiratory_rate_data['timestamp'] = pd.to_datetime(respiratory_rate_data['timestamp'])

    st.markdown("<h2 style='color: #00B0B9;text-align: center; text-decoration: bold'>Statistical Summary of Daily Respiratory Rate</h2>", unsafe_allow_html=True)
    summary = respiratory_rate_data['daily_respiratory_rate'].describe()
    st.write(summary)
    st.markdown("""We have 252 values.
    \nThe rate varies from 12.4 to 22.6 with an average of 16.2405 and a standard deviation of 0.9352.
    \nWhich means that the data is not very dispersed around the average.""")

    # Create an Histogram of Daily Respiratory Rate
    st.markdown("<h2 style='color: #00B0B9;text-align: center; text-decoration: bold'>Histogram of Daily Respiratory Rate</h2>", unsafe_allow_html=True)
    plt.figure(figsize=(10, 6))
    plt.hist(respiratory_rate_data['daily_respiratory_rate'], bins=20, color='skyblue', edgecolor='black')
    plt.xlabel('Daily Respiratory Rate')
    plt.ylabel('Frequency')
    plt.title('Histogram of Daily Respiratory Rate')
    st.pyplot(plt)
    st.markdown("""The histogram confirms the previous interpretation.
    \nWe note that the minimum and maximum were reached during peaks and are exceptional values. Generally speaking, the values fluctuate between 15 and 18.""")

    # Create a Line Plot of Daily Respiratory Rate Over Time
    st.markdown("<h2 style='color: #00B0B9;text-align: center; text-decoration: bold'>Line Plot of Daily Respiratory Rate Over Time</h2>", unsafe_allow_html=True)
    plt.figure(figsize=(10, 6))
    plt.plot(respiratory_rate_data['timestamp'], respiratory_rate_data['daily_respiratory_rate'], color='skyblue')
    plt.xlabel('Date')
    plt.ylabel('Daily Respiratory Rate')
    plt.title('Daily Respiratory Rate Over Time')
    st.pyplot(plt)
    st.markdown("""We notice that in general, the daily breathing rate shows slight fluctuations, but it generally remains stable, lying between 15 and 18 breaths per minute.
    \nHowever, there are two exceptional times when the respiration rate appears to fall outside of this normal range, as noted previously.
    \nA peak in April where the respiration rate dropped as low as 12.4 breaths per minute. This could indicate a period of slower or deeper breathing than normal.
    \nA peak in August where the respiration rate rose as high as 22.6 breaths per minute. This significant increase in breathing rate may indicate a period of intense physical activity, stress, or other factors that have caused a temporary increase in respiratory rate.""")

    
    # Sub-subtitle for the Sleep Scores for the Year section
    st.markdown("<h2 style='color: #00B0B9;text-align: center; text-decoration: bold'>- Sleep Scores Data for 2023</h2>", unsafe_allow_html=True)

    # Distribution of Sleep Scores
    st.markdown("<h2 style='color: #00B0B9;text-align: center; text-decoration: bold'>Distribution of Sleep Scores</h2>", unsafe_allow_html=True)
    fig, ax = plt.subplots(1, 2, figsize=(12, 6))
    sns.histplot(sleep_score_2023['overall_score'], bins=20, kde=True, color='skyblue', ax=ax[0])
    sns.histplot(sleep_score_2023['revitalization_score'], bins=20, kde=True, color='lightgreen', ax=ax[1])

    ax[0].set_xlabel('Overall Sleep Score')
    ax[1].set_xlabel('Revitalization Score')
    ax[0].set_ylabel('Frequency')
    ax[1].set_ylabel('Frequency')
    ax[0].set_title('Distribution of Overall Sleep Score')
    ax[1].set_title('Distribution of Revitalization Score')
    st.pyplot(fig)
    st.markdown("""The two distributions appear similar. Indeed, whether in terms of data distribution or scales, they are identical.""")

    # Evolution of Sleep Scores Over Time
    st.markdown("<h2 style='color: #00B0B9;text-align: center; text-decoration: bold'>Evolution of Sleep Scores Over Time</h2>", unsafe_allow_html=True)
    plt.figure(figsize=(12, 6))
    sns.lineplot(x='timestamp', y='overall_score', data=sleep_score_2023, color='skyblue')
    plt.xlabel('Date and Time')
    plt.ylabel('Overall Sleep Score')
    plt.title('Evolution of Overall Sleep Score Over Time')
    plt.xticks(rotation=45)
    st.pyplot(plt)
    st.markdown("""We observe a constant fluctuation in the overall sleep score over time.
    \nHowever, these fluctuations are similar whatever the month. The lowest peak is in February while the highest is in April.""")

    # Create an interactive histogram
    fig = px.histogram(sleep_score_2023, x='deep_sleep_in_minutes', nbins=30, title='Distribution of Deep Sleep in Minutes')
    fig.update_xaxes(title_text='Deep Sleep in Minutes')
    fig.update_yaxes(title_text='Frequency')
    st.plotly_chart(fig)
    st.markdown("""Most of my nights I spend between 70 and 74 minutes in deep sleep.
    \nDeep sleep is the phase where your body regenerates and repairs itself. Spending so much time in deep sleep is considered beneficial for your health.
    \nIt rarely happens that I spend between 140 and 144 or between 130 and 134 or between 10 and 14 minutes in deep sleep.
    \nGenerally speaking, I spend between 45 and 94 minutes in deep sleep per night. That's a good score.""")

    column_to_visualize = "resting_heart_rate"

    # Create an interactive chart with Altair
    chart = alt.Chart(sleep_score_2023).mark_bar().encode(
        x=alt.X(column_to_visualize, bin=True),
        y='count()',
        tooltip=[column_to_visualize, 'count()']
    ).properties(
        width=600,
        title=f'Distribution of {column_to_visualize}'
    ).interactive()

    # Display the chart
    st.altair_chart(chart, use_container_width=True)
    st.markdown("""In the majority of cases, the resting heart rate tends to be around 63 or 64 beats per minute (BPM). 
    \nIt is rarely 59 or 71bpm. These values are considered exceptions or less common cases in the data set. There can be a variety of reasons for these occasional variations, such as stressors, recent physical activities, medical conditions, or simply normal variations in heart rate from person to person.""")

    
    # Physical Activity section
    st.markdown("<h1 style='color: #00B0B9;text-align: center; text-decoration: bold'>Physical Activity Data</h1>", unsafe_allow_html=True)

    # Sub-subtitle for the distribution of Active Minutes by zone
    st.markdown("<h2 style='color: #00B0B9; text-align: center;text-decoration: bold'>Distribution of Active Minutes by zone</h2>", unsafe_allow_html=True)

    # Create a figure with a grid of 1 row and 2 columns
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

    # Create a Histogram of Distribution of Active Minutes by Fat Burn zone
    zone_Fat = active_zone_minutes_data[active_zone_minutes_data['heart_zone_id'] == 'FAT_BURN']
    ax1.hist(zone_Fat['total_minutes'], bins=20, color='red', edgecolor='black')
    ax1.set_xlabel('Minutes in FAT_BURN zone')
    ax1.set_ylabel('Frequency')
    ax1.set_title('Distribution of Minutes in FAT_BURN in 2023')

    # Create a Histogram of Distribution of Active Minutes by cardio zone
    zone_Cardio = active_zone_minutes_data[active_zone_minutes_data['heart_zone_id'] == 'CARDIO']
    ax2.hist(zone_Cardio['total_minutes'], bins=20, color='skyblue', edgecolor='black')
    ax2.set_xlabel('Minutes in CARDIO zone')
    ax2.set_ylabel('Frequency')
    ax2.set_title('Distribution of Minutes in CARDIO in 2023')
    st.pyplot(fig)

    st.markdown("""In 2023, my heart has been in the Cardio zone almost as many times as in the Fat burn zone.""")


    # Sub-subtitle for the evolution of Active Minutes Over Time
    st.markdown("<h2 style='color: #00B0B9;text-align: center; text-decoration: bold'>Evolution of Active Minutes Over Time</h2>", unsafe_allow_html=True)

    # Convert the 'date_time' column to datetime
    active_zone_minutes_data['date_time'] = pd.to_datetime(active_zone_minutes_data['date_time'])

    # Group by month and sum the active minutes
    monthly_total_minutes = active_zone_minutes_data.resample('M', on='date_time')['total_minutes'].sum()

    # Create a line chart
    plt.figure(figsize=(10, 6))
    plt.plot(monthly_total_minutes.index.strftime('%B %Y'), monthly_total_minutes.values, marker='o', linestyle='-')
    plt.xticks(rotation=45)
    plt.xlabel('Month')
    plt.ylabel('Total Active Minutes')
    plt.title('Evolution of Active Minutes per Month in 2023')
    st.pyplot(plt)
    st.markdown("""In September, the number of active minutes is low because we only have the first 10 days of September in data. 
    \nThe month I was most active was June. The one where I have been the least active is February.
    \nWe see that the number of active minutes varies a lot depending on the month. From spring onwards, this number is higher than in winter.""")

    # Sub-subtitle for the heatmap of Active Zones by Day of the Week and Time
    st.markdown("<h2 style='color: #00B0B9;text-align: center; text-decoration: bold'>Heatmap of Active Zones by Day of the Week and Time</h2>", unsafe_allow_html=True)

    # Convert the 'date_time' column to datetime
    active_zone_minutes_data['date_time'] = pd.to_datetime(active_zone_minutes_data['date_time'])

    # Extract the day of the week and hour
    active_zone_minutes_data['day_of_week'] = active_zone_minutes_data['date_time'].dt.day_name()
    active_zone_minutes_data['hour'] = active_zone_minutes_data['date_time'].dt.hour

    # Create a pivot table for the heatmap
    heatmap_data = active_zone_minutes_data.pivot_table(index='hour', columns='day_of_week', values='total_minutes', aggfunc='sum')

    # Create a heatmap
    plt.figure(figsize=(12, 8))
    sns.heatmap(heatmap_data, cmap='coolwarm', annot=True, fmt='.1f', cbar_kws={'label': 'Total Active Minutes'})
    plt.xlabel('Day of the Week')
    plt.ylabel('Hour of the Day')
    plt.title('Heatmap of Active Minutes by Day of the Week and Hour in 2023')
    st.pyplot(plt)
    st.markdown("""Generally speaking, the times when I am most in the active zone are Saturday mornings from 1:30 a.m. to 3:30 a.m. and Tuesday evenings from 7:30 p.m. to 9:30 p.m. 
    \nTuesdays correspond to my football training and Saturday mornings when I go out with my friends to go dancing.
    \nThe times when I am active during the month are Sunday evenings when I am in bed watching a series.""")


elif selected_value == "III. Conclusion":
    # Conclusion section
    st.markdown("<h1 style='color: #00B0B9;text-align: center; text-decoration: bold'>III. Conclusion</h1>", unsafe_allow_html=True)
    st.markdown("""This project to analyze my own personal data, taken from my Fitbit connected watch, for the year 2023 allowed me to better understand my health, my well-being and my lifestyle habits. I set out on this journey with a deep desire to proactively take charge of my health, and the results have been extremely enlightening.

\nAnalysis of my stress levels revealed that I generally maintain a moderate level of stress, with peaks during particular events such as returning to mobility or exam periods. This awareness is valuable because it allows me to identify times when I might need stress management techniques.

\nWhen it comes to my nighttime skin temperature, the data indicates stability, which suggests regular and restorative sleep quality. This is a positive sign of my overall well-being.

\nMy heart rate variability information showed significant variations in RMSSD, which may be related to various factors such as stress, physical activity and sleep quality. Continuing to monitor this data will allow me to better understand what it means in my personal context.

\nSleep scores reveal monthly fluctuations, but a general tendency to maintain quality sleep, with a sufficient amount of deep sleep, which is encouraging.

\nWhen it comes to my physical activity, the data reveals seasonal peaks, particularly in spring and summer, which correlate with my participation in football and nights out at dance bars. My time preferences for physical activity are also visible in the data.

\nOverall, this project highlights the importance of collecting and analyzing personal data to make informed decisions about my health and well-being. I saw the benefits of taking a proactive approach to my health through this in-depth analysis.

\nI plan to continue monitoring and analyzing this data to detect new trends and make adjustments to my lifestyle. Using this information, I can develop more specific strategies to improve my quality of life, reduce stress, and maintain a healthy balance between physical activity and rest.

\nIn short, this project highlights the positive impact of personal data analysis on health and well-being decision-making, allowing me to live a more conscious and balanced life. I am determined to continue exploring the potential of my data for a better quality of life in the future.""")