From flask import Flask, request, render_template_string
import requests
from bs4 import BeautifulSoup

app = Flask(_name_)

# Function to scrape job listings and filter those mentioning specified languages
def scrape_language_jobs(url):
    response = requests.get(url)  # Send a request to the provided URL

    if response.status_code != 200:
        return "Failed to retrieve the page", None

    soup = BeautifulSoup(response.text, 'html.parser')  # Parse the HTML content

    jobs = []  # To store job listings

    # Get the entire text content of the page
    full_text = soup.get_text()

    # List of target languages
    target_languages = ['English', 'French', 'Hindi', 'Dutch']

    # Check if any target language is mentioned
    found_languages = [lang for lang in target_languages if lang in full_text]

    if found_languages:
        # Create a job dictionary with the updated description mentioning the found languages
        job = {
            'title': 'Job found',
            'description': f'<strong style="color: black;">Applicants proficient in {", ".join(found_languages)} are welcome; other languages not required.</strong>',
            'link': url
        }
        jobs.append(job)
    else:
        return "No jobs requiring the specified languages were found on this page.", None

    return None, jobs  # Return jobs that match the specified languages

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        message, jobs = scrape_language_jobs(url)
        return render_template_string('''
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Global Talent Hub</title>
                <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
                <style>
                    body {
                        margin: 0;
                        padding: 0;
                        color: white;
                        font-family: Arial, sans-serif;
                        background: linear-gradient(45deg, #ff6f61, #de1b1b, #1bde56, #5b1bde);
                        background-size: 600% 600%;
                        animation: gradientAnimation 15s ease infinite;
                    }

                    @keyframes gradientAnimation {
                        0% { background-position: 0% 50%; }
                        50% { background-position: 100% 50%; }
                        100% { background-position: 0% 50%; }
                    }

                    .container {
                        position: relative;
                        z-index: 1;
                        margin-top: 50px;
                        text-align: center;
                    }

                    .highlight {
                        background-color: rgba(0, 0, 0, 0.7);
                        padding: 20px;
                        border-radius: 8px;
                        margin-bottom: 20px;
                    }

                    .card {
                        margin: 20px 0;
                    }

                    .footer {
                        position: fixed;
                        bottom: 0;
                        width: 100%;
                        padding: 20px;
                        background-color: rgba(0, 0, 0, 0.7);
                        color: white;
                        text-align: center;
                    }

                    .btn-primary {
                        background-color: #003d7a;
                        border-color: #003d7a;
                    }

                    .btn-primary:hover {
                        background-color: #00274d;
                        border-color: #00274d;
                    }
                </style>
            </head>
            <body>
                <div class="container">
                    <h1 class="my-4">Global Talent Hub</h1>
                    <div class="highlight">
                        <h2>Important: New Job Opportunities!</h2>
                        <p>Explore the latest job listings that require proficiency in English, French, Hindi, or Dutch.</p>
                    </div>
                    <form method="post" class="mb-4">
                        <div class="form-group">
                            <input type="text" name="url" class="form-control" placeholder="Enter job listing URL" required>
                        </div>
                        <button type="submit" class="btn btn-primary">Search</button>
                    </form>
                    {% if message %}
                        <div class="alert alert-info">
                            {{ message }}
                        </div>
                    {% elif jobs %}
                        <div class="row">
                            {% for job in jobs %}
                                <div class="col-md-6">
                                    <div class="card">
                                        <div class="card-body">
                                            <h5 class="card-title">{{ job.title }}</h5>
                                            <p class="card-text">{{ job.description|safe }}</p>
                                            <a href="{{ job.link }}" class="btn btn-primary" target="_blank">View Job Listing</a>
                                        </div>
                                    </div>
                                </div>
                            {% endfor %}
                        </div>
                    {% endif %}
                </div>
                <div class="footer">
                    <p>&copy; 2024 Global Talent Hub | All Rights Reserved</p>
                </div>
                <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
                <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.3/dist/umd/popper.min.js"></script>
                <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
            </body>
            </html>
        ''', message=message, jobs=jobs)

    return render_template_string('''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Global Talent Hub</title>
            <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
            <style>
                body {
                    margin: 0;
                    padding: 0;
                    color: white;
                    font-family: Arial, sans-serif;
                    background: linear-gradient(45deg, #ff6f61, #de1b1b, #1bde56, #5b1bde);
                    background-size: 600% 600%;
                    animation: gradientAnimation 15s ease infinite;
                }

                @keyframes gradientAnimation {
                    0% { background-position: 0% 50%; }
                    50% { background-position: 100% 50%; }
                    100% { background-position: 0% 50%; }
                }

                .container {
                    position: relative;
                    z-index: 1;
                    margin-top: 50px;
                    text-align: center;
                }

                .highlight {
                    background-color: rgba(0, 0, 0, 0.7);
                    padding: 20px;
                    border-radius: 8px;
                    margin-bottom: 20px;
                }

                .footer {
                    position: fixed;
                    bottom: 0;
                    width: 100%;
                    padding: 20px;
                    background-color: rgba(0, 0, 0, 0.7);
                    color: white;
                    text-align: center;
                }

                .btn-primary {
                    background-color: #003d7a;
                    border-color: #003d7a;
                }

                .btn-primary:hover {
                    background-color: #00274d;
                    border-color: #00274d;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1 class="my-4">Global Talent Hub</h1>
                <div class="highlight">
                    <h2>Important: New Job Opportunities!</h2>
                    <p>Explore the latest job listings that require proficiency in English, French, Hindi, or Dutch.</p>
                </div>
                <form method="post" class="mb-4">
                    <div class="form-group">
                        <input type="text" name="url" class="form-control" placeholder="Enter job listing URL" required>
                    </div>
                    <button type="submit" class="btn btn-primary">Search</button>
                </form>
            </div>
            <div class="footer">
                <p>&copy; 2024 Global Talent Hub | All Rights Reserved</p>
            </div>
            <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
            <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.3/dist/umd/popper.min.js"></script>
            <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
        </body>
        </html>
    ''')

if _name_ == '_main_':
    app.run(debug=True)