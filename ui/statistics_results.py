# ui/statistics_results.py


def show_statistics_results(
    st,
    result
):

    if result is None:

        return

    st.subheader(
        "Statistics"
    )

    st.write(
        f"Test: {result.test_name}"
    )

    st.write(
        f"Statistic: "
        f"{result.statistic:.4f}"
    )

    st.write(
        f"P-value: "
        f"{result.pvalue:.6g}"
    )

    st.write(
        f"Significance: "
        f"{result.stars}"
    )

    if result.posthoc is not None:

        st.subheader(
            "Post Hoc Tests"
        )

        st.dataframe(
            result.posthoc
        )