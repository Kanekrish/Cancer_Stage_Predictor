

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SEER Breast Cancer Prediction System</title>

    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: Arial, sans-serif;
        }

        body {
            background: #f4f7fb;
            color: #333;
            line-height: 1.7;
        }

        .container {
            width: 90%;
            max-width: 1200px;
            margin: 40px auto;
        }

        .hero {
            background: linear-gradient(135deg, #1f4e79, #2f80ed);
            color: white;
            padding: 60px;
            border-radius: 20px;
            box-shadow: 0 8px 25px rgba(0,0,0,0.15);
            text-align: center;
        }

        .hero h1 {
            font-size: 42px;
            margin-bottom: 15px;
        }

        .hero p {
            font-size: 18px;
            opacity: 0.95;
        }

        .section {
            background: white;
            margin-top: 30px;
            padding: 35px;
            border-radius: 18px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.08);
        }

        .section h2 {
            color: #1f4e79;
            margin-bottom: 20px;
            border-left: 6px solid #2f80ed;
            padding-left: 12px;
        }

        ul {
            padding-left: 20px;
        }

        li {
            margin-bottom: 10px;
        }

        .tech-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 20px;
            margin-top: 20px;
        }

        .card {
            background: #f8fbff;
            padding: 20px;
            border-radius: 15px;
            border: 1px solid #dce7f7;
            transition: 0.3s;
        }

        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 5px 20px rgba(0,0,0,0.1);
        }

        .card h3 {
            color: #1f4e79;
            margin-bottom: 10px;
        }

        .code-block {
            background: #1e1e1e;
            color: #00ff99;
            padding: 20px;
            border-radius: 12px;
            overflow-x: auto;
            margin-top: 15px;
            font-family: Consolas, monospace;
        }

        footer {
            text-align: center;
            margin: 40px 0;
            color: #666;
        }

        .badge {
            display: inline-block;
            padding: 8px 15px;
            border-radius: 30px;
            background: #2f80ed;
            color: white;
            margin: 5px;
            font-size: 14px;
        }

        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }

        table th, table td {
            border: 1px solid #ddd;
            padding: 14px;
            text-align: left;
        }

        table th {
            background: #1f4e79;
            color: white;
        }

        table tr:nth-child(even) {
            background: #f9f9f9;
        }
    </style>
</head>
<body>

    <div class="container">

        <div class="hero">
            <h1>🧬 SEER Breast Cancer Prediction System</h1>
            <p>
                Machine Learning-Based Clinical Decision Support System for Predicting
                Breast Cancer Survival Outcomes Using the SEER Clinical Dataset.
            </p>
        </div>

        <div class="section">
            <h2>📌 Project Overview</h2>
            <p>
                This project implements a machine learning-powered breast cancer prediction system
                using the SEER (Surveillance, Epidemiology, and End Results) clinical dataset.
                The system predicts patient survival outcomes using advanced machine learning algorithms
                and provides an interactive web-based dashboard for healthcare analytics.
            </p>
        </div>

        <div class="section">
            <h2>🚀 Key Features</h2>
            <ul>
                <li>Upload trained machine learning models (.pkl)</li>
                <li>Upload SEER clinical datasets (.csv)</li>
                <li>Predict breast cancer survival outcomes</li>
                <li>Interactive web dashboard using Streamlit</li>
                <li>Confusion matrix and performance visualization</li>
                <li>Download prediction reports</li>
                <li>Automatic preprocessing and data cleaning</li>
            </ul>
        </div>

        <div class="section">
            <h2>🤖 Machine Learning Algorithms</h2>

            <div class="tech-grid">
                <div class="card">
                    <h3>Logistic Regression</h3>
                    <p>
                        Baseline classification algorithm for predicting patient survival outcomes.
                    </p>
                </div>

                <div class="card">
                    <h3>Random Forest</h3>
                    <p>
                        Ensemble learning algorithm used for high-performance classification.
                    </p>
                </div>

                <div class="card">
                    <h3>XGBoost</h3>
                    <p>
                        Advanced gradient boosting algorithm optimized for predictive accuracy.
                    </p>
                </div>
            </div>
        </div>

        <div class="section">
            <h2>📊 Dataset Features</h2>

            <table>
                <tr>
                    <th>Feature</th>
                    <th>Description</th>
                </tr>
                <tr>
                    <td>Age</td>
                    <td>Patient age at diagnosis</td>
                </tr>
                <tr>
                    <td>Race</td>
                    <td>Patient ethnicity/racial background</td>
                </tr>
                <tr>
                    <td>T Stage</td>
                    <td>Tumor staging classification</td>
                </tr>
                <tr>
                    <td>N Stage</td>
                    <td>Lymph node staging classification</td>
                </tr>
                <tr>
                    <td>Tumor Size</td>
                    <td>Measured tumor size</td>
                </tr>
                <tr>
                    <td>Estrogen Status</td>
                    <td>Hormone receptor status</td>
                </tr>
                <tr>
                    <td>Status</td>
                    <td>Target variable (Alive / Dead)</td>
                </tr>
            </table>
        </div>

        <div class="section">
            <h2>🛠️ Technologies Used</h2>

            <span class="badge">Python</span>
            <span class="badge">Streamlit</span>
            <span class="badge">Scikit-learn</span>
            <span class="badge">XGBoost</span>
            <span class="badge">Pandas</span>
            <span class="badge">NumPy</span>
            <span class="badge">Matplotlib</span>
            <span class="badge">Joblib</span>
        </div>

        <div class="section">
            <h2>⚙️ System Workflow</h2>

            <ol>
                <li>Train machine learning model using SEER dataset</li>
                <li>Save best model as .pkl file</li>
                <li>Launch Streamlit web application</li>
                <li>Upload trained model (.pkl)</li>
                <li>Upload dataset (.csv)</li>
                <li>Generate predictions</li>
                <li>Visualize metrics and download reports</li>
            </ol>
        </div>

        <div class="section">
            <h2>▶️ Running the Application</h2>

            <p>Run the following command in Command Prompt:</p>

            <div class="code-block">
python -m streamlit run app.py
            </div>

            <p style="margin-top:20px;">
                After execution, open the generated localhost URL in your browser.
            </p>
        </div>

        <div class="section">
            <h2>📈 Expected Outputs</h2>

            <ul>
                <li>Prediction labels (Alive / Dead)</li>
                <li>Model accuracy metrics</li>
                <li>Confusion matrix visualization</li>
                <li>Prediction distribution charts</li>
                <li>Downloadable prediction reports</li>
            </ul>
        </div>

        <footer>
            <p>
                Developed for Breast Cancer Prediction Research using Machine Learning and the SEER Clinical Dataset.
            </p>
        </footer>

    </div>

</body>
</html>

