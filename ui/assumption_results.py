# ui/assumption_results.py


def show_assumption_report(
    st,
    report
):

    if report is None:

        return

    st.subheader(
        "Assumption Checks"
    )

    st.write(
        f"All Groups Normal: "
        f"{report['all_normal']}"
    )

    st.write(
        f"Equal Variance: "
        f"{report['equal_variance']}"
    )

    st.write(
        report["variance"]
    )