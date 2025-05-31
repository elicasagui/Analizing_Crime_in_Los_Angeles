<body>
  <h1>Crime in Los Angeles – Exploratory Data Analysis</h1>

  <h2>Project Overview</h2>
  <p>This project examines crime incidents in the City of Los Angeles using open‐source data. It includes exploratory data analysis and visualization with Python libraries such as pandas, NumPy, matplotlib, and folium for geospatial mapping. The goal is to uncover temporal and spatial patterns in reported crimes across different neighborhoods and crime categories.</p>

  <h2>Contents</h2>
  <p>This repository is organized as follows:</p>
  <pre><code># Crime_in_Los_Angeles/
├── data/                         # Raw dataset(s)
│   └── crimes.csv                # Main dataset of reported LA crimes
├── notebooks/                    # Jupyter notebooks for EDA and visualization
│   └── images/                   # Folder containing maps and plot images
│   └── 01_exploratory_analysis.ipynb  # Notebook with initial EDA and mapping
│   └── 02_time_series_analysis.ipynb  # Notebook analyzing trends over time
│   └── 03_spatial_heatmaps.ipynb      # Notebook generating crime heatmaps
├── src/                          # Python scripts for modularized functions
│   ├── __init__.py               # Package initializer
│   ├── load_data.py              # Functions to load and validate crime data
│   ├── clean_data.py             # Data cleaning and preprocessing functions
│   ├── analyze.py                # Functions for summary statistics and trends
│   ├── visualize.py              # Plotting functions (matplotlib, folium)
│   ├── dashboard.py              # Streamlit app for interactive exploration
│   └── utils.py                  # Utility functions (e.g., path management)
├── tests/                        # Unit tests for all src modules (pytest)
│   ├── test_load_data.py         # Verifies load_data.load_crimes reads CSV and checks for missing values
│   ├── test_clean_data.py        # Checks clean_data.clean_crimes removes invalid dates and normalizes categories
│   ├── test_analyze.py           # Ensures analyze.compute_crime_counts_by_neighborhood returns correct counts
│   └── test_visualize.py         # Confirms visualize.plot_time_series generates a Matplotlib figure
├── main.py                       # Script to run full analysis and generate summary reports
├── requirements.txt              # List of dependencies
└── README.html                   # This README file
</code></pre>

  <h2>Data Instructions</h2>
  <ol>
    <li>Download the crime dataset from the Los Angeles Open Data portal: <a href="https://data.lacity.org/">https://data.lacity.org/</a></li>
    <li>Search for and download the “Crime Data from 2010 to Present” CSV file.</li>
    <li>Move the downloaded <code>crimes.csv</code> file into the <code>data/</code> directory:</li>
  </ol>
  <pre><code>mkdir -p data/
mv ~/Downloads/crimes.csv data/</code></pre>

  <h2>Data Description</h2>
  <p>The <code>crimes.csv</code> file contains records of crime incidents reported in Los Angeles. Key columns include:</p>
  <ul>
    <li><code>DR_NO</code> – Unique incident identifier</li>
    <li><code>Date_Rptd</code> – Date the crime was reported (YYYY-MM-DD)</li>
    <li><code>YEAR</code> – Year when the crime occurred</li>
    <li><code>Crime_Code</code> – Numeric code corresponding to crime category</li>
    <li><code>Crm_Cd_Desc</code> – Description of the crime type (e.g., “BURGLARY THEFT FROM VEHICLE”)</li>
    <li><code>Vict_Age</code> – Age of the victim (if known)</li>
    <li><code>Vict_Sex</code> – Sex of the victim (M/F/U)</li>
    <li><code>Vict_Descent</code> – Victim’s ethnicity (e.g., “H”, “W”, “B”)</li>
    <li><code>Premis_Cd</code> – Numeric code for location type (e.g., “1000” = “STREET”)</li>
    <li><code>Premis_Desc</code> – Description of the location type (e.g., “STREET”, “RESIDENCE”)</li>
    <li><code>Weapon_Used_Cd</code> – Numeric code for weapon used (if any)</li>
    <li><code>Weapon_Desc</code> – Description of the weapon (e.g., “FIREARM”, “KNIFE”)</li>
    <li><code>Crm_Cd1</code> – Detailed crime code</li>
    <li><code>DATE_OCC</code> – Date the crime occurred (YYYY-MM-DD)</li>
    <li><code>TIME_OCC</code> – Time the crime occurred (HHMM format)</li>
    <li><code>AREA_NAME</code> – Police reporting area (neighborhood)</li>
    <li><code>LOCATION</code> – Geographic point (latitude, longitude)</li>
  </ul>

  <h2>Installation Steps</h2>
  <ol class="steps">
    <li><strong>Clone the repository:</strong>
      <pre><code>git clone https://github.com/elicasagui/Analizing_Crime_in_Los_Angeles.git
cd Crime_in_Los_Angeles</code></pre>
    </li>
    <li><strong>Create and activate a virtual environment:</strong>
      <pre><code>python -m venv venv</code></pre>
      <p><em>On Windows:</em></p>
 <pre><code>
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\venv\Scripts\Activate</code></pre>
      <p><em>On macOS/Linux:</em></p>
      <pre><code>source venv/bin/activate</code></pre>
    </li>
    <li><strong>Install dependencies:<br></strong>
      <pre><code>python -m pip install --upgrade pip
