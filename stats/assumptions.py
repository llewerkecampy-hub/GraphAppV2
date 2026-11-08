# statistics/assumptions.py

import numpy as np
import pandas as pd

from scipy.stats import (
    shapiro,
    levene
)

from core.models import (
    StatisticsResult
)


# =====================================================
# Normality
# =====================================================

def shapiro_normality_test(
    values,
    alpha=0.05
):

    values = pd.Series(
        values
    ).dropna()

    if len(values) < 3:

        return {
            "test": "Shapiro-Wilk",
            "pvalue": np.nan,
            "normal": False,
            "reason": "Insufficient sample size"
        }

    statistic, pvalue = shapiro(
        values
    )

    return {
        "test": "Shapiro-Wilk",
        "statistic": statistic,
        "pvalue": pvalue,
        "normal": pvalue >= alpha
    }


# =====================================================
# Group Normality Report
# =====================================================

def evaluate_group_normality(
    df,
    alpha=0.05
):

    results = {}

    for column in df.columns:

        results[column] = (
            shapiro_normality_test(
                df[column],
                alpha
            )
        )

    return results


# =====================================================
# Overall Normality
# =====================================================

def is_dataset_normal(
    df,
    alpha=0.05
):

    report = (
        evaluate_group_normality(
            df,
            alpha
        )
    )

    for result in report.values():

        if not result["normal"]:

            return False

    return True


# =====================================================
# Homogeneity of Variance
# =====================================================

def variance_homogeneity_test(
    df,
    alpha=0.05
):

    groups = []

    for column in df.columns:

        groups.append(
            df[column]
            .dropna()
            .values
        )

    statistic, pvalue = levene(
        *groups
    )

    return {
        "test": "Levene",
        "statistic": statistic,
        "pvalue": pvalue,
        "equal_variance": pvalue >= alpha
    }


# =====================================================
# Assumption Report
# =====================================================

def build_assumption_report(
    df,
    alpha=0.05
):

    normality = (
        evaluate_group_normality(
            df,
            alpha
        )
    )

    variance = (
        variance_homogeneity_test(
            df,
            alpha
        )
    )

    report = {

        "normality":
        normality,

        "variance":
        variance,

        "all_normal":
        is_dataset_normal(
            df,
            alpha
        ),

        "equal_variance":
        variance[
            "equal_variance"
        ]
    }

    return report


# =====================================================
# Automatic Test Recommendation
# =====================================================

def recommend_test(
    df,
    alpha=0.05
):

    n_groups = len(
        df.columns
    )

    report = (
        build_assumption_report(
            df,
            alpha
        )
    )

    all_normal = report[
        "all_normal"
    ]

    equal_variance = report[
        "equal_variance"
    ]

    # -------------------------
    # Two Groups
    # -------------------------

    if n_groups == 2:

        if all_normal:

            if equal_variance:

                return (
                    "Student T-Test"
                )

            return (
                "Welch T-Test"
            )

        return (
            "Mann-Whitney U"
        )

    # -------------------------
    # Three+ Groups
    # -------------------------

    if n_groups >= 3:

        if all_normal:

            return (
                "One-Way ANOVA"
            )

        return (
            "Kruskal-Wallis"
        )

    return "Unknown"


# =====================================================
# Summary Text
# =====================================================

def generate_assumption_summary(
    df,
    alpha=0.05
):

    report = (
        build_assumption_report(
            df,
            alpha
        )
    )

    recommendation = (
        recommend_test(
            df,
            alpha
        )
    )

    lines = []

    lines.append(
        f"Recommended Test: {recommendation}"
    )

    lines.append(
        f"All Groups Normal: "
        f"{report['all_normal']}"
    )

    lines.append(
        f"Equal Variance: "
        f"{report['equal_variance']}"
    )

    return "\n".join(
        lines
    )