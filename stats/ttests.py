# stats/ttests.py

import numpy as np
import pandas as pd

from scipy.stats import (
    ttest_ind
)

from core.models import (
    StatisticsResult,
    ComparisonResult
)


# =====================================================
# Significance Stars
# =====================================================

def significance_stars(
    pvalue
):

    if pvalue < 0.0001:
        return "****"

    if pvalue < 0.001:
        return "***"

    if pvalue < 0.01:
        return "**"

    if pvalue < 0.05:
        return "*"

    return "ns"


# =====================================================
# Utilities
# =====================================================

def get_two_groups(
    df
):

    if len(df.columns) != 2:

        raise ValueError(
            "T-tests require exactly two groups."
        )

    group1_name = df.columns[0]
    group2_name = df.columns[1]

    group1 = (
        df.iloc[:, 0]
        .dropna()
        .values
    )

    group2 = (
        df.iloc[:, 1]
        .dropna()
        .values
    )

    return (
        group1_name,
        group2_name,
        group1,
        group2
    )


# =====================================================
# Student T-Test
# =====================================================

def student_t_test(
    df
):

    (
        group1_name,
        group2_name,
        group1,
        group2
    ) = get_two_groups(df)

    statistic, pvalue = ttest_ind(
        group1,
        group2,
        equal_var=True
    )

    comparison = ComparisonResult(
        group1=group1_name,
        group2=group2_name,
        pvalue=float(pvalue),
        stars=significance_stars(
            pvalue
        )
    )

    return StatisticsResult(

        test_name="Student T-Test",

        statistic=float(
            statistic
        ),

        pvalue=float(
            pvalue
        ),

        stars=significance_stars(
            pvalue
        ),

        posthoc=None,

        comparisons=[
            comparison
        ]
    )


# =====================================================
# Welch T-Test
# =====================================================

def welch_t_test(
    df
):

    (
        group1_name,
        group2_name,
        group1,
        group2
    ) = get_two_groups(df)

    statistic, pvalue = ttest_ind(
        group1,
        group2,
        equal_var=False
    )

    comparison = ComparisonResult(
        group1=group1_name,
        group2=group2_name,
        pvalue=float(pvalue),
        stars=significance_stars(
            pvalue
        )
    )

    return StatisticsResult(

        test_name="Welch T-Test",

        statistic=float(
            statistic
        ),

        pvalue=float(
            pvalue
        ),

        stars=significance_stars(
            pvalue
        ),

        posthoc=None,

        comparisons=[
            comparison
        ]
    )


# =====================================================
# Dispatcher
# =====================================================

def run_t_test(
    df,
    method
):

    method = (
        method
        .strip()
        .lower()
    )

    if method in [

        "student",
        "student t-test",
        "student_t_test"

    ]:

        return student_t_test(
            df
        )

    if method in [

        "welch",
        "welch t-test",
        "welch_t_test"

    ]:

        return welch_t_test(
            df
        )

    raise ValueError(
        f"Unsupported t-test method: {method}"
    )