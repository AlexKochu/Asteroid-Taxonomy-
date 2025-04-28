Asteroid Taxonomy: A Comprehensive Data-Driven Study of Near-Earth Objects
Asteroid Taxonomy is an intricate data science project that applies sophisticated statistical techniques to the analysis of NASA's Near-Earth Object (NEO) dataset. The aim is to comprehensively explore the dynamics, risk assessment, and defining attributes of asteroids whose orbits intersect or come near Earth's orbit, providing valuable insights into their behaviour, potential hazards, and the underlying patterns governing their movement.

Project Overview
The objectives of this study are multifaceted and include:

Feature Analysis: To conduct an exhaustive analysis of critical asteroid characteristics, including estimated diameter, relative velocity, miss distance, and orbital elements. These key attributes are essential for understanding both the size and trajectory of NEOs, as well as their potential impact on Earth.

Exploratory Data Analysis (EDA): To identify significant trends, correlations, and anomalies through an advanced EDA process. This involves visualising and summarising the dataset to uncover hidden patterns and relationships between the NEO attributes, which may not be immediately apparent through basic statistical inspection.

Risk Assessment: To assess the potential risks associated with NEOs, focusing on identifying those that may pose a threat to Earth. This process involves calculating hazard probabilities based on asteroid characteristics, proximity, and frequency of Earth encounters.

Statistical Hypothesis Testing: To employ advanced statistical techniques such as Z-tests and T-tests to formally test hypotheses related to asteroid characteristics. This ensures the findings are statistically significant and can be generalised to a broader context.

Data Source
The dataset employed for this analysis was sourced from NASA's Near-Earth Object Web Service (NeoWs), which provides high-resolution data on asteroids and comets whose orbits bring them into close proximity with Earth's orbital path. The dataset contains a wealth of information, including detailed orbital parameters, physical dimensions, and relative velocities, making it an ideal resource for in-depth statistical analysis.

Tools and Technologies
The project makes use of the following tools and technologies to perform data manipulation, statistical analysis, and visualisation:

Python (3.x): The core programming language for data analysis, chosen for its extensive libraries and flexibility in handling complex datasets.

Pandas: Utilised for efficient data manipulation and preprocessing. Pandas allows for handling large datasets, transforming data into a usable format, and performing intricate data cleaning operations.

NumPy: Used for performing advanced numerical computations. NumPy’s array handling capabilities enable efficient mathematical operations on large datasets, crucial for statistical analysis.

Matplotlib and Seaborn: These libraries are employed to generate detailed and aesthetically compelling visualisations. From simple histograms to complex heatmaps, these visualisation tools help interpret trends and relationships within the data.

SciPy and Statsmodels: These libraries are central to hypothesis testing and statistical inference. They enable the application of Z-tests and T-tests to formally validate hypotheses and derive statistical conclusions.

Jupyter Notebook: An interactive environment that facilitates the iterative process of data exploration and analysis. Jupyter notebooks are used to document code, visualise results, and present findings in a clear and accessible format.

Key Features
Data Integrity and Cleaning: A comprehensive data cleaning procedure was implemented to address missing values, incorrect data types, and inconsistencies within the dataset. Missing values were imputed using appropriate statistical methods to maintain the integrity of the analysis.

Descriptive Statistics: Summary statistics were generated for each critical feature in the dataset. These include measures such as mean, median, standard deviation, skewness, and kurtosis, providing a comprehensive view of the distribution and central tendencies of the asteroid attributes.

Visual Exploratory Data Analysis: A wide range of graphical techniques was employed to explore the dataset. Histograms, scatter plots, kernel density estimations (KDEs), and heatmaps were used to visually identify relationships between key attributes such as asteroid size, speed, and proximity to Earth. Correlation matrices were also constructed to assess the strength of relationships between variables.

Outlier Detection and Analysis: Statistical methods such as the Z-score and IQR (Interquartile Range) were used to detect and investigate outliers in asteroid characteristics. Outliers are critical as they may represent extreme cases of NEOs that could pose significant risks.

Hypothesis Testing: To ensure the statistical significance of the findings, Z-tests and T-tests were applied to test hypotheses regarding the physical and orbital properties of NEOs. These tests helped confirm whether observed differences in asteroid characteristics were statistically meaningful or could have occurred by chance.

Asteroid Classification and Risk Profiling: The NEOs were classified into categories based on their statistical behaviours and orbital characteristics. This classification enables a structured risk assessment, which is crucial for understanding which NEOs might pose the greatest threat to Earth, allowing for more effective prioritisation in space research and planetary defence efforts.
