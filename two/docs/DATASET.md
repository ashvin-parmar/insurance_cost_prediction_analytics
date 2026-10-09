# Dataset Documentation & Data Dictionary

## 1. Source & Attribution
- **Dataset Title:** Medical Insurance Cost Prediction
- **Source:** Kaggle
- **URL:** [https://www.kaggle.com/datasets/rahulvyasm/medical-insurance-cost-prediction](https://www.kaggle.com/datasets/rahulvyasm/medical-insurance-cost-prediction)
- **Local Storage:** `data/insurance.csv`
- **Total Records:** 1,338 rows
- **Total Features:** 6 input features + 1 target column

---

## 2. Feature Schema & Data Dictionary

| Column Name | Data Type | Role | Domain / Units | Description |
|---|---|---|---|---|
| `age` | Integer | Input Feature | 18 – 64 (years) | Age of the primary beneficiary. |
| `sex` | Categorical | Input Feature | `{"female", "male"}` | Biological sex of the insurance contractor. |
| `bmi` | Float | Input Feature | 15.96 – 53.13 ($kg/m^2$) | Body Mass Index, indicating relative weight category. |
| `children` | Integer | Input Feature | 0 – 5 | Number of children/dependents covered by insurance. |
| `smoker` | Categorical | Input Feature | `{"yes", "no"}` | Regular tobacco smoking status. |
| `region` | Categorical | Input Feature | `{"northeast", "northwest", "southeast", "southwest"}` | Residential area in the US. |
| `charges` | Float | Target Variable | $1,121.87 – $63,770.43 (USD) | Individual medical costs billed by health insurance. |

---

## 3. Observed Statistics & Quality Audit

From the active dataset of 1,338 records:
- **Missing Values:** Zero missing / null entries across all 7 columns.
- **Duplicate Records:** 1 duplicate row detected (Row 581 matching Row 196: `age=19, sex=male, bmi=30.59, children=0, smoker=no, region=northwest, charges=1639.5631`). Retained in the dataset for raw transparency and reproducible Kaggle benchmarking.
- **Distribution Characteristics:**
  - `charges`: Right-skewed distribution. Mean is **$13,270.42** while Median is **$9,382.03**, driven by high healthcare costs associated with smoking and elevated BMI.
  - `smoker`: Strongest driver of insurance costs. Non-smokers have a median charge of ~$7,345, whereas smokers have a median charge exceeding ~$34,455.
  - `bmi`: Normal-like distribution centered around 30.66 (overweight/obese threshold is $\ge 30$).

---

## 4. Academic Limitations & Observational Disclaimer

> [!WARNING]
> This dataset is observational and historical. The machine learning models trained on this data estimate statistical associations, **not causal effects**. In particular:
> - Smoking status correlates strongly with higher billed charges, but this application does not simulate medical interventions or guaranteed insurance premiums.
> - The application outputs must be presented strictly as academic regression estimates, not binding financial quotes or clinical risk determinations.
