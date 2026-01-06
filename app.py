from flask import Flask
from datetime import datetime
import pytz


app = Flask(__name__)


IST = pytz.timezone('Asia/Kolkata')

@app.route('/')
def hello_world():
    """
    This function runs when someone visits the main page of the web app.
    It returns a simple HTML string to be displayed in the browser.
    """
   
    current_time_ist = datetime.now(IST).strftime('%Y-%m-%d %H:%M:%S %Z')
    
    
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Deployed Python App</title>
        <style>
            body {{
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                background-color: #f0f2f5;
                color: #333;
            }}
            .container {{
                text-align: center;
                padding: 40px;
                border-radius: 12px;
                background-color: #ffffff;
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
            }}
            h1 {{
                color: #007bff;
                margin-bottom: 10px;
            }}
            p {{
                font-size: 1.2rem;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Hello from Hyderabad!</h1>
            <p>This Python application was deployed successfully using GitHub Actions.</p>
            <p>Current Time in India: <strong>{current_time_ist}</strong></p>
        </div>
    </body>
    </html>
    """
    return html_content

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
