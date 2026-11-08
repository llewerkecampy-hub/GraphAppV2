# core/statistics_engine.py

from core.models import (
    StatisticsSettings,
    StatisticsResult
)

from stats.assumptions import (
    recommend_test,
    build_assumption_report
)

from stats.ttests import (
    student_t_test,
    welch_t_test
)

from stats.anova import (
    one_way_anova
)

from stats.nonparametric import (
    mann_whitney_u,
    kruskal_wallis
)


# =====================================================
# Auto Mode
# =====================================================

def run_auto(
    df,
    settings
):

    recommended = recommend_test(
        df,
        alpha=settings.alpha
    )

    return run_statistics_by_name(
        df,
        recommended,
        settings
    )


# =====================================================
# Dispatcher
# =====================================================

def run_statistics_by_name(
    df,
    method,
    settings
):

    method = method.strip()

    if method == "Student T-Test":

        return student_t_test(
            df
        )

    if method == "Welch T-Test":

        return welch_t_test(
            df
        )

    if method == "One-Way ANOVA":

        return one_way_anova(
            df,
            alpha=settings.alpha
        )

    if method == "Mann-Whitney U":

        return mann_whitney_u(
            df
        )

    if method == "Kruskal-Wallis":

        return kruskal_wallis(
            df,
            alpha=settings.alpha
        )

    raise ValueError(
        f"Unsupported method: {method}"
    )


# =====================================================
# Public API
# =====================================================

def run_statistics(
    df,
    statistics_settings
):

    method = (
        statistics_settings.method
    )

    if method == "Auto":

        return run_auto(
            df,
            statistics_settings
        )

    return run_statistics_by_name(
        df,
        method,
        statistics_settings
    )


# =====================================================
# Assumption Report API
# =====================================================

def get_assumption_report(
    df,
    statistics_settings
):

    return build_assumption_report(
        df,
        alpha=statistics_settings.alpha
    )


# =====================================================
# Recommendation API
# =====================================================

def get_recommended_test(
    df,
    statistics_settings
):

    return recommend_test(
        df,
        alpha=statistics_settings.alpha
    )