# statistics/nonparametric.py

from scipy.stats import (
    mannwhitneyu,
    kruskal
)

from core.models import (
    StatisticsResult,
    ComparisonResult
)

from stats.ttests import (
    significance_stars
)

from stats.posthoc import (
    dunn_posthoc
)


# =====================================================
# Helpers
# =====================================================

def get_two_groups(df):

    if len(df.columns) != 2:

        raise ValueError(
            "Mann-Whitney U requires exactly two groups."
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


def get_group_arrays(df):

    groups = []

    for column in df.columns:

        groups.append(
            df[column]
            .dropna()
            .values
        )

    return groups


# =====================================================
# Mann-Whitney U
# =====================================================

def mann_whitney_u(df):

    (
        group1_name,
        group2_name,
        group1,
        group2
    ) = get_two_groups(df)

    statistic, pvalue = mannwhitneyu(
        group1,
        group2,
        alternative="two-sided"
    )

    comparison = ComparisonResult(

        group1=group1_name,

        group2=group2_name,

        pvalue=float(
            pvalue
        ),

        stars=significance_stars(
            pvalue
        )
    )

    return StatisticsResult(

        test_name="Mann-Whitney U",

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
# Kruskal-Wallis
# =====================================================

def kruskal_wallis(
    df,
    alpha=0.05
):

    groups = get_group_arrays(
        df
    )

    statistic, pvalue = kruskal(
        *groups
    )

    posthoc_matrix = None
    comparisons = []

    if len(df.columns) >= 3:

        (
            posthoc_matrix,
            comparisons
        ) = dunn_posthoc(
            df,
            alpha=alpha
        )

    return StatisticsResult(

        test_name="Kruskal-Wallis",

        statistic=float(
            statistic
        ),

        pvalue=float(
            pvalue
        ),

        stars=significance_stars(
            pvalue
        ),

        posthoc=posthoc_matrix,

        comparisons=comparisons
    )


# =====================================================
# Dispatcher
# =====================================================

def run_nonparametric(
    df,
    method,
    alpha=0.05
):

    method = (
        method
        .strip()
        .lower()
    )

    if method in [

        "mann-whitney",
        "mann-whitney u",
        "mann_whitney",
        "mannwhitney"

    ]:

        return mann_whitney_u(
            df
        )

    if method in [

        "kruskal",
        "kruskal-wallis",
        "kruskal wallis"

    ]:

        return kruskal_wallis(
            df,
            alpha=alpha
        )

    raise ValueError(
        f"Unsupported nonparametric method: {method}"
    )