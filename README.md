# TikTok Reporting Bot

## Overview  
The TikTok Reporting Bot is designed to automate the process of reporting inappropriate content on TikTok. It leverages TikTok's API to identify and report videos that violate community guidelines.

## Features  
- **Automated Reporting**: The bot automatically flags videos based on predefined criteria.  
- **Customizable Filters**: Users can set specific filters to target certain types of content.  
- **Scheduled Reporting**: Users can schedule reports to run at specific times or intervals.  
- **Email Notifications**: Get alerts for every report action taken by the bot.

## Installation  
1. Clone the repository:  
   ```bash
   git clone https://github.com/ad-dagestan/tiktok-reporting.git
   ```  
2. Navigate to the project directory:  
   ```bash
   cd tiktok-reporting
   ```  
3. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```

## Configuration  
Before running the bot, configure the following settings in the `config.json` file:
- **API_KEY**: Your TikTok API key.
- **TARGET_USERS**: List of usernames to monitor.
- **REPORT_CRITERIA**: Specific criteria for reporting.

## Usage  
Run the bot using the following command:  
```bash
python main.py
```

## Contributing  
If you would like to contribute to the project, please fork the repository and create a pull request.

## License  
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.