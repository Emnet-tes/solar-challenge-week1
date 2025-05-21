# Solar Data Discovery - Week 0 Challenge

This repository contains my submission for the Week 0 challenge of the **10 Academy Artificial Intelligence Mastery (AIM)** program. The project focuses on exploring and analyzing solar farm data from **Benin**, **Sierra Leone**, and **Togo** to identify high-potential regions for solar energy investment.

## 🎯 Project Overview

### Business Context
MoonLight Energy Solutions is seeking to expand its solar energy operations across West Africa. This analysis provides data-driven insights to support strategic investment decisions by identifying regions with optimal solar potential.

### Key Objectives
- Analyze environmental measurements across three countries
- Identify regions with highest solar potential
- Provide actionable recommendations for investment
- Ensure data quality and reliability through robust cleaning processes

## 📊 Project Structure

```
solar-challenge-week1/
├── data/               # Raw and cleaned datasets
├── notebooks/         # Jupyter notebooks for analysis
├── src/              # Source code modules
│   ├── data/         # Data processing modules
│   ├── visualization/# Plotting utilities
│   └── utils/        # Helper functions
├── tests/            # Unit tests
├── scripts/          # Utility scripts
└── .github/          # CI/CD workflows
```

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Git
- Virtual environment (recommended)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/solar-challenge-week1.git
cd solar-challenge-week1
```

2. Create and activate virtual environment:
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## 📈 Analysis Components

### 1. Data Profiling & Cleaning
- Comprehensive EDA for each country
- Missing value analysis and treatment
- Outlier detection and handling
- Time-series trend analysis
- Data quality assessment

### 2. Exploratory Data Analysis
- Statistical summaries
- Correlation analysis
- Time-series visualizations
- Wind rose plots
- Bubble plots for geographical insights

### 3. Cross-Country Comparison
- GHI, DNI, and DHI analysis
- Statistical testing (ANOVA)
- Comparative visualizations
- Regional potential assessment

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- 10 Academy for providing the challenge
- MoonLight Energy Solutions for the business context
- Open-source community for various tools and libraries used