python -m pip install -r requirements.txt
      </code></pre>
    </li>
    <li><strong>Download the CSV of Crimes:</strong>
      <ol>
        <li>Activa tu entorno virtual:</li>
        <pre><code>python -m venv venv</code></pre>
        <p>Abre PowerShell como Administrador y ejecuta:</p>
        <pre><code>Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
        .\venv\Scripts\Activate</code></pre>
        <li>Ejecuta el script para descargar el CSV desde Google Drive:</li>
        <pre><code>python src/download_data.py</code></pre>
        <li>Ahora el archivo <code>data/crimes.csv</code> estará disponible para el análisis.</li>
      </ol>
    </li>
    <li><strong>Run main analysis script:</strong>
      <pre><code>python main.py</code></pre>
      <p>This will produce summary CSVs and figures in the <code>outputs/</code> folder.</p>
    </li>
    <li><strong>Launch Jupyter Notebook:</strong>
      <pre><code>jupyter notebook</code></pre>
      <p>Then open notebooks under the <code>notebooks/</code> directory to explore the analyses interactively.</p>
    </li>
  </ol>

  <h2>Streamlit Dashboard</h2>
  <p>To explore crime data interactively, launch the Streamlit app:</p>
  <ol class="steps">
    <li><strong>Activate your virtual environment</strong> (if not already active):<br>
      <pre><code>On Windows (PowerShell as Administrator):
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\venv\Scripts\Activate

On macOS/Linux:
source venv/bin/activate</code></pre>
    </li>
    <li><strong>Run the Streamlit app:</strong><br>
      <pre><code>streamlit run src/dashboard.py</code></pre>
    </li>
    <li>Open your browser at <code>http://localhost:8501</code> to view the dashboard.</li>
  </ol>
  <p>Use the sidebar controls to:</p>
  <ul>
    <li>Select one or more crime categories</li>
    <li>Choose a time range (year or month)</li>
    <li>Filter by police reporting area (neighborhood)</li>
  </ul>
  <p>The dashboard provides three tabs:</p>
  <ul>
    <li><strong>Crime Trends:</strong> Line chart of incident counts over time</li>
    <li><strong>Spatial Distribution:</strong> Interactive map showing crime density by neighborhood</li>
    <li><strong>Top Offenders:</strong> Bar chart of most frequent crime types</li>
  </ul>

  <h2>Project Questions</h2>
  <ul>
    <li>Which neighborhoods in Los Angeles have the highest crime rates?</li>
    <li>How have crime counts trended over the past five years?</li>
    <li>What are the most common types of violent vs. property crimes?</li>
    <li>At what times of day do certain crimes peak?</li>
  </ul>

  <h2>Key Insights</h2>
  <table border="1">
    <tr>
      <th>Insight ID</th>
      <th>Description</th>
      <th>Visualization</th>
    </tr>
    <tr>
      <td>1</td>
      <td>Neighborhoods with highest overall crime density</li>
      <td>
        <div class="image-container">
          <img src="notebooks/images/top_crime_neighborhoods.png" alt="Top Crime Neighborhoods">
        </div>
      </td>
    </tr>
    <tr>
      <td>2</td>
      <td>Yearly trend showing a spike in theft-related incidents in 2021</li>
      <td>
        <div class="image-container">
          <img src="notebooks/images/theft_spike_2021.png" alt="Theft Spike 2021">
        </div>
      </td>
    </tr>
    <tr>
      <td>3</td>
      <td>Heatmap of violent crimes concentrated in central LA districts</li>
      <td>
        <div class="image-container">
          <img src="notebooks/images/violent_crime_heatmap.png" alt="Violent Crime Heatmap">
        </div>
      </td>
    </tr>
  </table>
  <p>For the complete analysis and visualizations, see the notebooks in <a href="notebooks/01_exploratory_analysis.ipynb">01_exploratory_analysis.ipynb</a> and <a href="notebooks/03_spatial_heatmaps.ipynb">03_spatial_heatmaps.ipynb</a>.</p>

  <h2>Running Tests</h2>
  <p>Ensure <code>pytest</code> is installed and run:</p>
  <pre><code>pip install pytest
pytest tests/</code></pre>
  <p>All unit tests should pass without errors before merging new code.</p>

  <h2>Dependencies</h2>
  <ul>
    <li>Python 3.8+</li>
    <li>pandas</li>
    <li>numpy</li>
    <li>matplotlib</li>
    <li>seaborn</li>
    <li>folium</li>
    <li>streamlit</li>
    <li>jupyter</li>
  </ul>

  <h2>License</h2>
  <p>This project is licensed under the MIT License. See the <code>LICENSE</code> file for details.</p>

  <h2>Created by</h2>
  <p>
    Eliecer Castro<br>
    Data Scientist / Python Developer<br>
    GitHub link: <a href="https://github.com/elicasagui/Crime_in_Los_Angeles">Crime in Los Angeles Repository</a>
  </p>
</body>
</html>

