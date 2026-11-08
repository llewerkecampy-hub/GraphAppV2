# statistics/posthoc.py

import pandas as pd

import scikit_posthocs as sp

from core.models import (
    ComparisonResult
)

from stats.ttests import (
    significance_stars
)

# =====================================================
# Dunn's Post Hoc Test
# =====================================================

def dunn_posthoc(
    df,
    alpha=0.05,
    p_adjust="bonferroni"
):

    long_df = build_long_dataframe(
        df
    )

    matrix = sp.posthoc_dunn(
        long_df,
        val_col="Value",
        group_col="Group",
        p_adjust=p_adjust
    )

    comparisons = (
        matrix_to_comparisons(
            matrix,
            alpha
        )
    )

    return (
        matrix,
        comparisons
    )


# =====================================================
# Long Format Conversion
# =====================================================

def build_long_dataframe(
    df
):

    frames = []

    for column in df.columns:

        temp = pd.DataFrame(
            {
                "Group": column,
                "Value": df[column].dropna()
            }
        )

        frames.append(
            temp
        )

    return pd.concat(
        frames,
        ignore_index=True
    )


# =====================================================
# Matrix Converter
# =====================================================

def matrix_to_comparisons(
    matrix,
    alpha=0.05
):

    comparisons = []

    groups = list(
        matrix.columns
    )

    for i in range(len(groups)):

        for j in range(i + 1, len(groups)):

            group1 = groups[i]
            group2 = groups[j]

            pvalue = float(
                matrix.loc[
                    group1,
                    group2
                ]
            )

            comparison = ComparisonResult(

                group1=group1,

                group2=group2,

                pvalue=pvalue,

                stars=significance_stars(
                    pvalue
                )
            )

            comparisons.append(
                comparison
            )

    return comparisons


# =====================================================
# Significant Comparisons Only
# =====================================================

def significant_comparisons(
    comparisons,
    alpha=0.05
):

    return [

        comparison

        for comparison in comparisons

        if comparison.pvalue < alpha

    ]


# =====================================================
# Lookup Comparison
# =====================================================

def get_comparison(
    comparisons,
    group1,
    group2
):

    for comparison in comparisons:

        match1 = (

            comparison.group1 == group1
            and
            comparison.group2 == group2

        )

        match2 = (

            comparison.group1 == group2
            and
            comparison.group2 == group1

        )

        if match1 or match2:

            return comparison

    return None