1. Description Overview

The Real-Time Weather Monitoring System* is a Python application that continuously monitors weather conditions in major Indian metros using the OpenWeatherMap API. 
The system provides users with real-time weather data, daily summaries, and alerts for extreme weather conditions, enhancing awareness and preparedness.

2. Features

- Real-Time Data Retrieval: Automatically fetches weather data every 5 minutes for cities including Delhi, Mumbai, Chennai, Bangalore, Kolkata, and Hyderabad.
- Temperature Conversion: Converts temperatures from Kelvin to Celsius or Fahrenheit based on user preference.
- Daily Weather Summary: Aggregates daily weather data, calculating:
  - Average temperature
  - Maximum temperature
  - Minimum temperature
  - Dominant weather condition
- Alert System: Allows users to set thresholds for temperature and weather conditions, triggering alerts when these thresholds are exceeded.
- Data Visualization: Displays daily weather summaries, historical trends, and alert notifications for user-friendly insights.

3. Technologies Used

- Programming Language: Python
- Libraries: 
  - Requests (for API calls)
  - SQLite3 (for data storage)
  - Matplotlib or Seaborn (for visualizations)
- API: OpenWeatherMap API
- Database: SQLite (or another database of choice)

 4. Installation

1. *Clone the Repository*:
   ```bash
   git clone https://github.com/yourusername/weather_monitor.git

2. Navigate to the Project Directory:

cd weather_monitor


3. Install Required Dependencies:

pip install -r requirements.txt

5. Configuration

1. Get Your API Key:

Sign up at OpenWeatherMap to obtain your API key.

2. Update Configuration:

Modify the configuration file to include your API key.

6. Usage

Run the Application:

python main.py

Follow console instructions to configure alerts and view weather summaries.


7. Testing

Test Cases

Verify the successful connection to the OpenWeatherMap API.

Ensure accurate temperature conversions.

Validate calculations for daily weather summaries.

Test alert functionality for breached thresholds.


8. Contribution

Contributions are welcome! If you have suggestions for improvements or additional features, feel free to fork the repository and submit a pull request.

9. License

This project is licensed under the MIT License. See the LICENSE file for details.

10. Acknowledgments

Thanks to OpenWeatherMap for providing the weather data API.

Appreciation for Matplotlib and Seaborn for their data visualization tools.

11.Contact Information:
Rubeena Maddarki
9448236090
rubeenamaddarki85@gmail.com

