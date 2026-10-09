#!/usr/bin/env python3
"""Generates a professional academic PDF guide for Viva Voce and Project Presentation.

Output: planning/Viva_and_Project_Presentation_Guide.pdf
"""

import os
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.platypus import (
    HRFlowable,
    KeepTogether,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

PROJECT_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_PDF = PROJECT_ROOT / "planning" / "Viva_and_Project_Presentation_Guide.pdf"


class NumberedCanvas(canvas.Canvas):
    """Two-pass canvas to dynamically compute and print total page count."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, page_count):
        if self._pageNumber == 1:
            return  # Skip cover page

        self.saveState()
        self.setFont("Helvetica", 9)
        self.setFillColor(colors.HexColor("#6B7280"))

        # Running Header
        self.drawString(
            54, 750, "IET DAVV · B.Tech IV Year E&TC · Medical Insurance Cost Prediction (Group 11)"
        )
        self.setStrokeColor(colors.HexColor("#E5E7EB"))
        self.setLineWidth(0.5)
        self.line(54, 744, 558, 744)

        # Running Footer
        self.line(54, 45, 558, 45)
        self.drawString(
            54, 32, "Final-Year Viva Voce & Presentation Preparation Guide"
        )
        page_str = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(558, 32, page_str)
        self.restoreState()


def build_pdf():
    doc = SimpleDocTemplate(
        str(OUTPUT_PDF),
        pagesize=letter,
        leftMargin=54,
        rightMargin=54,
        topMargin=54,
        bottomMargin=54,
    )

    styles = getSampleStyleSheet()

    # Custom typography styles
    title_style = ParagraphStyle(
        "CoverTitle",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=24,
        leading=30,
        textColor=colors.HexColor("#1E3A8A"),
        alignment=1,
    )

    subtitle_style = ParagraphStyle(
        "CoverSubtitle",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=13,
        leading=18,
        textColor=colors.HexColor("#3B82F6"),
        alignment=1,
    )

    h1_style = ParagraphStyle(
        "Heading1_Custom",
        parent=styles["Heading1"],
        fontName="Helvetica-Bold",
        fontSize=16,
        leading=20,
        textColor=colors.HexColor("#1E3A8A"),
        spaceBefore=12,
        spaceAfter=6,
        keepWithNext=True,
    )

    h2_style = ParagraphStyle(
        "Heading2_Custom",
        parent=styles["Heading2"],
        fontName="Helvetica-Bold",
        fontSize=12,
        leading=16,
        textColor=colors.HexColor("#1F2937"),
        spaceBefore=10,
        spaceAfter=4,
        keepWithNext=True,
    )

    body_style = ParagraphStyle(
        "Body_Custom",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=9.5,
        leading=13.5,
        textColor=colors.HexColor("#374151"),
        spaceAfter=6,
    )

    bullet_style = ParagraphStyle(
        "Bullet_Custom",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=9.5,
        leading=13.5,
        textColor=colors.HexColor("#374151"),
        leftIndent=15,
        firstLineIndent=-10,
        spaceAfter=3,
    )

    q_style = ParagraphStyle(
        "QuestionStyle",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=10,
        leading=14,
        textColor=colors.HexColor("#1E40AF"),
        spaceBefore=8,
        spaceAfter=2,
        keepWithNext=True,
    )

    a_style = ParagraphStyle(
        "AnswerStyle",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=9.5,
        leading=13.5,
        textColor=colors.HexColor("#1F2937"),
        leftIndent=10,
        spaceAfter=6,
    )

    callout_style = ParagraphStyle(
        "CalloutStyle",
        parent=styles["Normal"],
        fontName="Helvetica-Oblique",
        fontSize=9,
        leading=13,
        textColor=colors.HexColor("#92400E"),
    )

    story = []

    # =========================================================================
    # COVER PAGE
    # =========================================================================
    story.append(Spacer(1, 40))
    story.append(
        Paragraph("INSTITUTE OF ENGINEERING & TECHNOLOGY (IET)", ParagraphStyle(
            "CollegeHeader",
            parent=styles["Normal"],
            fontName="Helvetica-Bold",
            fontSize=12,
            leading=16,
            textColor=colors.HexColor("#4B5563"),
            alignment=1,
        ))
    )
    story.append(
        Paragraph("DEVI AHILYA VISHWAVIDYALAYA (DAVV), INDORE", ParagraphStyle(
            "CollegeSubHeader",
            parent=styles["Normal"],
            fontName="Helvetica",
            fontSize=11,
            leading=15,
            textColor=colors.HexColor("#6B7280"),
            alignment=1,
        ))
    )
    story.append(Spacer(1, 15))
    story.append(HRFlowable(width="60%", thickness=2, color=colors.HexColor("#1E3A8A"), spaceBefore=5, spaceAfter=25))

    story.append(
        Paragraph("MEDICAL INSURANCE COST PREDICTION & ANALYTICS DASHBOARD", title_style)
    )
    story.append(Spacer(1, 10))
    story.append(
        Paragraph("Comprehensive Project Report & Viva Voce Examination Guide", subtitle_style)
    )
    story.append(Spacer(1, 40))

    # Academic metadata box
    meta_data = [
        [Paragraph("<b>Degree Program:</b>", body_style), Paragraph("B.Tech IV Year (Final Year)", body_style)],
        [Paragraph("<b>Branch:</b>", body_style), Paragraph("Electronics & Telecommunication Engineering (E&TC)", body_style)],
        [Paragraph("<b>Academic Session:</b>", body_style), Paragraph("2026 – 2027", body_style)],
        [Paragraph("<b>Section / Group:</b>", body_style), Paragraph("Section B  |  Group No. 11", body_style)],
        [Paragraph("<b>Domain:</b>", body_style), Paragraph("Software / Predictive Machine Learning", body_style)],
        [Paragraph("<b>Architecture:</b>", body_style), Paragraph("100% Pure Python Stack (Scikit-Learn, Streamlit, Plotly)", body_style)],
    ]
    meta_table = Table(meta_data, colWidths=[140, 280])
    meta_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#F8FAFC")),
        ("BOX", (0, 0), (-1, -1), 1, colors.HexColor("#CBD5E1")),
        ("INNERGRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#E2E8F0")),
        ("PADDING", (0, 0), (-1, -1), 6),
    ]))
    story.append(meta_table)

    story.append(Spacer(1, 50))
    story.append(
        Paragraph("<b>Prepared for:</b> Final Year Major Project Evaluation, External Examiners, & Viva Voce Examination", ParagraphStyle(
            "FooterNote",
            parent=styles["Normal"],
            fontName="Helvetica-Bold",
            fontSize=9.5,
            leading=13,
            textColor=colors.HexColor("#1E3A8A"),
            alignment=1,
        ))
    )
    story.append(PageBreak())

    # =========================================================================
    # SECTION 1: EXECUTIVE SUMMARY & OBJECTIVES
    # =========================================================================
    story.append(Paragraph("1. Executive Summary & Academic Alignment", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#CBD5E1"), spaceBefore=2, spaceAfter=8))

    story.append(Paragraph(
        "<b>Project Abstract:</b> Medical expenses and insurance costs vary significantly from individual to individual "
        "due to demographic characteristics, lifestyle factors, and physiological risk markers. Estimating potential "
        "insurance expenses accurately supports financial risk assessment and informed decision-making. "
        "This project develops an end-to-end machine learning system that formulates insurance cost estimation as a "
        "supervised continuous regression problem, benchmarks three algorithms on held-out test data, and delivers an "
        "interactive presentation dashboard featuring real-time predictions, exploratory data analytics, and what-if simulations.",
        body_style
    ))

    story.append(Paragraph("<b>Alignment with Academic Proforma-I Objectives:</b>", h2_style))
    objectives = [
        "<b>Objective 1 (Predictive System):</b> Developed an ML regression engine capable of estimating individualized annual charges from 6 demographic/lifestyle features.",
        "<b>Objective 2 (Feature Identification):</b> Quantified relationships between input variables and billed charges (identifying smoking and BMI as primary drivers).",
        "<b>Objective 3 (Categorical Encoding):</b> Encapsulated One-Hot Encoding within Scikit-Learn ColumnTransformer pipelines with strict leakage prevention.",
        "<b>Objective 4 (Multi-Model Comparison):</b> Trained and benchmarked Multiple Linear Regression, Random Forest Regressor, and Gradient Boosting Regressor.",
        "<b>Objective 5 (Quantitative Evaluation):</b> Evaluated held-out test data using standard metrics: Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), and R² Score.",
        "<b>Objective 6 (Interactive Presentation App):</b> Delivered a 5-module responsive Streamlit dashboard with interactive Plotly visualizations and scenario analysis.",
    ]
    for obj in objectives:
        story.append(Paragraph(f"• {obj}", bullet_style))

    story.append(Spacer(1, 10))

    # =========================================================================
    # SECTION 2: DATASET SPECIFICATION & STATISTICAL AUDIT
    # =========================================================================
    story.append(Paragraph("2. Dataset Specification & Statistical Audit", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#CBD5E1"), spaceBefore=2, spaceAfter=8))

    story.append(Paragraph(
        "The project utilizes the verified <b>Medical Insurance Cost Dataset</b> (1,338 records, 7 columns) sourced from Kaggle. "
        "All 7 columns were verified through an automated data audit engine.",
        body_style
    ))

    # Dataset Table
    ds_data = [
        ["Feature", "Data Type", "Role", "Observed Domain", "Clinical / Demographic Significance"],
        ["age", "Integer", "Input", "18 – 64 yrs", "Biological age; exhibits positive linear cost trend."],
        ["sex", "Categorical", "Input", "female, male", "Biological sex; minor overall direct effect."],
        ["bmi", "Float", "Input", "15.96 – 53.13", "Body Mass Index; non-linear threshold at BMI ≥ 30."],
        ["children", "Integer", "Input", "0 – 5", "Dependent count covered under policy."],
        ["smoker", "Categorical", "Input", "yes, no", "Tobacco smoking; single largest cost multiplier (~3.8x)."],
        ["region", "Categorical", "Input", "NE, NW, SE, SW", "US residential territory; southeast shows slightly higher charges."],
        ["charges", "Float (Target)", "Target", "$1,121.87 – $63,770.43", "Billed annual hospital/insurance charge in USD."],
    ]
    ds_table = Table(ds_data, colWidths=[55, 65, 45, 100, 235])
    ds_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1E3A8A")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 8),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#D1D5DB")),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#F9FAFB")]),
        ("PADDING", (0, 0), (-1, -1), 4),
    ]))
    story.append(ds_table)

    story.append(Spacer(1, 12))

    # =========================================================================
    # SECTION 3: SYSTEM ARCHITECTURE & DATA LEAKAGE PREVENTION
    # =========================================================================
    story.append(Paragraph("3. Technical Architecture & Machine Learning Methodology", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#CBD5E1"), spaceBefore=2, spaceAfter=8))

    story.append(Paragraph(
        "<b>Strict Data Leakage Prevention Protocol:</b><br/>"
        "1. <b>Pre-Split Partitioning:</b> The raw dataset was partitioned into 80% training (N=1,070) and 20% test (N=268) "
        "using a fixed random seed (seed=42) <i>prior</i> to computing any scalers, statistics, or encoders.<br/>"
        "2. <b>Encapsulated Pipeline:</b> All preprocessing transformations are encapsulated inside Scikit-Learn <code>ColumnTransformer</code> "
        "objects. Scalers (<code>StandardScaler</code>) and categorical encoders (<code>OneHotEncoder</code>) are fitted "
        "strictly on <code>X_train</code> and serialized together with the estimators into <code>.joblib</code> artifacts.<br/>"
        "3. <b>Zero Target Contamination:</b> The target column (<code>charges</code>) is never passed into the feature transformer.",
        body_style
    ))

    story.append(Spacer(1, 5))

    # Architecture Layer Summary Box
    arch_data = [
        [Paragraph("<b>Layer</b>", body_style), Paragraph("<b>Key Modules</b>", body_style), Paragraph("<b>Responsibilities</b>", body_style)],
        [Paragraph("<b>Presentation UI</b>", body_style), Paragraph("<code>app.py</code><br/><code>pages/*.py</code>", body_style), Paragraph("Streamlit multi-page interface; renders input forms, Plotly charts, KPI cards, and what-if comparisons.", body_style)],
        [Paragraph("<b>Services Layer</b>", body_style), Paragraph("<code>PredictionService</code><br/><code>ScenarioService</code>", body_style), Paragraph("Authoritative business logic decoupled from UI widgets; handles validation, inference, and delta calculations.", body_style)],
        [Paragraph("<b>ML Pipeline</b>", body_style), Paragraph("<code>preprocessing.py</code><br/><code>registry.py</code>", body_style), Paragraph("Encapsulates <code>ColumnTransformer</code>, loads fitted <code>.joblib</code> models, checks metadata.", body_style)],
        [Paragraph("<b>Data Layer</b>", body_style), Paragraph("<code>loader.py</code><br/><code>validation.py</code>", body_style), Paragraph("Loads <code>data/insurance.csv</code>, executes automated 7-column audits, checks duplicates and nulls.", body_style)],
    ]
    arch_table = Table(arch_data, colWidths=[90, 110, 300])
    arch_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#374151")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("FONTSIZE", (0, 0), (-1, -1), 8),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#D1D5DB")),
        ("PADDING", (0, 0), (-1, -1), 4),
    ]))
    story.append(arch_table)

    story.append(PageBreak())

    # =========================================================================
    # SECTION 4: MODEL BENCHMARK RESULTS & EMPIRICAL FINDINGS
    # =========================================================================
    story.append(Paragraph("4. Empirical Model Benchmarks & Results", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#CBD5E1"), spaceBefore=2, spaceAfter=8))

    story.append(Paragraph(
        "All three models were trained on 80% data (N=1,070) and evaluated on the exact same held-out test split (20%, N=268, seed=42). "
        "The empirical results are summarized below:",
        body_style
    ))

    # Results Table
    res_data = [
        ["Model Architecture", "MAE ($ USD)", "RMSE ($ USD)", "R² Score", "Rank & Verdict"],
        ["Gradient Boosting Regressor", "$2,401.61", "$4,325.64", "0.8795", "🥇 1st Place (Top Performer - Default)"],
        ["Random Forest Regressor", "$2,552.04", "$4,590.28", "0.8643", "🥈 2nd Place (Strong Non-Linear Fit)"],
        ["Multiple Linear Regression", "$4,181.19", "$5,796.28", "0.7836", "🥉 3rd Place (Interpretable Baseline)"],
    ]
    res_table = Table(res_data, colWidths=[140, 75, 75, 60, 150])
    res_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1E3A8A")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 8.5),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#D1D5DB")),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.HexColor("#ECFDF5"), colors.white, colors.white]),
        ("PADDING", (0, 0), (-1, -1), 5),
    ]))
    story.append(res_table)

    story.append(Spacer(1, 10))
    story.append(Paragraph("<b>Key Analytical Insights to Present to Examiners:</b>", h2_style))
    insights = [
        "<b>Why Gradient Boosting Won:</b> Healthcare costs exhibit strong synergistic interactions—specifically, patients with BMI ≥ 30 who also smoke experience exponential cost increases (> $40,000). Linear regression cannot capture this interaction without explicit polynomial interaction terms, whereas Gradient Boosting models it naturally via sequential tree splits, achieving an R² of 0.8795.",
        "<b>Smoking Factor Multiplier:</b> Regular smoking is the dominant feature. The mean cost for smokers is $32,050 compared to $8,434 for non-smokers (~3.8x higher).",
        "<b>Age Progression Slope:</b> Across all demographic subgroups, age exhibits a steady linear slope of approximately +$250 to +$300 per additional year of age.",
        "<b>Residual Symmetry:</b> Residual error diagnostics reveal zero-mean error distribution centered at $0, confirming unbiased regression estimates.",
    ]
    for ins in insights:
        story.append(Paragraph(f"• {ins}", bullet_style))

    story.append(Spacer(1, 12))

    # =========================================================================
    # SECTION 5: STREAMLIT PRESENTATION DASHBOARD TOUR
    # =========================================================================
    story.append(Paragraph("5. Interactive Presentation Dashboard Modules", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#CBD5E1"), spaceBefore=2, spaceAfter=8))

    modules = [
        ("app.py (Main Landing)", "Displays institutional header (IET DAVV B.Tech IV Year Group 11), academic disclaimer, live dataset health KPI cards (1,338 records, 100% clean), and quick navigation links."),
        ("Module A: 1_Overview.py", "Comprehensive EDA with dynamic filters (Smoker/Non-smoker, Sex, Region), charges distribution with median reference line, continuous Age/BMI histograms, categorical box plots, and Pearson correlation heatmaps."),
        ("Module B: 2_Predict.py", "Interactive form with sliders/dropdowns, BMI health classification indicator, real-time USD estimate card, population mean/median comparison benchmarks, multi-model estimate comparison, and JSON export."),
        ("Module C: 3_Model_Insights.py", "Quantitative model benchmark table, comparative MAE/R² bar charts, actual vs. predicted scatter plots (y=x line), residual distribution histogram, relative feature importance chart, and full JSON benchmark export."),
        ("Module D: 4_What_If.py", "Scenario simulator comparing Baseline vs. Alternative profiles with one-click presets (Stop Smoking, Reduce BMI, 10 Years Older), absolute dollar delta ($Δ), relative percent change (%Δ), and changed feature callouts."),
        ("Module E: 5_About.py", "Academic proforma details, formal objectives, methodology workflow, and Kaggle open-source citations."),
    ]
    for name, desc in modules:
        story.append(Paragraph(f"<b>{name}:</b> {desc}", bullet_style))

    story.append(PageBreak())

    # =========================================================================
    # SECTION 6: HIGH-YIELD VIVA VOCE QUESTIONS & MODEL ANSWERS
    # =========================================================================
    story.append(Paragraph("6. High-Yield Viva Voce Questions & Model Answers", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#CBD5E1"), spaceBefore=2, spaceAfter=8))

    qa_list = [
        (
            "Q1: Why is medical insurance cost prediction formulated as a regression problem instead of classification?",
            "<b>Answer:</b> The target variable (<code>charges</code>) is a continuous numerical quantity measured in US Dollars ($ USD) ranging from $1,121.87 to $63,770.43, rather than a discrete categorical label (e.g., high/low risk). Therefore, it requires supervised regression algorithms capable of predicting real continuous values."
        ),
        (
            "Q2: What is Data Leakage, and how did your project strictly prevent it?",
            "<b>Answer:</b> Data leakage occurs when information from outside the training dataset (specifically from the test set) is inadvertently used during training or transformation fitting. In our project: (1) The dataset was partitioned into 80% train and 20% test *before* any feature scaling or encoding. (2) All scalers (<code>StandardScaler</code>) and encoders (<code>OneHotEncoder</code>) were fitted *strictly on X_train* inside Scikit-Learn <code>ColumnTransformer</code> pipelines. (3) The test set was held out exclusively for final unbiased evaluation."
        ),
        (
            "Q3: Why did you use One-Hot Encoding instead of Label Encoding for categorical features?",
            "<b>Answer:</b> Categorical features such as <code>region</code> (northeast, northwest, southeast, southwest) and <code>sex</code> have no natural ordinal hierarchy. Label encoding assigns arbitrary integers (e.g., 1, 2, 3, 4), which would falsely imply that southwest (4) has a greater magnitude than northeast (1), distorting linear regression models. One-Hot Encoding creates independent binary indicator columns without artificial ordering."
        ),
        (
            "Q4: Why did Gradient Boosting and Random Forest significantly outperform Linear Regression?",
            "<b>Answer:</b> Multiple Linear Regression assumes a strictly additive linear equation. However, medical costs exhibit severe non-linear threshold effects and synergistic interactions. For example, individuals with BMI ≥ 30 who also smoke experience exponential cost increases (> $40,000) rather than a simple sum of BMI and smoking penalties. Decision tree ensembles naturally segment feature spaces and capture non-linear interactions, achieving a much higher R² (0.8795 vs. 0.7836)."
        ),
        (
            "Q5: What is the mathematical difference between MAE and RMSE, and why is RMSE notably higher here?",
            "<b>Answer:</b> MAE is the average absolute error ($\\frac{1}{n}\\sum |y_i - \\hat{y}_i|$), giving linear weight to all deviations. RMSE squares errors before averaging ($\\sqrt{\\frac{1}{n}\\sum (y_i - \\hat{y}_i)^2}$), heavily penalizing large outliers. In medical billing data, rare extreme hospitalization claims (e.g. $60,000) create larger residual penalties, which naturally causes RMSE ($4,325) to be higher than MAE ($2,401)."
        ),
        (
            "Q6: What does the R² score of 0.8795 mean in practical terms? Can R² be negative?",
            "<b>Answer:</b> An R² score of 0.8795 means our Gradient Boosting model explains approximately 87.95% of the total variance observed in annual medical charges. Yes, R² can be negative on an unseen test set if the model makes worse predictions than a naive baseline that simply predicts the mean target value."
        ),
        (
            "Q7: Why does the application include an explicit 'Non-Causal' disclaimer?",
            "<b>Answer:</b> The Kaggle dataset is historical and observational, not derived from a randomized clinical trial. While smoking correlates strongly with higher predicted expenses, machine learning regression models describe statistical correlations, not certified medical interventions or guaranteed financial quotes."
        ),
        (
            "Q8: How did you ensure software engineering quality and test coverage in this project?",
            "<b>Answer:</b> We built a comprehensive automated test suite with 21 unit and integration tests using <code>pytest</code>, covering schema validation, out-of-bounds boundary warnings, data auditing, pipeline fitting, metric formulas, and scenario delta calculations with 100% passing status."
        ),
    ]

    for q, a in qa_list:
        story.append(KeepTogether([
            Paragraph(q, q_style),
            Paragraph(a, a_style),
            Spacer(1, 4),
        ]))

    story.append(Spacer(1, 10))

    # =========================================================================
    # SECTION 7: EXAMINER PRESENTATION TIPS
    # =========================================================================
    story.append(Paragraph("7. Final Presentation Checklist & Viva Tips", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#CBD5E1"), spaceBefore=2, spaceAfter=8))

    tips = [
        "<b>Opening Demo Flow:</b> Start on <code>app.py</code> to explain project objectives and dataset quality (1,338 records, 0 missing). Navigate to <code>1_Overview.py</code> to show the smoking cost multiplier and BMI threshold.",
        "<b>Live Prediction:</b> Move to <code>2_Predict.py</code>, enter a sample profile (e.g. Age 40, BMI 33, Smoker=Yes), and show the estimated cost ($38k+) along with the population benchmark and multi-model comparison.",
        "<b>What-If Simulator (Examiner Favorite):</b> Go to <code>4_What_If.py</code> and click 'Stop Smoking Scenario'. Point out how charges decrease by ~$20k-$25k and explain the absolute and percentage delta metrics.",
        "<b>Model Justification:</b> When asked which model is best, refer to <code>3_Model_Insights.py</code>: state that Gradient Boosting achieved lowest MAE ($2,401) and highest R² (0.8795), and show the residual plot proving unbiased errors.",
        "<b>Testing & Code Quality:</b> Mention that all 21 automated pytest test cases pass cleanly, demonstrating software engineering rigor.",
    ]
    for tip in tips:
        story.append(Paragraph(f"✓ {tip}", bullet_style))

    # Build document
    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"PDF successfully generated at: {OUTPUT_PDF}")


if __name__ == "__main__":
    build_pdf()
