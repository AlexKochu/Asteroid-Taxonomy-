Asteroid Taxonomy: A Detailed Statistical Examination of Near-Earth Object Behaviour
Asteroid Taxonomy is an advanced analytical exploration that integrates space science with statistical methodology. This project delves into NASA’s Near-Earth Object (NEO) dataset, aiming to systematically examine the characteristics, risks, and underlying dynamics of asteroids whose trajectories bring them into close proximity with Earth's orbit.

Project Overview
This study is designed to fulfil several interconnected objectives:

Analysis of Key Features: To meticulously examine essential asteroid attributes, including estimated diameter, relative velocity, miss distance, and orbital elements. These attributes provide crucial insight into the physical characteristics of NEOs and their potential to impact Earth.

Exploratory Data Analysis (EDA): To uncover significant patterns, correlations, and anomalies through an extensive EDA. This process includes data visualisation, summarisation, and pattern recognition techniques aimed at revealing hidden structures and potential risks associated with NEOs.

Risk Assessment: To evaluate the potential threat posed by NEOs based on their proximity, speed, and size. This assessment is crucial for advancing planetary defence strategies and understanding the frequency of hazardous NEO encounters with Earth.

Statistical Hypothesis Testing: To apply rigorous statistical testing, including Z-tests and T-tests, to test hypotheses regarding NEO characteristics, ensuring the results are statistically valid and not due to random chance.

Data Source
The dataset used in this analysis was sourced from NASA’s Near-Earth Object Web Service (NeoWs), an authoritative platform providing detailed information on asteroids and comets whose orbits bring them into close proximity with Earth. This dataset includes a wide range of variables, such as asteroid size, speed, distance from Earth, and orbital parameters, providing a comprehensive foundation for analysis.

Tools and Technologies
The analysis is conducted using the following tools and technologies:

Python (3.x): The primary programming language used for data processing, statistical analysis, and visualisation. Python's extensive libraries allow for advanced data handling and statistical modelling.

Pandas: Utilised for data manipulation, cleaning, and transformation. Pandas facilitates the handling of large datasets, enabling efficient filtering, aggregation, and modification of data.

NumPy: Used for performing high-level numerical computations, including statistical analysis and mathematical modelling, essential for working with large numerical datasets.

Matplotlib and Seaborn: Employed for the creation of detailed visualisations. These libraries help generate a variety of plots—such as histograms, scatter plots, and heatmaps—that visually represent trends, distributions, and relationships within the dataset.

SciPy and Statsmodels: These libraries are pivotal for hypothesis testing and statistical inference. They enable the application of Z-tests and T-tests to formally validate hypotheses regarding asteroid characteristics.

Jupyter Notebook: An interactive environment that facilitates iterative exploration, analysis, and documentation of code, visualisation, and results. It allows for dynamic interaction with the data and the documentation of the entire analytical process.

Key Features
Data Cleaning and Preprocessing: A robust data cleaning process was employed to handle inconsistencies, missing values, and outliers within the dataset. Missing values were imputed using appropriate statistical techniques, ensuring that the analysis was not biased by incomplete data.

Descriptive Analytics: A thorough exploration of the dataset’s central tendencies and distributions was performed. This included calculating key summary statistics (mean, median, standard deviation, skewness) to describe the data’s structure and identify any inherent patterns.

Visual Exploratory Data Analysis: Advanced visualisation techniques were applied to explore the relationships between asteroid attributes. Visualisations such as histograms, scatter plots, kernel density estimates (KDEs), and heatmaps were generated to detect correlations, distributions, and outliers. These visuals were essential in revealing patterns that would not be immediately visible through raw data analysis.

Outlier Detection and Examination: Outliers were identified using statistical methods such as the Z-score and the Interquartile Range (IQR). The examination of outliers is particularly important in the context of NEOs, as extreme values (e.g., exceptionally large asteroids or extremely fast-moving objects) may represent outlying events with significant implications for Earth’s safety.

Hypothesis Testing: To confirm or challenge assumptions about the NEO dataset, Z-tests and T-tests were applied to various subsets of data. These statistical tests allowed for the evaluation of specific hypotheses, such as whether there is a significant difference in the mean velocity of larger versus smaller asteroids, or whether certain orbital parameters correlate with proximity to Earth.

Asteroid Classification and Risk Profiling: The NEOs were grouped into categories based on their characteristics, such as their size, velocity, and distance from Earth. This classification is essential for risk profiling, as different types of NEOs pose varying levels of threat. Large, high-velocity NEOs that pass closer to Earth are of particular concern, and the classification helps to identify and prioritise these objects for further study.
