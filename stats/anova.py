# statistics/anova.py

import pandas as pd

from scipy.stats import (
    f_oneway
)

from statsmodels.stats.multicomp import (
    pairwise_tukeyhsd
)

from core.models import (
    StatisticsResult,
    ComparisonResult
)

from stats.ttests import (
    significance_stars
)


# =====================================================
# Helpers
# =====================================================

def build_long_dataframe(
    df
):

    frames = []

    for column in df.columns:

        temp = pd.DataFrame(
            {
                "Group": str(column),
                "Value": pd.to_numeric(
                    df[column],
                    errors="coerce"
                )
            }
        ).dropna()

        frames.append(
            temp
        )

    return pd.concat(
        frames,
        ignore_index=True
    )


def get_group_arrays(
    df
):

    groups = []

    for column in df.columns:

        groups.append(
            df[column]
            .dropna()
            .values
        )

    return groups


# =====================================================
# Tukey HSD
# =====================================================

def tukey_posthoc(
    df,
    alpha=0.05
):

    long_df = build_long_dataframe(
        df
    )

    tukey = pairwise_tukeyhsd(
        endog=long_df["Value"],
        groups=long_df["Group"],
        alpha=alpha
    )

    tukey_df = pd.DataFrame(
        tukey._results_table.data[1:],
        columns=tukey._results_table.data[0]
    )

    comparisons = []

    for _, row in tukey_df.iterrows():

        pvalue = float(
            row["p-adj"]
        )

        comparison = ComparisonResult(
            group1=str(
                row["group1"]
            ),

            group2=str(
                row["group2"]
            ),

            pvalue=pvalue,

            stars=significance_stars(
                pvalue
            )
        )

        comparisons.append(
            comparison
        )

    return (
        tukey_df,
        comparisons
    )


# =====================================================
# One-Way ANOVA
# =====================================================

def one_way_anova(
    df,
    alpha=0.05
):

    groups = get_group_arrays(
        df
    )

    statistic, pvalue = f_oneway(
        *groups
    )

    posthoc_df = None
    comparisons = []

    if len(df.columns) >= 3:

        (
            posthoc_df,
            comparisons
        ) = tukey_posthoc(
            df,
            alpha
        )

    return StatisticsResult(

        test_name="One-Way ANOVA",

        statistic=float(
            statistic
        ),

        pvalue=float(
            pvalue
        ),

        stars=significance_stars(
            pvalue
        ),

        posthoc=posthoc_df,

        comparisons=comparisons
    )


# =====================================================
# Dispatcher
# =====================================================

def run_anova(
    df,
    alpha=0.05
):

    return one_way_anova(
        df,
        alpha
    )